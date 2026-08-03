def floyd_warshall(
    vertices: set[str], edges: list[tuple[str, str, float]]
) -> dict[str, dict[str, float]]:
    """모든 정점 쌍의 최단 거리 표를 구합니다.

    전제: 모든 간선 끝점은 `vertices`에 있고 음수 사이클은 없습니다.
    예: `floyd_warshall({"A"}, [])` → `{"A": {"A": 0}}`
    """
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

    # LEARNER_TASK: middle을 하나씩 허용하며 모든 source, target 쌍을 완화하세요.

    # LEARNER_TASK: 대각선 값이 음수이면 ValueError("음수 사이클이 있습니다")를 내세요.

    return distances
