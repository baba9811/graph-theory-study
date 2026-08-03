def floyd_warshall(
    vertices: set[str], edges: list[tuple[str, str, float]]
) -> dict[str, dict[str, float]]:
    distances = {
        source: {
            target: 0 if source == target else float("inf")
            for target in vertices
        }
        for source in vertices
    }
    for source, target, weight in edges:
        if source not in vertices or target not in vertices:
            raise ValueError("간선의 끝점이 vertices에 없습니다")
        distances[source][target] = min(distances[source][target], weight)

    for middle in sorted(vertices):
        for source in vertices:
            for target in vertices:
                distances[source][target] = min(
                    distances[source][target],
                    distances[source][middle] + distances[middle][target],
                )

    if any(distances[vertex][vertex] < 0 for vertex in vertices):
        raise ValueError("음수 사이클이 있습니다")
    return distances
