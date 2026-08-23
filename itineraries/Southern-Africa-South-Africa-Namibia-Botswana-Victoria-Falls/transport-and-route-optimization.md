# Transport and route optimization

## Final route geometry

The route is designed as a **mostly one-way arc**:

1. South Africa coast block.
2. Strategic flight to Windhoek.
3. Namibia south-west → north → north-east.
4. Cross the Okavango at **Mohembo** into Botswana.
5. Botswana west → east: Maun → Moremi → Khwai → Savuti → Kasane.
6. Short shuttle to Victoria Falls and fly out.

That is geographically cleaner than using Kasane as both Botswana entrance and exit.

## Major leg decisions

| Leg | Alternatives researched / planning time | Decision |
|---|---|---|
| Cape Town→Windhoek | Rome2Rio overview: fly ~211 min; drive ~859 min; bus ~1375 min | **Fly**. Driving adds a long positioning day and would push the trip south/north with little incremental value. |
| Garden Route/Gqeberha→Windhoek | Rome2Rio: fly ~360 min; drive ~1360 min; bus ~2115 min | If doing Garden Route, **fly from the best regional connection** rather than drive to Namibia. |
| Etosha→Maun | possible through eastern Namibia/Kasane or west-Botswana | **Etosha→Rundu→Divundu→Mohembo→Maun**; keeps forward motion. |
| Kasane→Victoria Falls | Rome2Rio overview: ~78 min drive / ~98 min bus before border variability | **Return vehicle Kasane + shuttle** is usually simpler than taking a rental across Zimbabwe. |
| Victoria Falls→Maun | ~511 min drive or flight options | Avoid: route should visit Maun **before** Kasane/Vic Falls. |
| Victoria Falls→Johannesburg | Rome2Rio overview: direct flight ~129 min; drive ~763 min | Only use JNB as a fare/connection hub on the way home, not as an overland leg. |
| Johannesburg→Cape Town | Rome2Rio: flight ~168 min | JNB can be a price hub, but the positioning flight erodes savings; compare total cost, not raw fare. |

## Why Mohembo is the key optimization

Botswana Tourism describes the Okavango Panhandle as beginning where the river crosses from Namibia at **Mohembo**. That is exactly the geographic seam needed here. Coming from Divundu/Mahango, the route can cross into Botswana and continue to Tsodilo/Maun without first going all the way east to Kasane.

If the route instead goes **Divundu→Kasane→Maun→Moremi→Kasane**, it creates a large east-west-east reversal and repeats the northern Botswana corridor. The proposed direction turns the remote safari into a natural progression ending at Chobe.

## Rental-car architecture

### South Africa

Use a standard car. There is little reason to pay 4×4 camper rates in Cape Town/Garden Route.

### Namibia + Botswana

Use a real 4×4 suitable for gravel and remote Botswana tracks. Important contractual items to confirm **in writing**:

- Namibia + Botswana cross-border authorization;
- permitted border posts including Mohembo;
- one-way return at Kasane (or alternative Katima Mulilo arrangement + transfer);
- Botswana park-road permission;
- tyre/windscreen exclusions and recovery rules;
- whether Zimbabwe is permitted at all;
- required vehicle letter/authority and border paperwork;
- spare tyres, jack, compressor, recovery equipment;
- emergency contact procedure outside mobile coverage.

One-way Windhoek→Kasane rentals exist in the regional rental market, but availability/fees vary heavily by operator and season. Treat this as a quote item, not a guaranteed fixed fee.

## Remote Botswana warning

**Moremi, Khwai and Savuti are the section where the trip changes from “road trip” to expedition-style self-drive.** Sand, water, wildlife, track ambiguity and lack of immediate recovery make experience relevant. The route is not dependent on self-driving that section: a guided mobile safari can substitute while preserving the itinerary.

### Safer alternative

- return/store vehicle in Maun;
- 3–5 night guided Moremi/Khwai mobile safari;
- fly Maun→Kasane;
- Chobe + Victoria Falls.

This is the recommended 60:40 architecture.

## Border logic

Allow substantial buffer even when map distances are short. Border opening times, vehicle papers, road conditions and queues can alter the day. Never schedule a long international flight immediately after a remote 4×4/border leg.

The **Kasane→Victoria Falls** distance is short enough that Victoria Falls works well as the terminal destination rather than a day trip back to Botswana.

## Overnight-stop logic

- **Rundu** is primarily fatigue management between Etosha and Divundu.
- **Divundu** is not filler: Mahango/Bwabwata adds a wetland/river ecosystem and sets up Mohembo cleanly.
- **Tsodilo** is a high-value optional stop on the 42-day route because the Mohembo geometry places it naturally between Divundu and Maun.
- **Swakopmund** is useful as a rest/resupply base; do not add days simply because it is a famous name.

## Road geometry in maps

The committed GeoJSON lines are explicitly labeled **planning connectors between verified stop coordinates**. They do not pretend to be GPS-accurate road centerlines. Flights/shuttle/remote-4×4 semantics are stored in each feature's `mode` property.