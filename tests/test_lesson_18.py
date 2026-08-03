import pytest


def test_combines_connectivity_route_and_infrastructure_cost(lesson_module):
    lesson = lesson_module(18)
    graph = {
        "A": {"B": 1, "C": 5},
        "B": {"A": 1, "C": 2},
        "C": {"A": 5, "B": 2},
    }
    report = lesson.analyze_transport_network(graph, "A", "C")
    assert report == {
        "connected": True,
        "route": ["A", "B", "C"],
        "distance": 3,
        "infrastructure_cost": 3,
    }


def test_reports_disconnected_destination(lesson_module):
    lesson = lesson_module(18)
    graph = {"A": {"B": 1}, "B": {"A": 1}, "C": {}}
    report = lesson.analyze_transport_network(graph, "A", "C")
    assert not report["connected"]
    assert report["route"] is None
    assert report["distance"] == float("inf")
    assert report["infrastructure_cost"] is None


def test_reports_disconnected_graph_when_destination_is_reachable(lesson_module):
    lesson = lesson_module(18)
    graph = {
        "A": {"B": 2},
        "B": {"A": 2},
        "C": {"D": 3},
        "D": {"C": 3},
    }
    report = lesson.analyze_transport_network(graph, "A", "B")
    assert report == {
        "connected": False,
        "route": ["A", "B"],
        "distance": 2,
        "infrastructure_cost": None,
    }


def test_rejects_asymmetric_transport_edge(lesson_module):
    lesson = lesson_module(18)
    with pytest.raises(ValueError, match="무방향"):
        lesson.analyze_transport_network({"A": {"B": 1}, "B": {}}, "A", "B")


def test_rejects_missing_start(lesson_module):
    lesson = lesson_module(18)
    with pytest.raises(ValueError, match="start와 end는 기존 정점"):
        lesson.analyze_transport_network({"A": {}, "B": {}}, "X", "B")


def test_rejects_missing_end(lesson_module):
    lesson = lesson_module(18)
    with pytest.raises(ValueError, match="start와 end는 기존 정점"):
        lesson.analyze_transport_network({"A": {}, "B": {}}, "A", "X")


def test_rejects_unknown_target_vertex(lesson_module):
    lesson = lesson_module(18)
    with pytest.raises(ValueError, match="무방향"):
        lesson.analyze_transport_network({"A": {"X": 1}}, "A", "A")


def test_rejects_mismatched_reverse_weight(lesson_module):
    lesson = lesson_module(18)
    graph = {"A": {"B": 1}, "B": {"A": 2}}
    with pytest.raises(ValueError, match="무방향"):
        lesson.analyze_transport_network(graph, "A", "B")


def test_rejects_negative_weight(lesson_module):
    lesson = lesson_module(18)
    graph = {"A": {"B": -1}, "B": {"A": -1}}
    with pytest.raises(ValueError, match="음수 가중치"):
        lesson.analyze_transport_network(graph, "A", "B")
