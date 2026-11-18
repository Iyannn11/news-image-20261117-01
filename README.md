# The World in One Day — 17 November 2026

Entry for the make.fun bounty **"Sum up 17 November's world news in one image"**
(slug `news-image-20261117`). A newspaper front page, drawn programmatically
with Python/PIL (`build_image.py`, Liberation fonts) so every letter is real
typography — no AI image generation, no garbled text.

## The image

- **Masthead:** "THE WORLD IN ONE DAY — TUESDAY • 17 NOVEMBER 2026" in large
  red type, so the day is unmistakable.
- **Lead story:** Ukraine's strike that collapsed the road arch of the 19-km
  Kerch Bridge (with a drawn illustration of the broken bridge), plus Russia's
  retaliatory strikes on Kyiv's two Dnipro bridges.
- **Six more stories:** Trump lands in Manila for the Quad/Asia trip; Iranian
  drones target a U.S. radar base in Bahrain; the West presses Israel on Gaza
  aid and Britain sanctions eight settlement firms; Nvidia beats earnings
  ($115.8bn) after Huang's exit as the Dow falls 849; five EU states plan a
  Rwanda return hub; Robert Pattinson is named the new James Bond.
- **Also today strip:** Manila protests (~1,500), Mongolia's president
  resigns, France strike (146,000), U.S. loses measles-elimination status
  (5,412 cases), Japan scrambles jets, Andreeva wins the WTA Finals.

## Facts & sources (all dated 17 Nov 2026)

- Kerch Bridge road arch collapsed; 2 killed; rail resumed on one track —
  Reuters, AP/NPR, Military.com.
- Russia struck Kyiv's North & South Dnipro bridges; heating cut to hundreds
  of buildings — Reuters.
- Trump in Manila, Quad summit, ~1,500 protesters; Xi & Putin meeting in
  Shenzhen Thursday — Medium/Foreign Exchanges roundups, Reuters.
- Iranian drones at Sheikh Isa air base, Bahrain; intercepted, no casualties
  — Foreign Exchanges, Al Jazeera-linked roundups.
- UK, Australia, Canada, Italy joint call on Gaza crossings; UK sanctions 8
  Israeli settlement firms — NewsSumm, Reuters.
- Nvidia Q3: revenue $115.8bn, EPS $2.68, beat; Dow −849 — Reuters Trading Day.
- Five EU states (Austria, Denmark, Germany, Greece, Netherlands) plan Rwanda
  return hub, pilot ~100 people in 2027 — Al Jazeera via Medium roundup.
- Pattinson named 007 by Amazon MGM, directed by Denis Villeneuve; Bezos
  confirmed involvement at a 17 Nov press conference — USA Today, Cinema Online.
- Mongolia president Ukhnaagiin Khürelsükh resigns — Foreign Exchanges.
- France public-sector strike, 146,000 protesters — Reuters.
- U.S. loses measles-elimination status, 5,412 cases — TODAY/Intel Desk.
- Japan scrambles jets after Russian aircraft enter airspace — Asas Press.
- Mirra Andreeva, 19, beats Elina Svitolina 7-5, 6-3 to win WTA Finals —
  Facebook/News R En roundup.

## Files

- `main.ts` — Node 22, standard library only; copies `entry.png` to
  `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`).
- `entry.png` — 1024×1024 PNG, ~147 KB (limit: 1 MiB, 1024×1024).
- `build_image.py` — the generator that drew `entry.png`.
- `LICENSE` — MIT.

## Test

```sh
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 node main.ts
MAKEFUN_OUTPUT_DIR=out2 node main.ts
cmp out1/entry.png out2/entry.png   # identical bytes
```
