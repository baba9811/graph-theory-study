from exercises.lesson_03 import reconstruct_path
from exercises.lesson_04 import connected_components
from exercises.lesson_08 import dijkstra
from exercises.lesson_11 import kruskal


def analyze_transport_network(
    graph: dict[str, dict[str, float]], start: str, end: str
) -> dict[str, object]:
    """교통망의 연결성·최단 경로·최소 기반 시설 비용을 보고합니다.

    전제: `start`, `end`는 기존 정점이고 가중치는 비음수이며 양방향 값이 같습니다.
    예: `analyze_transport_network({"A": {}}, "A", "A")` → `{"connected": True, "route": ["A"], "distance": 0, "infrastructure_cost": 0.0}`
    """
    if start not in graph or end not in graph:
        raise ValueError("start와 end는 기존 정점이어야 합니다")
    for source, neighbors in graph.items():
        for target, weight in neighbors.items():
            if target not in graph or graph[target].get(source) != weight:
                raise ValueError("교통망은 같은 가중치의 무방향 간선을 사용해야 합니다")
    unweighted = {vertex: set(neighbors) for vertex, neighbors in graph.items()}
    connected = len(connected_components(unweighted)) == 1
    distances, parents = dijkstra(graph, start)
    route = reconstruct_path(parents, start, end)
    infrastructure_cost = None
    if connected:
        # LEARNER_TASK: 양방향 간선을 한 번씩만 남긴 (source, target, weight)
        # 목록을 만들고 kruskal로 infrastructure_cost를 구하세요.
        pass

    # LEARNER_TASK: connected, route, distance, infrastructure_cost를 보고서로 반환하세요.
    raise NotImplementedError("LEARNER_TASK")
