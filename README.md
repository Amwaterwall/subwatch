# subwatch
A local tool that finds forgotten subscriptions in a bank CSV and reminds you before the next charge — with no bank login.

## Project structure

```
subwatch/
├── main.py              # thin entry point
├── user/cli.py          # User Layer
├── application/service.py  # Application Layer (orchestration)
├── domain/detector.py   # Domain Layer (pure detection logic)
├── data/csv_handler.py  # Data Layer (CSV I/O)
└── tests/
```

## Run

```
pip install -r requirements.txt
python3 main.py path/to/transactions.csv
python3 -m pytest
```
