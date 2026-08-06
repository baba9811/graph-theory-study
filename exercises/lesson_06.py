import heapq


def topological_sort(graph: dict[str, set[str]]) -> list[str]:
    """DAG의 정점을 사전순 우선으로 위상 정렬합니다.

    전제: 모든 이웃은 `graph`의 키이고 방향 사이클이 없어야 합니다.
    예: `topological_sort({"A": {"B"}, "B": set()})` → `["A", "B"]`
    """
    indegree = {vertex: 0 for vertex in graph}
    for g in graph:
        for neighbor in graph[g]:
            if neighbor not in graph:
                raise ValueError
            indegree[neighbor] += 1

    ready = [vertex for vertex, degree in indegree.items() if degree == 0]
    heapq.heapify(ready)
    order = []
    while ready:
        current = heapq.heappop(ready)
        order.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                heapq.heappush(ready, neighbor)

    if len(order) < len(graph):
        raise ValueError("사이클")
    return order
