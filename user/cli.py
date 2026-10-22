"""User Layer: parses command-line arguments and prints results."""
import argparse

from application.service import SubscriptionService


def run(argv=None):
    parser = argparse.ArgumentParser(
        prog="subwatch",
        description="Find recurring subscriptions in a bank CSV.",
    )
    parser.add_argument("csv_path", help="Path to the bank transactions CSV")
    args = parser.parse_args(argv)

    service = SubscriptionService()
    subscriptions = service.find_subscriptions(args.csv_path)

    if not subscriptions:
        print("No subscriptions found.")
        return
    for sub in subscriptions:
        print(sub)
