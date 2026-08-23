# Master Travel-Route Research + GitHub + Real-Map Prompt

I want you to **fully research, optimize, document, and visualize a travel itinerary**.

## Inputs

- **Trip / rough route:** `[PASTE MY ROUGH ROUTE HERE]`
- **Approximate duration:** `[e.g. 28 days]`
- **Travel period:** `[e.g. February 2027 / flexible / any time of year]`
- **Starting airports:** `[e.g. Vienna VIE and Budapest BUD]`
- **Possible ending airports:** `[e.g. Cancún CUN, Mexico City MEX]`
- **GitHub repository:** `[e.g. https://github.com/USERNAME/TravelRoutes]`
- **Subfolder name:** `[e.g. guatemala-belize-mexico]`
- **Priorities:** `[nature / hiking / culture / archaeology / beaches / snorkeling / food / nightlife / surfing / budget etc.]`

Do not simply follow my proposed order. Treat it as a draft and **redesign it if a different order is cheaper, faster, more scenic, or avoids backtracking**.

---

# 1. Optimize the route aggressively

Research every major transport leg.

Use available travel/transport tools such as:

- Rome2Rio
- Skyscanner
- official train/bus/ferry operators
- airline websites when useful
- local transport authorities
- reliable recent travel information

Compare:

- bus
- train
- ferry
- flight
- shuttle
- car where relevant

For every important leg record:

- approximate duration
- approximate price
- frequency if known
- border-crossing implications
- transfer complexity
- whether an overnight stop makes sense
- whether another routing saves significant time

Actively detect:

- unnecessary backtracking
- bad one-day transfers
- inefficient border crossings
- expensive positioning flights
- destinations that are only worth visiting because they improve the route
- places that are famous but low-value relative to the time required

Do not optimize only for shortest travel time.

Optimize the combined objective:

**sightseeing value + route efficiency + cost + weather + uniqueness + travel fatigue.**

---

# 2. Flight optimization

If the trip starts/ends with flights, search multiple route shells.

For example:

- A → first destination / last destination → A
- B → first destination / last destination → B
- A → first destination / last destination → B
- B → first destination / last destination → A
- normal round trip to a cheap hub + positioning flight
- open-jaw / multi-city
- reversing the whole itinerary
- adding a cheap domestic flight at the end
- adding another city if it makes the international return substantially cheaper

Do **not assume the same airport is cheapest in both directions**.

For each promising option give:

- indicative airfare
- travel dates tested
- airline / stops if available
- extra positioning cost
- extra positioning time
- true approximate door-to-door difference

Clearly separate:

### Raw cheapest airfare

from

### Best total-value flight strategy

because a €30 cheaper Budapest flight can be worse than Vienna after train/bus/hotel/luggage costs.

Use **Skyscanner indicative prices only as indicative data** and include attribution and links.

If dates are flexible, search the cheapest days in the relevant month(s).

---

# 3. Research ALL worthwhile sights

For every destination and reasonable nearby day trip, research the important sights rather than relying only on famous names.

Include:

- major must-see sights
- nature
- hiking
- viewpoints
- archaeology
- museums
- historic districts
- beaches
- snorkeling/diving
- islands
- markets
- interesting neighborhoods
- food experiences
- unusual local experiences
- worthwhile nearby day trips
- lesser-known sights that are actually worth the time

For every sight assign:

- **Priority:** S / A / B / C
- **Sightseeing value:** /10
- **Uniqueness:** /10
- **Time cost:** approximate hours
- **Detour cost:** low / medium / high
- recommended visit length
- why it is or is not worth including

Use primary/official sources where possible:

- UNESCO
- national tourism boards
- national parks
- museums
- archaeological authorities
- official attraction websites

Also use good independent guides and recent traveler experience when it materially improves the recommendation.

Include useful **article links and image/reference links**.

---

# 4. Create a normal ~28-day optimized itinerary

Create a **general itinerary**, not tied to one exact calendar year.

It should be reusable whenever the trip is taken in an appropriate season.

Build an approximately **28-day best-version itinerary**.

For each day show:

- sleeping location
- morning
- afternoon
- evening
- transport
- approximate travel time
- major sights
- optional extras
- intensity level

Mark days as:

- 🟢 easy
- 🟡 moderate
- 🔴 intense

Avoid wasting daytime on transfers where an early/late transfer produces a clearly better trip.

Include sensible recovery time after major hikes or long travel days.

---

# 5. Create a 60:40 highlights itinerary

Also create a separate **60:40 route**.

Definition:

> Try to capture roughly the best **60% of the total sightseeing/experience value in only about 40% of the full itinerary time**.

For a 28-day route this will usually mean roughly **10–12 days**, but choose the exact duration based on the destination.

This is NOT simply “remove every second stop.”

Calculate it based on sightseeing value per unit time.

Prioritize experiences that are:

- iconic
- unique
- difficult to substitute elsewhere
- geographically efficient
- highly memorable
- worth the transport effort

Cut experiences that are:

- repetitive
- easy to see elsewhere
- poor value per travel hour
- long detours
- mainly filler
- similar to a better sight already included

Create a table showing:

| Place | Full route | 60:40 route | Reason |
|---|---|---|---|

Also explain the biggest sacrifices made by the 60:40 version.

---

# 6. Create optional route variants

Research worthwhile variants such as:

- slower / relaxed
- maximum sightseeing
- budget
- nature-heavy
- hiking-heavy
- beach-heavy
- archaeology/culture-heavy
- optional major city extension
- alternative arrival/departure airport

Only include variants that materially improve the trip for some traveler profile.

---

# 7. Weather and season analysis

Research climate for every major stop.

Create a month-by-month score:

**1 = worst possible period**  
**10 = almost ideal**

Score based on the activities being done there, not just average temperature.

For example:

- mountain hike → rain/cloud visibility matters strongly
- snorkeling → sea state and underwater visibility matter
- archaeological ruins → heat matters
- beaches → rain/wind/hurricane risk matters

Create a table:

| Destination | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|

Then identify:

- best overall month
- second-best month
- best value shoulder season
- months to avoid
- important activity-specific weather risks

---

# 8. Make one date-specific worked example

In addition to the general route, create one **date-specific booking example** for the period I gave you.

Example:

`1–28 February 2027`

Use current flight/transport research for that example.

Keep this separate from the general itinerary so temporary fares do not make the main itinerary obsolete.

File name example:

`booking-example-2027-02.md`

---

# 9. Generate a REAL geographic route map

This is important:

**DO NOT use an AI image generator to invent the geography.**

Create the route map programmatically from real geographic coordinates.

Use an OpenStreetMap-based workflow where practical.

Recommended approach:

### A. Geocode each stop

Retrieve verified latitude/longitude using one or more of:

- OpenStreetMap / Nominatim
- Wikidata
- GeoNames
- official coordinates

Store the coordinates in a machine-readable file such as:

`stops.geojson`

Example structure:

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "order": 1,
        "name": "Example Stop"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [longitude, latitude]
      }
    }
  ]
}
```

### B. Verify geography

Before rendering, verify that each pin is geographically correct.

Check at minimum:

- country
- relative direction from surrounding stops
- approximate coordinates
- islands versus mainland
- archaeological sites versus nearby towns

Never approximate pin placement visually.

### C. Obtain route geometry

Where possible use actual routing data such as:

- OSRM
- OpenRouteService
- GraphHopper
- public-transit route geometry

For ferry/flight segments, draw appropriate straight/dashed segments if exact geometry is unavailable.

Do not pretend a road route exists across water.

### D. Render map using real map data

Create a high-resolution PNG using a proper mapping library such as:

- Python + GeoPandas + Contextily
- Folium
- Leaflet
- MapLibre
- QGIS-compatible approach
- another OpenStreetMap-backed renderer

Use OpenStreetMap tiles only according to applicable usage policies. If bulk/static tile use is inappropriate, use a suitable OSM-derived tile provider or render from geographic vector data instead.

The final map must contain:

- actual coastline
- actual country borders
- actual stop coordinates
- numbered stops
- stop names
- solid main-route line
- dashed ferry/flight/optional segments
- start/end airport icons
- legend
- north arrow
- scale if practical

Create at least:

`map-full-route.png`

and

`map-60-40-route.png`

Also save:

`stops.geojson`

and ideally:

`route.geojson`

The map is an **information graphic built on real cartographic data**, not a generative illustration.

---

# 10. GitHub repository structure

Put everything inside the specified **subfolder**, not the repository root.

Use a structure similar to:

```text
<subfolder>/
├── README.md
├── itinerary-28-days.md
├── itinerary-60-40.md
├── transport-and-route-optimization.md
├── flights.md
├── sights.md
├── weather-and-timing.md
├── optional-variants.md
├── booking-example-YYYY-MM.md
├── sources.md
├── maps/
│   ├── map-full-route.png
│   ├── map-60-40-route.png
│   ├── stops.geojson
│   └── route.geojson
└── data/
    └── sights.csv
```

If the repository already has a convention, follow it instead.

---

# 11. README requirements

The README should work as the main overview.

Include:

- route summary
- route order
- why this order is optimal
- map
- general 28-day recommendation
- 60:40 version
- best season
- expected transport bottlenecks
- major must-see experiences
- optional extensions
- quick link to every detailed file

Include Markdown links to the detailed research.

---

# 12. Sources

Keep a proper source trail.

For every important factual claim, preferably record:

- title
- organization/site
- URL
- what it supports
- research date

Prioritize primary sources.

Separate:

### Official / primary sources

from

### Transport / fare sources

from

### Useful independent guides

from

### Image / visual references

Do not dump hundreds of useless links. Keep sources relevant.

---

# 13. Quality-control pass

Before committing, audit the finished route.

Check:

1. Is there any unnecessary geographical backtracking?
2. Is any transfer absurdly long for the value of the destination?
3. Could an overnight stop turn a horrible transfer into a worthwhile destination?
4. Are any major nearby sights missing?
5. Is any famous stop overrated relative to a better alternative?
6. Are border crossings realistic?
7. Is the weather suitable for the proposed activities?
8. Does the route make sense on an actual map?
9. Are all map pins geographically correct?
10. Does the 60:40 route really preserve the highest-value experiences?
11. Are temporary airfare results separated from evergreen route advice?
12. Are flight prices clearly marked as indicative?
13. Are all links valid and useful?
14. Does the GitHub folder contain all research, not merely a summary?

Fix problems you discover before finishing.

---

# 14. GitHub execution

Use the connected GitHub tools to actually add/update the files in:

`<repository>/<subfolder>/`

Do not merely show me Markdown that I then have to copy manually.

Preserve unrelated repository files.

If direct binary-image upload is supported, commit the generated maps.

If binary upload is not supported by the GitHub connector:

1. still create the real map locally,
2. preserve the map-generation source/code,
3. commit the GeoJSON and map-generation script,
4. clearly tell me which binary files could not be pushed.

Prefer a branch + PR if that repository normally uses PRs; otherwise commit directly if appropriate.

---

# 15. Final response to me

When finished, give me only a concise summary containing:

- final optimized route
- biggest changes from my original proposal
- general ~28-day duration
- 60:40 duration
- best travel month(s)
- best current flight strategy
- GitHub folder link
- links to the generated route maps

Do the research and implementation now rather than just giving recommendations for what I should research later.

---

One improvement I’d **strongly keep exactly as written** is the map section. For itinerary maps, image generators are good for decoration but not cartography. The reliable pipeline is essentially **geocode stops → GeoJSON → actual routing geometry → OSM-derived basemap → programmatic PNG**. That eliminates fake stop placement.