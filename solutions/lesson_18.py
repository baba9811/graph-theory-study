from solutions.lesson_03 import reconstruct_path
from solutions.lesson_04 import connected_components
from solutions.lesson_08 import dijkstra
from solutions.lesson_11 import kruskal


def analyze_transport_network(
    graph: dict[str, dict[str, float]], start: str, end: str
) -> dict[str, object]:
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
        edges = [
            (source, target, weight)
            for source, neighbors in graph.items()
            for target, weight in neighbors.items()
            if source < target
        ]
        infrastructure_cost, _ = kruskal(set(graph), edges)
    return {
        "connected": connected,
        "route": route,
        "distance": distances[end],
        "infrastructure_cost": infrastructure_cost,
    }
