# Sources

Research date unless noted otherwise: **27 August 2026**.

The route uses current official/primary sources where possible, plus specialist/operator sources for conditions that governments and tourism boards do not publish at useful granularity. Temporary fares are kept in `flights.md` and the dated booking example rather than treated as evergreen facts.

## Scientific / season evidence

- **Satellite radar altimetry reveals spatial and temporal changes in water surface smoothness in the Salar de Uyuni, Bolivia** — *Communications Earth & Environment* (2025). https://www.nature.com/articles/s43247-025-02715-1  
  Supports: the wet-season smooth-water period begins in December, peaks from late January to early March, and late February has the highest observed share of mirror-like radar-smooth surfaces (~50% of bursts in the analysis).

## Official / primary heritage sources

- **Tiwanaku: Spiritual and Political Centre of the Tiwanaku Culture** — UNESCO World Heritage Centre. https://whc.unesco.org/en/list/567/  
  Supports: importance, altitude/context and verified Tiwanaku location.
- **Historic City of Sucre** — UNESCO World Heritage Centre. https://whc.unesco.org/en/list/566/  
  Supports: historic-city value and coordinates.
- **City of Potosí** — UNESCO World Heritage Centre. https://whc.unesco.org/en/list/420/  
  Supports: global silver-mining importance, coordinates, and current World Heritage in Danger status.
- **Bolivia World Heritage properties** — UNESCO. https://whc.unesco.org/en/statesparties/bo/  
  Supports: Bolivia property list and Cal Orck’o/Sajama tentative-list context.

## Official travel / safety sources

- **Bolivien – Reiseinformation** — Austrian Federal Ministry for European and International Affairs (BMEIA), status 12 Aug 2026. https://www.bmeia.gv.at/reise-services/reiseinformation/land/bolivien  
  Supports: regional safety level 3 in La Paz/El Alto, Cochabamba and Santa Cruz; level 2 elsewhere; protests/roadblocks; crime guidance; advice against night overland bus travel; entry/insurance requirements; altitude warning.
- **Peru – Reiseinformation** — BMEIA, status 15 Aug 2026. https://www.bmeia.gv.at/reise-services/reiseinformation/land/peru/  
  Supports: current Peru safety level and disruption context.
- **Chile – Reiseinformation** — BMEIA, status 18 Jul 2026. https://www.bmeia.gv.at/reise-services/reiseinformation/land/chile  
  Supports: current Chile safety level and theft/robbery context.
- **Bolivia road passability / roadblocks** — Administradora Boliviana de Carreteras. https://transitabilidad.abc.gob.bo/  
  Supports: current road-condition check referenced by BMEIA.

## Chile / Atacama official tourism sources

- **San Pedro de Atacama** — Chile Travel, updated 10 Feb 2026. https://chile.travel/en/destinations/san-pedro-de-atacama/  
  Supports: attraction cluster and Calama airport connection.
- **Tatio Geysers** — Chile Travel, updated 9 Feb 2026. https://chile.travel/en/attractions/tatio-geysers/  
  Supports: ~4,300 m altitude, dawn timing, ~80 km / 1.5 h road approach.
- **Piedras Rojas (Red Stones)** — Chile Travel, updated 9 Feb 2026. https://chile.travel/en/attractions/piedras-rojas-red-stones/  
  Supports: >4,000 m altitude, ~150 km / 2.5 h from San Pedro, acclimatization need.
- **San Pedro de Atacama 3–5 day itinerary** — Chile Travel, updated 21 Jul 2026. https://chile.travel/en/itineraries/san-pedro-de-atacama-romance-adventure-and-relaxation-in-the-heart-of-the-desert/  
  Supports: 3–5 day planning range.

## Uyuni mirror / practical tour sources

- **Best Time to Visit Salar de Uyuni for the Mirror Effect** — Salar de Uyuni Tours, updated 4 Apr 2026. https://salaruyunitours.com/best-time-to-visit-for-the-mirror-effect  
  Supports: practical interpretation of shallow-water/wind conditions, late-Jan–early-Mar peak, wet-season access limitations. Used as a specialist source; scientific timing is independently supported by the Nature paper above.
- **How to Visit Salar de Uyuni** — Salar de Uyuni Tours, 2026. https://salaruyunitours.com/how-to-visit  
  Supports: wet/dry season operational differences and Incahuasi access caveat.
- **Recommendations for visiting the Salar de Uyuni** — Uyuni Salt Flats travel guide, 2026. https://www.uyunisaltflats.travel/en/blog-en/recommendations-for-visiting-the-salar-de-uyuni/  
  Supports: rainy-season mirror and common 3-day 4×4 format.

## Transport research

- **Rome2Rio route search: La Paz → Sucre** — queried 27 Aug 2026. https://www.rome2rio.com/map/La-Paz/Sucre  
  Snapshot used: flight ~67 min, bus ~570 min; recheck operating schedule before booking.
- **Rome2Rio route search: Potosí → Uyuni** — queried 27 Aug 2026. https://www.rome2rio.com/map/Potos%C3%AD/Uyuni  
  Snapshot used: bus ~236 min.
- **Chile Travel / El Loa Airport context** — see San Pedro/Tatio sources above.  
  Supports: CJC as the practical San Pedro gateway.

## Flight / fare sources

Fare observations are intentionally labeled **indicative**. Inventory changes continuously.

- **Skyscanner** — VIE–LIM / BUD–LIM / BUD–SCL / VIE–VVI searches, accessed 27 Aug 2026. https://www.skyscanner.net/  
  Supports: relative fare-market anchors summarized in `flights.md`.
- **Austrian Airlines multi-city/open-jaw booking capability** — airline booking site, accessed Aug 2026. https://www.austrian.com/  
  Supports: multi-city/open-jaw booking strategy.
- **Air Europa / Boliviana de Aviación route research** — airline/route checks, Aug 2026. https://www.aireuropa.com/ and https://www.boa.bo/  
  Supports: Madrid–Santa Cruz as a nonstop positioning fallback and Bolivian domestic-air options.

## Geographic / map sources

The committed map is not AI-generated. Stop coordinates were cross-checked using a combination of:

- UNESCO World Heritage coordinates for Tiwanaku, Sucre and Potosí;
- OpenStreetMap / Nominatim and GeoNames/Wikidata-style gazetteer references for cities/natural features;
- official Chile Travel destination context for San Pedro/Calama-area attractions;
- repository map script using **Basemap/GSHHS coastlines and national borders**.

Route lines in `route.geojson` are deliberately labeled as planning connectors unless a real routed geometry is supplied. Flight, bus/road and 4×4 segments remain semantically distinct rather than pretending there is a single driveable road.

## Research quality caveat

The mirror effect and high-altiplano access are inherently variable. No source can guarantee water, calm wind or an open desert track on a specific future date. The itinerary manages this uncertainty with extra nights and downstream buffers rather than claiming certainty.
