from math import inf
import heapq


def dijkstra(
    graph: dict[str, dict[str, float]], start: str
) -> tuple[dict[str, float], dict[str, str | None]]:
    """start에서 각 정점까지의 최단 거리와 부모를 구합니다.

    전제: 시작점과 모든 이웃은 키이고 모든 가중치는 0 이상입니다.
    예: `dijkstra({"A": {}}, "A")` → `({"A": 0}, {"A": None})`
    """
    if start not in graph:
        raise ValueError
    for neighbors in graph.values():
        for neighbor, weight in neighbors.items():
            if neighbor not in graph:
                raise ValueError
            if weight < 0:
                raise ValueError("음수")

    distances = {}
    parents = {}
    for vertex in graph:
        if vertex == start:
            distances[vertex] = 0
        else:
            distances[vertex] = inf
        parents[vertex] = None
    heap = [(0, start)]
    while heap:
        distance, current = heapq.heappop(heap)
        if distance != distances[current]:
            continue
        for neighbor, weight in graph[current].items():
            candidate = distance + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                parents[neighbor] = current
                heapq.heappush(heap, (candidate, neighbor))
    return distances, parents
