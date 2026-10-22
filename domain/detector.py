"""Domain Layer: pure detection logic. No file I/O or printing here."""


def detect_subscriptions(transactions):
    """Return the transactions that look like recurring subscriptions.

    transactions: list of dicts, e.g. {"date": ..., "description": ..., "amount": ...}
    """
    # TODO: group by merchant/amount and check for regular intervals.
    return []
