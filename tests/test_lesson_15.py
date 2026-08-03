from collections import Counter


def normalized_edges(path):
    return Counter(tuple(sorted(edge)) for edge in zip(path, path[1:]))


def test_builds_euler_circuit(lesson_module):
    lesson = lesson_module(15)
    edges = [("A", "B"), ("B", "C"), ("C", "A")]
    path = lesson.eulerian_trail(edges)
    assert len(path) == 4
    assert path[0] == path[-1]
    assert normalized_edges(path) == Counter(tuple(sorted(edge)) for edge in edges)


def test_parallel_edges_remain_distinct(lesson_module):
    lesson = lesson_module(15)
    path = lesson.eulerian_trail([("A", "B"), ("A", "B")])
    assert path in (["A", "B", "A"], ["B", "A", "B"])


def test_rejects_disconnected_nonzero_degree_graph(lesson_module):
    lesson = lesson_module(15)
    assert lesson.eulerian_trail([("A", "B"), ("C", "D")]) is None
    assert lesson.eulerian_trail([]) == []
