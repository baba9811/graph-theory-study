def test_greedy_coloring_is_proper(lesson_module):
    lesson = lesson_module(17)
    graph = {"A": {"B", "C"}, "B": {"A", "C"}, "C": {"A", "B", "D"}, "D": {"C"}}
    colors = lesson.greedy_coloring(graph)
    assert all(colors[u] != colors[v] for u in graph for v in graph[u])
    assert set(colors) == set(graph)


def test_planar_edge_bound_for_small_and_general_graphs(lesson_module):
    lesson = lesson_module(17)
    assert lesson.within_planar_edge_bound(2, 1)
    assert not lesson.within_planar_edge_bound(2, 2)
    assert lesson.within_planar_edge_bound(4, 6)
    assert not lesson.within_planar_edge_bound(5, 10)


def test_rejects_negative_counts(lesson_module):
    import pytest

    lesson = lesson_module(17)
    with pytest.raises(ValueError):
        lesson.within_planar_edge_bound(-1, 0)
