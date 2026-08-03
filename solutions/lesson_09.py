def bellman_ford(
    vertices: set[str],
    edges: list[tuple[str, str, float]],
    start: str,
) -> tuple[dict[str, float], dict[str, str | None]]:
    if start not in vertices:
        raise ValueError("시작 정점이 vertices에 없습니다")
    if any(source not in vertices or target not in vertices for source, target, _ in edges):
        raise ValueError("간선의 끝점이 vertices에 없습니다")

    distances = {vertex: float("inf") for vertex in vertices}
    parents = {vertex: None for vertex in vertices}
    distances[start] = 0

    for _ in range(len(vertices) - 1):
        changed = False
        for source, target, weight in edges:
            candidate = distances[source] + weight
            if distances[source] != float("inf") and candidate < distances[target]:
                distances[target] = candidate
                parents[target] = source
                changed = True
        if not changed:
            break

    for source, target, weight in edges:
        if distances[source] != float("inf") and distances[source] + weight < distances[target]:
            raise ValueError("시작점에서 도달 가능한 음수 사이클이 있습니다")
    return distances, parents
