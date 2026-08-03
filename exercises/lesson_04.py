def connected_components(graph: dict[str, set[str]]) -> list[set[str]]:
    """무방향 그래프를 DFS 연결 요소들로 나눕니다.

    전제: 모든 이웃은 `graph`의 키이고 간선 표현은 양방향입니다.
    예: `connected_components({"A": set()})` → `[{"A"}]`
    """
    raise NotImplementedError("LEARNER_TASK")


def has_cycle(graph: dict[str, set[str]]) -> bool:
    """무방향 그래프에 사이클이 있는지 판별합니다.

    전제: 모든 이웃은 `graph`의 키이고 간선 표현은 양방향입니다.
    예: `has_cycle({"A": {"B"}, "B": {"A"}})` → `False`
    """
    raise NotImplementedError("LEARNER_TASK")
