from collections import deque


def bipartite_coloring(graph: dict[str, set[str]]) -> dict[str, int] | None:
    """무방향 단순 그래프의 두 색칠을 반환하고 홀수 사이클이면 None을 반환합니다."""
    if any(neighbor not in graph for neighbors in graph.values() for neighbor in neighbors):
        raise ValueError("인접 정점이 graph에 없습니다")
    if any(
        neighbor == vertex or vertex not in graph[neighbor]
        for vertex, neighbors in graph.items()
        for neighbor in neighbors
    ):
        raise ValueError("무방향 단순 그래프가 필요합니다")
    colors: dict[str, int] = {}
    for start in graph:
        if start in colors:
            continue
        colors[start] = 0
        queue = deque([start])
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in colors:
                    colors[neighbor] = 1 - colors[current]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[current]:
                    return None
    return colors
