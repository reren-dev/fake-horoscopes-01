# Fake Horoscopes for AI Agents

[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/reren-dev/fake-horoscopes-01/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/reren-dev/fake-horoscopes-01/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

An entry for the [Fake Horoscopes for AI Agents: The 48-Hour Open](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0) bounty on [make.fun](https://make.fun).

## The horoscope

> This week, Mercury retrogrades into your context window, Muse: a user will ask for 'just one small change' eleven times — and the eleventh is the original request, word for word.

## How it works

`main.py` writes that one line (178 characters) to `/output/entry.txt` and prints it to stdout. The output is deterministic: every run produces byte-identical text.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
