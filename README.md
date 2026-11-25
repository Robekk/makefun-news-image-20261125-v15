# The World in One Day — Wednesday 25 November 2026

[![bounty](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Robekk/makefun-news-image-20261125-v15/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Robekk/makefun-news-image-20261125-v15/reward.svg)](https://make.fun/bounty/news-image-20261125)

Entry for the [make.fun](https://make.fun) bounty **news-image-20261125** —
"Sum up 25 November's world news in one image."

One broadsheet front page carrying 38 dated stories from Wednesday
25 November 2026, drawn in a flat editorial style: a navy masthead, three
colour zones (Asia-Pacific, Europe · Africa · Middle East, Americas), a
numbers band, a UTC timeline, thirteen illustrated story cards, a world
map with a pin for every illustrated story, 25 one-line briefs, and a
date-check box listing the stories deliberately left out as other days'
news. Wires were read to 12:45 UTC on the day.

Headlines include Shenzhou-24 docking at Tiangong with the first foreign
astronaut aboard, the WHO pulling its Ebola teams out of a Congo
hospital, and Australia signing a security pact with Solomon Islands.

## Running it

`python3 main.py` copies the committed `entry.png` into the harness
output directory (`MAKEFUN_OUTPUT_DIR` or `OUTPUT_DIR`, falling back to
`/output`) and verifies the copy byte for byte. Standard library only.
