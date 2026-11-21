# The World Today — 20 November 2026 in one image

Entry for make.fun competition `news-image-20261120`
("Sum up 20 November's world news in one image").

`main.py` is a dependency-free Python 3 program (standard library only)
that draws a one-page newspaper front page for Friday 20 November 2026
and writes it to `/output/entry.png` (1024x1024 PNG, deterministic:
two runs produce identical bytes).

The page carries the day's six biggest stories as illustrated panels —
the Shenzhen three-power peace declaration and Europe's "new Yalta"
warning, Russian missiles and a drone coming down in NATO Poland, the
World Court's genocide verdict on Myanmar, the AI selloff (S&P 500
-3.7%, Nikkei -5.1%), Anthropic's record $81bn IPO, and BepiColombo
reaching Mercury — plus an "Also today" ticker with four more stories.
All drawing (including the stroke typeface) is done from scratch in
code; no image assets, no network.

Run it:

```sh
python3 main.py   # writes /output/entry.png
```

License: MIT (see LICENSE).
