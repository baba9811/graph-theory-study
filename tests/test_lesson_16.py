def assert_hamiltonian(graph, path):
    assert len(path) == len(graph)
    assert set(path) == set(graph)
    assert all(right in graph[left] for left, right in zip(path, path[1:]))


def test_finds_hamiltonian_path(lesson_module):
    lesson = lesson_module(16)
    graph = {"A": {"B"}, "B": {"A", "C", "D"}, "C": {"B", "D"}, "D": {"B", "C"}}
    assert_hamiltonian(graph, lesson.hamiltonian_path(graph))


def test_returns_none_when_no_path_exists(lesson_module):
    lesson = lesson_module(16)
    star = {"O": {"A", "B", "C"}, "A": {"O"}, "B": {"O"}, "C": {"O"}}
    assert lesson.hamiltonian_path(star) is None


def test_handles_empty_and_single_vertex_graphs(lesson_module):
    lesson = lesson_module(16)
    assert lesson.hamiltonian_path({}) == []
    assert lesson.hamiltonian_path({"A": set()}) == ["A"]
