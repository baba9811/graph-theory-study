def test_finds_strong_components(lesson_module):
    lesson = lesson_module(7)
    graph = {
        "A": {"B"}, "B": {"A", "C"},
        "C": {"D"}, "D": {"C", "E"}, "E": set(),
    }
    result = {frozenset(group) for group in lesson.strongly_connected_components(graph)}
    assert result == {frozenset({"A", "B"}), frozenset({"C", "D"}), frozenset({"E"})}


def test_empty_graph_has_no_strong_components(lesson_module):
    lesson = lesson_module(7)
    assert lesson.strongly_connected_components({}) == []


def test_rejects_unknown_neighbor(lesson_module):
    import pytest

    lesson = lesson_module(7)
    with pytest.raises(ValueError):
        lesson.strongly_connected_components({"A": {"B"}})
