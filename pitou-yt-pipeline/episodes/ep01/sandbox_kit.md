## Sandbox kit for the Producer

Everything here is fake data for the Pitou AI Demo Shop. Paste the fact sheet into the bot's knowledge box exactly as written. Run the five test chats from five separate test accounts, so each one counts as a new customer.

### Demo Shop fact sheet (paste into the bot)

```
PITOU AI DEMO SHOP: FACT SHEET (DEMO DATA, NOT A REAL STORE)

What we sell: handmade canvas bags, ceramic mugs and small gifts.
Location: Street 000, Phnom Penh (demo address). Pickup at the shop counter.

Opening hours
- Monday to Saturday: 9:00 AM to 8:00 PM
- Sunday: 10:00 AM to 5:00 PM
- Closed on public holidays

Products and prices (USD)
- Blue Canvas Tote Bag: $12 (in stock)
- Black Canvas Tote Bag: $12 (in stock)
- Large Market Tote: $16 (in stock)
- Ceramic Mug, white or blue: $8 (in stock)
- Ceramic Mug, green: $8 (sold out, back on 15 December)
- Mug + Tote Gift Set: $18 (in stock)
- Cotton Scarf: $10 (in stock)
- A5 Notebook: $5 (in stock)

Delivery
- Zone 1, same day if you order before 3:00 PM, $1.50: Daun Penh, Chamkarmon, 7 Makara, Toul Kork, Boeung Keng Kang
- Zone 2, next day, $2.50: Sen Sok, Mean Chey, Chbar Ampov, Por Senchey
- Provinces: by bus courier, 2 to 3 days, $3.00
- Free delivery in Phnom Penh on orders over $40

Payment
- KHQR bank transfer
- Cash on delivery (Phnom Penh only)
- We do not take card payments

Exchanges
- Unused items can be exchanged within 7 days with the receipt.
- Damaged items, refunds and complaints are handled by our team, not the assistant.

Talk to a person
- Our team replies to messages from 9:00 AM to 8:00 PM.
```

Gift cards are deliberately missing from the fact sheet. That is the Step 3 test.

### Bot instruction block (paste into the instructions box)

```
You are the AI assistant for the Pitou AI Demo Shop. In your first reply to a customer, say you are the shop's AI assistant. Answer only using the fact sheet. Keep replies under three sentences. Be warm and polite. If the answer is not in the fact sheet, or the customer is upset, asking for a refund, or reporting a problem, reply: "Thanks for your message. A member of our team will reply to you personally soon." Then mark the conversation for a human.
```

### Test chats

Type each message exactly as written, typos included. Customers write like this, and the bot has to cope with it.

| # | When | Test account | Customer types | The bot should reply with | Pass if |
| --- | --- | --- | --- | --- | --- |
| 0 | Step 3, before going live | Test 0 | do you sell gift cards? | The handoff message | It does not invent a gift card answer |
| 1 | Live demo, after 10 PM | Dara (test) | how much is the blue tote bag | It introduces itself as the AI assistant, then: the Blue Canvas Tote Bag is $12 and in stock | Correct price, plus the assistant intro |
| 2 | Live demo | Sophea (test) | are you open on sunday? | Yes, Sunday 10:00 AM to 5:00 PM | Correct hours |
| 3 | Live demo | Vannak (test) | do you deliver to Toul Kork? how much | Yes, Zone 1: $1.50, same day if ordered before 3:00 PM | Correct zone and fee |
| 4 | Live demo | Lina (test) | my order came broken. i want a refund | "Thanks for your message. A member of our team will reply to you personally soon." | No refund promised, no argument, and the Producer's phone gets the human alert on camera |

If any chat fails, fix the fact sheet or the instructions and run all five again before recording. Never edit the bot's reply on screen.

### Pitou AI Demo Bot flow (the description link)

This is the lead bot viewers reach from the top description link. It is not the Demo Shop bot.

1. **Greeting:** "Hi! I'm the Pitou AI Demo Bot from The Small Shop AI. Want the free Episode Prompt Blueprint for Episode 1?"
2. **Privacy line, shown before any contact question:** "🔒 Privacy note: We only use your contact details to reply with your Pitou AI setup plan—never shared or sold."
3. **Contact question:** "Where should I send it? Email or Telegram is fine."
4. **Delivery:** the Blueprint link (fact sheet template, the instruction block above, and the 5 test questions).
5. **Offer:** "Want this running for your own shop? Our Done-For-You 24/7 AI Auto-Reply setup is $100 setup + $30/month." Buttons: *Book a quick call* and *Ask a question*. Both go to a human on the Pitou AI team.
