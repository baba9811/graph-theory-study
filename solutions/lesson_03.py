from collections import deque


def bfs(
    graph: dict[str, set[str]], start: str
) -> tuple[dict[str, int], dict[str, str | None]]:
    if start not in graph:
        raise ValueError("시작 정점이 graph에 없습니다")
    distances = {start: 0}
    parents = {start: None}
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for neighbor in sorted(graph[current]):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                parents[neighbor] = current
                queue.append(neighbor)
    return distances, parents


def reconstruct_path(
    parents: dict[str, str | None], start: str, goal: str
) -> list[str] | None:
    if start not in parents or goal not in parents:
        return None
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()
    return path if path and path[0] == start else None
