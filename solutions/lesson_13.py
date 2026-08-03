def maximum_bipartite_matching(
    graph: dict[str, set[str]], left: set[str]
) -> dict[str, str]:
    if any(vertex not in graph for vertex in left):
        raise ValueError("모든 왼쪽 정점은 graph의 키여야 합니다")
    if any(neighbor in left for vertex in left for neighbor in graph[vertex]):
        raise ValueError("왼쪽과 오른쪽 파티션이 겹칩니다")
    # ponytail: O(|L||E|); 큰 희소 그래프가 필요하면 Hopcroft–Karp로 교체한다.
    matched_right: dict[str, str] = {}

    def augment(left_vertex: str, seen: set[str]) -> bool:
        for right_vertex in sorted(graph[left_vertex]):
            if right_vertex in seen:
                continue
            seen.add(right_vertex)
            if right_vertex not in matched_right or augment(matched_right[right_vertex], seen):
                matched_right[right_vertex] = left_vertex
                return True
        return False

    for left_vertex in sorted(left):
        augment(left_vertex, set())
    return {left_vertex: right_vertex for right_vertex, left_vertex in matched_right.items()}
