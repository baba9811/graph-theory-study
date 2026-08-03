def test_finds_all_connected_components(lesson_module):
    lesson = lesson_module(4)
    graph = {"A": {"B"}, "B": {"A"}, "C": set(), "D": {"E"}, "E": {"D"}}
    components = {frozenset(group) for group in lesson.connected_components(graph)}
    assert components == {frozenset({"A", "B"}), frozenset({"C"}), frozenset({"D", "E"})}


def test_detects_undirected_cycle(lesson_module):
    lesson = lesson_module(4)
    tree = {"A": {"B"}, "B": {"A", "C"}, "C": {"B"}}
    triangle = {"A": {"B", "C"}, "B": {"A", "C"}, "C": {"A", "B"}}
    assert not lesson.has_cycle(tree)
    assert lesson.has_cycle(triangle)


def test_empty_graph_has_no_components_or_cycle(lesson_module):
    lesson = lesson_module(4)
    assert lesson.connected_components({}) == []
    assert not lesson.has_cycle({})
