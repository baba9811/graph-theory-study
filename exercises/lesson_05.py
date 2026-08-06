from exercises.lesson_04 import connected_components


def is_tree(graph: dict[str, set[str]]) -> bool:
    """주어진 그래프가 트리인지 판별합니다.

    전제: 유효한 입력은 대칭인 무방향 단순 인접 리스트입니다.
    예: `is_tree({"A": set()})` → `True`
    """
    if graph == {}:
        return False
    for v in graph:
        if v in graph[v]:
            return False
        for neighbor in graph[v]:
            if neighbor not in graph or v not in graph[neighbor]:
                return False
    if len(connected_components(graph)) != 1:
        return False
    edge_count = 0
    for g in graph.values():
        edge_count += len(g)
    edge_count = edge_count // 2
    return edge_count == len(graph) - 1
