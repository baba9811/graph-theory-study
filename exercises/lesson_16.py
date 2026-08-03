def hamiltonian_path(graph: dict[str, set[str]]) -> list[str] | None:
    for neighbors in graph.values():
        for neighbor in neighbors:
            if neighbor not in graph:
                raise ValueError("인접 정점이 graph에 없습니다")
    if not graph:
        return []

    # ponytail: 최악 O(|V|!); 중간 크기 입력이 필요하면 부분집합 DP를 사용한다.
    def extend(path, used):
        if len(path) == len(graph):
            return path.copy()
        for neighbor in sorted(graph[path[-1]]):
            if neighbor not in used:
                # LEARNER_TASK: neighbor를 used와 path에 추가해 후보를 선택하세요.
                result = extend(path, used)
                if result is not None:
                    return result
                # LEARNER_TASK: 재귀 호출이 실패하면 path와 used에서 neighbor를 제거해 선택을 되돌리세요.
        return None

    for start in sorted(graph):
        result = extend([start], {start})
        if result is not None:
            return result
    return None
