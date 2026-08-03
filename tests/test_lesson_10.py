def test_computes_all_pairs_distances(lesson_module):
    lesson = lesson_module(10)
    distances = lesson.floyd_warshall(
        {"A", "B", "C"}, [("A", "B", 1), ("B", "C", 2), ("A", "C", 10)]
    )
    assert distances["A"]["C"] == 3
    assert distances["C"]["A"] == float("inf")
    assert all(distances[vertex][vertex] == 0 for vertex in {"A", "B", "C"})


def test_uses_smallest_parallel_edge(lesson_module):
    lesson = lesson_module(10)
    distances = lesson.floyd_warshall(
        {"A", "B"}, [("A", "B", 5), ("A", "B", 2)]
    )
    assert distances["A"]["B"] == 2


def test_rejects_negative_cycle(lesson_module):
    import pytest

    lesson = lesson_module(10)
    with pytest.raises(ValueError, match="음수 사이클"):
        lesson.floyd_warshall({"A", "B"}, [("A", "B", -2), ("B", "A", 1)])


def test_rejects_unknown_endpoint(lesson_module):
    import pytest

    lesson = lesson_module(10)
    with pytest.raises(ValueError):
        lesson.floyd_warshall({"A"}, [("A", "missing", 1)])
