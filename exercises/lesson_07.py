def strongly_connected_components(graph: dict[str, set[str]]) -> list[set[str]]:
    """방향 그래프를 강한 연결 요소들로 나눕니다.

    전제: 모든 이웃은 `graph`의 키입니다.
    예: `strongly_connected_components({"A": set()})` → `[{"A"}]`
    """
    if any(neighbor not in graph for neighbors in graph.values() for neighbor in neighbors):
        raise ValueError("모든 정점은 graph의 키여야 합니다")

    visited = set()
    finish_order = []

    def visit(vertex):
        # LEARNER_TASK: DFS를 마칠 때 정점을 finish_order에 추가하세요.
        pass

    for vertex in graph:
        if vertex not in visited:
            visit(vertex)

    reversed_graph = {vertex: set() for vertex in graph}
    for source, neighbors in graph.items():
        for target in neighbors:
            reversed_graph[target].add(source)

    visited.clear()
    components = []

    def collect(vertex, component):
        # LEARNER_TASK: 전치 그래프에서 DFS하며 component를 채우세요.
        pass

    # LEARNER_TASK: finish_order의 역순으로 아직 방문하지 않은 정점에서 collect를 시작하세요.
    return components
