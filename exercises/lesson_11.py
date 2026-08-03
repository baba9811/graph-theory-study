class DisjointSet:
    def __init__(self, vertices: set[str]) -> None:
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex: str) -> str:
        # LEARNER_TASK: 부모를 재귀적으로 찾아 대표를 반환하고, 지나간 정점의 부모를 대표로 바꾸세요.
        raise NotImplementedError

    def union(self, left: str, right: str) -> bool:
        # LEARNER_TASK: 두 대표가 같으면 False를, 다르면 rank가 큰 쪽에 합친 뒤 True를 반환하세요.
        raise NotImplementedError


def kruskal(
    vertices: set[str], edges: list[tuple[str, str, float]]
) -> tuple[float, list[tuple[str, str, float]]]:
    if not vertices:
        raise ValueError("빈 그래프에는 최소 신장 트리가 없습니다")
    if any(source not in vertices or target not in vertices for source, target, _ in edges):
        raise ValueError("간선의 끝점이 vertices에 없습니다")

    # LEARNER_TASK: 가중치순 간선을 훑으며 서로 다른 집합만 합쳐 |V|-1개를 고르세요.

    # LEARNER_TASK: 간선이 |V|-1개보다 적으면 ValueError("연결 그래프가 아닙니다")를 내세요.

    raise NotImplementedError
