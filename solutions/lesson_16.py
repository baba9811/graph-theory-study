def hamiltonian_path(graph: dict[str, set[str]]) -> list[str] | None:
    if not graph:
        return []

    # ponytail: 최악 O(|V|!); 중간 크기 입력이 필요하면 부분집합 DP를 사용한다.
    def extend(path, used):
        if len(path) == len(graph):
            return path.copy()
        for neighbor in sorted(graph[path[-1]]):
            if neighbor not in graph:
                raise ValueError("인접 정점이 graph에 없습니다")
            if neighbor not in used:
                used.add(neighbor)
                path.append(neighbor)
                result = extend(path, used)
                if result is not None:
                    return result
                path.pop()
                used.remove(neighbor)
        return None

    for start in sorted(graph):
        result = extend([start], {start})
        if result is not None:
            return result
    return None
