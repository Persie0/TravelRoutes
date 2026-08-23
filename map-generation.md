# Real Travel Map Generation Workflow

This document explains the map-generation approach used for the Guatemala → Belize → Mexico route and provides a reusable method for future itineraries.

The key rule is simple:

> **Do not use an AI image generator to invent geography.**
>
> Use verified coordinates + real cartographic data + programmatic rendering.

The maps for the Belize / Guatemala / Mexico route live in:

`central-america-guatemala-belize-mexico/maps/`

Relevant files include:

- `map-full-route.png`
- `map-full-route.svg`
- `map-60-40-route.png`
- `map-60-40-route.svg`
- `stops.geojson`
- `route.geojson`
- `README-map-method.md`

---

## 1. Verify coordinates for every stop

Every stop is represented by a real latitude/longitude pair.

Coordinate sources used for this route included:

- OpenStreetMap-derived place data where practical;
- UNESCO coordinates for World Heritage sites such as Tikal;
- Smithsonian Global Volcanism Program coordinates for Acatenango;
- GeoNames / other geographic cross-checks for major cities.

Example stop structure:

```json
{
  "type": "Feature",
  "properties": {
    "order": 1,
    "name": "Guatemala City",
    "country": "Guatemala",
    "coordinate_source": "GeoNames / geographic cross-check"
  },
  "geometry": {
    "type": "Point",
    "coordinates": [-90.513268, 14.640725]
  }
}
```

Remember that GeoJSON coordinates are always:

```text
[longitude, latitude]
```

not latitude first.

### Validation pass

Before rendering, verify each point against its neighbors.

Check at minimum:

1. correct country;
2. correct side of any international border;
3. island vs mainland;
4. archaeological site vs nearby town;
5. expected compass direction from previous/next stop;
6. no accidental lat/lon reversal.

For this itinerary the resulting point set is stored in:

`central-america-guatemala-belize-mexico/maps/stops.geojson`

---

## 2. Store stops in GeoJSON

Use a `FeatureCollection` so the same data can drive:

- static PNG maps;
- SVG maps;
- Leaflet / MapLibre web maps;
- GIS software;
- routing APIs;
- future itinerary scripts.

Recommended schema:

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "order": 1,
        "name": "Example Stop",
        "country": "Example Country"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [12.3456, 45.6789]
      }
    }
  ]
}
```

The stop file should be the source of truth for map pins rather than manually placing pins on an image.

---

## 3. Separate route semantics by transport type

The route is not one continuous road.

Segments should know what they represent, for example:

```text
road
road_border
hike
ferry
flight
flight_optional
```

For this route:

- Antigua ↔ Acatenango = hike;
- Belize City ↔ Caye Caulker = ferry;
- optional Cancún → Mexico City = flight;
- most other legs = road / overland connectors.

This makes it possible to render each mode differently:

- solid = road / normal overland segment;
- dash-dot = hike;
- dotted = ferry;
- dashed = flight / optional extension.

This prevents misleading lines such as drawing a normal road across open water.

---

## 4. Route geometry: planning connectors vs real road centerlines

Two levels of route geometry are useful.

### Level A — verified-stop connectors

This is what was used for the generated static route maps when a live routing endpoint was not available in the execution environment.

Each segment is a line between two verified geographic stop coordinates.

This is accurate for showing:

- overall itinerary geography;
- stop order;
- direction of travel;
- which segments are ferry, hike or flight;
- relative spacing between destinations.

It does **not** claim that the line follows the exact road centerline.

The repository therefore explicitly describes these lines as planning connectors.

### Level B — real routed geometry

When network access to a routing backend is available, this should be preferred for road segments.

Good options include:

#### OSRM

Open Source Routing Machine.

Typical API concept:

```text
/route/v1/driving/<lon1>,<lat1>;<lon2>,<lat2>?overview=full&geometries=geojson
```

Save the returned route geometry into `route.geojson`.

#### OpenRouteService

Useful when API access is available and may offer richer profile options.

#### GraphHopper

Another good option for road routing and multiple transport profiles.

### Important

Do not route ferry or air segments through a driving API.

Keep them explicitly classified and render them separately.

---

## 5. Real map base used for the static maps

The static route maps were rendered programmatically using real geographic coastline and country-boundary geometry.

The implementation used Python mapping tools with **GSHHS** geographic data through Basemap.

GSHHS provides real:

- coastlines;
- land/water boundaries;
- national-border geometry.

This avoids the problem that occurred with generative maps, where the shape of Belize, Guatemala and the Yucatán Peninsula was distorted and stops appeared in incorrect locations.

### Why this is better than asking an image model for a map

An image generator can create an attractive travel poster, but it does not guarantee:

- correct latitude/longitude;
- correct coastlines;
- correct country borders;
- correct relative location of cities;
- correct route geometry.

For travel planning, spatial correctness matters more than illustration quality.

---

## 6. Static rendering workflow

The practical workflow used was:

```text
verified coordinates
        ↓
stops.geojson
        ↓
route segment definitions
        ↓
real coastline/border data
        ↓
programmatic projection
        ↓
numbered route markers + labels
        ↓
PNG + SVG
```

The map renderer:

1. creates a north-up regional map extent;
2. draws real coastlines;
3. draws international boundaries;
4. places pins using longitude/latitude;
5. connects the appropriate route segments;
6. styles each mode separately;
7. adds labels and stop numbers;
8. adds a legend and geographic disclaimer;
9. exports both raster and vector versions.

### PNG

Best for:

- README preview images;
- messaging;
- social sharing;
- simple web display.

### SVG

Best for:

- GitHub;
- scalable display;
- editing in vector software;
- keeping text and linework sharp at any zoom.

---

## 7. Example Python structure

A simplified version looks like this:

```python
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

stops = {
    "Guatemala City": (14.640725, -90.513268),
    "Antigua Guatemala": (14.5568, -90.7337),
    "Tikal": (17.216667, -89.616667),
    "San Ignacio": (17.1528, -89.0762),
    "Caye Caulker": (17.7425, -88.0250),
    "Cancún": (21.1527, -86.8426),
}

fig, ax = plt.subplots(figsize=(10, 12))

m = Basemap(
    projection="merc",
    llcrnrlon=-92.4,
    llcrnrlat=13.7,
    urcrnrlon=-86.15,
    urcrnrlat=21.65,
    resolution="i",
    ax=ax,
)

m.drawcoastlines()
m.drawcountries()
m.fillcontinents(lake_color="lightblue")
m.drawmapboundary(fill_color="lightblue")

for name, (lat, lon) in stops.items():
    x, y = m(lon, lat)
    ax.scatter(x, y)
    ax.annotate(name, (x, y))

plt.savefig("map.png", dpi=180, bbox_inches="tight")
plt.savefig("map.svg", bbox_inches="tight")
```

The production version should also add mode-specific route lines, numbering, tuned label offsets and legends.

---

## 8. OpenStreetMap / Leaflet version

For an interactive map, use the same `stops.geojson` with Leaflet or MapLibre.

Example Leaflet concept:

```html
<div id="map"></div>

<script>
const map = L.map('map').setView([17.5, -89.5], 6);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

fetch('stops.geojson')
  .then(r => r.json())
  .then(data => {
    L.geoJSON(data).addTo(map);
  });
</script>
```

### OpenStreetMap tile warning

Do not bulk-download the public `tile.openstreetmap.org` service or use it as an unrestricted static-map rendering backend.

For larger/static production use, choose a suitable OSM-derived tile provider or render from geographic vector data.

Always keep the required map attribution.

---

## 9. 60:40 map generation

The condensed 60:40 map is generated from the same geographic dataset, not from a separately drawn picture.

Only the selected stops and segment list change.

For this route the 60:40 version protects high-value experiences such as:

- Acatenango / Fuego;
- Tikal;
- ATM Cave / San Ignacio;
- Caye Caulker + Belize reef;
- Chichén Itzá.

It can use strategic flights for time savings where that preserves a much higher ratio of sightseeing value per travel day.

Because both maps share the same coordinates, stop locations remain consistent between the full and 60:40 versions.

---

## 10. Recommended future implementation

For future TravelRoutes itineraries, use this pipeline:

### Step 1

Research the actual stop list.

### Step 2

Geocode every stop with Nominatim / OpenStreetMap, Wikidata, GeoNames or authoritative coordinates.

### Step 3

Verify the coordinates manually against a real map.

### Step 4

Write `stops.geojson`.

### Step 5

Classify every route leg:

```text
road / rail / ferry / flight / hike
```

### Step 6

Use OSRM / OpenRouteService / GraphHopper for routable land legs where possible.

### Step 7

Write `route.geojson`.

### Step 8

Render static maps using real geographic data.

Recommended libraries:

- GeoPandas;
- Cartopy;
- Matplotlib;
- Contextily with a suitable tile provider;
- MapLibre;
- QGIS for manual refinement.

### Step 9

Create a Leaflet/MapLibre interactive version from the same GeoJSON.

### Step 10

Export:

```text
maps/
├── map-full-route.png
├── map-full-route.svg
├── map-60-40-route.png
├── map-60-40-route.svg
├── stops.geojson
├── route.geojson
└── interactive-map.html
```

---

## 11. Quality-control checklist

Before accepting a generated route map, verify:

- [ ] coastlines are real geographic shapes;
- [ ] national borders are correct;
- [ ] every point is based on coordinates, not visual guessing;
- [ ] longitude and latitude are not reversed;
- [ ] island destinations appear offshore in the correct location;
- [ ] road lines are not drawn across water;
- [ ] ferry segments are visibly distinct;
- [ ] flight segments are visibly distinct;
- [ ] stop numbering matches the itinerary;
- [ ] the 60:40 map uses the same source coordinates;
- [ ] exact-road geometry is only claimed when a real routing API produced it;
- [ ] map-data attribution is retained where required.

---

## 12. Best-practice architecture for this repository

For each future itinerary subfolder, keep the geographic files next to the route research:

```text
trip-name/
├── README.md
├── itinerary-28-days.md
├── itinerary-60-40.md
├── transport-and-route-optimization.md
├── sights.md
├── weather-and-timing.md
└── maps/
    ├── map-full-route.png
    ├── map-full-route.svg
    ├── map-60-40-route.png
    ├── map-60-40-route.svg
    ├── stops.geojson
    ├── route.geojson
    └── interactive-map.html
```

The important architectural idea is that the **GeoJSON is the source of truth** and every visual map should be generated from it.
