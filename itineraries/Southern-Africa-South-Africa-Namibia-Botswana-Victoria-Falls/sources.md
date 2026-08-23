# Sources and research trail

Research date: **2026-08-23**.

## Official / primary sources

### South Africa — SANParks

- Table Mountain National Park overview — https://www.sanparks.org/parks/table-mountain  
  Supports: Cape Peninsula/Table Mountain importance, park extent and nature context.
- Cape of Good Hope & Cape Point — https://www.sanparks.org/parks/table-mountain/what-to-do/attractions/cape-of-good-hope-cape-point  
  Supports: hiking/outdoor value and Cape Point route.
- Table Mountain hikes/trails — https://www.sanparks.org/parks/table-mountain/what-to-do/activities/hikes-walks-trails  
  Supports: hiking options and trail planning.
- GPS waypoints — https://www.sanparks.org/parks/table-mountain/travel/gps-waypoints  
  Supports: geographic verification for Cape Point/Boulders area.

### Namibia Tourism Board / Visit Namibia

- Sossusvlei / other popular sites — https://visitnamibia.com.na/other-popular-sites/  
  Supports: Sossusvlei/Deadvlei significance and Big Daddy context.
- Namib-Naukluft Park — https://visitnamibia.com.na/2022/02/namib-naukluft-park/  
  Supports: Sossusvlei/Sesriem as core park highlights.
- Namib Sand Sea — https://visitnamibia.com.na/2022/02/namib-sand-sea/  
  Supports: UNESCO Namib Sand Sea context including Sandwich Harbour and Sossusvlei.
- Northern Region / Etosha season — https://visitnamibia.com.na/2022/03/northern-region/  
  Supports: Etosha viewing, May–October dry-season recommendation.
- Four Rivers Route — https://visitnamibia.com.na/the-four-river-route/  
  Supports: Kavango/Zambezi route logic and connection toward Chobe/Victoria Falls.

### Botswana Tourism Organisation

- Okavango Delta — https://www.botswanatourism.co.bw/explore/okavango-delta  
  Supports: Mohembo Panhandle geography, mokoro/boat/game activities, ecosystem value.
- Moremi Game Reserve — https://botswanatourism.co.bw/explore/moremi-game-reserve  
  Supports: Moremi's ecosystem and self-drive relevance.
- Chobe National Park — https://www.botswanatourism.co.bw/index.php/explore/chobe-national-park  
  Supports: dry-season elephant/buffalo concentrations and river-cruise value.
- Savuti and Linyanti — https://www.botswanatourism.co.bw/explore/savuti-and-linyanti  
  Supports: remote wilderness character and dry-season wildlife concentrations.
- Kasane — https://www.botswanatourism.co.bw/index.php/explore/kasane  
  Supports: Kasane as Chobe gateway and Victoria Falls being ~80 km away.

### Zambia Tourism

- Victoria Falls — https://www.zambia.travel/victoriafalls.html  
  Supports: waterfall dimensions/context, March–June prime flood season and dry-season Devil's Pool logic.
- Destination Zambia activities PDF — https://www.zambia.travel/OtherDocuments/DESTINATIONZAMBIAACTIVITIES.pdf  
  Supports: seasonal low-water activity planning such as Devil's Pool/rafting.

### Zimbabwe Parks

- Zambezi–Victoria Falls National Parks Management Plan 2024–2034 — https://www.zimparks.org.zw/media/2024/07/Zambezi-Victoria-Falls-GMP_April_2024-Final.pdf  
  Supports: protected-area / waterfall-rainforest management geography.

## Transport / fare research

### Rome2Rio route overviews — snapshot 2026-08-23

Connected route searches returned approximately:

- Cape Town→Windhoek: fly **211 min**, drive **859 min**, bus **1375 min**.
- Gqeberha→Windhoek: fly **360 min**, drive **1360 min**, bus **2115 min**.
- Kasane→Victoria Falls: drive **78 min**, bus **98 min** before allowing extra border time.
- Victoria Falls→Maun: drive **511 min**; available flight combinations demonstrate why backtracking after Vic Falls is poor geometry.
- Victoria Falls→Johannesburg: direct flight overview **129 min**.
- Johannesburg→Cape Town: flight overview **168 min**.

These are route-planning overviews, not guaranteed schedules or travel-day timings.

### Skyscanner indicative fares — snapshot 2026-08-23

Flexible month test, July 2027:

- VIE→CPT: from ~€600 one-way in returned results.
- VIE→JNB: from ~€516.
- BUD→JNB: from ~€515.
- BUD→CPT: no quote returned in tested search.
- VFA→VIE: no quote returned in tested search.

Attribution/search: https://skyscanner.net/g/referrals/v1/flights/home?mediaPartnerId=2850210&utm_term=skyscanner_chatgpt_app_data

Prices are indicative snapshots, not booking guarantees.

## Independent / operator evidence used cautiously

Regional 4×4 operators advertise Namibia/Botswana one-way and cross-border rental structures, supporting the feasibility of a Windhoek→Kasane architecture. Exact fees, permitted borders and documents are operator/vehicle/date-specific and therefore **not hard-coded** into this itinerary. Always obtain written authorization from the chosen rental firm.

## Mapping method

- Stops use geographic coordinates cross-checked against official/recognized gazetteer/heritage/map sources where practical.
- GeoJSON follows `[longitude, latitude]`.
- Static SVG uses Basemap/GSHHS coastlines and country borders via the repository's reusable Python renderer.
- Route LineStrings are explicitly marked as planning connectors unless routed geometry is available.
- The interactive map uses OpenStreetMap-backed Leaflet tiles at viewing time and includes standard OSM attribution.

See [`maps/README-map-method.md`](./maps/README-map-method.md).