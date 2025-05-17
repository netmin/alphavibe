# AlphaVibe

> **A self‑learning crypto idea machine** – AlphaVibe watches the market, asks an AI model to write tiny Python trading rules, tests them on historical data, and keeps the winners. No spreadsheets, no heavy math – just instant, readable ideas.

---

## 1 · What does AlphaVibe do?

1. **Collects prices** from public exchange APIs.
2. **Asks an AI model** (OpenAI Codex or a local Llama/Mistral) to write a few lines of strategy code.
3. **Back‑tests** that code on past candles with Backtesting.py.
4. **Learns**: good rules stay, weak ones get rewritten.

All results are saved as simple CSV/HTML reports so anyone can inspect them in a browser or spreadsheet.

---

## 2 · Why should you care?

* **Ideas, not black boxes** – every strategy is plain Python you can open and tweak.
* **Proof included** – equity curve, Sharpe ratio and draw‑down for each idea.
* **Runs locally** – your API keys never leave your machine.
* **Tiny footprint** – installs with one command, runs in a terminal.

---

## 3 · Quick start

```bash
# 1· clone & enter
git clone https://github.com/netmin/alphavibe.git
cd alphavibe

# 2· one‑shot install (fast "uv" manager)
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv --python 3.11 .venv && source .venv/bin/activate
uv sync                       # installs runtime + dev tools

# 3· run the learner
python -m alphavibe.learn
```

The first run fetches one month of BTC/USDT candles, writes a simple moving‑average rule, tests it and prints a score table.

---

## 4 · How to contribute

We ❤️ pull requests and friendly discussions.

1. **Fork** this repo and create a branch

   ```bash
   git checkout -b feature/my-cool-idea
   ```
2. **Write code or docs** – keep it functional, no heavy OOP.
3. **Run tests locally**

   ```bash
   uv run -- pytest -q
   ```
4. **Open a pull request** – GitHub CI will run the same tests.

Not sure where to start? Grab any *“good first issue”* or open an issue to discuss ideas.

---

## 5 · Code of Conduct

We follow the [Contributor Covenant v2.1](CODE_OF_CONDUCT.md). Be kind, stay constructive, harassment or hate speech is not welcome.

---

## 6 · License

AlphaVibe is released under the **MIT License** – free to use, modify and share, but **no warranties**.
