def test_finds_maximum_matching(lesson_module):
    lesson = lesson_module(13)
    graph = {"A": {"1", "2"}, "B": {"1"}, "C": {"2", "3"}}
    matching = lesson.maximum_bipartite_matching(graph, {"A", "B", "C"})
    assert set(matching) == {"A", "B", "C"}
    assert len(set(matching.values())) == 3
    assert all(right in graph[left] for left, right in matching.items())


def test_returns_partial_matching_when_perfect_is_impossible(lesson_module):
    lesson = lesson_module(13)
    matching = lesson.maximum_bipartite_matching({"A": {"1"}, "B": {"1"}}, {"A", "B"})
    assert len(matching) == 1


def test_rejects_overlapping_partitions(lesson_module):
    import pytest

    lesson = lesson_module(13)
    with pytest.raises(ValueError):
        lesson.maximum_bipartite_matching({"A": {"B"}, "B": set()}, {"A", "B"})


def test_rejects_missing_left_vertex(lesson_module):
    import pytest

    lesson = lesson_module(13)
    with pytest.raises(ValueError):
        lesson.maximum_bipartite_matching({"A": {"1"}}, {"A", "missing"})
