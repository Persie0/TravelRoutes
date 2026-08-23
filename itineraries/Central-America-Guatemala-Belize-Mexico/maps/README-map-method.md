# Map method

These maps are **programmatically rendered from real geographic coordinates**. They are not AI-generated geography.

## Canonical pipeline

1. Keep verified stop coordinates in `stops.geojson`.
2. Keep the full and 60:40 route semantics in `route.geojson` and `route-60-40.geojson`.
3. Render the maps as **SVG** using real coastline/country-border geometry.
4. Treat the SVG files as the final static map artifacts.
5. Commit/upload those SVG files directly to GitHub together with the GeoJSON source files.

Current shared generator:

```bash
python tools/python/script.py itineraries/Central-America-Guatemala-Belize-Mexico
```

The script writes:

- `map-full-route.svg`
- `map-60-40-route.svg`

No PNG copy is required by default.

## Geography sources

- Coastlines/country borders: Basemap/GSHHS data bundled with the mapping library.
- Stop coordinates: OSM-derived references where available, plus UNESCO/Smithsonian/other authoritative coordinates for major heritage and natural sites.
- `stops.geojson`: authoritative point dataset used to place pins.
- `route.geojson`: planning connectors between verified stops.

The saved connector lines **do not claim to follow exact road centerlines** unless a routed geometry source was explicitly used.

## Better network-enabled version

When network routing is available, replace road connector geometries with OSRM, OpenRouteService or GraphHopper output while preserving the same verified stop coordinates. Keep ferry, flight and hike segments semantically distinct and visually dashed/dotted as appropriate.

## GitHub output

The reproducible map package committed to GitHub is:

```text
map-full-route.svg
map-60-40-route.svg
stops.geojson
route.geojson
route-60-40.geojson
```

SVG is preferred because it is scalable, text-based, Git-friendly and can be embedded directly in Markdown. If a PNG is ever needed for another platform, it can be created later from the committed SVG without changing the repository's canonical map format.
