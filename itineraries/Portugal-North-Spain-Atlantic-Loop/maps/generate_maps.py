#!/usr/bin/env python3
"""Regenerate real-geography route maps as PNG and SVG.

Dependencies: matplotlib, basemap
Inputs: stops.geojson, route.geojson, route-60-40.geojson

Static cartography uses Basemap/GSHHS real coastlines and international borders.
Route lines are planning connectors between verified WGS84 stops, not claims of
exact road/rail centreline geometry. The interactive HTML uses OpenStreetMap.
"""
from pathlib import Path
import json
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from mpl_toolkits.basemap import Basemap

HERE = Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def render(route_file, title, subtitle, out_stem):
    stops = load("stops.geojson")
    route = load(route_file)
    fig, ax = plt.subplots(figsize=(11, 11), dpi=180)
    m = Basemap(
        projection="merc",
        llcrnrlon=-10.3,
        llcrnrlat=36.4,
        urcrnrlon=-2.0,
        urcrnrlat=44.2,
        resolution="i",
        ax=ax,
    )
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
        ls = ":" if "ferry" in mode else "--" if "public" in mode or "train" in mode else "-"
        ax.plot(xs, ys, lw=2.1, ls=ls, alpha=.9)

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
    # Keep the raster output for easy viewing and add a true vector SVG from
    # exactly the same figure so both formats stay in sync.
    fig.savefig(HERE / f"{out_stem}.png", bbox_inches="tight")
    fig.savefig(HERE / f"{out_stem}.svg", format="svg", bbox_inches="tight")
    plt.close(fig)


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
