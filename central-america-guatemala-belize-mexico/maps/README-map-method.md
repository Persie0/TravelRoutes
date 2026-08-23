# Map method

These maps are **programmatically rendered from real geographic coordinates**. They are not AI-generated geography.

- Coastlines/country borders: Basemap/GSHHS data bundled with the mapping library.
- Stop coordinates: OSM-derived Mapcarta entries where available, plus UNESCO and Smithsonian coordinates for heritage/natural sites.
- `stops.geojson`: authoritative stop-point dataset used to place pins.
- `route.geojson`: planning connectors between verified stops. These lines **do not claim to follow exact road centerlines** because a live OSRM/OpenRouteService endpoint was not available in the execution environment.

For a network-enabled rerun, replace connector geometries with OSRM/OpenRouteService/GraphHopper road routes while preserving the same stop coordinates and ferry/flight semantics.
