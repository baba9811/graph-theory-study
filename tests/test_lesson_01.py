def test_builds_undirected_graph_with_isolated_vertex(lesson_module):
    lesson = lesson_module(1)
    graph = lesson.build_adjacency_list(
        {"A", "B", "C"}, [("A", "B")]
    )
    assert graph == {"A": {"B"}, "B": {"A"}, "C": set()}


def test_directed_edges_are_not_reversed(lesson_module):
    lesson = lesson_module(1)
    graph = lesson.build_adjacency_list(
        {"A", "B"}, [("A", "B")], directed=True
    )
    assert graph == {"A": {"B"}, "B": set()}


def test_converts_list_to_matrix_in_requested_order(lesson_module):
    lesson = lesson_module(1)
    graph = {"A": {"B"}, "B": {"A"}, "C": set()}
    assert lesson.to_adjacency_matrix(graph, ["A", "B", "C"]) == [
        [0, 1, 0], [1, 0, 0], [0, 0, 0]
    ]


def test_rejects_unknown_endpoint(lesson_module):
    import pytest

    lesson = lesson_module(1)
    with pytest.raises(ValueError):
        lesson.build_adjacency_list({"A"}, [("A", "B")])
