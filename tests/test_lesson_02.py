def test_degree_sum_is_twice_the_edge_count(lesson_module):
    lesson = lesson_module(2)
    graph = {"A": {"B", "C"}, "B": {"A"}, "C": {"A"}}
    degrees = lesson.degree_map(graph)
    assert degrees == {"A": 2, "B": 1, "C": 1}
    assert sum(degrees.values()) == 4


def test_accepts_single_vertex_and_multi_vertex_paths(lesson_module):
    lesson = lesson_module(2)
    graph = {"A": {"B"}, "B": {"A", "C"}, "C": {"B"}}
    assert lesson.is_valid_path(graph, ["A"])
    assert lesson.is_valid_path(graph, ["A", "B", "C"])


def test_rejects_repeated_or_nonadjacent_vertices(lesson_module):
    lesson = lesson_module(2)
    graph = {"A": {"B"}, "B": {"A", "C"}, "C": {"B"}}
    assert not lesson.is_valid_path(graph, ["A", "B", "A"])
    assert not lesson.is_valid_path(graph, ["A", "C"])
    assert not lesson.is_valid_path(graph, [])
