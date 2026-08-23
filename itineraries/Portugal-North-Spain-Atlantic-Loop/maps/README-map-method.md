# Map method

- **Static PNGs:** generated locally and reproducibly with Basemap/GSHHS real coastlines and international borders.
- **Interactive map:** `interactive-map.html` uses Leaflet + OpenStreetMap tiles and the same WGS84 stop coordinates.
- **Coordinates:** city/POI centroids were checked against official tourism/location references; As Catedrais is aligned to the published Turismo de Galicia location.
- **Route geometry:** GeoJSON line segments are **planning connectors** between verified stops. They are intentionally not presented as exact road centreline geometry. Use a live router for turn-by-turn driving.
- No generative image model was used for geography.
- The session’s GitHub connector can write text but does not expose a local-binary-path upload parameter, so the generated PNGs are not embedded in the repository; regenerate them with `python generate_maps.py`.