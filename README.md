# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/tukiyatlampu/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/tukiyatlampu/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Wednesday 18 November 2026: 50 sourced stories, a UTC timeline and a date check.

One dense broadsheet poster (1024x1024, 197,338 bytes) summing up the day's world news: the US strike on Qeshm Island and Iran's retaliation against US bases in Kuwait and Bahrain, the Xi-Putin meeting in Shenzhen ahead of Thursday's three-way summit with Trump, and Ukraine's third strike on the Kerch Bridge in a week — plus 47 more sourced stories across regions and fields, a six-beat UTC timeline, and an explicit date check. Every story is tagged with its outlet (Reuters, AFP, AP, BBC, PAHO, IAEA, WHO, UNEP, EU, NASA, wire reports).

## Run it

```sh
python3 main.py
```

Decodes `image.b64` and writes it to `/output/entry.png`. No network. Two runs write identical bytes. The poster is drawn offline by `build_poster.py` (Pillow, standard library + PIL only for the build step; the entry program itself needs only the standard library).

## Design

- 3 lead stories, 6-beat UTC timeline, 41 one-line stories in two columns — 50 unique stories, asserted by `build_poster.py`.
- Flat colours only, so the PNG stays small (197 KB, well under the 1 MiB cap).
- Date check in the footer: Wednesday 18 November 2026, all 50 stories reported 18 Nov 2026, nothing from before 13 Nov 2026.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
