#!/usr/bin/env python3
"""Regenerate real-geography route maps as PNG and SVG.

Dependencies: matplotlib, basemap
Inputs: stops.geojson, route.geojson, route-60-40.geojson

PNG output uses Basemap/GSHHS real coastlines and international borders. SVG output
is a compact native-vector rendering built directly from the same Basemap coastline
and border datasets plus the same WGS84 route/stop coordinates. Route lines are
planning connectors, not claims of exact road/rail centreline geometry.
"""
from pathlib import Path
from html import escape
import json
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from mpl_toolkits.basemap import Basemap

HERE = Path(__file__).resolve().parent

BOUNDS = dict(llcrnrlon=-10.3, llcrnrlat=36.4, urcrnrlon=-2.0, urcrnrlat=44.2)


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def make_basemap(ax=None, resolution="i"):
    return Basemap(projection="merc", resolution=resolution, ax=ax, **BOUNDS)


def route_style(mode):
    if "ferry" in mode:
        return ":"
    if "public" in mode or "train" in mode:
        return "--"
    return "-"


def render_png(route_file, title, subtitle, out_stem):
    stops = load("stops.geojson")
    route = load(route_file)
    fig, ax = plt.subplots(figsize=(11, 11), dpi=180)
    m = make_basemap(ax=ax, resolution="i")
    m.fillcontinents(lake_color="white", alpha=.45)
    m.drawcoastlines(linewidth=.85)
    m.drawcountries(linewidth=1.0)
    m.drawparallels(range(37, 45, 2), labels=[1, 0, 0, 0], fontsize=7,
                    linewidth=.25, dashes=[2, 2])
    m.drawmeridians(range(-10, -1, 2), labels=[0, 0, 0, 1], fontsize=7,
                    linewidth=.25, dashes=[2, 2])

    for feature in route["features"]:
        pts = feature["geometry"]["coordinates"]
        mode = feature["properties"].get("mode", "")
        xy = [m(lon, lat) for lon, lat in pts]
        xs = [p[0] for p in xy]
        ys = [p[1] for p in xy]
        ax.plot(xs, ys, lw=2.1, ls=route_style(mode), alpha=.9)

    for feature in stops["features"]:
        order = feature["properties"]["order"]
        name = feature["properties"]["name"]
        lon, lat = feature["geometry"]["coordinates"]
        x, y = m(lon, lat)
        ax.scatter([x], [y], s=55, zorder=8, edgecolor="white", linewidth=1)
        ax.annotate(str(order), (x, y), ha="center", va="center", fontsize=7,
                    color="white", fontweight="bold", zorder=9)
        ax.annotate(name, (x, y), xytext=(6, 6), textcoords="offset points", fontsize=7,
                    bbox=dict(boxstyle="round,pad=.15", fc="white", alpha=.75, ec="none"),
                    zorder=10)

    ax.set_title(title, fontsize=18, fontweight="bold", pad=18)
    ax.text(.5, 1.01, subtitle, transform=ax.transAxes, ha="center", fontsize=9.5)
    ax.legend(handles=[
        Line2D([0], [0], lw=2.2, ls="--", label="public transport"),
        Line2D([0], [0], lw=2.2, label="rental car"),
        Line2D([0], [0], lw=2.2, ls=":", label="ferry"),
    ], loc="lower left", fontsize=8)
    ax.annotate("N", xy=(.95, .93), xytext=(.95, .86),
                xycoords="axes fraction", textcoords="axes fraction", ha="center",
                arrowprops=dict(arrowstyle="-|>", lw=1.5), fontsize=11, fontweight="bold")

    fig.tight_layout()
    fig.savefig(HERE / f"{out_stem}.png", bbox_inches="tight")
    plt.close(fig)


def svg_point(m, x, y, width, height, margin):
    sx = margin + (x - m.xmin) / (m.xmax - m.xmin) * (width - 2 * margin)
    sy = height - margin - (y - m.ymin) / (m.ymax - m.ymin) * (height - 2 * margin)
    return sx, sy


def path_from_segment(m, segment, width, height, margin):
    pts = [svg_point(m, float(x), float(y), width, height, margin) for x, y in segment]
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)


def render_svg(route_file, title, subtitle, out_stem):
    """Write a compact native SVG from real Basemap vector geography."""
    stops = load("stops.geojson")
    route = load(route_file)
    width, height, margin = 900, 980, 55

    # Low-resolution GSHHS keeps the SVG compact while retaining real vector
    # coastlines and borders. This is not a raster trace.
    fig, ax = plt.subplots(figsize=(1, 1))
    m = make_basemap(ax=ax, resolution="l")
    countries = m.drawcountries().get_segments()
    plt.close(fig)

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<g fill="none" stroke="#222" stroke-width="1.4" stroke-linejoin="round">',
    ]
    for seg in m.coastsegs:
        lines.append(f'<path d="{path_from_segment(m, seg, width, height, margin)}"/>')
    lines.append('</g><g fill="none" stroke="#777" stroke-width="0.9" stroke-dasharray="3 3">')
    for seg in countries:
        lines.append(f'<path d="{path_from_segment(m, seg, width, height, margin)}"/>')
    lines.append('</g>')

    for feature in route["features"]:
        mode = feature["properties"].get("mode", "")
        pts = []
        for lon, lat in feature["geometry"]["coordinates"]:
            x, y = m(lon, lat)
            sx, sy = svg_point(m, x, y, width, height, margin)
            pts.append(f"{sx:.1f},{sy:.1f}")
        if "ferry" in mode:
            dash, stroke = ' stroke-dasharray="2 5"', "#2b6cb0"
        elif "public" in mode or "train" in mode:
            dash, stroke = ' stroke-dasharray="8 5"', "#2b6cb0"
        else:
            dash, stroke = "", "#2f855a"
        lines.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{stroke}" stroke-width="3"{dash}/>')

    for feature in stops["features"]:
        order = feature["properties"]["order"]
        name = escape(feature["properties"]["name"])
        lon, lat = feature["geometry"]["coordinates"]
        x, y = m(lon, lat)
        sx, sy = svg_point(m, x, y, width, height, margin)
        lines.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="8" fill="#4a5568" stroke="white" stroke-width="1.2"/>')
        lines.append(f'<text x="{sx:.1f}" y="{sy+3:.1f}" text-anchor="middle" font-family="sans-serif" font-size="8" font-weight="700" fill="white">{order}</text>')
        lines.append(f'<text x="{sx+10:.1f}" y="{sy-7:.1f}" font-family="sans-serif" font-size="10" fill="#111" style="paint-order:stroke;stroke:white;stroke-width:3px;stroke-linejoin:round">{name}</text>')

    lines += [
        f'<text x="{width/2:.0f}" y="27" text-anchor="middle" font-family="sans-serif" font-size="20" font-weight="700">{escape(title)}</text>',
        f'<text x="{width/2:.0f}" y="46" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#444">{escape(subtitle)}</text>',
        '<g transform="translate(66,900)" font-family="sans-serif" font-size="11">',
        '<line x1="0" y1="0" x2="34" y2="0" stroke="#2b6cb0" stroke-width="3" stroke-dasharray="8 5"/><text x="42" y="4">public transport</text>',
        '<line x1="0" y1="22" x2="34" y2="22" stroke="#2f855a" stroke-width="3"/><text x="42" y="26">rental car</text>',
        '<line x1="0" y1="44" x2="34" y2="44" stroke="#2b6cb0" stroke-width="3" stroke-dasharray="2 5"/><text x="42" y="48">ferry</text>',
        '</g>',
        f'<g transform="translate({width-78},90)" stroke="#111" fill="#111"><line x1="0" y1="32" x2="0" y2="0" stroke-width="2"/><path d="M0,0 l-5,10 h10 z"/><text x="0" y="48" text-anchor="middle" stroke="none" font-family="sans-serif" font-size="15" font-weight="700">N</text></g>',
        '</svg>',
    ]
    (HERE / f"{out_stem}.svg").write_text("\n".join(lines), encoding="utf-8")


def render(route_file, title, subtitle, out_stem):
    render_png(route_file, title, subtitle, out_stem)
    render_svg(route_file, title, subtitle, out_stem)


render(
    "route.geojson",
    "Faro → Porto → Atlantic North Spain → Bilbao → Porto",
    "30-day route · real coastlines/borders + WGS84 stop coordinates",
    "map-full-route",
)
render(
    "route-60-40.geojson",
    "Faro → Porto → Santiago/Picos → Bilbao → Porto",
    "60:40 highlights route · ~12 days",
    "map-60-40-route",
)
