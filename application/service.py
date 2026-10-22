"""Application Layer: orchestrates data loading and detection."""
from data.csv_handler import load_transactions
from domain.detector import detect_subscriptions


class SubscriptionService:
    def find_subscriptions(self, csv_path):
        transactions = load_transactions(csv_path)
        return detect_subscriptions(transactions)
