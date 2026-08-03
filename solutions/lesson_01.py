def build_adjacency_list(
    vertices: set[str],
    edges: list[tuple[str, str]],
    directed: bool = False,
) -> dict[str, set[str]]:
    graph = {vertex: set() for vertex in vertices}
    for source, target in edges:
        if source not in graph or target not in graph or source == target:
            raise ValueError("간선의 양 끝점은 서로 다른 기존 정점이어야 합니다")
        graph[source].add(target)
        if not directed:
            graph[target].add(source)
    return graph


def to_adjacency_matrix(
    graph: dict[str, set[str]], order: list[str]
) -> list[list[int]]:
    if len(order) != len(set(order)) or set(order) != set(graph):
        raise ValueError("order에는 모든 정점이 정확히 한 번 있어야 합니다")
    index = {vertex: position for position, vertex in enumerate(order)}
    matrix = [[0] * len(order) for _ in order]
    for source, neighbors in graph.items():
        for target in neighbors:
            if target not in index:
                raise ValueError("인접 정점이 graph에 없습니다")
            matrix[index[source]][index[target]] = 1
    return matrix
