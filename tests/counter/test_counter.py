from src.pre_built.counter import count_ocurrences


def test_counter():
    test_cases = [
        ("analyze", 828),
        ("foreign", 149),
        ("Medical", 1639)
    ]

    for word, expected_count in test_cases:
        count = count_ocurrences("data/jobs.csv", word)
        assert count == expected_count
