from pathlib import Path

import pytest


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


def test_documented_trace_backtracks_before_finding_path(lesson_module):
    lesson = lesson_module(16)
    graph = {"A": {"B", "C"}, "B": {"D"}, "C": {"B"}, "D": set()}
    assert lesson.hamiltonian_path(graph) == ["A", "C", "B", "D"]

    workbook = Path("workbook/16-hamiltonian-paths.md").read_text(encoding="utf-8")
    solution = Path("solutions/16-hamiltonian-paths.md").read_text(encoding="utf-8")
    assert "`A: {B, C}, B: {D}, C: {B}, D: {}`" in workbook
    assert "`A → B → D`" in solution
    assert "`A → C → B → D`" in solution


@pytest.mark.parametrize(
    "graph",
    [
        {"A": {"X"}},
        {"A": {"B"}, "B": {"X"}},
    ],
)
def test_rejects_unknown_neighbors_before_accepting_complete_path(lesson_module, graph):
    lesson = lesson_module(16)
    with pytest.raises(ValueError, match="인접 정점이 graph에 없습니다"):
        lesson.hamiltonian_path(graph)
