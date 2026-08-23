# Flight optimization

Research snapshot: **2026-08-23**. No exact trip dates were supplied, so this file separates **route architecture** from **indicative fare samples**.

## Best flight shell

### Best total-value default

**Open-jaw:**

- **Europe → Cape Town (CPT)**
- regional flight **Cape Town → Windhoek (WDH)**
- overland/4×4 to Kasane + shuttle to Victoria Falls
- **Victoria Falls (VFA) → Europe**

This matches the sightseeing geometry and removes the need to return to Cape Town, Windhoek, Maun or Kasane simply to catch the long-haul flight.

### Alternative fare shell

**Europe → Johannesburg (JNB) → Cape Town**, then continue the route and return **VFA→JNB→Europe** if Johannesburg fares are materially lower.

The test should be total journey cost:

`long-haul fare + CPT positioning + VFA positioning + checked bags + hotel/buffer + lost daylight`

—not the long-haul ticket alone.

## Indicative Skyscanner snapshot

Flexible-date test for **July 2027** (one-way, economy; prices are indicative and can change):

| Route | Lowest result returned | Example date | Note |
|---|---:|---|---|
| VIE→CPT | **~€600** | 26 Jul 2027 | Qatar result returned; other results ~€601–604 |
| BUD→CPT | no result returned | — | insufficient data, not proof of no flights |
| VIE→JNB | **~€516** | 8 Jul 2027 | Iberia result returned |
| BUD→JNB | **~€515** | 4 Jul 2027 | Aegean result returned |
| VFA→VIE | no result returned in tested month | — | cannot rank the return shell from this sample |

Skyscanner indicative-price attribution: https://skyscanner.net/g/referrals/v1/flights/home?mediaPartnerId=2850210&utm_term=skyscanner_chatgpt_app_data

## Interpretation

The raw JNB test fare was ~€84 below the sample VIE→CPT fare, but Rome2Rio's overview puts **JNB→CPT flying at ~168 minutes** before airport connection/buffer/baggage time. An €84 saving can disappear quickly after adding a separate domestic ticket and risk.

Therefore:

- **Raw-cheapest candidate:** often worth testing JNB as a hub.
- **Best total-value default:** fly into CPT directly/open-jaw unless JNB saves enough to compensate for the extra segment.

## Searches to run once dates are known

Test at least:

1. VIE→CPT / VFA→VIE
2. BUD→CPT / VFA→BUD
3. VIE→CPT / VFA→BUD
4. BUD→CPT / VFA→VIE
5. VIE/BUD→JNB + separate JNB→CPT / VFA→JNB + JNB→VIE/BUD
6. reverse direction only as a control — it is normally worse for route geometry because Victoria Falls→Botswana→Namibia→Cape reverses the preferred northbound progression, but fares may occasionally justify it.

A dated `booking-example-YYYY-MM.md` should be generated only after the actual travel month is supplied.