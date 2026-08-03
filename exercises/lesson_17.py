def greedy_coloring(graph: dict[str, set[str]]) -> dict[str, int]:
    if any(neighbor not in graph for neighbors in graph.values() for neighbor in neighbors):
        raise ValueError("인접 정점이 graph에 없습니다")
    # ponytail: 탐욕 휴리스틱; 최소 색 수가 필수일 때 정확 탐색으로 교체한다.
    colors = {}
    order = sorted(graph, key=lambda vertex: (-len(graph[vertex]), vertex))
    for vertex in order:
        # LEARNER_TASK: 이미 색칠된 이웃의 색을 forbidden에 모으세요.
        forbidden = set()
        color = 0
        # LEARNER_TASK: forbidden에 없는 가장 작은 음이 아닌 색을 고르세요.
        colors[vertex] = color
    return colors


def within_planar_edge_bound(vertex_count: int, edge_count: int) -> bool:
    # LEARNER_TASK: 정점 수나 간선 수가 음수이면 ValueError를 발생시키세요.
    # LEARNER_TASK: 정점이 3개보다 적은 단순 그래프의 최대 간선 수를 검사하세요.
    # LEARNER_TASK: 그 밖에는 필요한 평면 간선 상한 |E| <= 3|V| - 6을 검사하세요.
    return False
