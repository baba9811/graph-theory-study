import heapq


def dijkstra(
    graph: dict[str, dict[str, float]], start: str
) -> tuple[dict[str, float], dict[str, str | None]]:
    """start에서 각 정점까지의 최단 거리와 직전 정점을 반환합니다."""
    # LEARNER_TASK: start가 graph에 있고, 모든 이웃이 graph의 키이며,
    # LEARNER_TASK: 모든 가중치가 0 이상인지 검사하고 아니면 ValueError를 발생시키세요.
    # LEARNER_TASK: distances, parents, 그리고 (0, start)를 담은 heap을 초기화하세요.
    # LEARNER_TASK: heap에서 최신 항목을 꺼내고, 이웃을 완화해 더 짧은 후보를 다시 넣으세요.
    raise NotImplementedError("LEARNER_TASK")
