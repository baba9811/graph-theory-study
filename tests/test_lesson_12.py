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
