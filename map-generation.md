# Real Travel Map Generation Workflow

This document describes the reusable map workflow used by TravelRoutes.

The key rules are:

> **Never use an AI image generator to invent geography.**
>
> **Use verified coordinates + real cartographic data + programmatic rendering.**
>
> **Generate SVG first, then rasterize that exact SVG to PNG.**

Reusable code lives at:

`tools/python/script.py`

Trip-specific geographic data and outputs live in each itinerary's `maps/` folder, for example:

`itineraries/Central-America-Guatemala-Belize-Mexico/maps/`

Run the shared generator from repository root with:

```bash
python tools/python/script.py itineraries/Central-America-Guatemala-Belize-Mexico
```

---

## 1. Source-of-truth coordinates

Every stop must be represented by a verified longitude/latitude pair.

Useful sources include:

- OpenStreetMap / Nominatim;
- Wikidata;
- GeoNames;
- UNESCO coordinates;
- official national-park / archaeological data;
- authoritative specialist sources such as Smithsonian Global Volcanism Program.

Store stops in:

`maps/stops.geojson`

Example:

```json
{
  "type": "Feature",
  "properties": {
    "order": 1,
    "name": "Guatemala City",
    "country": "Guatemala"
  },
  "geometry": {
    "type": "Point",
    "coordinates": [-90.513268, 14.640725]
  }
}
```

GeoJSON ordering is always:

```text
[longitude, latitude]
```

Check every stop for:

1. correct country;
2. correct side of borders;
3. island vs mainland;
4. city vs archaeological/natural site;
5. expected compass direction from neighboring stops;
6. accidental latitude/longitude reversal.

Pins must never be positioned by eyeballing a picture.

---

## 2. Route semantics

A route is not one continuous road. Give every segment an explicit transport mode, such as:

```text
road
rail
road_border
hike
ferry
flight
flight_optional
```

Render the modes differently, for example:

- solid — road / normal land transport;
- dash-dot — hike;
- dotted — ferry;
- dashed — flight / optional extension.

This prevents misleading graphics such as a road drawn across open water.

---

## 3. Route geometry

### Preferred: routed geometry

When available, obtain real route geometry with services such as:

- OSRM;
- OpenRouteService;
- GraphHopper;
- official public-transit geometry.

Example OSRM concept:

```text
/route/v1/driving/<lon1>,<lat1>;<lon2>,<lat2>?overview=full&geometries=geojson
```

Save returned geometries to files such as:

```text
maps/route.geojson
maps/route-60-40.geojson
```

### Fallback: verified-stop planning connectors

If a routing backend is unavailable, a straight connector between two **verified stop coordinates** is acceptable for an overview map.

It must be labeled honestly as a planning connector and must **not** be described as exact road-centerline geometry.

Flights, ferries and hikes should remain explicitly classified rather than being forced through a driving API.

---

## 4. Real map base

The Guatemala / Belize / Mexico static maps used real GSHHS coastlines and country boundaries through Python/Basemap.

Other good approaches include:

- GeoPandas + Cartopy;
- GeoPandas + Contextily with an appropriate OSM-derived provider;
- MapLibre;
- QGIS;
- other real vector/cartographic datasets.

For interactive maps, Leaflet + OpenStreetMap is appropriate when used according to OpenStreetMap's tile usage policy.

Do not bulk-download or abuse the public `tile.openstreetmap.org` service as an unrestricted static rendering backend.

---

## 5. Canonical SVG → PNG pipeline

This is the standard TravelRoutes map pipeline:

```text
verified coordinates
        ↓
stops.geojson
        ↓
route.geojson / route-60-40.geojson
        ↓
real coastline/border/routing data
        ↓
programmatic map rendering
        ↓
CANONICAL SVG
        ↓
SVG rasterization
        ↓
PNG
```

### Why SVG first?

Generating PNG and SVG independently can introduce differences in:

- label position;
- stop numbering;
- clipping;
- route geometry;
- map extent;
- fonts/layout.

Instead:

1. render the complete map as SVG;
2. inspect/accept the SVG;
3. rasterize that same SVG to PNG;
4. never separately re-render the PNG from raw plotting code.

This guarantees that raster and vector versions represent the same map.

### Expected outputs

```text
maps/
├── map-full-route.svg
├── map-full-route.png
├── map-60-40-route.svg
├── map-60-40-route.png
├── stops.geojson
├── route.geojson
├── route-60-40.geojson
└── interactive-map.html
```

---

## 6. Reusable script

The reusable Python tool is deliberately kept as one file:

```text
tools/python/script.py
```

It:

1. reads the itinerary's `maps/stops.geojson`;
2. reads `route.geojson` and optional `route-60-40.geojson`;
3. draws real coastlines/borders;
4. places stop pins from coordinates;
5. applies mode-specific route styling;
6. saves the **SVG** first;
7. rasterizes that SVG to the corresponding **PNG**.

Dependencies are documented in the script header. The preferred SVG→PNG converter is CairoSVG; the script also tries `rsvg-convert`, Inkscape and ImageMagick.

Typical command:

```bash
python tools/python/script.py itineraries/Central-America-Guatemala-Belize-Mexico
```

Reusable tooling belongs under `tools/`, not copied into every itinerary folder.

---

## 7. Interactive OpenStreetMap map

The same GeoJSON source can drive Leaflet or MapLibre.

Minimal Leaflet concept:

```html
<div id="map"></div>
<script>
const map = L.map('map').setView([17.5, -89.5], 6);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);
fetch('stops.geojson')
  .then(r => r.json())
  .then(data => L.geoJSON(data).addTo(map));
</script>
```

The interactive and static maps should use the same `stops.geojson` source so they cannot disagree about stop locations.

---

## 8. Full-route vs 60:40 maps

Do not manually redraw a second map.

Both map variants should use the same coordinate dataset. Only selected stops and route-segment lists change.

That ensures the same destination always appears at exactly the same coordinates in both maps.

The 60:40 version may include strategic flights that do not appear in the slower full route when those flights save major transfer time.

---

## 9. Map quality-control checklist

Before accepting a map, verify:

- [ ] coastlines are real geographic shapes;
- [ ] country borders are real/correct;
- [ ] every pin comes from coordinates;
- [ ] longitude/latitude are not reversed;
- [ ] islands are offshore in the correct location;
- [ ] road segments are not falsely drawn across water;
- [ ] ferry, flight and hike segments are visually distinguishable;
- [ ] stop numbering matches the itinerary;
- [ ] full and 60:40 maps share the same coordinate source;
- [ ] exact-road geometry is claimed only when produced by a real routing source;
- [ ] map attribution is retained where required;
- [ ] SVG was generated first;
- [ ] PNG was rasterized from that SVG;
- [ ] PNG visually matches the SVG exactly.

---

## 10. Repository architecture

The repository-wide convention is:

```text
TravelRoutes/
├── prompt.md
├── map-generation.md
├── itineraries/
│   ├── Central-America-Guatemala-Belize-Mexico/
│   │   ├── README.md
│   │   ├── *.md
│   │   ├── data/
│   │   └── maps/
│   └── Another-Trip/
│       └── ...
└── tools/
    └── python/
        └── script.py
```

The architectural principle is:

> **Trip folders contain research/data/output; root-level `tools/` contains reusable code. GeoJSON is the geographic source of truth, SVG is the visual source of truth, and PNG is a raster derivative of the SVG.**
