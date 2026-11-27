# EP01: I Built a 24/7 AI Reply Bot for a Small Shop (No Code)

[LOCKED 2026-11-27. Thumbnail: NEVER MISS A CUSTOMER. Narration source for voice/generate_voice.py. Lines in brackets are cues and are not spoken.]

## Hook (0:00 to 0:25)

[SCENE: a phone face-down on a dark shop counter lights up. Clock reads 11:47 PM.]
[ON-SCREEN TEXT: 11:47 PM. New message.]
[STYLE: calm, quiet, slightly hushed late-night tone]

It's eleven forty-seven at night. A customer just asked if you have their size in stock. You're asleep. By morning, they've bought it somewhere else.

[PAUSE]
[STYLE: none]

Today I'm building a reply bot that answers that message in seconds, for a small shop, without writing a single line of code. And I'll show you the one kind of message it should never answer on its own.

## Intro (0:25 to 0:50)

[SCENE: title card. The Small Shop AI, Powered by Pitou AI.]

Welcome to The Small Shop AI. Every week, we take one real task from a small business and hand it to AI, step by step.

[SCREEN: Pitou AI Demo Shop Facebook page, scrolling slowly]

Our test shop is the Pitou AI Demo Shop. It's a made-up store with fake products and fake customers, so you can copy everything you see without touching anyone's real data.

## The problem (0:50 to 1:50)

[SCENE: chat bubbles stack up one by one: "How much?", "Open today?", "Do you deliver?", "Still in stock?"]

If you run a shop, you know the pattern. Most messages are the same few questions. How much is this? Are you open today? Do you deliver to my area? Is this still in stock?

Each one takes thirty seconds to answer. But they arrive while you're serving a customer, driving, cooking dinner, or sleeping. So they wait. And a customer who waits often keeps scrolling.

[SCENE: two crossed-out options: "Hire someone to watch the inbox" and "Thanks, we'll get back to you"]

You could hire someone to watch the inbox all day. Most small shops can't. You could switch on one of those old auto-replies that say, thanks, we'll get back to you. Customers can tell that's not a real answer.

What we want is different. Something that gives the real answer, right away, using your own shop information. And knows when to stop and call you.

## The plan (1:50 to 2:40)

[SCENE: diagram builds left to right. Customer message, then bot reads the fact sheet, then answer. A branch drops down: complaint or unknown question, then a person.]

Here's the plan. Three parts.

One: a fact sheet. Everything customers usually ask, written down once. Products, prices, hours, delivery areas, how to pay.

Two: the bot. It reads each new message, finds the answer in your fact sheet, and replies in a short, friendly way.

Three: a handoff rule. If a message is a complaint, a refund, or anything the fact sheet doesn't cover, the bot doesn't guess. It tells the customer a person will reply, and it alerts you.

[ON-SCREEN TEXT: A bot that guesses is worse than no bot.]

That third part matters most. A bot that makes up answers is worse than no bot at all.

## Step 1: The fact sheet (2:40 to 3:50)

[SCREEN: a blank Google Doc titled "Demo Shop Fact Sheet" fills in section by section]

Let's start with the fact sheet. Open a plain document. No special format needed.

Write it the way you'd brief a new staff member on their first day. Your shop name and what you sell. Opening hours, including holidays. Prices for your best sellers. Delivery: which areas, how long it takes, how much it costs. How customers can pay. And how to reach a real person.

[ON-SCREEN TEXT: Use your customers' exact words.]

One tip. Scroll through your last fifty messages and copy the questions exactly as customers wrote them. If people type "how much," don't only write "price list." The bot finds the right answer more often when your fact sheet speaks your customers' language.

[SCREEN: the finished Demo Shop fact sheet, one page]

For the Demo Shop, the whole thing fits on one page. Give yours a quiet hour. It's the most important hour in this whole video.

## Step 2: Connect the bot (3:50 to 5:00)

[SCREEN: {BOT_PLATFORM} dashboard]

Next, the bot itself. We're using {BOT_PLATFORM}, a no-code chatbot builder. Most tools like it follow the same three steps.

[SCREEN: Connect channel, log in, choose the Demo Shop page]

First, connect the channel your customers already use. For the Demo Shop, that's our Facebook page. Click connect, log in, choose the page. Done.

[SCREEN: fact sheet pasted into the knowledge box]

Second, give the bot your fact sheet. Paste it in, or upload the document.

[SCREEN: instructions box. The instruction block below is typed in.]

Third, give it instructions. This is where you set its personality and its rules. Here's what we wrote.

[ON-SCREEN TEXT, full instruction block shown on screen for 10 seconds:]

> You are the AI assistant for the Pitou AI Demo Shop. In your first reply to a customer, say you are the shop's AI assistant. Answer only using the fact sheet. Keep replies under three sentences. Be warm and polite. If the answer is not in the fact sheet, or the customer is upset, asking for a refund, or reporting a problem, reply: "Thanks for your message. A member of our team will reply to you personally soon." Then mark the conversation for a human.

That last part is the handoff rule. Every word of this instruction is in the free Episode Prompt Blueprint, so you don't need to pause and copy it.

## Step 3: Test it like a difficult customer (5:00 to 6:00)

[SCREEN: the test chat panel in {BOT_PLATFORM}]

Before you go live, test it like your most annoying customer. Ask the normal questions. Then ask strange ones. Then ask something that isn't in the fact sheet at all.

[SCREEN: test message "Do you sell gift cards?" The bot replies with the handoff message.]

We asked about gift cards. The Demo Shop doesn't mention gift cards anywhere. And look: the bot didn't invent an answer. It handed off. That's what we want.

[ON-SCREEN TEXT: Wrong answer? Fix the fact sheet.]

If a test answer comes back wrong, the fix is almost always in the fact sheet, not in the bot. Add the missing fact. Test again.

## Live demo (6:00 to 7:30)

[PRODUCER DEMO, 60 to 90 seconds. Record the phone screen in real time with the clock visible after 10 PM. Use the four test chats from the sandbox kit, in order. No cuts that hide response time.]

Now the real test. It's after ten at night, and customers are messaging the Demo Shop.

[PAUSE]

Price. Answered.

[PAUSE]

Opening hours. Answered.

[PAUSE]

Delivery. Answered, with the fee straight from the fact sheet.

[PAUSE]

And now a complaint. A broken order and a refund request. The bot doesn't argue, and it doesn't promise anything. It tells the customer a person will reply, and my phone gets the alert.

That's exactly the line we want. The bot handles the routine. A human handles the relationship.

## Three rules before you switch it on (7:30 to 8:40)

[SCENE: three cards appear one at a time]

Three rules before you switch this on for your real shop.

[ON-SCREEN TEXT: 1. Say it's an assistant.]

Rule one: tell customers they're talking to an assistant. That's why our instruction makes the first reply say so. People are fine with a bot that's honest and fast. They're not fine with feeling tricked.

[ON-SCREEN TEXT: 2. Read every chat for a week.]

Rule two: read the conversations every day for the first week. Every wrong or weak answer points to a fact you should add.

[ON-SCREEN TEXT: 3. Keep the fact sheet fresh.]

Rule three: update the fact sheet whenever something changes. A new price, holiday hours, something out of stock. The bot only knows what you tell it. An old fact sheet gives confident, wrong answers.

## Recap (8:40 to 9:10)

[SCENE: the plan diagram from 1:50 returns, each part ticking green]

So here's the whole build. Write a one-page fact sheet in your customers' own words. Connect a no-code bot to the channel they already use. Give it strict instructions with a handoff rule. Test it like a difficult customer. Then read its chats every day for a week.

Your shop answers at midnight. And you still get to sleep.

## Call to action (9:10 to 9:35)

[ON-SCREEN TEXT: Free Episode Prompt Blueprint. Link at the top of the description.]
[STYLE: warm, friendly, unhurried]

Want the exact prompts I used today? Grab the free Episode Prompt Blueprint. The link is at the very top of the description. Our demo bot sends it to you in seconds, and you'll see how a 24/7 auto-reply feels from the customer's side. If you'd rather have it done for you, check our flat-rate setup pricing right inside the demo bot.

## Outro (9:35 to 9:50)

[SCENE: end screen with subscribe button and the next-video slot]

Next week: five boring shop tasks you can hand to AI this week. Subscribe so you don't miss it. See you then.
