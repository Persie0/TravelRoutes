#!/usr/bin/env python3
"""Generate real-geography itinerary maps as SVG.

Usage:
    python tools/python/script.py itineraries/<Trip-Slug>

Expected inputs under <itinerary>/maps/:
    stops.geojson
    route.geojson
    route-60-40.geojson   # optional
    map-config.json       # optional, recommended for generic itineraries

Outputs under <itinerary>/maps/:
    map-full-route.svg
    map-60-40-route.svg   # when a 60:40 route exists

map-config.json format:
    {
      "full": {"title": "...", "subtitle": "...", "stop_names": ["..."]},
      "compact": {"title": "...", "subtitle": "...", "stop_names": ["..."]}
    }

Design rule:
    SVG is the canonical and uploaded map artifact. Do not generate a second,
    independently rendered PNG version. The SVG should be committed directly to
    GitHub together with the GeoJSON source data.

Dependencies:
    matplotlib
    basemap
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
plt.rcParams["svg.fonttype"] = "none"
from matplotlib.lines import Line2D
from mpl_toolkits.basemap import Basemap


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def route_mode_style(mode: str) -> str:
    mode = mode.lower()
    if "flight" in mode:
        return "--"
    if "ferry" in mode or "boat" in mode:
        return ":"
    if "hike" in mode or "walk" in mode:
        return "-."
    return "-"


def make_basemap(ax, bounds: tuple[float, float, float, float], title: str, subtitle: str):
    min_lon, min_lat, max_lon, max_lat = bounds
    m = Basemap(
        projection="merc",
        llcrnrlon=min_lon,
        llcrnrlat=min_lat,
        urcrnrlon=max_lon,
        urcrnrlat=max_lat,
        resolution="l",
        ax=ax,
    )
    m.drawmapboundary(fill_color="#dfeff6", linewidth=0.8)
    m.fillcontinents(color="#eef0da", lake_color="#dfeff6")
    m.drawcoastlines(color="#476a72", linewidth=0.75)
    m.drawcountries(color="#666666", linewidth=0.9)
    ax.set_title(title, fontsize=19, fontweight="bold", pad=18)
    ax.text(0.5, 1.01, subtitle, transform=ax.transAxes, ha="center", fontsize=10)
    return m


def iter_coordinates(geometry: dict) -> Iterable[tuple[float, float]]:
    gtype = geometry.get("type")
    coords = geometry.get("coordinates", [])
    if gtype == "Point" and len(coords) >= 2:
        yield float(coords[0]), float(coords[1])
    elif gtype == "LineString":
        for coord in coords:
            if len(coord) >= 2:
                yield float(coord[0]), float(coord[1])
    elif gtype == "MultiLineString":
        for line in coords:
            for coord in line:
                if len(coord) >= 2:
                    yield float(coord[0]), float(coord[1])


def bounds_for_features(features: Iterable[dict], padding_ratio: float = 0.08):
    coords = []
    for feature in features:
        coords.extend(iter_coordinates(feature.get("geometry", {})))
    if not coords:
        raise ValueError("No usable coordinates found for map bounds")
    lons = [c[0] for c in coords]
    lats = [c[1] for c in coords]
    lon_span = max(max(lons) - min(lons), 1.0)
    lat_span = max(max(lats) - min(lats), 1.0)
    lon_pad = max(0.55, lon_span * padding_ratio)
    lat_pad = max(0.55, lat_span * padding_ratio)
    return (
        min(lons) - lon_pad,
        min(lats) - lat_pad,
        max(lons) + lon_pad,
        max(lats) + lat_pad,
    )


def draw_route_feature(ax, m, feature: dict, by_name: dict) -> None:
    props = feature.get("properties", {})
    mode = str(props.get("mode", "road"))
    geometry = feature.get("geometry", {})
    coordinates = list(iter_coordinates(geometry))

    # Prefer the stored geometry. Fall back to stop-to-stop coordinates for
    # older itinerary files that only carry from/to names.
    if len(coordinates) < 2:
        a, b = props.get("from"), props.get("to")
        if a in by_name and b in by_name:
            coordinates = [
                tuple(by_name[a]["geometry"]["coordinates"]),
                tuple(by_name[b]["geometry"]["coordinates"]),
            ]
    if len(coordinates) < 2:
        return

    xs, ys = m([c[0] for c in coordinates], [c[1] for c in coordinates])
    ax.plot(
        xs,
        ys,
        linestyle=route_mode_style(mode),
        linewidth=2.1,
        color="#d95f02",
        alpha=0.92,
        zorder=4,
    )


def render_svg(
    maps_dir: Path,
    route_file: str,
    stop_names: list[str],
    title: str,
    subtitle: str,
    svg_name: str,
    sequential_numbers: bool,
) -> Path:
    stops_geojson = load_json(maps_dir / "stops.geojson")
    route_geojson = load_json(maps_dir / route_file)
    by_name = {f["properties"]["name"]: f for f in stops_geojson["features"]}

    missing = [name for name in stop_names if name not in by_name]
    if missing:
        raise KeyError(f"Configured map stops are missing from stops.geojson: {missing}")

    selected_features = [by_name[n] for n in stop_names]
    bounds = bounds_for_features(selected_features)

    # Landscape works better for cross-country routes, but keep adequate height
    # for geographically tall itineraries.
    min_lon, min_lat, max_lon, max_lat = bounds
    aspect_hint = (max_lon - min_lon) / max(max_lat - min_lat, 0.01)
    figsize = (13.0, 9.5) if aspect_hint >= 1.0 else (10.5, 12.5)

    fig, ax = plt.subplots(figsize=figsize, dpi=180)
    m = make_basemap(ax, bounds, title, subtitle)

    def xy(name: str):
        lon, lat = by_name[name]["geometry"]["coordinates"]
        return m(lon, lat)

    selected = set(stop_names)
    for feature in route_geojson["features"]:
        props = feature.get("properties", {})
        a, b = props.get("from"), props.get("to")
        # If from/to metadata is present, do not draw branches outside the
        # selected compact route. Geometry-only features are drawn as supplied.
        if a and b and (a not in selected or b not in selected):
            continue
        draw_route_feature(ax, m, feature, by_name)

    # Offset labels deterministically to reduce collisions in dense clusters.
    offsets = [(7, 7), (7, -12), (-7, 8), (-7, -12), (10, 0), (-10, 0)]
    for index, name in enumerate(stop_names, start=1):
        x, y = xy(name)
        order = index if sequential_numbers else by_name[name]["properties"].get("order", index)
        ax.scatter([x], [y], s=66, color="#d95f02", edgecolor="white", linewidth=1.1, zorder=8)
        ax.annotate(
            str(order), (x, y), ha="center", va="center", fontsize=7.2,
            fontweight="bold", color="white", zorder=9,
        )
        label = name.replace(" National Park", "").replace(" / Fuego hike", " / Fuego")
        dx, dy = offsets[(index - 1) % len(offsets)]
        ha = "left" if dx >= 0 else "right"
        ax.annotate(
            label,
            (x, y),
            xytext=(dx, dy),
            textcoords="offset points",
            ha=ha,
            fontsize=7.7,
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=.15", fc="white", alpha=.80, ec="none"),
            zorder=10,
        )

    ax.legend(
        handles=[
            Line2D([0], [0], color="#d95f02", lw=2.2, label="road / overland / 4×4"),
            Line2D([0], [0], color="#d95f02", lw=2.2, linestyle="-.", label="hike / walk"),
            Line2D([0], [0], color="#d95f02", lw=2.2, linestyle=":", label="ferry / boat"),
            Line2D([0], [0], color="#d95f02", lw=2.2, linestyle="--", label="flight"),
        ],
        loc="lower left",
        fontsize=8,
        framealpha=0.92,
    )
    ax.text(
        0.995,
        0.005,
        "GSHHS coastlines/borders + geographic stop coordinates. Route lines are planning connectors unless routed geometry is supplied.",
        transform=ax.transAxes,
        ha="right",
        va="bottom",
        fontsize=6.3,
        bbox=dict(fc="white", alpha=.82, ec="0.6"),
    )

    fig.tight_layout()
    svg_path = maps_dir / svg_name
    fig.savefig(svg_path, format="svg", bbox_inches="tight")
    plt.close(fig)
    return svg_path


def legacy_central_america_config(stops: dict) -> tuple[dict, dict | None]:
    """Preserve behavior for the repository's original itinerary."""
    full_names = [
        f["properties"]["name"]
        for f in stops["features"]
        if int(f["properties"].get("order", 999)) <= 14
    ]
    compact_default = [
        "Guatemala City", "Antigua Guatemala", "Acatenango / Fuego hike",
        "Flores", "Tikal National Park", "San Ignacio", "Belize City",
        "Caye Caulker", "Valladolid", "Chichén Itzá", "Cancún",
    ]
    all_names = {f["properties"]["name"] for f in stops["features"]}
    compact_names = [n for n in compact_default if n in all_names]
    full = {
        "title": "Guatemala → Belize → Yucatán",
        "subtitle": "General ~28-day route · real geography + verified coordinates",
        "stop_names": full_names,
    }
    compact = None
    if compact_names:
        compact = {
            "title": "Guatemala → Belize → Yucatán",
            "subtitle": "60:40 highlights route · strategic time-saving transport",
            "stop_names": compact_names,
        }
    return full, compact


def read_map_config(maps_dir: Path, stops: dict) -> tuple[dict, dict | None]:
    config_path = maps_dir / "map-config.json"
    if config_path.exists():
        config = load_json(config_path)
        full = config.get("full")
        if not full or not full.get("stop_names"):
            raise ValueError("map-config.json requires full.stop_names")
        return full, config.get("compact")
    return legacy_central_america_config(stops)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("itinerary_dir", type=Path, help="Itinerary folder containing maps/ GeoJSON files")
    args = parser.parse_args()

    itinerary_dir = args.itinerary_dir.resolve()
    maps_dir = itinerary_dir / "maps"
    stops = load_json(maps_dir / "stops.geojson")
    full_cfg, compact_cfg = read_map_config(maps_dir, stops)

    outputs = [
        render_svg(
            maps_dir, "route.geojson", list(full_cfg["stop_names"]),
            str(full_cfg.get("title", itinerary_dir.name)),
            str(full_cfg.get("subtitle", "Full route · real geography")),
            "map-full-route.svg", sequential_numbers=False,
        )
    ]

    compact_route = maps_dir / "route-60-40.geojson"
    if compact_route.exists() and compact_cfg and compact_cfg.get("stop_names"):
        outputs.append(
            render_svg(
                maps_dir, "route-60-40.geojson", list(compact_cfg["stop_names"]),
                str(compact_cfg.get("title", itinerary_dir.name)),
                str(compact_cfg.get("subtitle", "60:40 highlights route")),
                "map-60-40-route.svg", sequential_numbers=True,
            )
        )

    print("Generated SVG maps:")
    for output in outputs:
        print(output)


if __name__ == "__main__":
    main()
