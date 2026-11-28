# Home essentials store (working name: Phteah Yeung Home)

A walk-in shop beside the market in Prek Ta Meak, Khsach Kandal, Kandal, plus online selling from the same room.

## What is here

| Path | What it is |
|---|---|
| `paste/1-chatgpt.txt` | Complete prompt for ChatGPT: market, prices, seasonality |
| `paste/2-kimi.txt` | Complete prompt for Kimi: factories, import routes, landed cost |
| `paste/3-gemini.txt` | Complete prompt for Gemini: official rules, couriers, Khmer copy |
| `paste/4-critic-after-plan.txt` | Short prompt to make one of them attack the finished plan |
| `plan/business-plan.md` | Business plan v1, sections A to O |
| `plan/financial-model.xlsx` | Model with Inputs, Monthly, UnitEconomics and WeeklyTracker sheets |
| `plan/product-scoring.csv` | 42 products scored and classed A, B or C |
| `plan/assumptions.md` | Every unverified number and how to check it |
| `ops/` | Reply scripts, checklists, warranty card, in Khmer and English |
| `inputs/` | Put the three AI answers here |

## How to run the other three AIs

1. Open one `paste` file, select all, copy, paste into the matching tool as a single message. Turn on deep research or web search in the tool if it has the option.
2. Attach the shop and wholesaler photos if the tool accepts images.
3. When the answer is finished, save it as `inputs/chatgpt.md`, `inputs/kimi.md`, `inputs/gemini.md` (or paste the HANDOVER SUMMARY section back into the Claude Code chat).
4. Claude Code then merges the three, lists contradictions and updates the plan and the model.
5. Last, paste `4-critic-after-plan.txt` followed by the updated business plan into whichever tool gave the sharpest answer.

Rule for conflicts: where two tools disagree on a fact, trust neither until a wholesaler quote, a courier rate card or an official page settles it.
