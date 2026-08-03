def test_topological_order_respects_every_edge(lesson_module):
    lesson = lesson_module(6)
    graph = {
        "intro": {"bfs", "dfs"},
        "bfs": {"flow"},
        "dfs": {"flow"},
        "flow": set(),
    }
    order = lesson.topological_sort(graph)
    position = {vertex: index for index, vertex in enumerate(order)}
    assert set(order) == set(graph)
    assert all(position[u] < position[v] for u in graph for v in graph[u])


def test_uses_stable_lexicographic_choice(lesson_module):
    lesson = lesson_module(6)
    assert lesson.topological_sort({"B": set(), "A": set()}) == ["A", "B"]


def test_rejects_cycle(lesson_module):
    import pytest

    lesson = lesson_module(6)
    with pytest.raises(ValueError, match="사이클"):
        lesson.topological_sort({"A": {"B"}, "B": {"A"}})


def test_lesson_distinguishes_cycle_from_downstream_vertices():
    from pathlib import Path

    lesson_text = Path("lessons/06-topological-sort.md").read_text()
    assert "방향 사이클이 존재함을 뜻합니다" in lesson_text
    assert "사이클에 의존하는 정점도 포함할 수 있습니다" in lesson_text
    assert "그 정점들은 방향 사이클에 묶여 있습니다" not in lesson_text
