from collections import deque


def bipartite_coloring(graph: dict[str, set[str]]) -> dict[str, int] | None:
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
