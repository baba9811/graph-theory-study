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


def test_rejects_asymmetric_transport_edge(lesson_module):
    import pytest

    lesson = lesson_module(18)
    with pytest.raises(ValueError, match="무방향"):
        lesson.analyze_transport_network({"A": {"B": 1}, "B": {}}, "A", "B")
