# The World in One Day — 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/xarfhltemberang/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/xarfhltemberang/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A make.fun `news-image-20261125` bounty entry: one 1024×1024 image summing up
the world's news of Wednesday 25 November 2026. Every story below was first
reported on 25 November 2026 (in at least one time zone) and verified against
Reuters / BusinessWorld / FXStreet / ESA coverage published that day.

## The six stories

1. **Trade (lead story) — US to unveil tariffs on 16 partners.**
   Washington is poised to release findings of its excess-capacity probe, with
   new duties on China, the EU, Japan and 13 others. China faces a 20% cap;
   the EU, Japan and South Korea 15%. (Reuters via BusinessWorld, 25 Nov 2026)
2. **Markets — Asian stocks tumble on tariff threats.**
   Asia-Pacific shares fell 2.3%. Seoul slid 5.3%, Taiwan 5.1% and the
   Nikkei 2.9%. (Reuters, Singapore, 25 Nov 2026)
3. **US economy — US inflation data due as Fed weighs hike.**
   October PCE and Q3 GDP land today, with a December hike near-certain.
   (BEA release due 25 Nov 13:30 GMT; CME FedWatch ~97% for a December hike)
4. **Australia — Australia inflation runs hotter than forecast.**
   October CPI rose 4.9%, beating forecasts and lifting the Aussie dollar.
   (Australian Bureau of Statistics / Reuters, 25 Nov 2026)
5. **Space — ESA unveils first close-ups of Dimorphos.**
   Hera shares its first close-up images of the asteroid DART struck in 2022.
   (ESA livestream reveal, 25 Nov 2026)
6. **Energy — Oil falls as glut fears offset Mideast tension.**
   Brent crude slipped to $90.97 a barrel as rising supply and a surplus
   outlook outweighed Strait of Hormuz disruption fears. (Reuters, Tokyo,
   25 Nov 2026)

## Method

- `draw.py` renders the infographic with Pillow (DejaVu fonts, navy/gold
  palette, one lead story, a 2×2 grid, one bottom story). Run it locally:
  `python3 draw.py` writes `entry.png` (1024×1024 PNG, deterministic bytes).
- `main.py` is the competition entrypoint (Python 3.13, standard library
  only): it copies the pre-rendered `entry.png` to `$MAKEFUN_OUTPUT_DIR`
  (`/output` in the grader), because the grader's container has no Pillow.
  Two runs write byte-identical output.
- Every story's date was verified against real outlets before submission;
  the lead, markets, Australia and oil figures match the Reuters wires of
  25 November 2026 exactly.

## Run it

```sh
python3 draw.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=xarfhltemberang&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>

## License

MIT — see `LICENSE`.
