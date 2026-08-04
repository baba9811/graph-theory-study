from collections import deque


def bfs(
    graph: dict[str, set[str]], start: str
) -> tuple[dict[str, int], dict[str, str | None]]:
    """시작 정점에서 BFS 거리와 부모를 반환합니다.

    전제: `start`와 모든 이웃은 `graph`의 키입니다.
    예: `bfs({"A": set()}, "A")` → `({"A": 0}, {"A": None})`
    """
    if start not in graph:
        raise ValueError
    distance = {start: 0}
    parents = {start: None}
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for neighbor in sorted(graph[current]):
            if neighbor in distance:
                continue
            distance[neighbor] = distance[current] + 1
            parents[neighbor] = current
            queue.append(neighbor)
    return distance, parents

def reconstruct_path(
    parents: dict[str, str | None], start: str, goal: str
) -> list[str] | None:
    """부모 딕셔너리에서 start부터 goal까지의 경로를 복원합니다.

    전제: `parents`는 BFS가 만든 부모 관계이고 시작점의 부모는 `None`입니다.
    예: `reconstruct_path({"A": None, "B": "A"}, "A", "B")` → `["A", "B"]`
    """
    if goal not in parents:
        return None
    path = [goal]
    current = goal
    while current != start:
        current = parents[current]
        path.append(current)
    path.reverse()
    return path
