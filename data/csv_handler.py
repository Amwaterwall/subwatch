"""Data Layer: reads and writes CSV files."""
import csv


def load_transactions(csv_path):
    """Read a bank CSV into a list of dicts, one per row."""
    with open(csv_path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))
