from collections import deque


def edmonds_karp(
    capacity: dict[str, dict[str, int]], source: str, sink: str
) -> tuple[int, set[str]]:
    if any(neighbor not in capacity for neighbors in capacity.values() for neighbor in neighbors):
        raise ValueError("모든 정점은 capacity의 키여야 합니다")
    vertices = set(capacity)
    if source not in vertices or sink not in vertices or source == sink:
        raise ValueError("서로 다른 기존 source와 sink가 필요합니다")
    residual = {left: {right: 0 for right in vertices} for left in vertices}
    adjacency = {vertex: set() for vertex in vertices}
    for left, neighbors in capacity.items():
        for right, amount in neighbors.items():
            if amount < 0:
                raise ValueError("용량은 음수일 수 없습니다")
            residual[left][right] += amount
            adjacency[left].add(right)
            adjacency[right].add(left)

    total = 0
    # LEARNER_TASK: adjacency를 따라 잔여 용량이 양수인 s-t 경로를 BFS로 찾으세요.
    # LEARNER_TASK: 병목값만큼 정방향 잔여 용량을 줄이고 역방향은 늘리세요.

    reachable = {source}
    queue = deque([source])
    while queue:
        current = queue.popleft()
        for neighbor in adjacency[current]:
            remaining = residual[current][neighbor]
            if remaining > 0 and neighbor not in reachable:
                reachable.add(neighbor)
                queue.append(neighbor)
    return total, reachable
