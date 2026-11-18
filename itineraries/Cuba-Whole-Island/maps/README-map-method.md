# Cuba map sources and method

Generated 2026-11-18. Source of truth: `stops.geojson`, `route.geojson`, `route-60-40.geojson`, `map-config.json`.

- Longitude/latitude follow GeoJSON `[longitude, latitude]`; every geocoded stop lies in Cuba. Settlement-centre coordinates use coordinate links recorded in each feature, from GeoNames, UNGEGN, geodatos and other geographic gazetteers.
- The SVG **land outline is actual Cuba polygon geometry**, sourced from the Natural Earth-based [johan/world.geo.json Cuba FeatureCollection](https://github.com/johan/world.geo.json/blob/master/countries/CUB.geo.json), not drawn by an image generator. Low-resolution shape sacrifices coastal detail; it is not a navigational chart.
- Links between coordinates are **geodesic planning connectors rendered as straight segments**, *not* surveyed road tracks. Flight line Santiago–Havana is conditional, **not a confirmed operating service**. No ferry or fictional bridge is implied.
- The SVG is a direct vector geographic rendering. The reusable repository script [tools/python/script.py](../../../../tools/python/script.py) can also regenerate an SVG from the same GeoJSON via Basemap/GSHHS; it may have different aesthetics. No bulk OpenStreetMap tiles were used in these SVGs.
- `interactive-map.html` loads the exact same GeoJSON with Leaflet and © OpenStreetMap contributors when hosted on a local server or GitHub Pages.
- Route conditions and transport schedules must be rechecked, especially under the 2026 fuel shortage; see [transport notes](../transport-and-route-optimization.md).
