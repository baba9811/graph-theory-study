import heapq


def dijkstra(
    graph: dict[str, dict[str, float]], start: str
) -> tuple[dict[str, float], dict[str, str | None]]:
    if start not in graph:
        raise ValueError("시작 정점이 graph에 없습니다")
    for neighbors in graph.values():
        for neighbor, weight in neighbors.items():
            if neighbor not in graph:
                raise ValueError("모든 정점은 graph의 키여야 합니다")
            if weight < 0:
                raise ValueError("다익스트라는 음수 가중치를 허용하지 않습니다")

    distances = {vertex: float("inf") for vertex in graph}
    parents = {vertex: None for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        distance, current = heapq.heappop(queue)
        if distance != distances[current]:
            continue
        for neighbor, weight in graph[current].items():
            candidate = distance + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                parents[neighbor] = current
                heapq.heappush(queue, (candidate, neighbor))
    return distances, parents
