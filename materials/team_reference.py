#!/usr/bin/env python3
"""team_reference.py - Python reference for the team-size bench (learn-team-management-with-phoebe).

Northline is a CONSTRUCTED 7-person data team. Nothing here is a measurement of a real team.

What is EXACT:   communication paths n(n-1)/2 per team, plus one path per declared interface;
                 bus factor = the fewest people whose departure leaves some work area with nobody
                 who knows it (= the smallest number of knowers over all areas).
What is MODELLED (stated on the widget, every rule below):
    week          2,400 minutes per person (40 hours)
    rituals       per team of n: daily stand-up 5 x (5 + 2n) min, weekly planning (30 + 5n) min,
                  fortnightly retro 60 min (30 a week), fortnightly review 40 min (20 a week)
    coordination  each path a person sits on costs that person 60 min a week ad hoc,
                  or 20 min a week once the team has a shared ritual set
    handoffs      work crossing a team boundary: 6 items a week in the split design, each costing
                  40 min to each of the two liaisons who carry it
    interrupts    seeded: each person has a weekly exposure e (minutes); week w draws
                  u = floor(r * 101) from mulberry32(SEED + 97 * person) and costs
                  5 * floor(e * (50 + u) / 500) minutes; 12 weeks, mean reported
    focus         2,400 - rituals - coordination - handoffs - interrupts
    late project  (anti-lever) two hires join a 7-person team with L weeks of work left; hires
                  deliver 0 / 25 / 50 / 75 / 100 percent of their focus in weeks 1-2 / 3-4 / 5-6 /
                  7-8 / 9+; each hire takes 360 min a week of veteran time in weeks 1-4 and 180 in
                  weeks 5-8 (spread across the seven); the team becomes 9 with 36 paths
    key person    (break) Priya leaves: every area she alone knew has nobody; its share of the
                  weekly work stops

Run:  python3 materials/team_reference.py            prints the canon as JSON (6 dp)
      python3 materials/team_reference.py --raw      full precision, for the node comparison
      python3 materials/team_reference.py --emit     also writes assets/northline-data.js
The node twin (materials/team-node.js) loads assets/team-live.js and must print identical JSON.
"""
import json
import math
import os
import sys

SEED = 20261010
WEEKS = 12
WEEK_MIN = 2400

AREAS = ["pipeline", "infrastructure", "dashboards", "models", "data quality", "experiments", "stakeholder requests"]
AREA_WEIGHT = [20, 10, 20, 15, 15, 10, 10]  # percent of the weekly work

PEOPLE = [
    {"name": "Ana", "role": "team lead", "e": 300, "areas": [6]},
    {"name": "Priya", "role": "data engineer", "e": 150, "areas": [0, 1]},
    {"name": "Tom", "role": "analytics engineer", "e": 180, "areas": [2, 4]},
    {"name": "Wei", "role": "data scientist", "e": 90, "areas": [3, 4, 5]},
    {"name": "Sam", "role": "analyst", "e": 240, "areas": [2, 6]},
    {"name": "Lena", "role": "data scientist", "e": 90, "areas": [3, 5]},
    {"name": "Kofi", "role": "platform engineer", "e": 90, "areas": [1, 4]},
    {"name": "Mo", "role": "analyst (hire)", "e": 60, "areas": [2]},
    {"name": "Jun", "role": "data engineer (hire)", "e": 60, "areas": [1]},
]

# Designs. "teams" lists member indexes; "learned" adds areas a person knows in that design.
DESIGNS = [
    {"id": "adhoc7", "label": "One team of 7, no shared rituals", "teams": [[0, 1, 2, 3, 4, 5, 6]],
     "rituals": False, "interfaces": [], "handoffs": 0, "learned": {}},
    {"id": "rituals7", "label": "One team of 7, weekly ritual set", "teams": [[0, 1, 2, 3, 4, 5, 6]],
     "rituals": True, "interfaces": [], "handoffs": 0, "learned": {}},
    {"id": "split43", "label": "Split 4 + 3, one interface", "teams": [[1, 3, 5, 6], [0, 2, 4]],
     "rituals": True, "interfaces": [[3, 2]], "handoffs": 6, "learned": {}},
    {"id": "nine", "label": "Nine people, after two hires have ramped up", "teams": [[0, 1, 2, 3, 4, 5, 6, 7, 8]],
     "rituals": True, "interfaces": [], "handoffs": 0, "learned": {"8": [0]}},
]

COORD_ADHOC = 60
COORD_RITUAL = 20
HANDOFF_COST = 40
RAMP = [0, 0, 25, 25, 50, 50, 75, 75]  # weeks 1-8, then 100
MENTOR = [360, 360, 360, 360, 180, 180, 180, 180]  # per hire per week, weeks 1-8, then 0
LEAVER = 1  # Priya


def mulberry32(a):
    state = [a & 0xFFFFFFFF]

    def imul(x, y):
        return ((x & 0xFFFFFFFF) * (y & 0xFFFFFFFF)) & 0xFFFFFFFF

    def nxt():
        state[0] = (state[0] + 0x6D2B79F5) & 0xFFFFFFFF
        a0 = state[0]
        t = imul(a0 ^ (a0 >> 15), 1 | a0)
        t = ((t + imul(t ^ (t >> 7), 61 | t)) & 0xFFFFFFFF) ^ t
        return ((t ^ (t >> 14)) & 0xFFFFFFFF) / 4294967296

    return nxt


def interrupts(i):
    r = mulberry32(SEED + 97 * i)
    e = PEOPLE[i]["e"]
    out = []
    for _ in range(WEEKS):
        u = int(r() * 101)
        out.append(5 * ((e * (50 + u)) // 500))
    return out


def ritual_minutes(n):
    return 5 * (5 + 2 * n) + (30 + 5 * n) + 30 + 20


def paths(n):
    return n * (n - 1) // 2


def knowers(members, learned):
    k = [[] for _ in AREAS]
    for i in members:
        areas = list(PEOPLE[i]["areas"]) + list(learned.get(str(i), []))
        for a in areas:
            if i not in k[a]:
                k[a].append(i)
    return k


def bus_factor(k):
    return min(len(x) for x in k)


def evaluate(d, leaver=None):
    teams = [[i for i in t if i != leaver] for t in d["teams"]]
    teams = [t for t in teams if t]
    members = [i for t in teams for i in t]
    interfaces = [f for f in d["interfaces"] if leaver not in f]
    handoffs = d["handoffs"] if interfaces else 0
    coord = COORD_RITUAL if d["rituals"] else COORD_ADHOC
    people = []
    for t in teams:
        n = len(t)
        rit = ritual_minutes(n) if d["rituals"] else 0
        for i in t:
            liaison = sum(1 for f in interfaces if i in f)
            co = (n - 1 + liaison) * coord
            ho = handoffs * HANDOFF_COST * liaison
            ints = interrupts(i)
            mean_int = sum(ints) / WEEKS
            focus = WEEK_MIN - rit - co - ho - mean_int
            people.append({"i": i, "ritual": rit, "coord": co, "handoff": ho, "interrupt": mean_int, "focus": focus})
    people.sort(key=lambda p: p["i"])
    total_paths = sum(paths(len(t)) for t in teams) + len(interfaces)
    k = knowers(members, d["learned"])
    stopped = [a for a in range(len(AREAS)) if not k[a]]
    n = len(people)
    return {
        "id": d["id"], "size": n, "paths": total_paths,
        "meetingHours": sum(p["ritual"] for p in people) / n / 60,
        "coordHours": sum(p["coord"] for p in people) / n / 60,
        "focusHours": sum(p["focus"] for p in people) / n / 60,
        "teamFocusHours": sum(p["focus"] for p in people) / 60,
        "minFocusHours": min(p["focus"] for p in people) / 60,
        "handoffs": handoffs,
        "busFactor": bus_factor(k),
        "single": [AREAS[a] for a in range(len(AREAS)) if len(k[a]) == 1],
        "stopped": [AREAS[a] for a in stopped],
        "stoppedShare": sum(AREA_WEIGHT[a] for a in stopped),
        "people": [{"name": PEOPLE[p["i"]]["name"], "focus": p["focus"] / 60} for p in people],
    }


def late_project(weeks_left):
    """Anti-lever. Returns weeks to finish without and with two hires."""
    base = evaluate(DESIGNS[1])
    weekly7 = base["teamFocusHours"] * 60
    work = weeks_left * weekly7
    nine = {"id": "late9", "teams": [[0, 1, 2, 3, 4, 5, 6, 7, 8]], "rituals": True, "interfaces": [], "handoffs": 0, "learned": {}}
    e9 = evaluate(nine)
    vet = sum(p["focus"] * 60 for p in e9["people"][:7])
    hire = [p["focus"] * 60 for p in e9["people"][7:]]
    done, w, mentor_total, idle_total = 0.0, 0, 0, 0.0
    while True:
        w += 1
        pct = RAMP[w - 1] if w <= len(RAMP) else 100
        men = 2 * (MENTOR[w - 1] if w <= len(MENTOR) else 0)
        deliver = vet - men + sum(math.floor(h * pct / 100) for h in hire)
        mentor_total += men
        idle_total += sum(h - math.floor(h * pct / 100) for h in hire)
        if done + deliver >= work:
            weeks = (w - 1) + (work - done) / deliver
            break
        done += deliver
        if w > 400:
            weeks = float("inf")
            break
    return {"weeksLeft": weeks_left, "withHires": weeks, "paths": e9["paths"],
            "mentorHours": mentor_total / 60, "hireIdleHours": idle_total / 60}


def canon():
    global COORD_ADHOC
    res = {"designs": [evaluate(d) for d in DESIGNS]}
    keep = COORD_ADHOC
    COORD_ADHOC = 30
    res["adhoc30"] = evaluate(DESIGNS[0])
    COORD_ADHOC = keep
    res["leaver"] = {d["id"]: evaluate(d, LEAVER) for d in DESIGNS}
    res["late"] = [late_project(L) for L in (2, 3, 4, 5, 6, 7, 8, 10, 20)]
    res["interrupts"] = [interrupts(i) for i in range(len(PEOPLE))]
    return res


def rounded(o):
    if isinstance(o, float):
        return round(o, 6)
    if isinstance(o, dict):
        return {k: rounded(v) for k, v in o.items()}
    if isinstance(o, list):
        return [rounded(v) for v in o]
    return o


def emit(repo):
    data = {"seed": SEED, "weeks": WEEKS, "areas": AREAS, "areaWeight": AREA_WEIGHT, "people": PEOPLE,
            "designs": DESIGNS, "coordAdhoc": COORD_ADHOC, "coordRitual": COORD_RITUAL,
            "handoffCost": HANDOFF_COST, "ramp": RAMP, "mentor": MENTOR, "leaver": LEAVER}
    path = os.path.join(repo, "assets", "northline-data.js")
    with open(path, "w") as f:
        f.write("/* Northline, a constructed 7-person data team (plus two hires). Generated by materials/team_reference.py --emit. */\n")
        f.write("window.NORTHLINE = " + json.dumps(data, separators=(",", ":")) + ";\n")
    return path


if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if "--emit" in sys.argv:
        print("wrote", emit(repo), file=sys.stderr)
    c = canon()
    print(json.dumps(c if "--raw" in sys.argv else rounded(c), indent=1, sort_keys=True))
