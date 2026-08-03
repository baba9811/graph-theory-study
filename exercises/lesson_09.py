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

    # LEARNER_TASK: 모든 간선을 |V|-1번 완화하고, 더 이상 갱신이 없으면 멈추세요.

    # LEARNER_TASK: 한 번 더 완화 가능한, 시작점에서 도달 가능한 간선이 있으면 ValueError를 내세요.

    return distances, parents
