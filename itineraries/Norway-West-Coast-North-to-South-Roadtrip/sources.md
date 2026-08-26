# Sources

Research date: **26 August 2026** unless noted.

## Official / primary

- SJ Norge — Nordlandsbanen: https://www.sj.no/strekning/nordlandsbanen/  
  Supports 729 km / roughly 10-hour Bodø–Trondheim rail journey and scenic positioning.
- SJ Norge — planned works / service status: https://www.sj.no/trafikk/planlagt-arbeid/  
  Supports current disruption/night-train caution.
- Visit Norway — Nordland Railway: https://www.visitnorway.com/plan-your-trip/getting-around/by-train/nordland-line/  
  Supports Arctic Circle route and current operational caveats.
- Troms fylkeskommune — Gryllefjord–Andenes 2026 summer ferry: https://www.tromsfylke.no/aktuelt/innforer-passasjerbetaling-pa-senja-ferge.76189.aspx  
  Supports 2026 operating period through 27 September and passenger-payment trial.
- Norwegian Scenic Routes — all routes / GPX: https://www.nasjonaleturistveger.no/en/routes/ and https://www.nasjonaleturistveger.no/en/gpx-files/  
  Supports route list and official scenic-road geometry references.
- Geiranger–Trollstigen: https://www.nasjonaleturistveger.no/en/routes/geiranger--trollstigen/  
  Supports seasonal-road information.
- Trollstigen access status: https://www.nasjonaleturistveger.no/en/routes/geiranger--trollstigen/trollstigen-closed/  
  Supports rockfall closure warning.
- Gamle Strynefjellsvegen: https://www.nasjonaleturistveger.no/en/routes/gamle-strynefjellsvegen/  
  Supports 27 km route and seasonal opening/closure history.
- Gaularfjellet: https://www.nasjonaleturistveger.no/en/routes/gaularfjellet  
  Supports 114 km route, Utsikten and winter closure information.
- Visit Norway — summer climate: https://www.visitnorway.com/plan-your-trip/seasons-climate/summer/  
  Supports Fjord Norway/Northern Norway weather and summer hiking context.
- Visit Tromsø — hiking: https://www.visittromso.no/hiking  
  Supports June–October main hiking season and rapidly changing weather.
- Visit Norway — right to roam: https://www.visitnorway.com/plan-your-trip/travel-tips-a-z/right-of-access/  
  Supports vehicle-parking limits and 150 m / two-night camping guidance.
- AutoPASS: https://www.autopass.no/en/  
  Supports automated road-toll system.
- AutoPASS for ferry / FerryPay: https://autopassferje.no/en/ and https://www.autopassferje.no/en/ferrypay-en/  
  Supports ferry-payment options.

## Transport / fare research

- Rome2Rio route comparison, Bodø → Trondheim, queried 26 Aug 2026: train ~586 min; drive ~593 min.
- Skyscanner indicative-price snapshot, queried 26 Aug 2026: VIE→TOS July/August 2027 and BGO→VIE August 2027.  
  https://skyscanner.net/g/referrals/v1/flights/home?mediaPartnerId=2850210&utm_term=skyscanner_chatgpt_app_data

## Map data/method

- Stop coordinates are geographic planning points checked against established place coordinates and official Scenic Route endpoint/viewpoint coordinates where available.
- Static SVGs rendered with the repository's `tools/python/script.py` approach using **Basemap/GSHHS real coastline and borders**.
- Route GeoJSON connectors are intentionally labelled as planning connectors when exact OSRM/road geometry is not present; ferry/train/flight semantics are preserved.
