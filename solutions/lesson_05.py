from solutions.lesson_04 import connected_components


def is_tree(graph: dict[str, set[str]]) -> bool:
    """무방향 그래프가 트리이면 True를 반환합니다."""
    if not graph:
        return False
    if any(
        neighbor not in graph or vertex not in graph[neighbor]
        for vertex, neighbors in graph.items()
        for neighbor in neighbors
    ):
        return False
    edge_count = sum(len(neighbors) for neighbors in graph.values()) // 2
    return len(connected_components(graph)) == 1 and edge_count == len(graph) - 1
