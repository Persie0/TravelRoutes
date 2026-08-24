#!/usr/bin/env python3
"""Generate real-geography itinerary maps as SVG.

Usage:
    python tools/python/script.py itineraries/<Trip-Slug>

Inputs under <itinerary>/maps/:
    stops.geojson
    route.geojson
    route-60-40.geojson   # optional
    map-config.json       # recommended

Outputs:
    map-full-route.svg
    map-60-40-route.svg   # when compact route exists

Route feature properties may include ``mode``. Common values are road,
train/rail, bus, ferry/boat, flight and hike/walk. Their line styles/colors are
kept distinct in the output so the transport semantics remain visible.

SVG is the canonical static map artifact. Commit it together with the GeoJSON
source data. Coastlines/borders are rendered from Basemap/GSHHS.

Dependencies: matplotlib, basemap
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from mpl_toolkits.basemap import Basemap

plt.rcParams["svg.fonttype"] = "none"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def mode_style(mode: str) -> tuple[str, str, str]:
    """Return (color, linestyle, legend label) for a route mode."""
    m = mode.lower()
    if "flight" in m or "plane" in m:
        return "#1b9e77", "--", "flight"
    if "ferry" in m or "boat" in m:
        return "#984ea3", ":", "ferry / boat"
    if "hike" in m or "walk" in m:
        return "#8c510a", "-.", "hike / walk"
    if "train" in m or "rail" in m or "bus" in m or "coach" in m:
        return "#377eb8", "--", "rail / coach"
    return "#e6550d", "-", "road / overland / 4×4"


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
    gtype, coords = geometry.get("type"), geometry.get("coordinates", [])
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
    coords = [c for f in features for c in iter_coordinates(f.get("geometry", {}))]
    if not coords:
        raise ValueError("No usable coordinates found for map bounds")
    lons, lats = [c[0] for c in coords], [c[1] for c in coords]
    lon_span, lat_span = max(max(lons) - min(lons), 1.0), max(max(lats) - min(lats), 1.0)
    lon_pad, lat_pad = max(0.55, lon_span * padding_ratio), max(0.55, lat_span * padding_ratio)
    return min(lons)-lon_pad, min(lats)-lat_pad, max(lons)+lon_pad, max(lats)+lat_pad


def feature_coordinates(feature: dict, by_name: dict) -> list[tuple[float, float]]:
    coordinates = list(iter_coordinates(feature.get("geometry", {})))
    if len(coordinates) >= 2:
        return coordinates
    props = feature.get("properties", {})
    a, b = props.get("from"), props.get("to")
    if a in by_name and b in by_name:
        return [tuple(by_name[a]["geometry"]["coordinates"]), tuple(by_name[b]["geometry"]["coordinates"])]
    return []


def draw_route_feature(ax, m, feature: dict, by_name: dict) -> None:
    coordinates = feature_coordinates(feature, by_name)
    if len(coordinates) < 2:
        return
    mode = str(feature.get("properties", {}).get("mode", "road"))
    color, linestyle, _ = mode_style(mode)
    xs, ys = m([c[0] for c in coordinates], [c[1] for c in coordinates])
    ax.plot(xs, ys, linestyle=linestyle, linewidth=2.2, color=color, alpha=0.94, zorder=4)


def render_svg(maps_dir: Path, route_file: str, stop_names: list[str], title: str,
               subtitle: str, svg_name: str, sequential_numbers: bool) -> Path:
    stops_geojson, route_geojson = load_json(maps_dir / "stops.geojson"), load_json(maps_dir / route_file)
    by_name = {f["properties"]["name"]: f for f in stops_geojson["features"]}
    missing = [n for n in stop_names if n not in by_name]
    if missing:
        raise KeyError(f"Configured map stops are missing from stops.geojson: {missing}")

    bounds = bounds_for_features([by_name[n] for n in stop_names])
    min_lon, min_lat, max_lon, max_lat = bounds
    aspect_hint = (max_lon-min_lon) / max(max_lat-min_lat, 0.01)
    fig, ax = plt.subplots(figsize=(13.0, 9.5) if aspect_hint >= 1 else (10.5, 12.5), dpi=180)
    m = make_basemap(ax, bounds, title, subtitle)

    selected, used_modes = set(stop_names), []
    for feature in route_geojson["features"]:
        props = feature.get("properties", {})
        a, b = props.get("from"), props.get("to")
        if a and b and (a not in selected or b not in selected):
            continue
        draw_route_feature(ax, m, feature, by_name)
        used_modes.append(str(props.get("mode", "road")))

    offsets = [(7,7),(7,-12),(-7,8),(-7,-12),(10,0),(-10,0)]
    for index, name in enumerate(stop_names, 1):
        lon, lat = by_name[name]["geometry"]["coordinates"]
        x, y = m(lon, lat)
        order = index if sequential_numbers else by_name[name]["properties"].get("order", index)
        ax.scatter([x],[y],s=66,color="#c83e2d",edgecolor="white",linewidth=1.1,zorder=8)
        ax.annotate(str(order),(x,y),ha="center",va="center",fontsize=7.2,fontweight="bold",color="white",zorder=9)
        dx,dy=offsets[(index-1)%len(offsets)]
        ax.annotate(name,(x,y),xytext=(dx,dy),textcoords="offset points",ha="left" if dx>=0 else "right",
                    fontsize=7.7,fontweight="bold",bbox=dict(boxstyle="round,pad=.15",fc="white",alpha=.80,ec="none"),zorder=10)

    legend=[]; seen=set()
    for mode in used_modes:
        color,linestyle,label=mode_style(mode)
        if label in seen: continue
        seen.add(label)
        legend.append(Line2D([0],[0],color=color,lw=2.2,linestyle=linestyle,label=label))
    if legend:
        ax.legend(handles=legend, loc="lower left", fontsize=8, framealpha=.92)
    ax.text(.995,.005,"GSHHS coastlines/borders + verified geographic stop coordinates. Route lines are planning connectors unless routed geometry is supplied.",
            transform=ax.transAxes,ha="right",va="bottom",fontsize=6.3,bbox=dict(fc="white",alpha=.82,ec="0.6"))
    fig.tight_layout()
    path=maps_dir/svg_name
    fig.savefig(path,format="svg",bbox_inches="tight")
    plt.close(fig)
    return path


def legacy_central_america_config(stops: dict) -> tuple[dict, dict | None]:
    full_names=[f["properties"]["name"] for f in stops["features"] if int(f["properties"].get("order",999))<=14]
    defaults=["Guatemala City","Antigua Guatemala","Acatenango / Fuego hike","Flores","Tikal National Park","San Ignacio","Belize City","Caye Caulker","Valladolid","Chichén Itzá","Cancún"]
    all_names={f["properties"]["name"] for f in stops["features"]}
    compact_names=[n for n in defaults if n in all_names]
    full={"title":"Guatemala → Belize → Yucatán","subtitle":"General ~28-day route · real geography + verified coordinates","stop_names":full_names}
    compact={"title":"Guatemala → Belize → Yucatán","subtitle":"60:40 highlights route · strategic time-saving transport","stop_names":compact_names} if compact_names else None
    return full,compact


def read_map_config(maps_dir: Path, stops: dict) -> tuple[dict, dict | None]:
    path=maps_dir/"map-config.json"
    if not path.exists():
        return legacy_central_america_config(stops)
    cfg=load_json(path); full=cfg.get("full")
    if not full or not full.get("stop_names"):
        raise ValueError("map-config.json requires full.stop_names")
    return full,cfg.get("compact")


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("itinerary_dir",type=Path,help="Itinerary folder containing maps/ GeoJSON files")
    args=parser.parse_args(); maps_dir=args.itinerary_dir.resolve()/"maps"
    stops=load_json(maps_dir/"stops.geojson"); full_cfg,compact_cfg=read_map_config(maps_dir,stops)
    outputs=[render_svg(maps_dir,"route.geojson",list(full_cfg["stop_names"]),str(full_cfg.get("title",args.itinerary_dir.name)),str(full_cfg.get("subtitle","Full route · real geography")),"map-full-route.svg",False)]
    if (maps_dir/"route-60-40.geojson").exists() and compact_cfg and compact_cfg.get("stop_names"):
        outputs.append(render_svg(maps_dir,"route-60-40.geojson",list(compact_cfg["stop_names"]),str(compact_cfg.get("title",args.itinerary_dir.name)),str(compact_cfg.get("subtitle","60:40 highlights route")),"map-60-40-route.svg",True))
    print("Generated SVG maps:")
    for output in outputs: print(output)


if __name__ == "__main__":
    main()
