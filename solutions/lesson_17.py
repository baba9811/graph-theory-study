def greedy_coloring(graph: dict[str, set[str]]) -> dict[str, int]:
    if any(neighbor not in graph for neighbors in graph.values() for neighbor in neighbors):
        raise ValueError("인접 정점이 graph에 없습니다")
    # ponytail: 탐욕 휴리스틱; 최소 색 수가 필수일 때 정확 탐색으로 교체한다.
    colors = {}
    order = sorted(graph, key=lambda vertex: (-len(graph[vertex]), vertex))
    for vertex in order:
        forbidden = {colors[neighbor] for neighbor in graph[vertex] if neighbor in colors}
        color = 0
        while color in forbidden:
            color += 1
        colors[vertex] = color
    return colors


def within_planar_edge_bound(vertex_count: int, edge_count: int) -> bool:
    if vertex_count < 0 or edge_count < 0:
        raise ValueError("정점 수와 간선 수는 음수일 수 없습니다")
    if vertex_count < 3:
        return edge_count <= vertex_count * (vertex_count - 1) // 2
    return edge_count <= 3 * vertex_count - 6
