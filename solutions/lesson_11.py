class DisjointSet:
    def __init__(self, vertices: set[str]) -> None:
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex: str) -> str:
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, left: str, right: str) -> bool:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root == right_root:
            return False
        if self.rank[left_root] < self.rank[right_root]:
            left_root, right_root = right_root, left_root
        self.parent[right_root] = left_root
        if self.rank[left_root] == self.rank[right_root]:
            self.rank[left_root] += 1
        return True


def kruskal(
    vertices: set[str], edges: list[tuple[str, str, float]]
) -> tuple[float, list[tuple[str, str, float]]]:
    if not vertices:
        raise ValueError("빈 그래프에는 최소 신장 트리가 없습니다")
    if any(source not in vertices or target not in vertices for source, target, _ in edges):
        raise ValueError("간선의 끝점이 vertices에 없습니다")

    groups = DisjointSet(vertices)
    tree = []
    total = 0.0
    for source, target, weight in sorted(edges, key=lambda edge: edge[2]):
        if groups.union(source, target):
            tree.append((source, target, weight))
            total += weight
            if len(tree) == len(vertices) - 1:
                break

    if len(tree) != len(vertices) - 1:
        raise ValueError("연결 그래프가 아닙니다")
    return total, tree
