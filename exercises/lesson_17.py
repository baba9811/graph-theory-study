def greedy_coloring(graph: dict[str, set[str]]) -> dict[str, int]:
    """무방향 단순 그래프에 결정적인 탐욕 색칠을 만듭니다.

    전제: 입력은 대칭이고 자기 루프가 없는 무방향 단순 그래프입니다.
    예: `greedy_coloring({"A": set()})` → `{"A": 0}`
    """
    if any(neighbor not in graph for neighbors in graph.values() for neighbor in neighbors):
        raise ValueError("인접 정점이 graph에 없습니다")
    if any(
        neighbor == vertex or vertex not in graph[neighbor]
        for vertex, neighbors in graph.items()
        for neighbor in neighbors
    ):
        raise ValueError("무방향 단순 그래프가 필요합니다")
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
    """단순 그래프의 정점·간선 수가 평면 간선 상한 안인지 확인합니다.

    전제: 두 개수는 음이 아닌 정수이며 결과는 평면성의 필요조건일 뿐입니다.
    예: `within_planar_edge_bound(4, 6)` → `True`
    """
    # LEARNER_TASK: 정점 수나 간선 수가 음수이면 ValueError를 발생시키세요.
    # LEARNER_TASK: 정점이 3개보다 적은 단순 그래프의 최대 간선 수를 검사하세요.
    # LEARNER_TASK: 그 밖에는 필요한 평면 간선 상한 |E| <= 3|V| - 6을 검사하세요.
    return False
