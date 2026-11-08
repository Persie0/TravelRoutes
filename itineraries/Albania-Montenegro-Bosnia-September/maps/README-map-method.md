# Geographic map method — Albania / Montenegro / Bosnia

The route's static maps are **real SVG geographic visualizations**, not generated geographic illustrations.

## Input data and accuracy

- `stops.geojson` has **21 WGS84 location points**, with standard GeoJSON coordinate order **[longitude, latitude]** and country labels. These are approximate town/park/place centers (not precise airport gate, ferry pier or trailhead coordinates).
- `route.geojson` and `route-60-40.geojson` contain explicit mode strings (road, bus/rail, ferry, hike) for the trip's key travel legs. **Each two-point LineString is a straight planning connector**, not routed OSRM geometry. Do not use lines as driving/hiking navigation.
- `map-config.json` defines the numbered stops and scope for each static SVG.
- Geographic bounds encompass Bosnia, Montenegro, Albania, the Dubrovnik gateway and Corfu exit. Latitude and longitude were sanity-checked for broad country, relative direction and coastline consistency.

## Rendering and cartography

**Map lineage:** checked place centres and route geometry → GeoJSON → static **SVG** with real GSHHS/Basemap low-resolution **coastline and country borders** → committed map files.

- `map-full-route.svg`: main 28-day route with numbered stops, real shoreline/border vectors, legend, north arrow, attribution.
- `map-60-40-route.svg`: condensed 12-day route with same geographic extent and mode legend.
- The included SVGs use an equirectangular city-to-canvas transformation scaled to a fixed regional viewport and cartographic GSHHS path features extracted and transformed to the same view. They are *not hand-estimated* coastlines or invented road tracks.
- The existing root [shared generator](../../../tools/python/script.py) is the **reproducible conventional renderer**, using GeoJSON plus Basemap directly. Run from root: `python tools/python/script.py itineraries/Albania-Montenegro-Bosnia-September`. This regenerates the SVGs and may change visual styling/layout while preserving the geographic source of truth.
- `interactive-map.html` uses Leaflet, standard user-driven OpenStreetMap tiles, and inline WGS84 place-centre equivalents. It loads no tiles in batches.
- The Speedrun uses the same material sequence of stops as the full route, so a redundant static Speedrun map is unnecessary.

## Limitations and attribution

- The boundary vectors are from GSHHS via Basemap; `OpenStreetMap contributors` credit applies to geocoding/map-reference checks and dynamic OSM tiles, not as an assertion that GSHHS is OSM.
- The static SVG is suitable for geographical overview and travel planning only. For navigation and border crossings use current operator guidance, actual ferry tickets, official hiking route maps and current turn-by-turn routing.
- Stop coordinates require more precise pier, pickup, museum or trailhead coordinates before navigation.
- In case a ferry, hiking trail or mountain pass is closed, the straight connectors **must not** imply a feasible route through that location.
