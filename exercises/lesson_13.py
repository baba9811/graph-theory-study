def maximum_bipartite_matching(
    graph: dict[str, set[str]], left: set[str]
) -> dict[str, str]:
    """증강 경로로 최대 이분 매칭을 구합니다.

    전제: 모든 `left` 정점은 키이고 그 이웃은 왼쪽 파티션에 속하지 않습니다.
    예: `maximum_bipartite_matching({"A": {"1"}}, {"A"})` → `{"A": "1"}`
    """
    if any(vertex not in graph for vertex in left):
        raise ValueError("모든 왼쪽 정점은 graph의 키여야 합니다")
    if any(neighbor in left for vertex in left for neighbor in graph[vertex]):
        raise ValueError("왼쪽과 오른쪽 파티션이 겹칩니다")
    matched_right: dict[str, str] = {}

    def augment(left_vertex: str, seen: set[str]) -> bool:
        for right_vertex in sorted(graph[left_vertex]):
            if right_vertex in seen:
                continue
            seen.add(right_vertex)
            # LEARNER_TASK: 비어 있는 오른쪽 정점에는 연결하고, 이미 매칭되었다면
            # LEARNER_TASK: 그 왼쪽 정점을 재귀적으로 옮길 수 있을 때 재배정하세요.
            pass
        return False

    for left_vertex in sorted(left):
        augment(left_vertex, set())
    return {left_vertex: right_vertex for right_vertex, left_vertex in matched_right.items()}
