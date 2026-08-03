def build_adjacency_list(
    vertices: set[str],
    edges: list[tuple[str, str]],
    directed: bool = False,
) -> dict[str, set[str]]:
    """정점과 간선으로 인접 리스트를 만듭니다.

    전제: 모든 간선 끝점은 `vertices`에 있고 자기 루프는 없습니다.
    예: `build_adjacency_list({"A", "B"}, [("A", "B")])` → `{"A": {"B"}, "B": {"A"}}`
    """
    adjacency_list = {vertex: set() for vertex in vertices}
    for u, v in edges:
        if u not in vertices or v not in vertices:
            raise ValueError("unknown endpoint")
        adjacency_list[u].add(v)
        if not directed:
            adjacency_list[v].add(u)
    return adjacency_list


def to_adjacency_matrix(
    graph: dict[str, set[str]], order: list[str]
) -> list[list[int]]:
    """인접 리스트를 주어진 정점 순서의 인접 행렬로 바꿉니다.

    전제: `order`에는 `graph`의 모든 정점이 정확히 한 번 나옵니다.
    예: `to_adjacency_matrix({"A": {"B"}, "B": {"A"}}, ["A", "B"])` → `[[0, 1], [1, 0]]`
    """
    matrix = []
    for u in order:
        row = []
        for v in order:
            row.append(1 if v in graph[u] else 0)
        matrix.append(row)
    return matrix
