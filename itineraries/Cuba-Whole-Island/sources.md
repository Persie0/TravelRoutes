# Research sources and evidence ledger

Snapshot **18 November 2026**. Direct URL availability and commercial schedules may change. Geographic points are separately sourced in `maps/stops.geojson`.

## Official / primary

| Organization | Link | Evidence used |
|---|---|---|
| Austria BMEIA | https://www.bmeia.gv.at/reise-services/reiseinformation/land/kuba | Entry requirements; official warnings; payments; insurance; east-province warning |
| Canadian travel advice | https://travel.gc.ca/destinations/cuba | Fuel shortages, electricity, transport and essential supplies crisis |
| US CBP ESTA | https://esta.cbp.dhs.gov/faq | Post-12-Jan-2021 Cuba travel normally disqualifies US ESTA under Visa Waiver Program |
| US Department of State VWP | https://travel.state.gov/content/travel/en/us-visas/tourism-visit/visa-waiver-program.html | Legal eligibility context for US travel |
| UNESCO Cuba | https://whc.unesco.org/en/statesparties/cu/ | 9 inscribed World Heritage sites; primary heritage identity |
| UNESCO Old Havana | https://whc.unesco.org/en/list/204 | Havana historic town and fortifications |
| UNESCO Viñales | https://whc.unesco.org/en/list/840 | Viñales landscape |
| UNESCO Trinidad | https://whc.unesco.org/en/list/460 | Trinidad and sugar estates |
| Cuba Travel | https://www.cuba.travel/en/wheretogo/havana/usefulinformation/howtoget | Tourist bus operator and booking procedure |
| Cuba Travel nature | https://www.cuba.travel/sobre-cuba/naturaleza-en-cuba | Main nature sites such as Las Terrazas, Topes, El Nicho |
| Cuba tourist eVisa | https://evisacuba.cu/en/solicitar/visa | Official visa application route, as linked by BMEIA |
| Cuba D'Viajeros | https://dviajeros.mitrans.gob.cu/inicio | Mandatory arrival registration, 7 days before flight |

## Transport / fare

| Provider | Link | Evidence |
|---|---|---|
| Skyscanner (indicative fares) | https://skyscanner.net/g/referrals/v1/flights/home?mediaPartnerId=2850210&utm_term=skyscanner_chatgpt_app_data | 2027 Feb/Mar VIE/BUD/VRA/HOG searches on 18 Nov 2026; see flights.md |
| Rome2Rio | https://www.rome2rio.com/ | Planning options and approximate durations for 9 intercity legs; **not** confirmation of 2027 bus/flight operations |
| Viazul official | https://viazul.wetransp.com | Actual traveler should check and reserve verified schedules at operator, as linked by Cuban tourism authority |
| Cuban official tourism | https://www.cuba.travel/en/destinations/pinar-del-rio/how-to-get-to-pinar-del-rio | Havana–Viñales travel distance and land transport context |

## Current-risk and independent cross-check

| Publication | Link | Use |
|---|---|---|
| Reuters, 22 October 2026 | https://www.reuters.com/world/americas/cubas-public-transport-plunges-all-time-low-amid-us-fuel-blockade-minister-says-2026-10-22/ | Recent collapse in public transit |
| IFRC, 29 October 2026 | https://www.ifrc.org/press-release/cuba-red-cross-support-and-energy-solutions-sustain-recovery-provinces-most-affected | Continued eastern hurricane recovery |
| Lonely Planet | https://www.lonelyplanet.com/articles/best-time-to-visit-cuba | Season/weather guidance |
| Rough Guides | https://www.roughguides.com/cuba/when-to-go/ | Independent season cross-check |

## Geography and images

- Actual low-resolution coastline data used to render SVG: [Natural Earth-derived Cuba country polygon](https://github.com/johan/world.geo.json/blob/master/countries/CUB.geo.json); original dataset: https://www.naturalearthdata.com/ .
- Main city coordinates: https://time-ok.com/coordinates/cuba and https://www.geonames.org/advanced-search.html?country=CU&q= . Other stop-specific coordinate URLs are stored per feature in `maps/stops.geojson`.
- Visual references: [Cuba tourism destination galleries](https://www.cuba.travel/en), [UNESCO Cuba World Heritage imagery](https://whc.unesco.org/en/statesparties/cu/), [Lonely Planet classic cars](https://www.lonelyplanet.com/articles/classic-cars-cuba).
- Cartographic source and renderer design: `maps/README-map-method.md`. Route lines are straight-line planning connectors, **not actual road geometries**.
