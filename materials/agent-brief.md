# Agent brief - shared by every fan-out page of learn-team-management-with-phoebe

You are writing ONE static HTML session page. No servers, no npm. **If your target file already
exists on disk, do not write it; report that and stop.** Write the file, return its path and one
line of coverage. No HTML in your reply.

## Read first, in this order

1. The template page. Copy its structure, classes, SVG grammar and quiz markup EXACTLY, including
   four options per question:
   - `/Users/phoebe.fu/Documents/claude_work/github_repo/learn-team-management-with-phoebe/courses/01-a-team-not-a-group.html`
   - For rhythm on a page with more numbers, also skim
     `/Users/phoebe.fu/Documents/claude_work/github_repo/learn-team-management-with-phoebe/courses/04-the-team-size-bench.html`
2. The source map: every verified number, its evidence tier, per-session coverage, the seams. Use
   ONLY its numbers; never invent a statistic; if a fact is missing, teach the uncertainty.
   `/Users/phoebe.fu/Documents/claude_work/github_repo/learn-team-management-with-phoebe/materials/official-course-map.md`
3. The stylesheet `:root` block (first 30 lines only) for the palette tokens:
   `/Users/phoebe.fu/Documents/claude_work/github_repo/learn-team-management-with-phoebe/assets/style.css`

## Page skeleton (keep every component)

toolbar (crumb EXACTLY "learn-team-management-with-phoebe / Session N of 6", #toggle-all,
#zoom-toggle) · masthead (eyebrow "Learn Team Management with Phoebe · Session N of 6", h1 with one
`<span class="accent">`, .sub, .chip-row with the level chip (🟡 Core for sessions 2 and 3, 🟠 Deeper
for 5 and 6), two .chip.audience, .chip.time "45 min", .agenda a1-a4) · main.wrap · section#intro
(Part 0: kicker, .lede, .legend pills, .callout.win "★ What you walk out with tonight") · 3 Parts,
each `section.section#part-N` with section-kicker (klabel "Part N · covers ...", h2, `.tag.concept
"N min live"`), a `.lede`, ONE figure, `details.card` accordions (summary: `.mode.live` or
`.mode.self`, title, `.mini`, `.caret ▶`), at least one `.callout.example` with `span.ex-pill` "Real
world" on the page · section#demo-1 Build-along (kicker `.tag.demo "★ 22 min · everyone builds"`,
.lede, ONE figure, `.steps > .step`, each with a `.prompt-box.good` carrying a `span.label`; the
build-along is a Northline artifact written step by step, and the learner writes the same for their
own team) · section#exercise Homework (ol, 4 items) · section#quiz (3 x `.quiz-q data-answer="0-based"`,
`p.qtext`, four `button.qopt` "A · ..." to "D · ...", `p.qwhy`; one `p.quiz-score` after the last) ·
section#official, h2 EXACTLY "What this session teaches, and where it came from", `.covered >
.covered-row` (pill solid ✓ / light ◐ + name + note), then the `.mono` line EXACTLY "Every fact on
this page, and its verification tier, is recorded in the course's source map." ·
section.cheat#cheatsheet (h3 "Session N cheat sheet <span>· pin this</span>", .grid-2 of six
.cheat-item) · `.callout.next` with `.nx-pill` "Next session" (last page: a closing callout pointing
back to the course home and the bench) · footer.pagefoot · `<script src="../assets/app.js?v=1">`.

Head: the template's social meta block with this page's own title/description/url;
`<title>Session N · <title> - learn team management with phoebe</title>`;
`<link rel="stylesheet" href="../assets/style.css?v=3">`. Nothing else external.

First `details.card` in the FIRST Part is `open`; no other. Sentence case headings. Warm
practitioner voice, concrete, never dry. Inside prompt-boxes escape `&` `<` `>` (write `->` as
`-&gt;`). 450 to 650 lines is guidance about depth, never a target: never collapse whitespace,
dissolve a list into a paragraph, or drop a component to fit.

## Hard rules (a violation is rework)

- NEVER an em dash or en dash, anywhere (prose, code, aria-labels, comments). Hyphen only.
- No meta text: never "this course", "in this course", "the course teaches", "banned here". State
  the professional norm directly with its reason. The two exact estate phrases above are the only
  self-references; "session 5" cross-references are fine.
- Attribution "by Phoebe Fu". Never "built with" a tool.
- Every number comes from the map or is labelled constructed. Northline numbers you make up for a
  build-along (e.g. how many requests a week) are marked "constructed" in the step text. Bench numbers
  are quoted ONLY from the map's canon table, exactly as written there (one decimal).
- Contested or missing evidence: teach the disagreement; never resolve what the literature has not.
- Citations in the exact form of the map's appendix; anything marked reported is "reported" on the page.
- NEVER "lottery" or "lotteries"; say the mechanism.
- Default to the English word. No Chinese terms needed on these pages.
- Titles, widget ids and class names must not collide with siblings. Banned titles: "A system you
  keep", "The one-page marketing plan", "Is it worth the time?", "Where your week actually goes",
  "The team shape", "The weekly operating rhythm", "Conflict is a routing problem". Use exactly the
  session titles below.
- Quiz answer letters: use EXACTLY the data-answer pattern given in your file outline.
- No named real employers as examples (Google appears only as the re:Work report the map cites). No
  salary or pay figures. Stress means workload and planning, never medical advice.
- Seams: never teach onboarding, coaching, growth plans, career ladders, PIPs, hard conversations or
  exits (Performance Management), delegation frameworks or feedback (AI Leadership), hiring or
  interviews (AI HR), goal-setting (OKR), RACI (Tech Project PMO), or running a single meeting
  (Facilitation). Name the seam in one sentence with the absolute link and move on.
- Famous unsourced management claims (7-38-55, "multitasking costs 40 percent", "23 minutes to
  refocus", "1:1s are the most important meeting", Eisenhower's quote, an ideal team size): never
  state them as fact. If you mention one, tier it as the map does.

## Figure grammar (hand-drawn, every figure)

Palette, ONLY these hexes (no invented greys): ink `#2B1D16` · muted `#6B5A4F` · accent `#9C4A1E` ·
accent-deep `#6B3012` · accent-mid `#84401A` · soft `#EBCDB8` · tint `#FBF1EA` · faint `#DCCBBF` ·
hairline `#EFE4DC` · contrast `#3E5C8A` · contrast-ink `#2A4165` · contrast-tint `#E9EEF6` ·
`#FFFFFF` · universal reds `#991B1B` `#FEF2F2` `#FCA5A5` only for a wrong-way panel.

- `<figure class="zoomable">` > `<svg viewBox="0 0 880 H" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="the data, not the
  shape">` > `<defs>` + `<style>` + content, then `<figcaption>🔍 Click to zoom - takeaway</figcaption>`.
  Grow H, never W.
- Prefix unique per figure, used for every class and id: `t<session><letter>` (t2a, t2b, t2c, t2d
  for session 2; t3a... for session 3; t5a...; t6a...). Never reuse t1* or t4*.
- `<defs>` holds, with the figure prefix P: a wobble filter `id="PSk"`
  (`feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="<int>"` +
  `feDisplacementMap scale="2.4" xChannelSelector="R" yChannelSelector="G"`, `x="-3%" y="-3%"
  width="106%" height="106%"`), a hachure pattern `id="PHc"` if used (7x7 userSpaceOnUse,
  rotate(-38), one accent line, opacity .5), an open arrowhead `id="PAr"` if used (path `M1 1 L9 5
  L1 9`, fill none, ink stroke 1.6). ALL shapes sit inside ONE `<g filter="url(#PSk)" fill="none"
  stroke="#2B1D16" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">`; rects carry a
  tiny rotation (-4 to 4 degrees for hand-placed items, under 1 for panels). Fills: white, tint, the
  hachure for "the pile" or "the data", and the contrast colour ONLY for the one thing the figure is
  about. One doodle anchor per figure, simple strokes, never a mascot. Text classes: `.PH` 800 12px
  ink heading · `.PL` 600 12px ink label · `.PS` 400 11px muted · `.PB` 800 11px contrast-ink ·
  `.PV` 800 16-20px accent-deep value · `.PW` 800 11px white on a dark fill · `.PA` 700 11px accent
  axis caption · `.PN` 400 12px muted note. Hand-stacked items must not overlap as painted rects.
- ALL `<text>` outside the filtered group, sans stack, never below 10.5px.
- Fit: max chars ≈ (box width - 20) / 7 at 12px, 6.4px/char at 11px; full-width note under 110
  chars; 40px between neighbouring point labels; bottom note 22px below the last row, H clears it by
  8px. When in doubt, shorten.
- **No line, arrow, curve or box border may pass through a label.** Leader lines end before the text
  starts; a label never sits on a dashed boundary. Place labels in empty space and check every
  path's route against every text box.
- Floor: one figure per Part plus one in the build-along. Draw the MECHANISM (who routes a request
  to whom, where an hour goes, which path a decision travels, which person holds which knowledge),
  never a metaphor literally, never decoration.

## Voice and honesty

Every Part gets a real-world story ("Real world" callouts describe common patterns, never a named
company). Constructed cases say "constructed" on the page: Northline (Ana, Priya, Tom, Wei, Sam,
Lena, Kofi; hires Mo and Jun), its stakeholders (a merchandising lead and a finance lead, unnamed or
invented names), and every Northline number you make up. The bench numbers are modelled on a
constructed team; say so when you quote one.

## Cross-links (absolute URLs)

- Performance Management: https://phoebefu6.github.io/learn-performance-management-with-phoebe/ (hard conversations: .../courses/b8-hard-conversations.html; onboarding: .../courses/b2-onboarding-ramp.html)
- AI Leadership: delegation https://phoebefu6.github.io/learn-ai-leadership-with-phoebe/courses/b6-delegation.html ; meetings https://phoebefu6.github.io/learn-ai-leadership-with-phoebe/courses/b7-meetings-synthesis.html ; feedback https://phoebefu6.github.io/learn-ai-leadership-with-phoebe/courses/b5-feedback-performance.html
- AI HR: https://phoebefu6.github.io/learn-ai-hr-with-phoebe/
- OKR: https://phoebefu6.github.io/learn-okr-with-phoebe/
- RACI: https://phoebefu6.github.io/learn-tech-project-pmo-with-phoebe/courses/05-ownership-and-raci.html
- Facilitation (single meetings, decision rules): https://phoebefu6.github.io/learn-facilitation-with-phoebe/courses/03-diverge-converge-decide.html
- Hub: https://phoebefu6.github.io/learn-with-phoebe/

## Footer chain and session titles

Footer left: "Session N of 6 · learn-team-management-with-phoebe · by Phoebe Fu &nbsp;·&nbsp; 📚 <a href="https://phoebefu6.github.io/learn-with-phoebe/">Learn with Phoebe ↗</a>"
Footer right: "<a href="PREV">← Prev: <title></a> &nbsp;·&nbsp; <a href="NEXT">Next: <title> →</a>" (last page: "← Prev" and "<a href="../index.html">Course home →</a>").

Session titles (exact, sentence case, one accent span in h1):
1. 01-a-team-not-a-group.html · A <span class="accent">team</span> is not a group of people with the same manager
2. 02-who-decides-what.html · Who <span class="accent">decides</span> what
3. 03-rhythm-and-cost.html · The team's <span class="accent">rhythm</span> and what it costs
4. 04-the-team-size-bench.html · The <span class="accent">team-size</span> bench
5. 05-safety-and-conflict.html · Safety, conflict and the <span class="accent">disagreement</span> you need
6. 06-remote-async-key-person.html · Remote, async and the person who knows <span class="accent">everything</span>
