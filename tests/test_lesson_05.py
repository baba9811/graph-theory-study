from pathlib import Path


def test_tree_equivalences_explicitly_require_a_nonempty_graph():
    lesson_text = Path("lessons/05-trees-and-forests.md").read_text()
    assert "정점이 하나 이상인 유한 무방향 그래프" in lesson_text


def test_single_vertex_and_path_are_trees(lesson_module):
    lesson = lesson_module(5)
    assert lesson.is_tree({"A": set()})
    assert lesson.is_tree({"A": {"B"}, "B": {"A", "C"}, "C": {"B"}})


def test_empty_disconnected_and_cyclic_graphs_are_not_trees(lesson_module):
    lesson = lesson_module(5)
    assert not lesson.is_tree({})
    assert not lesson.is_tree({"A": set(), "B": set()})
    assert not lesson.is_tree(
        {"A": {"B", "C"}, "B": {"A", "C"}, "C": {"A", "B"}}
    )


def test_rejects_asymmetric_undirected_representation(lesson_module):
    lesson = lesson_module(5)
    assert not lesson.is_tree({"A": {"B"}, "B": set()})
