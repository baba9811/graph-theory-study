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


def test_cycle_definition_requires_three_vertices_and_no_repeated_edge():
    lesson = open("lessons/02-degree-path-cycle.md", encoding="utf-8").read()
    assert "최소 세 개의 서로 다른 정점" in lesson
    assert "같은 간선을 두 번 지나지" in lesson
