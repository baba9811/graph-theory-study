def connected_components(graph: dict[str, set[str]]) -> list[set[str]]:
    visited = set()
    components = []
    for start in sorted(graph):
        if start in visited:
            continue
        component = set()
        stack = [start]
        visited.add(start)
        while stack:
            current = stack.pop()
            component.add(current)
            for neighbor in graph[current]:
                if neighbor not in graph:
                    raise ValueError("인접 정점이 graph에 없습니다")
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        components.append(component)
    return components


def has_cycle(graph: dict[str, set[str]]) -> bool:
    if any(neighbor not in graph for neighbors in graph.values() for neighbor in neighbors):
        raise ValueError("인접 정점이 graph에 없습니다")
    visited = set()
    for start in graph:
        if start in visited:
            continue
        visited.add(start)
        stack = [(start, None)]
        while stack:
            current, parent = stack.pop()
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, current))
                elif neighbor != parent:
                    return True
    return False
