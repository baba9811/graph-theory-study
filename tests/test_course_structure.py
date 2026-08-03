from pathlib import Path

import pytest


LESSONS = [
    (1, "graph-foundations"),
    (2, "degree-path-cycle"),
    (3, "breadth-first-search"),
    (4, "depth-first-search"),
    (5, "trees-and-forests"),
    (6, "topological-sort"),
    (7, "strongly-connected-components"),
    (8, "dijkstra-shortest-path"),
    (9, "bellman-ford"),
    (10, "floyd-warshall"),
    (11, "minimum-spanning-tree"),
    (12, "bipartite-graphs"),
    (13, "bipartite-matching"),
    (14, "maximum-flow"),
    (15, "euler-trails"),
    (16, "hamiltonian-paths"),
    (17, "coloring-and-planarity"),
    (18, "transport-network-capstone"),
]


@pytest.mark.parametrize(("number", "slug"), LESSONS)
def test_every_lesson_has_all_learning_artifacts(number, slug):
    paths = [
        Path(f"lessons/{number:02d}-{slug}.md"),
        Path(f"workbook/{number:02d}-{slug}.md"),
        Path(f"exercises/lesson_{number:02d}.py"),
        Path(f"solutions/lesson_{number:02d}.py"),
        Path(f"solutions/{number:02d}-{slug}.md"),
        Path(f"tests/test_lesson_{number:02d}.py"),
    ]
    assert all(path.is_file() and path.stat().st_size > 0 for path in paths)


def test_reference_solutions_contain_no_learner_markers():
    for path in Path("solutions").glob("lesson_*.py"):
        assert "LEARNER_TASK" not in path.read_text(encoding="utf-8")
