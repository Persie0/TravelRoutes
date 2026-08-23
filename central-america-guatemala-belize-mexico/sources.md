# Sources, articles, coordinate references & visuals

Research snapshot: **2026-08-23**.

This file favors primary/official sources. Independent visual references are separated from factual sources.

## Official / primary destination sources

| Source | Organization | Supports |
|---|---|---|
| https://whc.unesco.org/en/list/65/ | UNESCO | Antigua Guatemala heritage significance |
| https://whc.unesco.org/en/list/64/ | UNESCO | Tikal World Heritage status, coordinates, cultural/natural value |
| https://whc.unesco.org/en/list/764/ | UNESCO | Belize Barrier Reef Reserve System |
| https://volcano.si.edu/volcano.cfm?vn=342080 | Smithsonian Global Volcanism Program | Acatenango coordinates/elevation/volcanic context |
| https://www.travelbelize.org/attraction/actun-tunichil-muknal-atm/ | Belize Tourism | ATM route/physical nature/archaeological context |
| https://www.travelbelize.org/attraction/blue-hole/ | Belize Tourism | Great Blue Hole size and ways to experience it |
| https://www.travelbelize.org/attraction/hol-chan-marine-reserve/ | Belize Tourism | Hol Chan reserve |
| https://www.travelbelize.org/attraction/shark-ray-alley/ | Belize Tourism | Shark Ray Alley |
| https://yucatan.travel/en/archeological-area/chichen-itza/ | Yucatán Tourism | Chichén Itzá monuments and heritage |
| https://yucatan.travel/en/culture/magic-town-of-valladolid/ | Yucatán Tourism | Valladolid and nearby archaeology |
| https://yucatan.travel/en/archaeological-sites/ | Yucatán Tourism | regional archaeology context |
| https://www.gob.mx/sectur/articulos/bacalar-quintana-roo?idiom=es | Mexico Secretaría de Turismo | Bacalar attractions |

## Climate / season sources

| Source | Supports |
|---|---|
| https://nms.gov.bz/climate-services/climate-summary/ | Belize dry/rainy season, hurricane/cold-front climatology |
| https://nms.gov.bz/climate-services/climatology/ | Belize 1991–2020 monthly climate normals |
| https://www.yucatan.gob.mx/procivy/temporada_ciclones.php | official Yucatán tropical cyclone season |
| https://www.yucatan.gob.mx/procivy/ver_nota.php?id=1041 | September as critical cyclone period in Yucatán |
| https://www.weather.gov/media/tbw/1921/Climatology.pdf | Atlantic hurricane climatology / September peak |

## Transport / flight sources

| Source | Supports |
|---|---|
| https://www.rome2rio.com/ | route-mode comparison and planning durations |
| https://skyscanner.net/g/referrals/v1/flights/home?mediaPartnerId=2850210&utm_term=skyscanner_chatgpt_app_data | indicative Europe↔Central America/Yucatán airfare research |
| https://www.tropicair.com/route-map/ | Tropic Air network |
| https://flights.tropicair.com/en/flights-from-belize-city-goldson-international-to-cancun | BZE→CUN service |
| https://www.directflights.com/GUA-FRS | current nonstop GUA→FRS schedule overview |
| https://www.flightconnections.com/flights-from-gua-to-frs | GUA→FRS airline/frequency cross-check |

## Real-map coordinate sources

The maps are generated from the coordinates saved in `maps/stops.geojson`.

OSM-derived Mapcarta pages:
- Antigua: https://mapcarta.com/Antigua_Guatemala
- Semuc Champey: https://mapcarta.com/Semuc_Champey
- Flores: https://mapcarta.com/Flores_%28Guatemala%29
- San Ignacio: https://mapcarta.com/San_Ignacio_%28Belize%29
- Belize City: https://mapcarta.com/Belize_City
- Caye Caulker: https://mapcarta.com/Caye_Caulker
- Bacalar: https://mapcarta.com/Bacalar
- Valladolid: https://mapcarta.com/Valladolid_%28Mexico%29
- Cancún: https://mapcarta.com/Canc%C3%BAn
- Mexico City: https://mapcarta.com/Mexico_City

Authoritative specialist coordinates:
- Acatenango: Smithsonian GVP, 14.501 N / 90.876 W.
- Tikal: UNESCO, N17 13 0 / W89 37 0.
- Chichén Itzá: UNESCO protected-property coordinate around N20 40 51.596 / W88 34 5.059.

## Visual / article references

Use these to understand the look/character of the stops; they are not map-coordinate sources.

- Acatenango/Fuego visual article: https://uprootedtraveler.com/acatenango-hike/
- Semuc Champey visual article: https://myadventuresacrosstheworld.com/visiting-semuc-champey-guatemala/
- Tikal visual reference: https://www.anywhere.com/guatemala/attractions/tikal
- Belize reef context: https://caribbeanlifestyle.com/glovers-reef-atoll/
- Yucatán/Chichén: https://yucatan.travel/en/archeological-area/chichen-itza/

## Map-data methodology

The generated maps are **not AI-generated geography**.

- stop pins: verified geographic coordinates;
- coastline/country borders: GSHHS real cartographic data;
- route lines: planning connectors between verified stops;
- ferry/flight segments: visually distinct;
- `route.geojson` explicitly labels connector geometry as non-road-centerline.

A live OSRM/OpenRouteService endpoint was not available inside the execution environment. The repository keeps the GeoJSON and map-generation source so exact road-centerline routing can be substituted later without changing the verified stop coordinates.
