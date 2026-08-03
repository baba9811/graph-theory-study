def test_finds_weighted_shortest_paths(lesson_module):
    lesson = lesson_module(8)
    graph = {
        "A": {"B": 4, "C": 1},
        "B": {"D": 1},
        "C": {"B": 2, "D": 5},
        "D": {},
        "E": {},
    }
    distances, parents = lesson.dijkstra(graph, "A")
    assert distances["D"] == 4
    assert parents["D"] == "B" and parents["B"] == "C"
    assert distances["E"] == float("inf")


def test_rejects_negative_weight(lesson_module):
    import pytest

    lesson = lesson_module(8)
    with pytest.raises(ValueError, match="음수"):
        lesson.dijkstra({"A": {"B": -1}, "B": {}}, "A")


def test_rejects_unknown_start(lesson_module):
    import pytest

    lesson = lesson_module(8)
    with pytest.raises(ValueError):
        lesson.dijkstra({"A": {}}, "Z")
