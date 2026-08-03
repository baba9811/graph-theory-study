from collections import deque


def bipartite_coloring(graph: dict[str, set[str]]) -> dict[str, int] | None:
    """Return a two-coloring, or None if an odd cycle prevents one."""
    colors: dict[str, int] = {}
    for start in graph:
        if start in colors:
            continue
        colors[start] = 0
        queue = deque([start])
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in graph:
                    raise ValueError("인접 정점이 graph에 없습니다")
                if neighbor not in colors:
                    colors[neighbor] = 1 - colors[current]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[current]:
                    return None
    return colors
