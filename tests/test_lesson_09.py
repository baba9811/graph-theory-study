def test_handles_negative_edges_without_negative_cycle(lesson_module):
    lesson = lesson_module(9)
    vertices = {"A", "B", "C", "D"}
    edges = [("A", "B", 4), ("A", "C", 5), ("B", "C", -2), ("C", "D", 3)]
    distances, parents = lesson.bellman_ford(vertices, edges, "A")
    assert distances == {"A": 0, "B": 4, "C": 2, "D": 5}
    assert parents["C"] == "B"


def test_detects_reachable_negative_cycle(lesson_module):
    import pytest

    lesson = lesson_module(9)
    edges = [("A", "B", 1), ("B", "C", -2), ("C", "B", -2)]
    with pytest.raises(ValueError, match="음수 사이클"):
        lesson.bellman_ford({"A", "B", "C"}, edges, "A")


def test_ignores_unreachable_negative_cycle(lesson_module):
    lesson = lesson_module(9)
    distances, _ = lesson.bellman_ford(
        {"A", "B", "C"}, [("B", "C", -2), ("C", "B", -2)], "A"
    )
    assert distances["B"] == float("inf")
