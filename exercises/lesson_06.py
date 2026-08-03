import heapq


def topological_sort(graph: dict[str, set[str]]) -> list[str]:
    """DAG의 정점을 사전순으로 안정적으로 위상 정렬합니다."""
    indegree = {vertex: 0 for vertex in graph}
    # LEARNER_TASK: 모든 간선을 순회해 indegree를 세고, 없는 정점은 ValueError로 거절하세요.

    ready = [vertex for vertex, degree in indegree.items() if degree == 0]
    heapq.heapify(ready)
    order = []
    # LEARNER_TASK: ready에서 하나씩 꺼내고, 이웃의 indegree가 0이 되면 넣으세요.

    raise NotImplementedError("LEARNER_TASK")
