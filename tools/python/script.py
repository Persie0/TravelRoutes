#!/usr/bin/env python3
"""Generate real-geography itinerary maps as SVG, then derive PNG from SVG.

Usage:
    python tools/python/script.py itineraries/Central-America-Guatemala-Belize-Mexico

Expected inputs under <itinerary>/maps/:
    stops.geojson
    route.geojson
    route-60-40.geojson

Outputs under <itinerary>/maps/:
    map-full-route.svg
    map-full-route.png
    map-60-40-route.svg
    map-60-40-route.png

Important design rule:
    SVG is the canonical rendered map. PNG is generated from that exact SVG,
    never rendered independently, so both outputs have identical geography,
    labels and route geometry.

Dependencies:
    matplotlib
    basemap
    cairosvg  # preferred SVG -> PNG converter

If cairosvg is unavailable, the script tries rsvg-convert, Inkscape and then
ImageMagick's `magick` command.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from mpl_toolkits.basemap import Basemap


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def svg_to_png(svg_path: Path, png_path: Path, width: int = 2200) -> None:
    """Rasterize the canonical SVG to PNG using the best available converter."""
    try:
        import cairosvg  # type: ignore

        cairosvg.svg2png(
            url=str(svg_path),
            write_to=str(png_path),
            output_width=width,
        )
        return
    except Exception:
        pass

    if shutil.which("rsvg-convert"):
        subprocess.run(
            ["rsvg-convert", "-w", str(width), "-o", str(png_path), str(svg_path)],
            check=True,
        )
        return

    if shutil.which("inkscape"):
        subprocess.run(
            [
                "inkscape",
                str(svg_path),
                "--export-type=png",
                f"--export-filename={png_path}",
                f"--export-width={width}",
            ],
            check=True,
        )
        return

    if shutil.which("magick"):
        subprocess.run(
            ["magick", "-density", "220", str(svg_path), str(png_path)],
            check=True,
        )
        return

    raise RuntimeError(
        "No SVG→PNG converter found. Install cairosvg, librsvg, Inkscape, or ImageMagick."
    )


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
        resolution="i",
        ax=ax,
    )
    m.drawmapboundary(fill_color="#dfeff6", linewidth=0.8)
    m.fillcontinents(color="#eef0da", lake_color="#dfeff6")
    m.drawcoastlines(color="#476a72", linewidth=0.75)
    m.drawcountries(color="#666666", linewidth=0.9)
    ax.set_title(title, fontsize=19, fontweight="bold", pad=18)
    ax.text(0.5, 1.01, subtitle, transform=ax.transAxes, ha="center", fontsize=10)
    return m


def bounds_for_features(features: Iterable[dict], padding_deg: float = 0.65):
    coords = [f["geometry"]["coordinates"] for f in features]
    lons = [c[0] for c in coords]
    lats = [c[1] for c in coords]
    return (
        min(lons) - padding_deg,
        min(lats) - padding_deg,
        max(lons) + padding_deg,
        max(lats) + padding_deg,
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

    selected_features = [by_name[n] for n in stop_names]
    bounds = bounds_for_features(selected_features)

    fig, ax = plt.subplots(figsize=(10, 12.5), dpi=180)
    m = make_basemap(ax, bounds, title, subtitle)

    def xy(name: str):
        lon, lat = by_name[name]["geometry"]["coordinates"]
        return m(lon, lat)

    for feature in route_geojson["features"]:
        props = feature.get("properties", {})
        a = props.get("from")
        b = props.get("to")
        mode = str(props.get("mode", "road"))
        if not a or not b or a not in by_name or b not in by_name:
            continue
        x1, y1 = xy(a)
        x2, y2 = xy(b)
        ax.plot(
            [x1, x2],
            [y1, y2],
            linestyle=route_mode_style(mode),
            linewidth=2.1,
            color="#d95f02",
            alpha=0.92,
            zorder=4,
        )

    for index, name in enumerate(stop_names, start=1):
        x, y = xy(name)
        order = index if sequential_numbers else by_name[name]["properties"].get("order", index)
        ax.scatter(
            [x], [y], s=66, color="#d95f02", edgecolor="white", linewidth=1.1, zorder=8
        )
        ax.annotate(
            str(order),
            (x, y),
            ha="center",
            va="center",
            fontsize=7.5,
            fontweight="bold",
            color="white",
            zorder=9,
        )
        label = name.replace(" / Fuego hike", " / Fuego").replace(" National Park", "")
        ax.annotate(
            label,
            (x, y),
            xytext=(7, 7),
            textcoords="offset points",
            fontsize=8,
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=.15", fc="white", alpha=.78, ec="none"),
            zorder=10,
        )

    ax.legend(
        handles=[
            Line2D([0], [0], color="#d95f02", lw=2.2, label="road / overland"),
            Line2D([0], [0], color="#d95f02", lw=2.2, linestyle="-.", label="hike"),
            Line2D([0], [0], color="#d95f02", lw=2.2, linestyle=":", label="ferry"),
            Line2D([0], [0], color="#d95f02", lw=2.2, linestyle="--", label="flight"),
        ],
        loc="lower left",
        fontsize=8,
        framealpha=0.92,
    )
    ax.text(
        0.995,
        0.005,
        "Real coastlines/borders + verified coordinates. Route lines are planning connectors unless routed geometry is supplied.",
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "itinerary_dir",
        type=Path,
        help="Itinerary folder containing maps/stops.geojson and route GeoJSON files",
    )
    args = parser.parse_args()

    itinerary_dir = args.itinerary_dir.resolve()
    maps_dir = itinerary_dir / "maps"
    stops = load_json(maps_dir / "stops.geojson")

    full_names = [
        f["properties"]["name"]
        for f in stops["features"]
        if int(f["properties"].get("order", 999)) <= 14
    ]

    compact_default = [
        "Guatemala City",
        "Antigua Guatemala",
        "Acatenango / Fuego hike",
        "Flores",
        "Tikal National Park",
        "San Ignacio",
        "Belize City",
        "Caye Caulker",
        "Valladolid",
        "Chichén Itzá",
        "Cancún",
    ]
    compact_names = [n for n in compact_default if any(f["properties"]["name"] == n for f in stops["features"])]

    full_svg = render_svg(
        maps_dir,
        "route.geojson",
        full_names,
        "Guatemala → Belize → Yucatán",
        "General ~28-day route · real geography + verified coordinates",
        "map-full-route.svg",
        sequential_numbers=False,
    )
    svg_to_png(full_svg, maps_dir / "map-full-route.png")

    compact_route = maps_dir / "route-60-40.geojson"
    if compact_route.exists() and compact_names:
        compact_svg = render_svg(
            maps_dir,
            "route-60-40.geojson",
            compact_names,
            "Guatemala → Belize → Yucatán",
            "60:40 highlights route · strategic time-saving transport",
            "map-60-40-route.svg",
            sequential_numbers=True,
        )
        svg_to_png(compact_svg, maps_dir / "map-60-40-route.png")

    print(f"Generated SVG + PNG maps in {maps_dir}")


if __name__ == "__main__":
    main()
