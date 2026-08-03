def test_colors_disconnected_bipartite_graph(lesson_module):
    lesson = lesson_module(12)
    graph = {"A": {"B"}, "B": {"A"}, "C": {"D"}, "D": {"C"}, "E": set()}
    colors = lesson.bipartite_coloring(graph)
    assert set(colors) == set(graph)
    assert all(colors[u] != colors[v] for u in graph for v in graph[u])


def test_odd_cycle_is_not_bipartite(lesson_module):
    lesson = lesson_module(12)
    triangle = {"A": {"B", "C"}, "B": {"A", "C"}, "C": {"A", "B"}}
    assert lesson.bipartite_coloring(triangle) is None


def test_empty_graph_has_empty_coloring(lesson_module):
    lesson = lesson_module(12)
    assert lesson.bipartite_coloring({}) == {}


def test_rejects_non_simple_or_asymmetric_input(lesson_module):
    import pytest

    lesson = lesson_module(12)
    with pytest.raises(ValueError, match="무방향 단순 그래프"):
        lesson.bipartite_coloring({"A": {"A"}})
    with pytest.raises(ValueError, match="무방향 단순 그래프"):
        lesson.bipartite_coloring({"A": {"B"}, "B": set()})
