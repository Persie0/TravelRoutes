# Sources and methodology

**Research date 2026-11-19.** The travel warning, attraction fees and air quotes are time-sensitive and need refreshing prior to bookings.

| Type | Source | Verification purpose |
|---|---|---|
| Official | [BMEIA Austrian travel advisory](https://www.bmeia.gv.at/reise-services/reiseinformation/land/jordanien) | Level 3/4 security, Austrian visa and registration rules |
| Official | [Jordan Pass official pricing](https://jordanpass.jo/contents/Prices.aspx) | 70/75/80 JOD, visa fee waiver with minimum stay |
| Official | [Jordan MOTA attraction fees](https://www.tourism.jo/EN/Pages/Entrance_Fees) | Jerash, Wadi Rum, Amman theatre, Karak etc |
| Official | [Petra tickets authority](https://visitpetra.jo/en/Petrafees) | Petra visitor tickets / consecutive days |
| Official | [Jordan archaeological ticket hours](https://ticket.gov.jo/en/opening-hours) | Season-dependent opening hours |
| Official | [UNESCO Jordan](https://whc.unesco.org/en/statesparties/jo) | World Heritage inscriptions / archaeology |
| Official | [UNESCO Petra](https://whc.unesco.org/en/list/326) | Nabataean city and outlying sites |
| Official | [UNESCO Wadi Rum](https://whc.unesco.org/en/list/1377) | Natural-cultural desert UNESCO status |
| Official | [Jordan Tourism Board](https://international.visitjordan.com/where-to-go/) | Destination descriptions, route clusters |
| Official | [Jerash visitor guide](https://jerash.visitjordan.com/en/Sites/1) | Roman site-specific circuit |
| Official | [Dana Feynan tourism board](https://international.visitjordan.com/wheretogo/dana-feynan/) | Trails, seasonal route |
| Official | [RSCN](https://www.rscn.org.jo/) | Reserve/water-trail operation; current PDF rates to reconfirm |
| Transport | [JETT official live timetable](https://jett.com.jo/en/live-schedule) | Buses; checked November 2026 |
| Transport | [Skyscanner referral and indicative results](https://skyscanner.net/g/referrals/v1/flights/home?mediaPartnerId=2850210&utm_term=skyscanner_chatgpt_app_data) | 2027 Apr/Oct monthly price shells; credit 19 Nov 2026 |
| Transport | [Rome2Rio](https://www.rome2rio.com/) | Overview durations for eight major legs 19 Nov 2026 |
| Independent | [Experience Jordan Mujib 2026](https://www.experiencejordan.com/wadi-mujib-siq-trail-guide/) | Siq Trail season and age, 2026 price estimate |
| Independent | [Jordan weather by destination](https://jordantravel.com/weather/) | Month-specific activity tradeoffs |
| Coordinate | [Jordan Department of Antiquities Amman Citadel](https://doa.gov.jo/EN/ListDetails/Archeological_Sites/1157/2) | Official coordinate, 31.95401697 N 35.93486821 E |
| Coordinate | [Mapcarta / OSM](https://mapcarta.com/) | Individual OSM-backed coordinate pages recorded in each GeoJSON feature |
| Border | [Natural Earth-derived GeoJSON country shapes](https://github.com/johan/world.geo.json) | Generalized political boundaries: JOR, ISR, PSE, SYR, IRQ, SAU, EGY |
| Images | [Wikimedia Commons Jordan](https://commons.wikimedia.org/wiki/Category:Jordan) | Reusable photography subject to per-photo license |
| Images | [Jordan Tourism Board visuals](https://international.visitjordan.com/where-to-go/) | Official destination image reference |
| Images | [UNESCO Petra media](https://whc.unesco.org/en/list/326/gallery/) | Site photography |

## Cartography provenance

- WGS84 longitude–latitude stops use linked OSM/Mapcarta coordinates and an official DoA coordinate for the Amman Citadel.
- World geographic borders are generalized GeoJSON from `johan/world.geo.json` (Natural Earth source); country geometry is used without artificial, invented coastline points.
- Straight lines in `route.geojson` are **planning connectors**, not verified OSRM driving polylines. The final SVG clearly discloses that. No footpath or highway shape is implied.
- The reusable generator is [tools/python/script.py](../../tools/python/script.py), which accepts `maps/stops.geojson`, `maps/route.geojson` and `maps/map-config.json` and outputs SVG with Basemap/GSHHS coastline and borders. The committed SVGs use the generalized real-country geometry from the source above, so regeneration yields a different (more detailed) cartographic background but the same verified stops.
- Sample airfares and operator timetables are not continuously monitored; quoted fares are not live ticket guarantees.
