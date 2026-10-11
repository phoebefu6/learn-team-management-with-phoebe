# Team Management - official course map (source of truth)

learn-team-management-with-phoebe · bucket lead · d2 · audience leader · single-track, 6 sessions x 45
min · icon 👥 (as on the hub) · palette cinnamon #9C4A1E (deep #6B3012, mid #84401A, soft #EBCDB8, tint #FBF1EA) with
slate blue #3E5C8A as the warm contrast (ink #2A4165, tint #E9EEF6); ink #2B1D16, muted #6B5A4F, faint
#DCCBBF, hairline #EFE4DC, paper #FFFCF9. Built 2026-10-10 by the course lead. Re-scoped by Phoebe on
2026-10-10: **how a team runs**, not how to manage one person's performance.

Evidence tiers: **read** = read at source (the paper's own abstract or page, the publisher, the official
page). **reported** = stated by a named secondary source, not read at source; say "reported" on the page.
**practitioner** = a practitioner book or company page, read at source but not research; say so.
**not verified** = never taught as fact.

## Running case (constructed, say so on every page that uses it)

**Northline** is a constructed 7-person data team inside an invented retail company. Members (all
invented): **Ana** (team lead), **Priya** (data engineer, the only person who knows the pipeline),
**Tom** (analytics engineer), **Wei** (data scientist), **Sam** (analyst), **Lena** (data scientist),
**Kofi** (platform engineer). Two hires join in session 4: **Mo** (analyst) and **Jun** (data engineer).
Work areas: pipeline, infrastructure, dashboards, models, data quality, experiments, stakeholder
requests. Northline's problems: everyone syncs with everyone ad hoc, two stakeholders send competing
requests straight to whoever answers, nobody knows who decides priorities, and the pipeline lives in
Priya's head. No number about Northline is a measurement. Every Northline page says "constructed".

## Session arc and coverage

| # | File | Title (h1, accent word) | Covers |
|---|---|---|---|
| 1 | 01-a-team-not-a-group.html | A **team** is not a group of people with the same manager | Group vs team: shared outcome, interdependence, a boundary (Hackman's "real team", reported); size and communication paths n(n-1)/2 (Conway 1968 read; Brooks 1975 reported); "ideal team size" and Dunbar's number as a disagreement (Lindenfors et al. 2021 read; Google: team size not significant, read); team shapes: Team Topologies' four team types and three interaction modes (practitioner, read on teamtopologies.com), Conway's law (read). Build-along: Northline's one-page team charter. |
| 2 | 02-who-decides-what.html | Who **decides** what | Decision rights: list the recurring decisions, name one decider each, who is consulted, who is told; reversible vs hard-to-reverse decisions get different processes (common practice, no single source); how disagreement is closed: the rule named in advance (Kaner's decision rules, read, cited via the facilitation map), an escalation path with a time limit, and committing after the decision; the decision log. Google's "structure and clarity" dynamic (read). Build-along: Northline's decision-rights table for eight recurring decisions. |
| 3 | 03-rhythm-and-cost.html | The team's **rhythm** and what it costs | The operating rhythm as a budget: which rituals, how often, who attends, in person-hours; the bench's ritual formulas; a ritual set pays only when it replaces ad hoc coordination (bench: at 60 ad hoc minutes per path it saves 0.5 h a person; at 30 it costs 2.5 h); interrupts and focus (Mark, Gudith and Klocke 2008, read); protecting focus time. Build-along: Northline's ritual budget, line by line. |
| 4 | 04-the-team-size-bench.html | The **team-size** bench | Exact paths, modelled hours: four designs (7 ad hoc, 7 with rituals, split 4+3 with one interface, 9 after two hires), anti-lever "add two people to a late project" (Brooks, essay claim; model shows later up to about 6 weeks out, sooner beyond), break button "Priya leaves" (bus factor and stopped work). |
| 5 | 05-safety-and-conflict.html | Safety, conflict and the **disagreement** you need | Psychological safety at source (Edmondson 1999, read: abstract); Google's Project Aristotle (company report, read; tiered as such); the 2017 meta-analysis (Frazier et al., read: abstract); task vs relationship conflict as a live disagreement (De Dreu and Weingart 2003 vs de Wit, Greer and Jehn 2012, both read: abstract); conflict between priorities routed through decision rights. Build-along: Northline's priority-conflict protocol and a safety check the team runs on itself. |
| 6 | 06-remote-async-key-person.html | Remote, async and the person who knows **everything** | Remote work and collaboration networks (Yang et al. 2021, read: Microsoft Research summary page; sample size reported); async defaults (write it down, decide in writing, overlap hours); key-person risk and bus factor (Avelino et al. 2016, read: abstract); interrupt load: a rotating shield; the break button result as the plan's target. Build-along: Northline's key-person plan for the pipeline, checked on the bench. |

Difficulty per card: 1 green, 2 yellow, 3 yellow, 4 red (bench night), 5 orange, 6 orange.

## Seams (link, never teach) - absolute links

- Onboarding, coaching, growth plans, career ladders, PIPs, hard conversations, exits:
  https://phoebefu6.github.io/learn-performance-management-with-phoebe/
  (onboarding ramp: .../courses/b2-onboarding-ramp.html; hard conversations: .../courses/b8-hard-conversations.html)
- Delegation (automate / augment / keep), meetings and synthesis, feedback, AI team enablement:
  https://phoebefu6.github.io/learn-ai-leadership-with-phoebe/ (delegation .../courses/b6-delegation.html;
  meetings .../courses/b7-meetings-synthesis.html; feedback .../courses/b5-feedback-performance.html)
- Hiring, structured interviews, screening: https://phoebefu6.github.io/learn-ai-hr-with-phoebe/
  (structured interviews .../courses/b5-structured-interviews.html)
- Goals and fair measurement: https://phoebefu6.github.io/learn-okr-with-phoebe/
- RACI: https://phoebefu6.github.io/learn-tech-project-pmo-with-phoebe/courses/05-ownership-and-raci.html
- Running a single meeting well: https://phoebefu6.github.io/learn-facilitation-with-phoebe/
  (decision rules .../courses/03-diverge-converge-decide.html)
- Body side of stress (sleep, exercise, recovery): the planned move-shelf courses on the hub
  https://phoebefu6.github.io/learn-with-phoebe/ . This course treats stress as workload and planning only
  and says so on the landing page and session 1.

## Verified facts (cite exactly as here)

### Conway (1968) - read at source (melconway.com, the author's own copy)
- Conway, M. E. (1968). How do committees invent? Datamation, April 1968.
- Thesis: organizations which design systems "are constrained to produce designs which are copies of
  the communication structures of these organizations". (Later named Conway's law; the name is not in
  the paper.)
- The number of possible communication paths "is approximately half the square of the number of
  people"; the paper argues against "the assumption that adding manpower simply adds to productivity".
- The exact formula n(n-1)/2 is arithmetic (pairs among n people), not a claim from any source.

### Brooks (1975) - reported
- Brooks, F. P. (1975). The Mythical Man-Month: Essays on Software Engineering. Addison-Wesley;
  anniversary edition 1995 with four extra chapters. "Brooks's law": adding manpower to a late software
  project makes it later. Reasons given: tasks cannot be perfectly partitioned, new people take time to
  learn, communication overhead grows. (reported: Wikipedia and catalogue records; chapter not read.)
- Do NOT quote any 1995 self-assessment by Brooks of the law; not read.
- **Teach:** an essay claim from experience, not a measured law. On the bench's own rules it holds when
  the deadline is close and fails when there is time to ramp up (canon below).
- Sibling note: learn-data-pmo-with-phoebe calls the law "still undefeated"; this course tiers it. Not
  edited here (another repo); reported to the main thread.

### Dunbar's number - teach the disagreement
- Dunbar's ~150 figure for human social group size: reported (Dunbar's 1990s work; not read).
- Lindenfors, P., Wartel, A., Lind, J. (2021). "'Dunbar's number' deconstructed". Biology Letters
  17(5): 20210158. Read at source (PMC8103230). Re-running the comparative analysis with Bayesian and GLS
  phylogenetic methods gives mean group sizes of about 69-109 (Bayesian) and 16-42 (GLS) with 95%
  intervals of 4-520 and 2-336; the authors conclude "specifying any one number is futile".
- **Teach:** neither number is about work teams. Do not use Dunbar to size a team.

### Google re:Work, Project Aristotle - read (company report; tier it as such)
- re:Work guide "Understand team effectiveness": 180 teams (115 engineering project teams, 65 sales
  pods), team sizes 3 to 50, median nine. Five dynamics in order: psychological safety, dependability,
  structure and clarity, meaning, impact. Psychological safety defined with Edmondson's words.
  Effectiveness measured from executive, team-lead and team-member evaluations and sales against quota.
  Not significant at Google: colocation, consensus-driven decision making, extroversion, individual
  performance, workload size, seniority, team size, tenure.
- **Tier:** a company's summary of its internal study; methods and data not published. Say "Google
  reports".
- The page mentions research suggesting teams under 10 perform better, but the source of that is not
  given on the page: do not repeat it as a finding.

### Edmondson (1999) - read (abstract, Harvard DASH record)
- Edmondson, A. (1999). Psychological safety and learning behavior in work teams. Administrative Science
  Quarterly 44(2): 350-383. doi:10.2307/2666999.
- 51 work teams in a manufacturing company; team psychological safety is associated with learning
  behaviour, team efficacy is not (once safety is controlled); learning behaviour mediates between team
  psychological safety and team performance. Definition (via re:Work, quoting Edmondson): "a shared
  belief held by members of a team that the team is safe for interpersonal risk taking".
- Effect sizes not read: never quote one. Survey items not read: never quote them.

### Frazier et al. (2017) - read (abstract)
- Frazier, M. L., Fainshmidt, S., Klinger, R. L., Pezeshkan, A., Vracheva, V. (2017). Psychological
  safety: A meta-analytic review and extension. Personnel Psychology 70(1): 113-165.
  doi:10.1111/peps.12183. 136 independent samples, over 22,000 individuals, nearly 5,000 groups.
- "Most included studies were cross-sectional, so causal conclusions cannot be drawn": reported (a
  state-agency summary), not read in the paper.

### Conflict - teach the disagreement
- De Dreu, C. K. W., Weingart, L. R. (2003). Task versus relationship conflict, team performance, and
  team member satisfaction: A meta-analysis. Journal of Applied Psychology 88(4): 741-749.
  doi:10.1037/0021-9010.88.4.741. Read (abstract, University of Amsterdam record): strong negative
  correlations between relationship conflict and both performance and satisfaction, and also between
  task conflict and both, "instead of the predicted positive".
- de Wit, F. R. C., Greer, L. L., Jehn, K. A. (2012). The paradox of intragroup conflict: A
  meta-analysis. Journal of Applied Psychology 97(2): 360-390. doi:10.1037/a0024844. Read (abstract,
  Erasmus repository): 116 studies, 8,880 groups; did NOT find a strong negative association between
  task conflict and performance; relationship and process conflict negatively related to outcomes;
  task conflict more positive where it is weakly tied to relationship conflict, in top management teams,
  and where performance is financial or decision quality (moderators: reported via the search summary of
  the abstract; the repository page excerpt shows the headline only).
- **Teach:** "task conflict is good for teams" is not settled; "relationship conflict hurts" is the
  stable part. The useful move is keeping task disagreement from turning personal.

### Interrupts - read
- Mark, G., Gudith, D., Klocke, U. (2008). The cost of interrupted work: more speed and stress. CHI
  2008, 107-110. Read (full text abstract): context of the interruption made no difference; people
  completed interrupted tasks in less time with no difference in quality, and paid for it in more
  stress, frustration, time pressure and effort. Lab study, email task, mostly German university students.
- The famous "23 minutes to get back on task" figure is NOT from this paper: not taught.
- "Multitasking costs 40 percent of productivity": not verified, not taught.

### Remote and async - read (summary page) / reported
- Yang, L., Holtz, D., Jaffe, S., Suri, S., Sinha, S., Weston, J., Joyce, C., Shah, N., Sherman, K.,
  Hecht, B., Teevan, J. (2021). The effects of remote work on collaboration among information workers.
  Nature Human Behaviour. doi:10.1038/s41562-021-01196-4. Read on the Microsoft Research summary page:
  firm-wide remote work made groups less interconnected and more siloed; time with cross-group
  connections fell by about 25% of the pre-pandemic level; people added fewer new collaborators; total
  meeting and call hours fell about 5% while asynchronous communication (email, IM) rose.
- 61,182 US employees, first half of 2020: reported (secondary coverage), not read in the paper.
- **Teach:** one company, one forced transition, 2020. Remote is not the same as async, and a team can
  be remote and still decide synchronously.

### Key-person risk - read
- Avelino, G., Passos, L., Hora, A., Valente, M. T. (2016). A novel approach for estimating truck
  factors. ICPC 2016 (arXiv:1604.06766). Read (abstract): truck factor = "the minimal number of
  developers that have to be hit by a truck (or quit) before a project is incapacitated"; 65% of 133
  popular GitHub projects have a truck factor of 2 or less.
- The bench's bus factor is a simpler declared-map version: the smallest number of knowers over all
  work areas. Say so.

### Hackman (2002) - reported
- Hackman, J. R. (2002). Leading Teams: Setting the Stage for Great Performances. Harvard Business School
  Press. Five conditions: a real team, a compelling direction, an enabling structure, a supportive
  organizational context, competent coaching (reported: publisher listings and summaries). A "real team"
  has clear boundaries, interdependence and some stability (reported). Any team-size figure attributed to
  Hackman: not verified, not taught.

### Team Topologies - practitioner, read at source
- Skelton, M., Pais, M. (2019). Team Topologies. IT Revolution (book reported; concepts read on
  teamtopologies.com/key-concepts). Four team types: stream-aligned (a flow of work, usually a segment of
  the business domain), enabling (helps stream-aligned teams overcome obstacles), complicated subsystem
  (work needing significant specialist expertise), platform (an internal product that speeds up
  stream-aligned delivery). Three interaction modes: collaboration, X-as-a-Service, facilitating. Teams
  have a limited cognitive load. The key-concepts page does not mention team size or Conway's law.
- **Tier on the page:** practitioner framework, not research.

### Kaner decision rules - read (cited from the facilitation course map, 2026-10-06)
- Kaner, S. et al. (2014). Facilitator's Guide to Participatory Decision-Making, 3rd ed. Jossey-Bass.
  Indexed decision rules: unanimous agreement, majority vote, flip a coin, person-in-charge decides after
  discussion, person-in-charge decides without discussion.

## Bench canon (python == node, 389 values identical)

`python3 materials/team_reference.py --raw` vs `node materials/team-node.js --compare` (exit 0;
the comparator fails on a planted change: HANDOFF_COST 41 gives 10 differences). Seed 20261010,
12 weeks. `materials/canon.json` holds the 6-dp canon.

Rules (print on the widget): 40-hour week (2,400 min). Rituals per team of n: stand-up 5 x (5 + 2n),
planning 30 + 5n, retro 60 fortnightly (30/wk), review 40 fortnightly (20/wk); n=7: 210 min (3.5 h),
n=4: 165, n=3: 150, n=9: 240 (4.0 h). Coordination: each path costs each of its two people 60 min a week
ad hoc, 20 min with the ritual set. Handoffs: 6 a week across the split's interface, 40 min to each of
the two liaisons per item. Interrupts: seeded, mean over 12 weeks (Ana 279.2 min, Priya 165.8, Tom 163.8,
Wei 84.6, Sam 232.1, Lena 90.8, Kofi 86.7, Mo 65.8, Jun 54.6).

| Design | people | paths | meeting h / person | coordination h / person | focus h / person | team focus h | lowest focus | handoffs | bus factor | single-knower areas |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 One team of 7, no rituals (ad hoc 60) | 7 | 21 | 0.0 | 6.0 | 31.4 | 219.6 | 29.3 (Ana) | 0 | 1 | pipeline |
| 1 at ad hoc 30 | 7 | 21 | 0.0 | 3.0 | 34.4 | | | 0 | 1 | pipeline |
| 2 One team of 7, ritual set | 7 | 21 | 3.5 | 2.0 | 31.9 | 223.1 | 29.8 (Ana) | 0 | 1 | pipeline |
| 3 Split 4 + 3, one interface | 7 | 10 | 2.6 | 0.95 | 32.6 | 228.5 | 29.8 (Tom) | 6 | 1 | pipeline |
| 4 Nine, two hires ramped | 9 | 36 | 4.0 | 2.7 | 31.1 | 279.6 | 28.7 (Ana) | 0 | 2 | none |

Per person, design 2: Ana 29.8, Priya 31.7, Tom 31.8, Wei 33.1, Sam 30.6, Lena 33.0, Kofi 33.1.
Design 3: Ana 32.2, Priya 33.5, Tom 29.8, Wei 30.5 (Tom and Wei are the liaisons), Sam 33.0, Lena 34.7,
Kofi 34.8. Design 4: Ana 28.7, Priya 30.6, Tom 30.6, Wei 31.9, Sam 29.5, Lena 31.8, Kofi 31.9, Mo 32.2,
Jun 32.4. Design 4 adds 56.5 team focus hours for two people (two veterans' worth would be about 63.7).

Readings to teach: the ritual set costs 3.5 h a person and saves 4.0 h of ad hoc coordination at 60
min a path (net +0.5 h); at 30 min a path the team without rituals has 34.4 h, so the set costs 2.5 h.
The split halves the paths (21 to 10) and raises mean focus to 32.6 h, but the 6 handoffs land on the
two liaisons, who become the most squeezed people on the team. Nine people: 36 paths, more total focus,
less per person.

**Break, Priya leaves** (exact on the declared map): designs 1-3: pipeline has nobody, 20% of the weekly
work stops, bus factor 1 to 0, infrastructure now rests on Kofi alone; paths 21 to 15 (split: 10 to 7).
Design 4 (Jun has learned the pipeline): nothing stops, bus factor 2 to 1, pipeline now rests on Jun
alone; paths 36 to 28.

**Anti-lever, add two people to a late project** (modelled; 7 people with ritual set, 223.1 team focus
h/week; hires ramp 0/0/25/25/50/50/75/75 then 100%; mentoring 360 min/week per hire weeks 1-4, 180 weeks
5-8; team of 9 has 36 paths):

| weeks of work left (7 people) | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 10 | 20 |
|---|---|---|---|---|---|---|---|---|---|
| weeks with two hires | 2.2 | 3.2 | 4.2 | 5.1 | 6.0 (6.05) | 6.9 | 7.8 | 9.4 | 17.4 |
| verdict | later | later | later | later | later | sooner | sooner | sooner | sooner |

At 4 weeks (the default): 4.2 weeks, 54 veteran hours mentoring, 259 new-hire hours not yet productive.
Crossover between 6 and 7 weeks on these rules. **Honesty:** the crossover is a property of the stated
ramp and mentoring numbers, not of teams; the lesson is the shape, not the week.

## Not covered (honest list)

- Individual performance, coaching, onboarding, career ladders, PIPs, exits (performance management).
- Hiring and interviewing (AI HR). Goal-setting and OKRs (OKR). RACI charts (tech project PMO).
- Running a single meeting (facilitation). Delegation frameworks (AI leadership).
- Org-design at company scale (reorgs, spans of control above one team); Graicunas's span-of-control
  formula: not read, not taught.
- Any "ideal team size" number: none is taught as a finding.
- The 7-38-55 rule, "1:1s are the most important meeting", Eisenhower's matrix quote, "multitasking
  costs 40 percent": not verified, not used.
- Stress as health: not taught; pointer to the planned move shelf.
- Effect sizes from Edmondson 1999 and Frazier 2017: not read, not quoted.

## Citation appendix

1. Conway, M. E. (1968). How do committees invent? Datamation, April 1968. https://www.melconway.com/Home/Committees_Paper.html
2. Brooks, F. P. (1975). The Mythical Man-Month. Addison-Wesley (reported). https://en.wikipedia.org/wiki/The_Mythical_Man-Month
3. Lindenfors, P., Wartel, A., Lind, J. (2021). 'Dunbar's number' deconstructed. Biology Letters 17(5): 20210158. https://pmc.ncbi.nlm.nih.gov/articles/PMC8103230/
4. Google re:Work. Guide: Understand team effectiveness. https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness
5. Edmondson, A. (1999). Psychological safety and learning behavior in work teams. Administrative Science Quarterly 44(2): 350-383. https://doi.org/10.2307/2666999
6. Frazier, M. L. et al. (2017). Psychological safety: A meta-analytic review and extension. Personnel Psychology 70(1): 113-165. https://doi.org/10.1111/peps.12183
7. De Dreu, C. K. W., Weingart, L. R. (2003). Task versus relationship conflict, team performance, and team member satisfaction: A meta-analysis. Journal of Applied Psychology 88(4): 741-749. https://doi.org/10.1037/0021-9010.88.4.741
8. de Wit, F. R. C., Greer, L. L., Jehn, K. A. (2012). The paradox of intragroup conflict: A meta-analysis. Journal of Applied Psychology 97(2): 360-390. https://doi.org/10.1037/a0024844
9. Mark, G., Gudith, D., Klocke, U. (2008). The cost of interrupted work: more speed and stress. CHI 2008: 107-110. https://www.ics.uci.edu/~gmark/chi08-mark.pdf
10. Yang, L. et al. (2021). The effects of remote work on collaboration among information workers. Nature Human Behaviour. https://doi.org/10.1038/s41562-021-01196-4
11. Avelino, G., Passos, L., Hora, A., Valente, M. T. (2016). A novel approach for estimating truck factors. ICPC 2016. https://arxiv.org/abs/1604.06766
12. Hackman, J. R. (2002). Leading Teams. Harvard Business School Press (reported).
13. Skelton, M., Pais, M. (2019). Team Topologies. IT Revolution (practitioner). https://teamtopologies.com/key-concepts
14. Kaner, S. et al. (2014). Facilitator's Guide to Participatory Decision-Making, 3rd ed. Jossey-Bass. https://www.wiley.com/en-us/Facilitator%27s+Guide+to+Participatory+Decision+Making%2C+3rd+Edition-p-9781118404959
