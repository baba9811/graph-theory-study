def test_disjoint_set_union_reports_merge(lesson_module):
    lesson = lesson_module(11)
    groups = lesson.DisjointSet({"A", "B", "C"})
    assert groups.union("A", "B")
    assert not groups.union("A", "B")
    assert groups.find("A") == groups.find("B")


def test_kruskal_returns_minimum_tree(lesson_module):
    lesson = lesson_module(11)
    vertices = {"A", "B", "C", "D"}
    edges = [
        ("A", "B", 1),
        ("B", "C", 2),
        ("A", "C", 4),
        ("C", "D", 1),
        ("B", "D", 5),
    ]
    total, tree = lesson.kruskal(vertices, edges)
    assert total == 4
    assert len(tree) == 3


def test_kruskal_rejects_disconnected_graph(lesson_module):
    import pytest

    lesson = lesson_module(11)
    with pytest.raises(ValueError, match="연결"):
        lesson.kruskal({"A", "B", "C"}, [("A", "B", 1)])
