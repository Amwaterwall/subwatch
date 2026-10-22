from domain.detector import detect_subscriptions


def test_empty_input_returns_empty_list():
    assert detect_subscriptions([]) == []
