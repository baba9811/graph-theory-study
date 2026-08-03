def eulerian_trail(edges: list[tuple[str, str]]) -> list[str] | None:
    """무방향 다중 그래프의 오일러 트레일을 구합니다.

    전제: 각 튜플은 무방향 간선 하나이며 평행 간선은 별개로 유지됩니다.
    예: `eulerian_trail([])` → `[]`
    """
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

    # LEARNER_TASK: start에서 도달 가능한 정점을 찾아 모든 비영차 정점이 연결됐는지 확인하세요.
    # 연결되지 않았다면 None을 반환하세요.

    used: set[int] = set()
    stack = [start]
    trail: list[str] = []
    # LEARNER_TASK: 아직 쓰지 않은 간선을 따라 stack을 확장하고, 막다른 정점은 trail에
    # 옮기는 Hierholzer 순회를 구현하세요. 같은 edge_id의 반대쪽 항목도 건너뛰어야 합니다.
    return None
