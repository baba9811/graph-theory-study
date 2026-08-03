from collections import deque


def edmonds_karp(
    capacity: dict[str, dict[str, int]], source: str, sink: str
) -> tuple[int, set[str]]:
    if any(neighbor not in capacity for neighbors in capacity.values() for neighbor in neighbors):
        raise ValueError("모든 정점은 capacity의 키여야 합니다")
    vertices = set(capacity)
    if source not in vertices or sink not in vertices or source == sink:
        raise ValueError("서로 다른 기존 source와 sink가 필요합니다")
    # ponytail: O(|V|²) 잔여 행렬; 메모리가 문제일 때 희소 dict로 교체한다.
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
    while True:
        parents = {source: None}
        queue = deque([source])
        while queue and sink not in parents:
            current = queue.popleft()
            for neighbor in adjacency[current]:
                remaining = residual[current][neighbor]
                if remaining > 0 and neighbor not in parents:
                    parents[neighbor] = current
                    queue.append(neighbor)
        if sink not in parents:
            break
        amount = float("inf")
        current = sink
        while current != source:
            previous = parents[current]
            amount = min(amount, residual[previous][current])
            current = previous
        current = sink
        while current != source:
            previous = parents[current]
            residual[previous][current] -= amount
            residual[current][previous] += amount
            current = previous
        total += amount
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
