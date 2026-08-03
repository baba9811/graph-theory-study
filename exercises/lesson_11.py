class DisjointSet:
    """서로 겹치지 않는 정점 집합들의 합치기 상태를 관리합니다.

    전제: 초기 정점들은 서로 다른 원소입니다.
    예: `DisjointSet({"A"}).find("A")` → `"A"`
    """

    def __init__(self, vertices: set[str]) -> None:
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex: str) -> str:
        """vertex가 속한 집합의 대표를 반환합니다.

        전제: `vertex`는 생성할 때 준 정점 집합에 속합니다.
        예: `DisjointSet({"A"}).find("A")` → `"A"`
        """
        # LEARNER_TASK: 부모를 재귀적으로 찾아 대표를 반환하고, 지나간 정점의 부모를 대표로 바꾸세요.
        raise NotImplementedError

    def union(self, left: str, right: str) -> bool:
        """두 정점의 집합을 합치고 실제 병합 여부를 반환합니다.

        전제: `left`, `right`는 생성할 때 준 정점 집합에 속합니다.
        예: 새 `DisjointSet({"A", "B"}).union("A", "B")` → `True`
        """
        # LEARNER_TASK: 두 대표가 같으면 False를, 다르면 rank가 큰 쪽에 합친 뒤 True를 반환하세요.
        raise NotImplementedError


def kruskal(
    vertices: set[str], edges: list[tuple[str, str, float]]
) -> tuple[float, list[tuple[str, str, float]]]:
    """연결 무방향 가중 그래프의 최소 신장 트리를 구합니다.

    전제: `vertices`는 비어 있지 않고 모든 간선 끝점이 그 집합에 있으며 그래프가 연결됩니다.
    예: `kruskal({"A"}, [])` → `(0, [])`
    """
    if not vertices:
        raise ValueError("빈 그래프에는 최소 신장 트리가 없습니다")
    if any(source not in vertices or target not in vertices for source, target, _ in edges):
        raise ValueError("간선의 끝점이 vertices에 없습니다")

    # LEARNER_TASK: 가중치순 간선을 훑으며 서로 다른 집합만 합쳐 |V|-1개를 고르세요.

    # LEARNER_TASK: 간선이 |V|-1개보다 적으면 ValueError("연결 그래프가 아닙니다")를 내세요.

    raise NotImplementedError
