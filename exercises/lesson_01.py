def build_adjacency_list(
    vertices: set[str],
    edges: list[tuple[str, str]],
    directed: bool = False,
) -> dict[str, set[str]]:
    """정점과 간선으로 인접 리스트를 만듭니다.

    >>> build_adjacency_list({"A", "B"}, [("A", "B")])
    {'A': {'B'}, 'B': {'A'}}
    """
    raise NotImplementedError("LEARNER_TASK")


def to_adjacency_matrix(
    graph: dict[str, set[str]], order: list[str]
) -> list[list[int]]:
    """인접 리스트를 주어진 정점 순서의 인접 행렬로 바꿉니다.

    >>> to_adjacency_matrix({"A": {"B"}, "B": {"A"}}, ["A", "B"])
    [[0, 1], [1, 0]]
    """
    raise NotImplementedError("LEARNER_TASK")
