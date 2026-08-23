#!/usr/bin/env python3
"""
Regenerate the real-geography route maps.

Dependencies:
    matplotlib
    basemap

Inputs:
    stops.geojson
    route.geojson
    route-60-40.geojson

The map base uses Basemap/GSHHS coastlines and country boundaries. Pins come from
verified geographic coordinates. Route lines are planning connectors; they do not
claim to follow exact road centerlines.
"""
from pathlib import Path
import json
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from mpl_toolkits.basemap import Basemap

HERE = Path(__file__).resolve().parent

def load(path):
    return json.loads((HERE/path).read_text(encoding="utf-8"))

stops = load("stops.geojson")
by = {f["properties"]["name"]: f for f in stops["features"]}

def basemap(ax, title, subtitle):
    m = Basemap(
        projection="merc",
        llcrnrlon=-92.4, llcrnrlat=13.7,
        urcrnrlon=-86.15, urcrnrlat=21.65,
        resolution="i", ax=ax
    )
    m.fillcontinents(lake_color="white", alpha=.45)
    m.drawcoastlines(linewidth=.8)
    m.drawcountries(linewidth=1.0)
    m.drawparallels(range(14,22,2), labels=[1,0,0,0], fontsize=7, linewidth=.25, dashes=[2,2])
    m.drawmeridians(range(-92,-85,2), labels=[0,0,0,1], fontsize=7, linewidth=.25, dashes=[2,2])
    ax.set_title(title, fontsize=19, fontweight="bold", pad=18)
    ax.text(.5,1.01,subtitle,transform=ax.transAxes,ha="center",fontsize=10)
    return m

def xy(m,name):
    lon,lat=by[name]["geometry"]["coordinates"]
    return m(lon,lat)

def draw_route(ax,m,route):
    for f in route["features"]:
        a=f["properties"]["from"]; b=f["properties"]["to"]; mode=f["properties"]["mode"]
        x1,y1=xy(m,a); x2,y2=xy(m,b)
        style="--" if "flight" in mode else ":" if "ferry" in mode else "-." if "hike" in mode else "-"
        ax.plot([x1,x2],[y1,y2],linestyle=style,linewidth=2.1,alpha=.9)

def add_points(ax,m,names):
    for i,name in enumerate(names,1):
        x,y=xy(m,name)
        ax.scatter([x],[y],s=55,zorder=8,edgecolor="white",linewidth=1)
        ax.annotate(str(i),(x,y),ha="center",va="center",fontsize=7.5,fontweight="bold",color="white",zorder=9)
        ax.annotate(name.replace(" / Fuego hike"," / Fuego").replace(" National Park",""),
                    (x,y),xytext=(7,7),textcoords="offset points",fontsize=8,
                    bbox=dict(boxstyle="round,pad=.15",fc="white",alpha=.75,ec="none"),zorder=10)

def render(route_file,names,title,subtitle,out_name):
    fig,ax=plt.subplots(figsize=(10,12.5),dpi=180)
    m=basemap(ax,title,subtitle)
    draw_route(ax,m,load(route_file))
    add_points(ax,m,names)
    ax.legend(handles=[
        Line2D([0],[0],lw=2.2,label="road/overland"),
        Line2D([0],[0],lw=2.2,linestyle="-.",label="hike"),
        Line2D([0],[0],lw=2.2,linestyle=":",label="ferry"),
        Line2D([0],[0],lw=2.2,linestyle="--",label="flight"),
    ],loc="lower left",fontsize=8)
    fig.tight_layout()
    fig.savefig(HERE/out_name,bbox_inches="tight")
    plt.close(fig)

full_names=[f["properties"]["name"] for f in stops["features"] if f["properties"]["order"] <= 14]
compact=["Guatemala City","Antigua Guatemala","Acatenango / Fuego hike","Flores","Tikal National Park",
         "San Ignacio","Belize City","Caye Caulker","Valladolid","Chichén Itzá","Cancún"]

render("route.geojson",full_names,"Guatemala → Belize → Yucatán",
       "General ~28-day route · real cartography + verified coordinates","map-full-route.png")
render("route-60-40.geojson",compact,"Guatemala → Belize → Yucatán",
       "60:40 highlights route · strategic flights save transfer days","map-60-40-route.png")
