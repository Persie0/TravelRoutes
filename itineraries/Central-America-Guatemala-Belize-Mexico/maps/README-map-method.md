# Map method

These maps are **programmatically rendered from real geographic coordinates**. They are not AI-generated geography.

## Canonical pipeline

1. Keep verified stop coordinates in `stops.geojson`.
2. Keep the full and 60:40 route semantics in `route.geojson` and `route-60-40.geojson`.
3. Render the map to **SVG first** using real coastline/country-border geometry.
4. Treat that SVG as the canonical visual artifact.
5. Generate the PNG **from the exact SVG** rather than rendering PNG independently. This guarantees identical pin positions, route lines, labels, borders and crop.

Current shared generator:

```bash
python ../../../tools/python/script.py ..
```

When run from this `maps/` folder, `..` resolves to the itinerary directory. From the repository root, use:

```bash
python tools/python/script.py itineraries/Central-America-Guatemala-Belize-Mexico
```

The script writes:

- `map-full-route.svg`
- `map-full-route.png` — rasterized from `map-full-route.svg`
- `map-60-40-route.svg`
- `map-60-40-route.png` — rasterized from `map-60-40-route.svg`

## Geography sources

- Coastlines/country borders: Basemap/GSHHS data bundled with the mapping library.
- Stop coordinates: OSM-derived references where available, plus UNESCO/Smithsonian/other authoritative coordinates for major heritage and natural sites.
- `stops.geojson`: authoritative point dataset used to place pins.
- `route.geojson`: planning connectors between verified stops.

The saved connector lines **do not claim to follow exact road centerlines** unless a routed geometry source was explicitly used.

## Better network-enabled version

When network routing is available, replace road connector geometries with OSRM, OpenRouteService or GraphHopper output while preserving the same verified stop coordinates. Keep ferry, flight and hike segments semantically distinct and visually dashed/dotted as appropriate.

## SVG → PNG conversion

The shared Python tool prefers `cairosvg`. It falls back to `rsvg-convert`, Inkscape, or ImageMagick if available. The important rule is that PNG must be generated from the committed SVG, not separately redrawn.
