def connected_components(graph: dict[str, set[str]]) -> list[set[str]]:
    """무방향 그래프를 DFS 연결 요소들로 나눕니다.

    전제: 모든 이웃은 `graph`의 키이고 간선 표현은 양방향입니다.
    예: `connected_components({"A": set()})` → `[{"A"}]`
    """
    visited = set()
    results = []
    for start in graph:
        if start in visited:
            continue
        component = set()
        stack = [start]
        visited.add(start)
        while stack:
            current = stack.pop()
            component.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        results.append(component)
    return results

def has_cycle(graph: dict[str, set[str]]) -> bool:
    """무방향 그래프에 사이클이 있는지 판별합니다.

    전제: 모든 이웃은 `graph`의 키이고 간선 표현은 양방향입니다.
    예: `has_cycle({"A": {"B"}, "B": {"A"}})` → `False`
    """
    visited = set()
    for start in graph:
        if start in visited:
            continue
        visited.add(start)
        stack=[(start, None)]
        while stack:
            current, parent = stack.pop()
            for neighbor in graph[current]:
                if neighbor == parent:
                    continue
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, current))
                    continue
                return True
    return False
