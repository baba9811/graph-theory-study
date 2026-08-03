def eulerian_trail(edges: list[tuple[str, str]]) -> list[str] | None:
    if not edges:
        return []
    adjacency: dict[str, list[tuple[str, int]]] = {}
    for edge_id, (left, right) in enumerate(edges):
        adjacency.setdefault(left, []).append((right, edge_id))
        adjacency.setdefault(right, []).append((left, edge_id))
    odd = [vertex for vertex, neighbors in adjacency.items() if len(neighbors) % 2]
    if len(odd) not in (0, 2):
        return None
    start = min(odd) if odd else min(adjacency)
    reached = set()
    stack = [start]
    while stack:
        current = stack.pop()
        if current in reached:
            continue
        reached.add(current)
        stack.extend(neighbor for neighbor, _ in adjacency[current])
    if reached != set(adjacency):
        return None
    used = set()
    stack = [start]
    trail = []
    while stack:
        current = stack[-1]
        while adjacency[current] and adjacency[current][-1][1] in used:
            adjacency[current].pop()
        if not adjacency[current]:
            trail.append(stack.pop())
            continue
        neighbor, edge_id = adjacency[current].pop()
        used.add(edge_id)
        stack.append(neighbor)
    trail.reverse()
    return trail if len(used) == len(edges) else None
