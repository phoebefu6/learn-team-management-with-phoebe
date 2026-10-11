# Learn Team Management with Phoebe

Six 45-minute sessions on how a team runs, as distinct from how to manage any one person in it:
what turns a group with one manager into a team, who decides what and how a disagreement is
closed, the team's rituals and what they cost in hours, psychological safety and conflict as the
research describes them, and remote work, async decisions and key-person risk. The running case is
constructed: Northline, an invented 7-person data team.

**Live site:** https://phoebefu6.github.io/learn-team-management-with-phoebe/

| # | Session | Signature thing |
|---|---|---|
| 1 | A team is not a group of people with the same manager | Shared outcome and boundary, paths n(n-1)/2, Team Topologies' four shapes, the one-page charter |
| 2 | Who decides what | A decision-rights table, reversible vs hard-to-reverse calls, closing a disagreement on time |
| 3 | The team's rhythm and what it costs | The ritual budget in person-hours; a ritual set pays only when it replaces ad hoc coordination |
| 4 | The team-size bench | Exact paths and a modelled week for four designs, the late-project anti-lever, the key-person break button |
| 5 | Safety, conflict and the disagreement you need | Edmondson 1999 at source, Project Aristotle tiered as a company report, the task-conflict disagreement |
| 6 | Remote, async and the person who knows everything | Remote vs async, written decision defaults, an interrupt shield, a key-person plan |

The bench in session 4 (`assets/team-live.js`, data in `assets/northline-data.js`) computes
communication paths and the bus factor exactly on a declared, constructed team, and models every
hour from rules printed on the widget: 40-hour week, ritual minutes by team size, 60 or 20 minutes
per path for coordination, 40 minutes per handoff for each liaison, and seeded interrupts over 12
weeks. Seven people with a ritual set: 21 paths, 3.5 meeting hours and 31.9 focus hours a person a
week. Split 4 + 3: 10 paths and 32.6 focus hours on average, while the two liaisons drop to 29.8 and
30.5. The anti-lever, adding two people to a late project, finishes later up to about six weeks out
(4 weeks left becomes 4.2) and sooner beyond (20 becomes 17.4). The break button removes the one
person who knows the pipeline: 20 percent of the weekly work stops and the bus factor goes from 1
to 0. The Python reference (`python3 materials/team_reference.py --raw`) and the browser engine
(`node materials/team-node.js --compare`) agree on all 389 values.

Northline and everyone in it are constructed. Stress on these pages means workload and planning,
never medical advice.

By Phoebe Fu.
