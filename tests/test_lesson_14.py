def test_finds_max_flow_and_min_cut(lesson_module):
    lesson = lesson_module(14)
    capacity = {
        "s": {"a": 3, "b": 2},
        "a": {"b": 1, "t": 2},
        "b": {"t": 3},
        "t": {},
    }
    value, source_side = lesson.edmonds_karp(capacity, "s", "t")
    assert value == 5
    assert isinstance(value, int)
    assert "s" in source_side and "t" not in source_side


def test_zero_capacity_path_carries_no_flow(lesson_module):
    lesson = lesson_module(14)
    value, source_side = lesson.edmonds_karp({"s": {"t": 0}, "t": {}}, "s", "t")
    assert value == 0
    assert isinstance(value, int)
    assert source_side == {"s"}


def test_rejects_negative_capacity_and_unknown_endpoint(lesson_module):
    import pytest

    lesson = lesson_module(14)
    with pytest.raises(ValueError):
        lesson.edmonds_karp({"s": {"t": -1}, "t": {}}, "s", "t")

    with pytest.raises(ValueError):
        lesson.edmonds_karp({"s": {"t": 1}}, "s", "t")


def test_rejects_missing_or_identical_terminals(lesson_module):
    import pytest

    lesson = lesson_module(14)
    capacity = {"s": {"t": 1}, "t": {}}
    with pytest.raises(ValueError):
        lesson.edmonds_karp(capacity, "missing", "t")
    with pytest.raises(ValueError):
        lesson.edmonds_karp(capacity, "s", "missing")
    with pytest.raises(ValueError):
        lesson.edmonds_karp(capacity, "s", "s")
