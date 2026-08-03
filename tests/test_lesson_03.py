def test_bfs_distances_and_path(lesson_module):
    lesson = lesson_module(3)
    graph = {
        "A": {"B", "C"}, "B": {"A", "D"},
        "C": {"A", "D"}, "D": {"B", "C"}, "E": set(),
    }
    distances, parents = lesson.bfs(graph, "A")
    assert distances == {"A": 0, "B": 1, "C": 1, "D": 2}
    path = lesson.reconstruct_path(parents, "A", "D")
    assert path[0] == "A" and path[-1] == "D" and len(path) == 3
    assert lesson.reconstruct_path(parents, "A", "E") is None


def test_bfs_rejects_unknown_start(lesson_module):
    import pytest

    lesson = lesson_module(3)
    with pytest.raises(ValueError):
        lesson.bfs({"A": set()}, "Z")
