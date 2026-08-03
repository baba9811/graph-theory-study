from collections import deque


def bipartite_coloring(graph: dict[str, set[str]]) -> dict[str, int] | None:
    """무방향 그래프의 두 색칠을 구하거나 불가능하면 None을 반환합니다.

    전제: 입력은 대칭이고 자기 루프가 없는 무방향 단순 그래프입니다.
    예: `bipartite_coloring({"A": set()})` → `{"A": 0}`
    """
    if any(neighbor not in graph for neighbors in graph.values() for neighbor in neighbors):
        raise ValueError("인접 정점이 graph에 없습니다")
    if any(
        neighbor == vertex or vertex not in graph[neighbor]
        for vertex, neighbors in graph.items()
        for neighbor in neighbors
    ):
        raise ValueError("무방향 단순 그래프가 필요합니다")
    colors: dict[str, int] = {}
    for start in graph:
        # LEARNER_TASK: 색칠된 시작점은 건너뛰고, 새 시작점에 0을 칠해 deque에 넣으세요.
        if start in colors:
            continue
        queue = deque()
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                # LEARNER_TASK: 이웃의 색을 검사해 반대색을 전파하거나 같은 색 충돌에 None을 반환하세요.
                pass
    return colors
