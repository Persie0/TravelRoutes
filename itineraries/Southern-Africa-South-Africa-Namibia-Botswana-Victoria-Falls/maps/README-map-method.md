# Map method

The static route maps in this folder are **not AI-generated geography**.

## Source of truth

- `stops.geojson`: verified point coordinates.
- `route.geojson`: full-route planning connectors.
- `route-60-40.geojson`: condensed-route planning connectors.
- `map-config.json`: titles and explicit stop lists for the reusable renderer.

Coordinates were cross-checked against combinations of **GeoNames, Wikidata, UNESCO geographic data, official park/tourism material, and OpenStreetMap-backed map sources**. GeoJSON uses `[longitude, latitude]`.

## Geometry limitation

The saved LineStrings connect verified stops and preserve transport semantics (`road`, `4x4`, `flight`, `border shuttle`, etc.), but they are **planning connectors, not claimed road-centerline GPS tracks**. This is deliberate where a reliable live routing export was unavailable during research.

## Rendering

Run from repository root:

```bash
python tools/python/script.py itineraries/Southern-Africa-South-Africa-Namibia-Botswana-Victoria-Falls
```

The generator uses real GSHHS/Basemap coastlines and country borders and writes SVG directly. The SVG is the canonical static artifact. The Leaflet file uses OpenStreetMap tiles interactively and retains OSM attribution.