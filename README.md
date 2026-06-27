# Duolingo Database Project

A relational database modeling a Duolingo-style language learning platform, built for 67-262 Database Design and Development at Carnegie Mellon University.

## Overview

Designed and implemented a normalized PostgreSQL database supporting core Duolingo features including leaderboards, streaks, gamification, virtual lessons, and vocabulary management. The schema is in BCNF and covers 16 tables with realistic seed data.

## Tech Stack

- PostgreSQL
- Python (psycopg2, prettytable)

## Setup

1. Update the file paths in `sql_scripts/initialize.sql` to match your local `data/` directory
2. Run the initialization script:
```bash
   psql -U isdb -f sql_scripts/initialize.sql
```
3. Install Python dependencies:
```bash
   pip install psycopg2 prettytable
```

## Running User Stories

Each script in `sql_query_scripts/` implements one user story:

| File | User Story |
|------|------------|
| us1-track-props-operational-simple.py | Track props/boosters |
| us2-view-leaderboard-rank-complex-analytical.py | View leaderboard rank |
| us3-track-streaks-operational-simple.py | Track streaks and daily goals |
| us4-view-avg-accuracy-analytical-simple.py | View exercise accuracy |
| us5-upload-vocabulary-simple-operational.py | Upload vocabulary |
| us6-evaluate-game-features-complex-analytical.py | Evaluate game features |
| us7-retire-course-complex-operational.py | Retire a course |
| us8-flag-suspicious-account-simple-operational.py | Flag suspicious account |
| us9-view-avg-xp-analytical-simple.py | View average daily XP |
| us10-join-virtual-lesson-operational-complex.py | Join a virtual lesson |

Run any script from the `sql_query_scripts/` directory:
```bash
python us1-track-props-operational-simple.py
```

## Schema

See `report.pdf` for the full ERD, relational model, functional dependencies, and normalization analysis.
