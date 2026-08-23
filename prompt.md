# Master Travel-Route Research + GitHub + Real-Map Prompt

I want you to **fully research, optimize, document, and visualize a travel itinerary**, then write the complete result into my TravelRoutes GitHub repository.

## Inputs

- **Trip / rough route:** `[PASTE MY ROUGH ROUTE HERE]`
- **Approximate duration:** `[e.g. 28 days]`
- **Travel period:** `[e.g. February 2027 / flexible / any time of year]`
- **Starting airports:** `[e.g. Vienna VIE and Budapest BUD]`
- **Possible ending airports:** `[e.g. Cancún CUN, Mexico City MEX]`
- **GitHub repository:** `[e.g. https://github.com/USERNAME/TravelRoutes]`
- **Itinerary slug:** `[e.g. Central-America-Guatemala-Belize-Mexico]`
- **Priorities:** `[nature / hiking / culture / archaeology / beaches / snorkeling / food / nightlife / surfing / budget etc.]`

Do not simply follow my proposed order. Treat it as a draft and **redesign it if another order is cheaper, faster, more scenic, avoids backtracking, improves weather, or preserves more high-value sights**.

---

# 1. Optimize the route aggressively

Research every major transport leg using available tools and current sources such as:

- Rome2Rio;
- Skyscanner;
- official train/bus/ferry operators;
- airline websites where useful;
- local transport authorities;
- reliable recent travel information.

Compare bus, train, ferry, flight, shuttle and car where relevant.

For every important leg record:

- approximate duration;
- approximate price;
- frequency if known;
- border-crossing implications;
- transfer complexity;
- whether an overnight stop makes sense;
- whether another routing saves significant time.

Actively detect:

- unnecessary backtracking;
- bad one-day transfers;
- inefficient border crossings;
- expensive positioning flights;
- destinations that improve an otherwise ugly transfer;
- famous places with poor sightseeing-value-per-hour.

Do not optimize only for shortest travel time. Optimize the combined objective:

**sightseeing value + route efficiency + cost + weather + uniqueness + travel fatigue.**

---

# 2. Flight optimization

Search multiple route shells instead of assuming a normal same-airport return is best.

Test combinations such as:

- A → first destination / last destination → A;
- B → first destination / last destination → B;
- A → first destination / last destination → B;
- B → first destination / last destination → A;
- normal round trip to a cheap hub + positioning flight;
- open-jaw / multi-city;
- reversed itinerary direction;
- adding a cheap domestic flight at the end;
- adding another city when it materially improves the international fare.

Do **not assume the same airport is cheapest in both directions**.

For each promising option give:

- indicative airfare;
- dates tested;
- airline/stops if available;
- positioning cost;
- positioning time;
- realistic door-to-door difference.

Clearly separate:

### Raw cheapest airfare

from

### Best total-value flight strategy

because a small airfare saving can disappear after positioning transport, luggage, meals, hotel buffers and lost time.

Use **Skyscanner indicative prices only as indicative data**, clearly date the research snapshot and include attribution/linking. When dates are flexible, search cheapest days in the relevant month(s).

---

# 3. Research ALL worthwhile sights

For every destination and reasonable nearby day trip, research the important sights instead of relying only on famous names.

Include where relevant:

- major must-see sights;
- nature;
- hiking;
- viewpoints;
- archaeology;
- museums;
- historic districts;
- beaches;
- snorkeling/diving;
- islands;
- markets;
- interesting neighborhoods;
- food experiences;
- unusual local experiences;
- worthwhile nearby day trips;
- genuinely worthwhile lesser-known sights.

For every sight assign:

- **Priority:** S / A / B / C;
- **Sightseeing value:** /10;
- **Uniqueness:** /10;
- **Time cost:** approximate hours;
- **Detour cost:** low / medium / high;
- recommended visit length;
- why it is or is not worth including.

Use primary/official sources wherever practical:

- UNESCO;
- national tourism boards;
- national parks;
- museums;
- archaeological authorities;
- official attraction websites.

Supplement with strong independent guides and recent traveler experience when it materially improves the recommendation.

Include useful **article links and image/reference links**.

Store normalized sight data in a machine-readable file such as `data/sights.csv` so it can support route scoring and the 60:40 analysis.

---

# 4. Create a general ~28-day optimized itinerary

Create an **evergreen, date-agnostic itinerary**, not tied to one calendar year.

Build approximately the best **28-day first-trip version** for the route.

For each day show:

- sleeping location;
- morning;
- afternoon;
- evening;
- transport;
- approximate travel time;
- major sights;
- optional extras;
- intensity level.

Mark days as:

- 🟢 easy;
- 🟡 moderate;
- 🔴 intense.

Avoid wasting useful daylight on transfers where an early/late move is clearly better. Include sensible recovery/weather buffers after demanding hikes or weather-dependent activities.

---

# 5. Create a 60:40 highlights route

Also create a separate **60:40 route**.

Definition:

> Capture roughly the best **60% of total sightseeing/experience value in only about 40% of the full itinerary time**.

For a 28-day route this will often mean roughly **10–12 days**, but choose the exact duration based on route geometry and experience value.

This is NOT “delete every second stop.” Optimize based on value per unit time.

Prioritize experiences that are:

- iconic;
- highly unique;
- difficult to substitute elsewhere;
- geographically efficient;
- highly memorable;
- worth their transport cost.

Cut experiences that are:

- repetitive;
- easily substituted;
- poor value per transfer hour;
- long detours;
- filler;
- similar to a stronger experience already retained.

It is acceptable for the 60:40 route to spend more money on a strategic internal flight if doing so saves one or more sightseeing days.

Create a comparison table:

| Place | Full route | 60:40 route | Reason |
|---|---|---|---|

Explain the biggest sacrifices and estimate how much of the normalized experience score the condensed route preserves.

---

# 6. Create worthwhile variants

Research variants only where they materially change the trip, such as:

- relaxed;
- maximum sightseeing;
- budget;
- nature-heavy;
- hiking-heavy;
- beach/reef-heavy;
- archaeology/culture-heavy;
- optional major-city extension;
- alternative arrival/departure airport.

Do not create variants just to inflate the document count.

---

# 7. Weather and season analysis

Research climate for every major stop and create a month-by-month travel score:

**1 = worst possible period**  
**10 = almost ideal**

Score weather for the activity being done there, not just temperature.

Examples:

- mountain hike → cloud, rain, wind and visibility matter;
- snorkeling/diving → sea state, storms and underwater visibility matter;
- archaeology → heat/humidity matter;
- beach/island route → rain, wind and cyclone risk matter.

Create:

| Destination | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|

Then identify:

- best overall month;
- second-best month;
- best-value shoulder season;
- months to avoid;
- important activity-specific risks.

---

# 8. Create one date-specific worked example

In addition to the evergreen route, create a date-specific booking example for the period I supplied.

Example:

`1–28 February 2027`

Use current flight/transport research for that example and clearly date all fare snapshots.

Keep this separate from the evergreen route so temporary fares do not make the core itinerary obsolete.

Suggested files:

- `booking-example-YYYY-MM.md` — fare/booking layer;
- `itinerary.md` or another clearly named file — detailed dated schedule.

---

# 9. Generate a REAL geographic route map

This is critical:

**DO NOT use an AI image generator to invent the geography.**

Create maps programmatically from verified coordinates and real cartographic data.

## A. Geocode every stop

Retrieve verified latitude/longitude using one or more of:

- OpenStreetMap / Nominatim;
- Wikidata;
- GeoNames;
- UNESCO / official coordinates;
- authoritative specialist sources for natural features.

Store the points in:

`maps/stops.geojson`

GeoJSON coordinates must be `[longitude, latitude]`.

## B. Verify geography

Before rendering, verify at minimum:

- correct country;
- relative direction from surrounding stops;
- approximate coordinate correctness;
- island vs mainland;
- archaeological site vs nearby town;
- no latitude/longitude reversal.

Never place a pin by eyeballing an illustration.

## C. Obtain route geometry

Where possible use actual routing geometry such as:

- OSRM;
- OpenRouteService;
- GraphHopper;
- official/public-transit route geometry.

For ferry/flight/hike segments, preserve explicit transport semantics. Do not pretend a driving road exists across water.

If live routing is unavailable, straight connectors between **verified** stop coordinates are acceptable only when clearly labeled as planning connectors rather than exact road tracks.

Save route data such as:

- `maps/route.geojson`;
- `maps/route-60-40.geojson`.

## D. Render using real geographic data

Use an appropriate real mapping workflow, for example:

- Python + GeoPandas / Cartopy / Matplotlib;
- Basemap/GSHHS;
- Contextily with an appropriate tile provider;
- Leaflet;
- MapLibre;
- QGIS-compatible output;
- another OpenStreetMap-backed/vector geographic renderer.

Respect OpenStreetMap tile usage policy. Do not bulk-render from the public tile service in a way that violates its usage requirements.

The static map should include where practical:

- real coastline;
- real country borders;
- verified stop coordinates;
- numbered stops;
- stop names;
- route line;
- visibly distinct road/rail/ferry/flight/hike segments;
- legend;
- north orientation;
- scale;
- required data attribution.

## E. SVG OUTPUT — UPLOAD THE SVG TO GITHUB

**This is a hard requirement.**

The map-generation pipeline must be:

```text
verified coordinates
        ↓
stops.geojson + route.geojson
        ↓
real geographic renderer
        ↓
SVG
        ↓
commit/upload SVG to GitHub
```

Rules:

1. Generate each static map directly as **SVG**.
2. Treat the SVG as the final static map artifact.
3. **Commit/upload the SVG itself to the itinerary's `maps/` folder in GitHub.**
4. Do not require a PNG copy by default.
5. Do not use an AI-generated image as a substitute for the SVG map.
6. Verify the SVG contains the correct stops, numbering, labels, route geometry, borders and extent before committing it.
7. Keep the corresponding GeoJSON source files in GitHub so the SVG remains reproducible.

Create at least:

```text
maps/
├── map-full-route.svg
├── map-60-40-route.svg
├── stops.geojson
├── route.geojson
└── route-60-40.geojson       # when applicable
```

Also create an interactive Leaflet/MapLibre map when useful, preferably from the same GeoJSON source of truth.

The maps are **information graphics built on real cartographic data**, not generative illustrations.

---

# 10. Repository structure

Use the repository-wide organization when available.

Preferred structure:

```text
repository-root/
├── prompt.md
├── map-generation.md
├── itineraries/
│   └── <Trip-Slug>/
│       ├── README.md
│       ├── general-28-day-route.md
│       ├── itinerary-28-days.md
│       ├── itinerary-60-40.md
│       ├── itinerary.md                    # dated example when applicable
│       ├── booking-example-YYYY-MM.md
│       ├── transport-and-route-optimization.md
│       ├── flights.md
│       ├── sights.md
│       ├── weather-and-timing.md
│       ├── optional-variants.md
│       ├── sources.md
│       ├── maps/
│       │   ├── map-full-route.svg
│       │   ├── map-60-40-route.svg
│       │   ├── stops.geojson
│       │   ├── route.geojson
│       │   └── interactive-map.html
│       └── data/
│           └── sights.csv
└── tools/
    └── python/
        └── script.py
```

For future routes, put itinerary/research material under `itineraries/<Trip-Slug>/` and keep reusable generation scripts under root-level `tools/` rather than copying tool code into each trip folder.

Preserve unrelated repository files.

---

# 11. README requirements

The itinerary README should act as the main overview and include:

- route summary;
- optimized route order;
- why this order wins;
- embedded real SVG map;
- general ~28-day recommendation;
- 60:40 version;
- best season;
- transport bottlenecks;
- major must-see experiences;
- optional extensions;
- quick links to every detailed file;
- map-data/method note.

---

# 12. Sources

Keep a proper source trail.

For important factual claims record where useful:

- title;
- organization/site;
- URL;
- what it supports;
- research date.

Separate:

### Official / primary sources

### Transport / fare sources

### Useful independent guides

### Image / visual references

Prefer strong primary sources and do not dump hundreds of low-value links.

---

# 13. Quality-control pass

Before committing, audit the finished route and files.

Check:

1. Is there unnecessary geographical backtracking?
2. Is any transfer absurdly long for the value of the stop?
3. Could an overnight stop improve a horrible transfer?
4. Are major nearby sights missing?
5. Is a famous stop overrated compared with an alternative?
6. Are border crossings realistic?
7. Is the weather appropriate for the activities?
8. Does the route make sense on a real map?
9. Are all pins based on verified coordinates?
10. Does the 60:40 route really protect the highest-value experiences?
11. Are temporary fare snapshots separated from evergreen advice?
12. Are flight prices marked as indicative and dated?
13. Are links valid after any repository reorganization?
14. Does the GitHub itinerary contain the actual research, not just a short summary?
15. Was the map generated from real geography rather than generative imagery?
16. Does the SVG render correctly?
17. Was the **SVG itself committed/uploaded to GitHub**?
18. Do the map's stops, numbering and route geometry match the itinerary and GeoJSON?
19. Are reusable map scripts stored under `tools/`?

Fix problems you discover before finishing.

---

# 14. GitHub execution

Use connected GitHub tools to actually create/update the repository files. Do not merely print Markdown for me to copy manually.

Preserve unrelated work and re-read the latest tree before major restructuring so concurrent changes are not accidentally overwritten.

For maps:

1. generate the real map as SVG;
2. commit/upload `map-full-route.svg`;
3. commit/upload `map-60-40-route.svg` when applicable;
4. commit the GeoJSON source files;
5. commit reusable map-generation code under `tools/python/script.py`;
6. verify the committed SVG links render correctly on GitHub.

Do **not** skip the SVG upload and merely tell me where a local file exists.

Prefer the repository's existing workflow (direct main commits vs branch/PR) rather than imposing a different convention without reason.

---

# 15. Final response

When finished, give me a concise summary containing:

- final optimized route;
- biggest changes from my original proposal;
- general duration;
- 60:40 duration;
- best travel month(s);
- best current flight strategy;
- GitHub itinerary-folder link;
- links to the committed real SVG route maps;
- link to the reusable tool/script.

Do the research and implementation now rather than just telling me what I should research later.

---

The core map rule to remember is:

**geocode verified stops → GeoJSON → real routing/cartography → SVG → upload SVG to GitHub.**
