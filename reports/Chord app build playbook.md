# [APP NAME] build playbook: phase-by-phase mega prompts for a chords app that competes with Ultimate Guitar

This document is a working playbook for a solo founder. Every section is meant to be pasted into an AI coding agent (Claude Code) or an AI writing tool with minimal editing. It is grounded in the five research notes in `research_notes/Ultimate Guitar SaaS teardown/` (product_and_business, pricing_and_funnel, complaints_and_gaps, competitors, licensing_and_tech), all compiled on 2026-10-09 from search snippets rather than full page reads. Where a number in the notes was flagged as an estimate or unverified, it is flagged the same way here. Nothing in this document is legal advice; the licensing sections are practical guidance for a founder to take to a lawyer.

## Working assumptions (confirm or change before starting Phase 0)

- Founder: solo, based in Cambodia, operating as Pitou AI, building with AI coding agents, limited budget, wants revenue early rather than a long free-growth phase.
- Product working name: "[APP NAME]" everywhere in this document.
- Market order: Khmer-language catalog first (unserved: the only prior Khmer chord apps were iOS-only and have been delisted), then Thai, Vietnamese, Indonesian and Filipino catalogs, plus a global English long tail. Worship musicians and absolute beginners are the beachhead segments.
- Platforms: Android and mobile web first (both prior Khmer chord apps were iOS-first and died), iOS second.
- Legal posture: chords plus song structure first, user-generated content under a notice-and-takedown policy, lyrics licensing (LyricFind or Musixmatch style) only after revenue, and never copying Ultimate Guitar tab text.
- Monetization: a free tier with no forced trial; a local-priced subscription (a sub-$2 per month tier in Cambodia, founder assumption, not yet validated) billed by KHQR per-cycle invoice on web and by app store IAP through RevenueCat; a global tier priced below Ultimate Guitar; a one-time ad-removal purchase matching the Southeast Asian norm; and transparent cancellation as a stated differentiator against Ultimate Guitar's billing complaints and the 2025 class action.

## 1. One-page summary

### What Ultimate Guitar does

Ultimate Guitar (UG) is the founding brand of Muse Group (Limassol, Cyprus), which also owns MuseScore, Audacity, StaffPad, Hal Leonard and Tonebridge, and which bought out its private equity investor with debt in June 2026 ([Music Business Worldwide](https://www.musicbusinessworldwide.com/francisco-partners-exits-its-minority-investment-in-muse-group-owner-of-audacity-hal-leonard-and-ultimate-guitar/)). Muse Group's own page claims 2.1M+ tabs, 30M monthly active users and 102M app downloads ([mu.se](https://www.mu.se/ultimate-guitar)). The product is a two-track catalog: roughly two million user-submitted chord and tab pages, moderated and approved within about 48 hours ([UG Help](https://help.ultimate-guitar.com/en/articles/6749103-how-long-does-it-usually-take-for-my-tab-to-be-approved)), plus 22,500 to 29,000 staff-made, licensed "Official" tabs with backing tracks that sit behind the Pro paywall. Growth comes mainly from organic search on "song name + chords" queries, which deliver 50 to 64 percent of web traffic according to Semrush and Similarweb estimates ([Semrush](https://www.semrush.com/website/ultimate-guitar.com/), [Similarweb](https://www.similarweb.com/website/ultimate-guitar.com/)). Revenue comes from Pro subscriptions (web list price about $24.99 per month or $99.99 per year, almost always shown at "80% off"; US App Store bundle $9.99 per month or $59.99 per year; all prices as observed by third parties, not verified against a live price page) and from ads on the free tier ([Guitar Chalk](https://www.guitarchalk.com/ultimate-guitar-pro-review/), [App Store](https://apps.apple.com/us/app/ultimate-guitar-chords-tabs/id357828853)).

### Where it is weak

The complaint record is consistent across Trustpilot, the app stores and forums. The largest theme is billing: a 7-day trial attached to the annual plan, auto-renewal at list price, refunds refused, and a multi-step cancellation that must be completed on the platform of purchase ([Trustpilot](https://www.trustpilot.com/review/www.ultimate-guitar.com), [UG Help](https://help.ultimate-guitar.com/en/articles/6741667-how-to-cancel-your-ultimate-guitar-subscription)). A federal class action, Teilmann et al. v. Ultimate Guitar USA LLC, 25-cv-5310 (N.D. Cal., June 2025), alleges inadequate auto-renew disclosure and hard cancellation ([Truth in Advertising](https://truthinadvertising.org/class-action/ultimate-guitar/)). The second theme is ad and upsell pressure, including for paying subscribers ([unitQ](https://unitq.com/unitq-scorecards/ultimateguitar)). The third is paywall creep: Transpose, Simplify and autoscroll were once free and are now Pro ([App Store ZA reviews](https://apps.apple.com/za/app/id357828853)). Then come forced onboarding (a 14-step quiz straight into a three-tier paywall, per [ScreensDesign](https://screensdesign.com/apps/ultimate-guitar-chords-tabs/)), inaccurate user tabs, and a cluttered small-screen UI. Offline access is limited to favorites that must be re-downloaded after reinstall ([UG Help](https://help.ultimate-guitar.com/en/articles/7936845-mobile-offline-access-to-your-favorites-how-to-add-load-and-troubleshoot)). Non-Western catalogs are thin and user-dependent: in Indonesia and Thailand, free local sites (Chordtela, DoChord, ChordTabs) out-rank UG, and Khmer is essentially unserved ([GoodStats](https://data.goodstats.id/statistic/10-website-musik-paling-banyak-dikunjungi-di-indonesia-2026-ELc0K), [Semrush](https://fr.semrush.com/website/chordtabs.in.th/competitors), [appshunter: Khmer Chords](https://appshunter.io/ios/app/khmer-chords/id1630776488)).

### The wedge for [APP NAME]

Each wedge below maps to a finding in the notes.

Khmer catalog with Khmer-script search. The only two dedicated Khmer apps (Khmer Chords, Khmer Worship) were iOS-only, last updated February 2023, and are no longer on the App Store; no Khmer chord website surfaced at all ([appshunter: Khmer Worship](https://appshunter.io/ios/app/khmerworship/id1581311822)). Cambodia is Android-dominant, so Android plus web first is the correct platform order.

Full-catalog offline. Hợp âm chuẩn in Vietnam ships its whole catalog offline with incremental updates over Wi-Fi or 3G, and sells ad removal for $1.99 one-time ([App Store](https://apps.apple.com/us/app/-/id1057211347)). UG caches favorites only. For prepaid-data, mid-range Android users this is a decisive difference.

Honest billing. Monthly-first, price shown before any trial, cancel in one tap inside the app, a reminder before every renewal, and no silent second subscriptions. This converts the single largest UG complaint class and the fact pattern in the 2025 class action into a marketing message.

Beginner layer. "No strumming pattern for this song yet" is a stock placeholder on UG pages ([UG tab](https://tabs.ultimate-guitar.com/tab/maryzark/hindi-na-chords-498596)), and beginners on the JustinGuitar forum say charts show when chords change but not the bars in between ([JustinGuitar community](https://community.justinguitar.com/t/strumming-patterns/79747)). Chordtela's Indonesian success is built on "basic chords" positioning ([Mojok](https://mojok.co/terminal/chordtela-adalah-solusi-bagi-orang-yang-skill-gitarannya-pas-pasan-kayak-saya/)).

Worship features. Nashville numbers, one-tap key change, setlists and team sync are absent from UG's mobile product and served instead by OnSong (Apple-only, $59.99 one-time or $5.99 per month) and Planning Center Music Stand (about $10 per month) ([learnofchrist](https://learnofchrist.com/resources/onsong), [CRCNA](https://network.crcna.org/topic/worship/general-worship/what-are-pros-and-cons-using-planning-center-online)). Those prices are high relative to Cambodian church budgets, and a delisted "Khmer Worship" app proves local demand existed.

Teacher tools. Tonara shut down on December 8, 2023 and no chord-chart-first assignment tool has replaced it ([Wikipedia](https://en.wikipedia.org/wiki/Tonara_(company))).

Local pricing. The Southeast Asian norm is free with ads plus a cheap one-time ad removal or a low monthly premium (Hợp âm chuẩn $1.99 one-time, U-FRET 650 yen per month), not $40 per year ([App Store JP: U-FRET](https://apps.apple.com/jp/app/u-fret-70000%E6%9B%B2%E4%BB%A5%E4%B8%8A%E3%81%AE%E3%82%AE%E3%82%BF%E3%83%BC%E3%82%B3%E3%83%BC%E3%83%89/id1483940246)).

What [APP NAME] should not try to do first: licensed Official tabs with backing tracks, note-for-note Guitar Pro style tabs (the riskiest unlicensed content category per the MPA's 2006 campaign, see [Arizona Law Review](https://arizonalawreview.org/pdf/50-2/50arizlrev611.pdf)), or a video course library. Those are UG's moats and its licensing cost base.

## 2. Product spec by tier

The song page layout copies what works at UG: chord diagrams at the top, lyrics with chords above them, a sticky toolbar with transpose, capo, simplify, autoscroll and font size, and a rating plus "suggest correction" link. The underlying data model is ChordPro source per song with client-side transposition, which is the standard the notes recommend ([ChordSheetJS](https://github.com/bettermusic/ChordSheetJS), [SVGuitar](https://github.com/omnibrain/svguitar)).

### Free tier (no trial, no sign-up required to read)

- Full catalog of community chord sheets in Khmer and English (later Thai, Vietnamese, Indonesian, Filipino), with chords, section labels, key, capo and difficulty.
- Chord diagrams at top of page for guitar, ukulele and piano, with left-handed toggle.
- Transpose, capo and Simplify, kept free permanently and stated as such in the listing (direct answer to UG's paywall creep).
- Autoscroll with adjustable speed.
- Khmer-script and romanized search, artist pages, Top 100 per language, newest and trending lists.
- Full-catalog offline in the Android app (text only, small footprint) with background delta sync.
- Favorites and up to three personal setlists.
- Strumming pattern line (down and up arrows per bar) on every chart that has one, plus a "no pattern yet, add one" contributor prompt.
- Beginner mode toggle: simplified chord set (no barre chords where a substitute exists), bigger font, suggested capo for singer's range.
- Community contribution with ChordPro editor, preview, moderation queue and 48-hour review target (matching UG's stated SLA).
- "Clips": short performance videos linked to a song page, with a weekly featured set (UG's Shots with #featureme, see [UG Help](https://help.ultimate-guitar.com/en/articles/6741295-ug-shots)).
- Banner ads only, never interstitials longer than five seconds, never for paying users.

### Pro (local tier and global tier, monthly-first)

- No ads of any kind, including no cross-promotion.
- Unlimited setlists, setlist export to PDF and ChordPro, print.
- Nashville numbers and Roman numerals view with one-tap key change across a whole setlist.
- Chord variations (choose voicing per chord), custom chord diagrams.
- Personal edits saved as a private version of any public chart.
- YouTube IFrame sync: chords highlight in time with the embedded video (time-synced from stored timestamps; never from extracted audio).
- Chords-from-audio: upload a recording you have rights to and receive a draft chart (Phase 5), with an explicit accuracy notice.
- Mic chord checker for practice (Phase 5), presented as a helper, not a grader.
- Cloud sync across devices.

### Teacher and Worship tier (per leader, team members free)

- Team workspace: shared setlists, shared key per singer, per-member transpose and capo preferences.
- Assignments: a teacher assigns charts to students with a due date; students mark practice days; teacher sees a practice log (fills the gap left by Tonara).
- Setlist mode: full-screen, pedal and volume-button page turns, dark stage theme.
- Shared private song library for the team's own arrangements and original songs (no licensing exposure for the church's own compositions).
- Export: PDF with letters or numbers per member (the JotChord pattern, see [JotChord](https://www.jotchord.com/for-worship-leaders)).

### One-time purchase

- Ad removal forever, priced at the local norm (Hợp âm chuẩn is $1.99; the exact [APP NAME] price is an open question).

## 3. Phase-by-phase build prompts

Each phase lists goal, duration estimate, exit criteria and a prompt block to paste into Claude Code. Durations assume one founder working with an agent most days and are estimates, not commitments. The stack is held constant across phases so the agent does not re-decide it: Next.js (App Router, TypeScript), Supabase (Postgres, Auth, Storage, Row Level Security on every table), ChordPro as the canonical song format, SVGuitar for diagrams on web, Expo for mobile, RevenueCat for entitlements, a Python worker for audio analysis.

One licensing note before Phase 1: a mirror listing reports ChordSheetJS as GPL-3.0 ([SourceForge mirror](https://www.sourceforge.net/mirror/chordsheetjs)). If that is confirmed, using it in a closed-source commercial app has implications; the first prompt below asks the agent to verify the license and fall back to the TypeScript `chorpro-parser` ([GitHub](https://github.com/chordproject/chorpro-parser)) or a small in-house parser if needed. SVGuitar is MIT and alphaTab is MPL-2.0, both compatible with commercial use.

### Phase 0: Validation and catalog seeding

Goal: prove demand with twenty real users and seed a catalog of a few hundred Khmer and English charts that [APP NAME] has the right to host. Duration: 3 to 4 weeks, overlapping with Phase 1. Exit criteria: at least 300 reviewed charts in ChordPro (200 Khmer, 100 English), ten worship leaders or teachers who have agreed to test, a written takedown policy, and a contributor agreement.

Sourcing rules, in plain terms. Never copy text from Ultimate Guitar, Chordtela, DoChord or any other site; those pages are their contributors' work and the structure is theirs. For English, write charts yourself or through contributors who listen to the recording and transcribe chords and section structure only; bare chord progressions are the one element even publishers' critics treat as unprotectable ([Digital Music News](https://www.digitalmusicnews.com/2014/03/10/chordify/)). Do not host full lyrics until Phase 6; store section labels and short cue words at most, and get a lawyer's view on cue words before launch. For Khmer, the practical source is musicians: Khmer worship songs are often written by local churches that will license their own songs to you directly, and older Khmer songs may be out of term (one unverified blog argues Sinn Sisamouth's compositions enter the public domain in 2026 under the life-plus-50 term, [Interspace Music](https://interspacemusic.com/blog/?p=19083), which needs a lawyer's confirmation before you rely on it). Cambodia has been a Berne member since March 9, 2022, so foreign works are protected there and "hosted in Cambodia" is not a shield ([WIPO](https://www.wipo.int/wipolex/es/treaties/notifications/details/treaty_berne_287)). Register a DMCA agent with the US Copyright Office ($6 per filing, renewed every three years) and adopt a repeat-infringer policy ([US Copyright Office](https://copyright.gov/newsnet/2016/640.html)).

```text
You are helping me set up catalog tooling for [APP NAME], a chords app. Build a small internal
toolkit in a monorepo folder /tools/catalog using Node 20 and TypeScript.

Requirements:
1. Define the canonical song format as ChordPro. Write a JSON Schema for song metadata
   (title, artist, language code [km, en, th, vi, id, tl], key, capo, difficulty [1-5],
   time signature, strumming pattern as a string of D/U/x tokens per bar, contributor id,
   source_type [original, contributor_transcription, licensed, public_domain],
   rights_note, youtube_video_id, created_at, updated_at). Store chord sheets as .cho
   files plus a sidecar .json in /catalog/{lang}/{artist-slug}/{song-slug}/.
2. Write a validator CLI (`npm run validate`) that parses every .cho file, rejects any
   file containing more than 8 consecutive words of lyrics without a chord marker
   (we only host chords, section labels and short cue words until licensing is in place),
   checks that every chord symbol is in our chord dictionary, and checks that Khmer text
   is NFC-normalized Unicode.
3. Write a Google Sheets importer that reads a contributor sheet (columns: title, artist,
   language, key, capo, chordpro_text, contributor_email, rights_attestation) and emits
   files, failing any row where rights_attestation is not "yes".
4. Generate a contributor agreement template (Markdown) that grants [APP NAME] a
   non-exclusive license to host and display the chart, states the contributor transcribed
   it themselves and did not copy from another site, and explains the takedown policy.
   Also generate a notice-and-takedown policy page (Markdown) with a contact email,
   a 48-hour acknowledgement target and a repeat-infringer rule. Mark both as drafts
   for legal review.
5. Write a chord dictionary JSON for guitar, ukulele and piano: for each of the 12 roots,
   include maj, min, 7, maj7, min7, sus2, sus4, dim, aug, add9 with at least one voicing
   (fingers, barres, base fret) in the shape SVGuitar expects, plus a "simplify" map that
   points every extended chord to its nearest major or minor triad.

Acceptance criteria:
- `npm run validate` passes on a sample set of 10 Khmer and 10 English charts I will add.
- Validator exits non-zero with a clear message on a file that contains a full lyric verse.
- Chord dictionary covers at least 120 chord symbols and every entry renders with SVGuitar
  in a tiny test page.
- No network calls other than the Sheets import.
Do not scrape any website. Do not fetch anything from ultimate-guitar.com or similar sites.
```

### Phase 1: Web MVP

Goal: a fast, indexable chords site with Khmer-first search. Duration: 4 to 6 weeks. Exit criteria: song pages render in under 1.5 seconds on a mid-range Android phone over 3G, Google Search Console shows pages indexed, transpose and autoscroll work without login, and Khmer search returns correct results for both script and romanized queries.

SEO reasoning behind the prompt: chord queries are high-volume informational queries ("let it be chords" has about 38,100 monthly searches per Semrush, [Semrush](https://cw.semrush.com/website/e-chords.com/overview)), Google answers lyrics queries in the results page but does not show chords, and since March 2024 Google's scaled content abuse policy punishes mass pages with little unique value ([Google Search Central](https://developers.google.com/search/blog/2024/03/core-update-spam-policies)). So every page must carry real data (key, capo, diagrams, difficulty, strumming pattern, ratings) and no page should go live without a reviewed chart.

```text
Build the web app for [APP NAME] (a chords site) in a new Next.js project using the App
Router, TypeScript, Tailwind, and Supabase (Postgres, Auth, Storage). Use the catalog format
and chord dictionary from /tools/catalog.

Before writing code: check the license of the npm package chordsheetjs. If it is GPL-3.0
(a mirror listing says it is), do NOT use it; instead use chorpro-parser (TypeScript) or
write a minimal ChordPro parser plus transposer in /lib/chordpro that supports directives
{title} {artist} {key} {capo} {start_of_chorus} {end_of_chorus} {comment}, inline [Chord]
markers, and transposition by semitones with enharmonic spelling chosen by target key.
Use svguitar (MIT) for chord diagrams rendered server-side to inline SVG.

Database (write SQL migrations, enable Row Level Security on every table, and write
policies; anonymous users may only read published songs):
- songs(id, slug, title, title_km, artist_id, language, key, capo, difficulty, time_sig,
  strum_pattern, chordpro_text, status [draft, in_review, published, removed],
  contributor_id, source_type, youtube_video_id, rating_avg, rating_count,
  created_at, updated_at)
- artists(id, slug, name, name_km, language)
- song_versions(id, song_id, chordpro_text, author_id, created_at, note)
- ratings(song_id, user_id, stars)
- corrections(id, song_id, user_id, proposed_text, status)
- takedown_requests(id, song_id, claimant_email, reason, status, created_at)
- search: add a generated column with the title, title_km, romanized title and artist
  names; index with pg_trgm for substring matching because Khmer has no spaces between
  words and users type partial strings. Add a romanization table (khmer_token, latin) so
  "som lea" matches a Khmer title; make romanization lookups case and diacritic insensitive.

Pages:
- /chords/[artist-slug]/[song-slug]: chord diagrams at top (guitar default, ukulele and
  piano tabs), toolbar (transpose -/+, capo select with auto-recompute of shapes, Simplify
  toggle using the simplify map, autoscroll with speed slider using requestAnimationFrame,
  font size, beginner mode), the chart body, strumming pattern line, YouTube IFrame embed
  rendered beside the chart (not overlaid), rating widget, "suggest a correction" link,
  related songs. Use ISR with 1 hour revalidation.
- /artist/[slug], /top-100/[lang], /new, /search?q=, /contribute (ChordPro editor with live
  preview, requires login), /policy/takedown, /pricing (placeholder).
- JSON-LD on song pages: MusicComposition (name, composer if known, inLanguage,
  musicalKey), VideoObject for the embed, BreadcrumbList. Add hreflang for km and en,
  a sitemap index split by language with lastmod, and robots rules that exclude draft and
  removed pages.
- Khmer typography: load Noto Sans Khmer via next/font, set line-height to 1.8 for Khmer
  text, and make sure chord markers align over Khmer syllables (test with mixed-script
  lines).

Acceptance criteria:
- Lighthouse mobile performance 90+ on a song page with Slow 4G throttling; no layout
  shift when diagrams load.
- Transposing a song in G up 2 semitones yields A, B minor, D, with capo recompute
  correct; Simplify turns F#m7 into F#m and Bb into A# or Bb according to target key.
- Autoscroll keeps scrolling at a constant rate when the browser zoom is 125% (UG's
  Safari autoscroll breaks at non-100% zoom; ours must not).
- Searching "ស្រឡាញ់" and "srolanh" both return the same song.
- A draft or removed song returns 404 and is absent from the sitemap.
- RLS test: an anonymous Supabase client cannot read drafts or write to any table.
- All pages work with JavaScript disabled for reading (chart text and diagrams are
  server-rendered).
```

### Phase 2: Android app with full offline catalog

Goal: an Android app that is useful without a connection. Duration: 4 to 5 weeks. Exit criteria: full text catalog downloads on first launch in under 20 seconds on 3G, delta sync works, app works in airplane mode, installs on Android 9 devices with 2 GB RAM, Play Store listing live in Khmer and English.

Reasoning: UG's React Native app was already too large for the 4 MB instant app limit in 2018 ([Android Developers](https://developer.android.com/stories/instant-apps/ultimate-guitar)), Android users produce 61 percent of complaints in unitQ's sample ([unitQ](https://unitq.com/unitq-scorecards/ultimateguitar)), and the Hợp âm chuẩn model of whole-catalog offline is the local reference. A text-only catalog of 10,000 songs is a few megabytes, so this is cheap.

```text
Build the Android app for [APP NAME] with Expo (latest SDK; the June 2026 SDK 57 with
React Native 0.86 or newer), expo-router, TypeScript, and expo-sqlite. Reuse the ChordPro
parser from the web repo as a shared package in the monorepo (/packages/chordpro). Render
chord diagrams with react-native-svg from the same chord dictionary JSON (do not depend on
svguitar at runtime on mobile; port its drawing of frets, strings, dots, barres and
open/muted markers).

Offline catalog:
- A Supabase Edge Function /catalog/snapshot returns a gzipped JSON of all published songs
  (metadata plus chordpro_text) and a server timestamp. /catalog/delta?since= returns
  changed and removed songs.
- On first launch, download the snapshot into SQLite (songs table with FTS where possible;
  for Khmer use a LIKE-based substring search over an NFC-normalized title column plus the
  romanization table). Show progress and allow use of already-inserted rows.
- Background delta sync on app open when on Wi-Fi or when the user taps Refresh; never
  block reading on network.
- Favorites, setlists and per-song settings (transpose, capo, font size) are stored
  locally first and synced to Supabase when logged in.

Screens: Home (Top 100 per language, New, Continue), Search, Song (same toolbar as web:
transpose, capo, Simplify, autoscroll, font size, beginner mode, instrument switch,
left-handed), Setlists, Contribute (opens the web editor in a browser tab for now),
Settings (language km/en, theme, offline status, "Delete all downloaded data").

Quality bar:
- Minimum SDK 28. Test with a 2 GB RAM device profile in the emulator. Keep the release
  APK under 30 MB and cold start under 2 seconds on that profile.
- Full accessibility labels on every control (a blind UG user reported unlabeled buttons;
  ours must pass the Android Accessibility Scanner with no "missing label" findings).
- Volume buttons can page the chart when setlist mode is on.
- Khmer font bundled (Noto Sans Khmer) so rendering does not depend on the device.

Acceptance criteria:
- In airplane mode after first sync, search, open, transpose and autoscroll all work.
- After a song is removed server-side, the next delta sync removes it locally.
- EAS build profile for Play internal testing exists and a signed AAB is produced by
  `eas build -p android --profile production`.
- Play listing text in Khmer and English is generated in /store/android/ with no
  numeric user claims and no earnings claims.
```

### Phase 3: Accounts, subscription, payments and transparent cancel

Goal: take money in Cambodia and abroad without reproducing UG's billing complaints. Duration: 3 to 4 weeks. Exit criteria: a user can go free to Pro by Google Play IAP or by KHQR on web, see the next charge date and amount everywhere, cancel in one tap, and receive a reminder three days before any renewal.

Facts behind the design. Google Play's fee split began June 30, 2026 in the US, UK and EEA: a 10 percent service fee on the first $1M of annual earnings and on auto-renewing subscriptions, plus a 5 percent billing fee only when Google Play Billing is used, with global rollout through September 2027 ([Shopifreaks](https://www.shopifreaks.com/google-starts-cutting-play-store-fees-to-a-flat-10-service-fee-on-the-first-1m-and-allows-external-payment-links-making-good-on-its-epic-games-settlement/), [Help Net Security](https://www.helpnetsecurity.com/2026/03/05/google-play-store-changes-android-app-distribution/)); figures above $1M conflict between sources and Cambodia's timing in the rollout is unconfirmed. Apple's Small Business Program is 15 percent, dropping to 10 percent on subscriptions after the first year ([Apple](https://developer.apple.com/app-store/small-business-program/)). RevenueCat charges about 1 percent of tracked revenue after $2,500 per month free ([App Pricing Lab](https://apppricinglab.com/playbook/revenuecat-review)). KHQR through ABA PayWay is a push-payment rail with dynamic QR, expiry and webhooks but no documented merchant-initiated recurring charge ([PayWay KHQR guideline](https://developer.payway.com.kh/khqr-guideline-3192101f0.md), [CartDNA](https://www.cartdna.com/en_GB/shopify-payment-methods/aba-payments)), so the design is per-cycle invoicing with reminders and 3, 6 and 12 month prepay. A 2022 explainer says Stripe is not available to Cambodia-based businesses ([Cambodia Investment Review](https://cambodiainvestmentreview.com/2022/06/14/explainer-how-to-receive-money-in-cambodia/)); this is unverified for 2026 and is an open question. For the Philippines, Indonesia, Vietnam and Thailand, Xendit documents subscriptions with Maya and GrabPay autodebit, and PayMongo offers a Subscriptions API in the Philippines ([Xendit](https://help.xendit.co/hc/en-us/articles/4408498827545--PH-How-to-activate-subscription-payments-for-my-business), [PayMongo](https://paymongo.com/solution/utilities)).

```text
Implement accounts, entitlements and payments for [APP NAME] across the Next.js web app
and the Expo Android app, using Supabase Auth and RevenueCat.

Auth: email magic link, Google, and Facebook login (Facebook is the dominant network in
Cambodia); phone OTP optional behind a feature flag. Reading never requires login.

Entitlements: a single source of truth table entitlements(user_id, product
[pro_local, pro_global, team, ad_free_lifetime], source [play, apple, khqr, card],
active_until, auto_renew boolean, next_charge_amount, next_charge_currency,
cancel_requested_at). RevenueCat webhooks update rows for store purchases; the KHQR
flow updates rows directly. The app and web read only from this table.

Google Play (via RevenueCat): monthly and yearly SKUs for pro_local and pro_global, a
one-time ad_free_lifetime SKU, and a team SKU. No free trial on the yearly plan. If a trial
is offered at all it is on the monthly plan only, and the paywall must show the exact
post-trial price and date in the same font size as the headline.

KHQR per-cycle flow (web): on Upgrade, create an invoice row, call the PayWay API to
generate a dynamic KHQR with the invoice reference and a 30-minute expiry, show the QR and
a deep link for ABA Mobile, poll our own invoice status which is set by the PayWay webhook
handler (verify the webhook signature; make the handler idempotent). On success, extend
active_until by the period purchased (1, 3, 6 or 12 months) and set auto_renew=false,
because KHQR has no recurring charge. Schedule reminder emails and push notifications 7
and 3 days before expiry and on the day, each with a one-tap QR renewal link. Never
lock a user out early; grace period of 3 days after expiry.

Other markets: add a provider abstraction with Xendit (PH, ID, VN, TH e-wallet subscriptions
where the method supports autodebit) and a Stripe adapter that is enabled only if the
STRIPE_ENABLED flag is set (Stripe availability for a Cambodian entity is unresolved).

Transparent cancellation (these are product requirements, not optional):
- A "Manage subscription" screen in app and on web shows product, price, next charge
  date, payment source and a single "Cancel renewal" button. For store purchases, deep
  link to the Play subscription page AND set cancel_requested_at so we stop any promo
  messaging. For KHQR there is nothing to cancel; say so plainly.
- Confirmation email on every purchase, cancellation and renewal, with the amount.
- A renewal reminder is sent 3 days before every store renewal using RevenueCat's
  renewal date.
- No "pause" state that silently renews later. No dismiss-to-discount paywall tricks.
- Paying users never see ads or upsell interstitials; assert this in an e2e test.

Ads (free tier only): Google AdMob banner at the bottom of song pages and in list
screens, no interstitials, no rewarded ads, frequency cap set in code. Cifra Club's
owner reported AdMob mediation improved ad quality and reduced uninstalls; start with
AdMob alone.

Acceptance criteria:
- RevenueCat sandbox purchase on Android flips entitlement within 10 seconds and removes
  ads immediately.
- KHQR sandbox payment via webhook extends active_until; a replayed webhook does not
  extend it twice.
- Reminder jobs run from a Supabase cron and are visible in a jobs table with status.
- Playwright test: a Pro user visiting 20 song pages sees zero ad slots and zero upsell
  modals.
- Pricing page shows local currency (KHR and USD) and the post-trial price in the same
  size as the headline price.
```

### Phase 4: Growth loops

Goal: repeatable acquisition in Cambodia and a measurable SEO flywheel in English. Duration: ongoing from week 8; first review after 6 weeks. Exit criteria: 1,000 indexed song pages with non-zero impressions, a weekly featured Clips set, ten worship teams on the Teacher and Worship tier, and a video ad creative with a measured cost per install (number to be set by the founder once the first campaign runs).

UG's own loops are worth copying with care: long-tail song pages at scale, app store ranking, an affiliate CPI program whose creative rules require real app UI and store screenshots ([affi.io Admitad listing](https://affi.io/m/ultimate-guitar-many-geos-android)), perpetual discount promotions, and Shots as the retention loop. The "most accurate chords" and "learn to play in 1 day" claims seen in UG ads appear in no indexed source and the "trusted by 200M musicians" figure could not be matched to any official number; [APP NAME] should use only demonstrable claims.

```text
Implement growth tooling for [APP NAME].

1. Programmatic SEO with a quality gate: a nightly job publishes only songs with
   status=published that have at least key, capo, difficulty and a reviewer sign-off.
   Add per-language hub pages (/km, /en, /th later) and "chords in the key of X" and
   "easy songs for beginners" pages that are generated from real data (count of
   non-barre chords, difficulty). Add an internal-linking block of 8 related songs by
   artist, key and difficulty. Submit sitemaps automatically to Google Search Console
   via API. Add a /stats page for me showing indexed pages, impressions and clicks per
   language, pulled from the Search Console API weekly.
2. Clips (UGC loop): users attach a 60-second vertical video to a song page; store in
   Supabase Storage with a 50 MB cap and server-side transcode to 720p; feed sorted by
   recency with a weekly "Featured" set chosen by an admin flag; a #featureme style
   opt-in checkbox on upload. Moderation queue with a one-click remove and a report
   button on every clip. No algorithmic ranking in v1.
3. Share cards: every song page and setlist has a share image (Open Graph) rendered
   server-side with the title in Khmer and English, key and capo, and the chord
   diagrams of the first four chords, sized for Facebook and Telegram previews.
4. Worship and teacher channels: a /for-worship page and a /for-teachers page in Khmer
   and English describing the team tier, with a form that creates a lead row and sends
   me a Telegram message. A referral link per team leader that grants their members
   the free tier plus the team workspace.
5. Ad creative kit: a script in /marketing/ads that takes a song slug and renders a
   15-second MP4 (use Remotion) showing the real app UI scrolling the chart with
   chord diagrams at the top, a Khmer and English headline, and an end card with the
   store badge. Headlines must come from /marketing/claims.json, which contains only
   claims we can show on screen (for example "Khmer songs with chords, works offline,
   free to start"). Reject any headline containing numbers of users, "most accurate",
   or time-to-learn promises.

Acceptance criteria:
- Nightly job refuses to publish a song missing any required field, and logs why.
- Share image renders Khmer text correctly (no tofu boxes) in a headless test.
- Clip upload over a throttled 3G connection resumes after interruption.
- The ad renderer fails the build if a headline is not in claims.json.
```

### Phase 5: AI features with honest limits

Goal: ship chords-from-audio and a mic chord checker without overpromising. Duration: 5 to 8 weeks, including a GPU worker. Exit criteria: a draft chart from a 4-minute upload in under 3 minutes, measured major/minor accuracy on an internal labeled set of 50 Khmer and English songs reported inside the product, and a correction UI so that every AI draft is reviewed before it becomes public.

Accuracy ceiling. Open-source chord recognition plateaued: Chordino reaches about 80 percent chord symbol recall ([ISMIR 2015](https://www.ismir2015.uma.es/articles/271_Paper.pdf)), autochord scores 67 percent on Billboard ([ISMIR 2021](https://archives.ismir.net/ismir2021/latebreaking/000008.pdf)), the field "still has not exceeded 90 percent" on simple labels ([ISMIR 2021 LBD](https://archives.ismir.net/ismir2021/latebreaking/000051.pdf)), and 2025 work describes a glass ceiling partly caused by annotator disagreement ([arXiv 2509.01588](https://arxiv.org/abs/2509.01588v1)). An LLM post-processing pass over stems and model output adds only 1 to 2.77 points ([ChordCoT, arXiv 2509.18700](https://arxiv.org/html/2509.18700v1)). HT-Demucs reaches about 7.5 dB SDR on MUSDB18-HQ ([SCNet paper](https://arxiv.org/pdf/2401.13276)), which is good enough to isolate the harmonic content. Expect 65 to 80 percent on triads and worse on extended chords; this is why the product must show the AI output as a draft with a confidence per section, and why Chordify, Moises and Chord ai all rely on user edits and gate precision behind paid tiers ([Moises](https://moises.ai/blog/latest/advanced-chord-detection/)).

YouTube limit. UG's May 2026 "AI chords" feature takes a YouTube link ([UG Help](https://help.ultimate-guitar.com/en/articles/14771579-mobile-what-are-the-ai-chords)), but YouTube's terms prohibit extracting audio and the IFrame API only permits playback with limits on overlays ([Google Developers](https://developers.google.com/youtube/terms/required-minimum-functionality)). [APP NAME] should accept a YouTube link only to attach the embed and to sync existing chords by polling the player's current time. Chord analysis runs on audio the user uploads or records and warrants they have rights to, processed in memory and deleted after analysis. Whether to go further than this is an open question for a lawyer.

```text
Build the audio analysis service for [APP NAME] as a Python 3.11 FastAPI worker in
/services/analyze, deployable to a single GPU instance (document CPU fallback timing).

Pipeline for POST /analyze (multipart audio file up to 15 minutes, plus optional
youtube_video_id used only for later sync, never for fetching audio):
1. Validate and transcode to 44.1 kHz mono WAV with ffmpeg; reject files over 15 minutes.
2. Source separation with Demucs (htdemucs_ft). Keep the "no drums" mix and the bass stem.
3. Beat and downbeat tracking with madmom on the full mix.
4. Chord estimation on the no-drums mix with madmom's deep chroma chord recognizer
   (major/minor vocabulary) as the baseline; keep a pluggable interface so a
   conformer-class model can replace it later. Snap chord boundaries to beats.
5. Key estimation from the chroma histogram. Produce a per-section confidence score.
6. LLM cleanup pass: send the beat-synchronous chord list, the estimated key and the
   bass-stem root estimates to the Claude API with a prompt that (a) enforces diatonic
   consistency where confidence is low, (b) collapses one-beat flickers into the
   surrounding chord, (c) detects repeated sections and labels them Verse/Chorus/Bridge,
   and (d) outputs ChordPro with [Chord] markers on beat-aligned placeholder lines and no
   lyrics. The LLM must never invent lyrics or chords outside the input vocabulary;
   validate the output against the input chord set and reject on violation.
7. Return a draft with timestamps so the web and app can show "chords in time" against
   the YouTube IFrame player via getCurrentTime polling.
8. Delete the uploaded audio and stems immediately after the response; store only the
   chord JSON and a hash of the file.

Evaluation: write /services/analyze/eval that runs the pipeline against a labeled set in
/eval/songs/*.lab (I will provide 50 songs) and reports MIREX-style majmin and root
accuracy. Print the number in the README and surface it in the product as "Draft chords,
about N percent accurate on our test set. Please review before sharing."

Mic chord checker (client side, Pro feature): in the web app, an AudioWorklet computing
a 12-bin chroma from a 4096-point FFT at 50 ms hops, template matching against
major/minor triads with a 300 ms hold, and a UI that lights the expected chord green when
the match is correct for 3 consecutive frames. Label it "Practice helper" and document
that it will miss extended chords and struggle with background noise. In the Expo app,
implement the same with a native audio module and a small TFLite chroma classifier only if
the AudioWorklet approach proves usable; otherwise ship web-only first.

Acceptance criteria:
- A 4-minute file returns a draft in under 180 seconds on the GPU profile.
- Eval report shows majmin accuracy on the labeled set; the product copy reads the number
  from the eval output, not from a hard-coded string.
- Any LLM output with a chord not in the input set fails validation and the raw model
  output is returned instead.
- The upload directory is empty after each request in an integration test.
- Drafts are saved with status=draft, private to the uploader, and are never included in
  sitemaps or the offline catalog until a human publishes them.
```

### Phase 6: iOS, lyrics licensing and scale

Goal: reach iPhone users, add licensed lyrics where it pays, and extend the catalog model to Thai, Vietnamese, Indonesian and Filipino. Duration: 8 to 12 weeks, after revenue exists. Exit criteria: iOS app approved with the same honest paywall, a signed lyrics agreement or a documented decision not to pursue one yet, and at least one second-language catalog with a local moderator.

Lyrics economics. The only concrete figures in the notes are from 2015: Musixmatch quoted a $25,000 minimum annual data license and a per-display rate of not less than $1.40 per 1,000 lyric views ([Audacious issue #502](https://redmine.audacious-media-player.org/issues/502)); LyricFind prices by usage and requires contact ([LyricFind press clipping](https://lyricfind.rockpaperscissors.biz/artist/8830/press_clips/10258/white)). Both are dated and unverified for 2026. For Khmer, Thai, Vietnamese, Indonesian and Filipino repertoire there is no aggregator with deep coverage; the realistic route is direct deals with local labels and publishers, which in SEA often own both master and publishing, and with the national societies (FILSCAP, WAMI, MCT, VCPMC), none of which publishes a lyric-display tariff ([Music Business Worldwide on AAMRO](https://www.musicbusinessworldwide.com/sesac-partners-with-five-southeast-asian-collection-societies-to-form-multi-territorial-digital-licensing-hub/)). Chordify's path, chords first and licensed lyrics through LyricFind later, is the template ([MusicRadar](https://www.musicradar.com/news/chordify-lyrics-live-chord-detection)).

Apple specifics. Join the Small Business Program. Outside the US, EU, UK, Japan and Korea, Apple's anti-steering rules still apply, so the iOS app must not link to web checkout; rely on IAP in-app and on web sign-ups that happen outside the app. The US external-link commission is before a court as of October 2026 and should be re-checked.

```text
Extend [APP NAME] to iOS and prepare for lyrics licensing and multi-language scale.

iOS: configure the Expo project for iOS with EAS, add Apple IAP products mirroring the
Android SKUs through RevenueCat, implement Sign in with Apple, and make sure no screen
links to web checkout (anti-steering outside the US). Reuse all accessibility labels;
run the Xcode Accessibility Inspector audit and fix every issue. Produce App Store
listing text in Khmer and English with no user-count or earnings claims.

Lyrics readiness (do not fetch lyrics from anywhere): add a lyrics_provider abstraction
with a null provider now and interface methods getLyrics(isrc or title+artist, language)
and reportView(song_id, user_id, timestamp) for usage reporting. Add a per-song
lyrics_license_status field [none, licensed_aggregator, licensed_direct, own_work,
public_domain]. The chart renderer shows lyric lines only when the status is not "none".
Add a monthly usage export (views per song per territory) suitable for an aggregator
report.

Multi-language catalog: generalize the romanization and search layer to Thai (no spaces,
use ICU word segmentation via the intl extension in Postgres or a trigram fallback),
Vietnamese (diacritic-insensitive matching), Indonesian and Filipino. Add a moderator
role per language with its own review queue and a dashboard of queue age. Add per-language
Top 100 pages and sitemaps.

Scale: move song page rendering to full static generation with on-demand revalidation
triggered by a Supabase webhook on publish; put Supabase Storage behind a CDN; add read
replicas only if p95 query latency exceeds 100 ms in the dashboard. Add Sentry to web,
app and worker.

Acceptance criteria:
- iOS TestFlight build passes a checklist: cancel in one tap, next charge date visible,
  no web checkout links, ads absent for Pro.
- Switching lyrics_license_status to "none" hides lyric lines without a redeploy.
- Thai search "รัก" returns matching songs after a 500-song Thai seed.
- Usage export produces a CSV for a given month with song, territory and view count.
```

## 4. Marketing and sales prompts

These are for an AI writing tool. All of them carry the same guardrails: no earnings claims, no "trusted by N musicians" or any user count until it is true and documented, no "most accurate" claim, no time-to-learn promise, prices shown with currency and billing period, and Khmer copy written by a native speaker or reviewed by one before use.

### App store listing

```text
Write a Google Play listing for [APP NAME], a chords app for guitar, ukulele and piano.
Audience: Cambodian musicians, worship teams and beginners; secondary audience: English
speakers in Southeast Asia. Produce: an app title (30 characters), short description
(80 characters), and full description (under 3,000 characters) in English, then a Khmer
version of each written for a Khmer reader rather than translated word for word.
Content to cover: Khmer song chords with Khmer-script search; chord diagrams at the top of
every song; transpose, capo and Simplify always free; autoscroll; the whole catalog works
offline; strumming patterns and a beginner mode; setlists and one-tap key change for
worship teams; community corrections; Pro removes ads with no trial tricks, a clear price,
cancel any time in one tap, and a reminder before every renewal. State the free tier
first. Do not include any user counts, download counts, accuracy claims, "best" or
"ultimate" wording, earnings claims or learning-time promises. Include a short
"We do not host lyrics yet" line in plain language.
```

### Video ad scripts

```text
Write three 15-second vertical video ad scripts for Facebook Reels and TikTok promoting
[APP NAME] in Cambodia. Format for each: shot list with on-screen text in Khmer and
English, voiceover line, and end card. The visual must be the real app UI (a chart
scrolling with chord diagrams at the top), the way Ultimate Guitar's ads show its app,
but every claim must be something the viewer can see happening on screen.
Ad 1: a worship leader changes the key of a whole setlist in one tap.
Ad 2: a beginner turns on beginner mode and the chart simplifies, strumming arrows appear.
Ad 3: the app is used in airplane mode in a tuk-tuk.
Rules: no user counts, no "most accurate", no "learn in one day", no earnings claims,
no discount countdowns. The price line, if used, must show the full monthly price in
riel and dollars and the words "cancel any time in the app".
```

### Onboarding and paywall copy (ethical version of the quiz-to-paywall flow)

Ultimate Guitar runs a 14-step quiz that lands on a three-tier paywall with a trial attached to the annual plan ([ScreensDesign](https://screensdesign.com/apps/ultimate-guitar-chords-tabs/)); RevenueCat's data shows Education apps have the lowest same-day conversion of any category at 28.5 percent and that trials of 17 to 32 days convert at a median 42.5 percent versus 25.5 percent for trials under 4 days ([RevenueCat 2026](https://www.revenuecat.com/state-of-subscription-apps-2026-education), [RevenueCat benchmarks](https://www.revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026)). The ethical version keeps the personalization and removes the pressure.

```text
Write onboarding and paywall copy for [APP NAME] in English and Khmer.
Onboarding: at most 3 optional questions (instrument; goal: play for myself, lead
worship, teach; level: beginner or not), each with a visible "Skip" link, and no sign-up
required to reach the catalog. After the questions, show a personalized home screen,
not a paywall.
Paywall: shown only when a user taps a Pro feature or the Remove ads button. One screen,
two choices: Pro monthly at [local price] per month, and Ad-free forever at [one-time
price]. A yearly plan is a secondary link with the full yearly amount written out.
Required lines on the screen: what is free forever (transpose, capo, Simplify, offline),
the exact amount and date of the next charge, "Cancel in one tap from Settings", and
"We send a reminder 3 days before every renewal". If a trial is offered, it is on the
monthly plan only and the copy must state the exact price charged when the trial ends.
Do not use countdown timers, "80% off" anchors, or a dismiss-to-discount offer.
Provide a short "Why we price this way" paragraph for the pricing page that mentions
local pricing for Cambodia without naming competitors.
```

### Win-back emails

```text
Write a 3-email win-back sequence for [APP NAME] users whose Pro subscription expired
or who stopped opening the app for 30 days. Email 1 (day 3 after lapse): a plain note
that their setlists and favorites are still there, with one link; no offer. Email 2
(day 14): what is new in the catalog in their language, three song links. Email 3
(day 30): a single honest renewal offer with the full price shown, valid without a
countdown; include the sentence "You will get a reminder before any renewal and can
cancel in one tap." Subject lines under 45 characters. No urgency language, no "we miss
you" guilt, no discount stacking. Provide English and Khmer versions.
```

### Worship leader outreach message

```text
Write a short outreach message (Telegram or Facebook Messenger, under 120 words) from
the founder of [APP NAME] to a worship leader at a Cambodian church, in Khmer with an
English version for reference. Purpose: invite them to test the team features (shared
setlists, one-tap key change, Nashville numbers, offline) for free for 60 days in
exchange for a 20-minute call and their honest feedback. Mention that their church's
own songs stay private to their team. Do not mention any other app by name, do not
claim any number of users, and do not promise future features. End with one question
that is easy to answer with yes or no.
```

## 5. Metrics and benchmarks

Benchmarks are from the RevenueCat and Adapty reports cited in the notes; Education is the closest category since no vendor publishes a music sub-category. Targets are founder assumptions to be revised after the first 90 days of data.

| Metric | Benchmark from the notes | Source | Target for [APP NAME] (assumption) |
|---|---|---|---|
| Download to trial (Education) | 6.5% | [RevenueCat 2026](https://www.revenuecat.com/state-of-subscription-apps) | Not applicable at launch (no forced trial); track download to first paywall view instead, target 15% |
| Install to trial (all categories, median) | 27.8% | [Adapty 2026](https://adapty.io/state-of-in-app-subscriptions-report/) | Track install to Pro screen view, target 20% |
| Trial to paid (all categories, median) | 59.2% | [Adapty 2026](https://adapty.io/state-of-in-app-subscriptions-report/) | If monthly trial is used: 40% |
| Freemium D35 trial to paid | 2.1% (vs 10.7% hard paywall) | [RevenueCat 2026](https://www.revenuecat.com/state-of-subscription-apps) | 3% of monthly actives paying within 35 days of first Pro screen view |
| Day-0 conversion (Education) | 28.5%, lowest of any category | [RevenueCat 2026 Education](https://www.revenuecat.com/state-of-subscription-apps-2026-education) | Do not optimize for day 0; measure day 7 and day 30 |
| D14 revenue per install (Education) | $0.30 (all-category median $0.23) | [RevenueCat 2026 Education](https://www.revenuecat.com/state-of-subscription-apps-2026-education) | Cambodia: $0.05 at D14 given local pricing; global English: $0.20 |
| 12-month LTV (Education) | $45.10 | [Adapty Education benchmarks](https://adapty.io/blog/markdown/education-app-subscription-benchmarks.md) | Not targeted in year one; report blended LTV by country |
| Year-one retention, yearly plans | 28% median; low-priced yearly 36% median, 53% top quartile | [RevenueCat 2025](https://revenuecat.com/state-of-subscription-apps-2025) | 40% on yearly (low price band) |
| Year-one retention, monthly plans | 8% median | [RevenueCat 2025](https://revenuecat.com/state-of-subscription-apps-2025) | 15% at month 12 for monthly, helped by KHQR prepay options |
| First renewal rate | 45.1% | [Adapty 2026](https://adapty.io/state-of-in-app-subscriptions-report/) | 50% |
| Share of annual cancellations in month 1 | 35% | [RevenueCat benchmarks 2026](https://www.revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026) | Under 20%, because the price is shown before purchase |
| Annual plan refund rate | 4.2% | [Adapty Education benchmarks](https://adapty.io/blog/markdown/education-app-subscription-benchmarks.md) | Under 2%, with refunds granted on request within 14 days |
| Organic search share of web traffic (UG) | 50 to 64% (estimates) | [Semrush](https://www.semrush.com/website/ultimate-guitar.com/), [Similarweb](https://www.similarweb.com/website/ultimate-guitar.com/) | 50% of web sessions from organic by month 9 |
| Moderation SLA (UG) | 48 hours | [UG Help](https://help.ultimate-guitar.com/en/articles/6749103-how-long-does-it-usually-take-for-my-tab-to-be-approved) | 48 hours, with queue age shown on the admin dashboard |
| Complaint share about upsell frequency (UG) | about 20% of reviewers (AI-generated aggregate) | [unitQ](https://unitq.com/unitq-scorecards/ultimateguitar) | Zero upsell interstitials; track "ads" mentions in reviews monthly |
| Chord recognition accuracy (open source) | 67% (autochord) to about 80% (Chordino); field under 90% | [ISMIR 2021](https://archives.ismir.net/ismir2021/latebreaking/000008.pdf), [ISMIR 2015](https://www.ismir2015.uma.es/articles/271_Paper.pdf) | Report measured majmin accuracy on an internal set; ship only with a human review step |

## 6. Risk register

| Risk | Evidence in the notes | Mitigation |
|---|---|---|
| Publisher takedowns or a claim that chord-plus-structure charts are derivative works | MPA and NMPA pressure closed OLGA and MXtabs in 2006; no US court has ruled on tabs; Genius v. Google treated lyric transcriptions as derivative works ([Arizona Law Review](https://arizonalawreview.org/pdf/50-2/50arizlrev611.pdf), [Music Business Worldwide](https://www.musicbusinessworldwide.com/judge-throws-out-genius-lawsuit-accusing-google-of-copying-lyrics/)) | Chords and structure only until licensed; no lyrics; no note-for-note tabs; DMCA agent registered; takedown within 48 hours; remove on any rights-holder request as Chordify does; keep per-song source_type and contributor attestation; budget for a lawyer in Cambodia and one US consult |
| Cambodia is now in Berne, so foreign works are protected locally | Accession in force March 9, 2022 ([WIPO](https://www.wipo.int/wipolex/es/treaties/notifications/details/treaty_berne_287)) | Treat the app stores, Google Search and payment processors as the real enforcement points; do not rely on jurisdiction |
| Chord detection accuracy ceiling near 80% | Chordino about 80%; autochord 67%; field under 90%; LLM cleanup adds 1 to 2.77 points ([ISMIR 2015](https://www.ismir2015.uma.es/articles/271_Paper.pdf), [arXiv 2509.18700](https://arxiv.org/html/2509.18700v1)) | Present AI output as drafts with measured accuracy; require human review before publishing; major/minor vocabulary by default; never feed AI drafts into SEO pages |
| YouTube terms forbid audio extraction | YouTube API minimum functionality rules; embedding is permitted with restrictions ([Google Developers](https://developers.google.com/youtube/terms/required-minimum-functionality)) | Use the IFrame player for sync only; analyze user-uploaded audio; delete audio after analysis |
| App store fees and shifting rules | Google Play 10% service plus 5% billing fee from June 30, 2026 in US, UK and EEA, global rollout to September 2027, higher tiers conflicting across sources; Apple 15% then 10% on renewals; US external-link rate before a court ([Shopifreaks](https://www.shopifreaks.com/google-starts-cutting-play-store-fees-to-a-flat-10-service-fee-on-the-first-1m-and-allows-external-payment-links-making-good-on-its-epic-games-settlement/), [Apple](https://developer.apple.com/app-store/small-business-program/)) | Web plus KHQR as the primary Cambodian path; IAP for convenience; re-check Google's Cambodia rollout date and Apple's US ruling quarterly; model margins at 15% worst case |
| Stripe not available to a Cambodian entity; KHQR has no recurring billing | 2022 explainer says Stripe is unavailable in Cambodia (unverified for 2026); PayWay docs show no merchant-initiated recurring charge ([Cambodia Investment Review](https://cambodiainvestmentreview.com/2022/06/14/explainer-how-to-receive-money-in-cambodia/), [CartDNA](https://www.cartdna.com/en_GB/shopify-payment-methods/aba-payments)) | Per-cycle KHQR invoices with reminders and 3, 6, 12 month prepay; Xendit or PayMongo for PH, ID, VN, TH; decide on a foreign entity for Stripe only when global revenue justifies it |
| Ultimate Guitar's SEO moat in English | 294K to 670K ranking keywords, authority score 83, top terms are song plus chords ([Similarweb](https://www.similarweb.com/website/ultimate-guitar.com/), [Ahrefstop](https://ahrefstop.com/websites/ultimate-guitar.com)) | Win the Khmer, then Thai and Vietnamese long tail where UG is thin; in English, target beginner and worship intents with unique data (strumming, numbers, difficulty) rather than head terms |
| Google scaled content abuse policy | March 2024 policy targets mass low-value pages regardless of method ([Google Search Central](https://developers.google.com/search/blog/2024/03/core-update-spam-policies)) | Quality gate before publishing; every page carries reviewed data; no auto-published AI drafts |
| ChordSheetJS license may be GPL-3.0 | Mirror listing reports GPL-3.0 ([SourceForge mirror](https://www.sourceforge.net/mirror/chordsheetjs)) | Verify; use chorpro-parser or an in-house parser if confirmed |
| Supabase tables shipped without Row Level Security by AI agents | 2026 security study ([pkgpulse](https://www.pkgpulse.com/guides/tag/mobile)) | RLS and policy tests are acceptance criteria in every phase |
| Local sites copy the model quickly | Chordtela, DoChord and Hợp âm chuẩn are free and established in their markets | Khmer first where there is no incumbent; compete on curation, offline, worship and teacher tools rather than catalog size |
| Solo founder capacity | Every phase depends on one person | Keep Phase 5 and 6 behind revenue; use contributors and a per-language moderator; keep the stack narrow |

## 7. Open questions for the founder

- Which legal entity will own [APP NAME] and hold the app store, RevenueCat, PayWay and (if any) Stripe accounts: a Cambodian company under Pitou AI, or a foreign entity for Stripe and lyrics agreements?
- Is Stripe available to your entity today? The notes only have a 2022 source saying it is not.
- What is the Cambodian Pro price in riel and dollars, and what is the one-time ad-removal price? The sub-$2 per month figure is an assumption; Hợp âm chuẩn's $1.99 one-time is the only local comparable in the notes.
- Will the free tier carry ads at all, or will you start ad-free and rely on Pro and the team tier to keep the free experience clean as a differentiator?
- Who are the first ten worship leaders and five teachers you can reach personally, and which churches write their own songs that they would license to you directly?
- How will Khmer charts be sourced: your own transcriptions, paid contributors, or community contributors with a per-chart payment?
- Do you want cue words or section-only structure on charts before lyrics are licensed? This needs a lawyer's view.
- Has a lawyer confirmed the public-domain status of older Khmer repertoire, including the claim about Sinn Sisamouth's compositions in 2026?
- Will you accept YouTube links for chord analysis the way UG does, or only user-uploaded audio as recommended here?
- Which second language comes first: Thai, Vietnamese, Indonesian or Filipino? The notes show Chordtela is strongest in Indonesia, DoChord and ChordTabs in Thailand, and Hợp âm chuẩn in Vietnam; the Philippines has no dominant local chord site identified.
- What is the monthly budget for a GPU worker in Phase 5, and should it wait until Pro revenue covers it?
- Is ChordSheetJS's license acceptable, or should the parser be in-house from day one?
- What is the real product name, and has the Khmer spelling and the Play Store and domain availability been checked?
