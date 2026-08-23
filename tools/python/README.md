# TravelRoutes Python map tools

Reusable scripts used for the real-geography itinerary maps.

## Files

- `script.py` — main renderer. Reads an itinerary's `maps/stops.geojson`, `route.geojson`, and optional `route-60-40.geojson`; renders **SVG first**, then derives PNG from that SVG.
- `svg_to_png.py` — standalone SVG → PNG converter for existing maps.
- `requirements.txt` — Python dependencies for the preferred rendering path.

## Generate maps

From the repository root:

```bash
pip install -r tools/python/requirements.txt
python tools/python/script.py itineraries/Central-America-Guatemala-Belize-Mexico
```

Expected output:

```text
<itinerary>/maps/
├── map-full-route.svg
├── map-full-route.png
├── map-60-40-route.svg
└── map-60-40-route.png
```

## Convert SVG separately

```bash
python tools/python/svg_to_png.py \
  itineraries/Central-America-Guatemala-Belize-Mexico/maps/map-full-route.svg \
  itineraries/Central-America-Guatemala-Belize-Mexico/maps/map-60-40-route.svg
```

Use `--width 3000` for a larger raster export.

## Important invariant

**SVG is canonical. PNG must be rasterized from that exact SVG, not rendered independently.**

That guarantees both files show identical stop coordinates, coastline/border geometry, labels, numbering, and route lines.

The static renderer uses real GSHHS/Basemap geography and verified coordinates. When real OSRM/OpenRouteService/GraphHopper routing geometry is available, store that in the route GeoJSON rather than pretending straight planning connectors are exact roads.
