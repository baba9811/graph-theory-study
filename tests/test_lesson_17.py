import pytest


def test_greedy_coloring_is_proper(lesson_module):
    lesson = lesson_module(17)
    graph = {"A": {"B", "C"}, "B": {"A", "C"}, "C": {"A", "B", "D"}, "D": {"C"}}
    colors = lesson.greedy_coloring(graph)
    assert all(colors[u] != colors[v] for u in graph for v in graph[u])
    assert set(colors) == set(graph)
    assert colors == {"C": 0, "A": 1, "B": 2, "D": 1}


def test_greedy_coloring_rejects_unknown_neighbor(lesson_module):
    lesson = lesson_module(17)
    with pytest.raises(ValueError, match="인접 정점이 graph에 없습니다"):
        lesson.greedy_coloring({"A": {"X"}})


def test_greedy_coloring_rejects_non_simple_or_asymmetric_input(lesson_module):
    lesson = lesson_module(17)
    with pytest.raises(ValueError, match="무방향 단순 그래프"):
        lesson.greedy_coloring({"A": {"A"}})
    with pytest.raises(ValueError, match="무방향 단순 그래프"):
        lesson.greedy_coloring({"A": {"B"}, "B": set()})


def test_planar_edge_bound_for_small_graphs(lesson_module):
    lesson = lesson_module(17)
    assert lesson.within_planar_edge_bound(0, 0)
    assert not lesson.within_planar_edge_bound(0, 1)
    assert lesson.within_planar_edge_bound(1, 0)
    assert not lesson.within_planar_edge_bound(1, 1)
    assert lesson.within_planar_edge_bound(2, 0)
    assert lesson.within_planar_edge_bound(2, 1)
    assert not lesson.within_planar_edge_bound(2, 2)


def test_planar_edge_bound_for_general_graphs(lesson_module):
    lesson = lesson_module(17)
    assert lesson.within_planar_edge_bound(4, 6)
    assert not lesson.within_planar_edge_bound(5, 10)


def test_rejects_negative_vertex_count(lesson_module):
    lesson = lesson_module(17)
    with pytest.raises(ValueError):
        lesson.within_planar_edge_bound(-1, 0)


def test_rejects_negative_edge_count(lesson_module):
    lesson = lesson_module(17)
    with pytest.raises(ValueError):
        lesson.within_planar_edge_bound(1, -1)
