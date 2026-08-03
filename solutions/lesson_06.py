import heapq


def topological_sort(graph: dict[str, set[str]]) -> list[str]:
    """DAG의 정점을 사전순으로 안정적으로 위상 정렬합니다."""
    indegree = {vertex: 0 for vertex in graph}
    for neighbors in graph.values():
        for neighbor in neighbors:
            if neighbor not in indegree:
                raise ValueError("모든 정점은 graph의 키여야 합니다")
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

    if len(order) != len(graph):
        raise ValueError("방향 사이클이 있어 위상 정렬할 수 없습니다")
    return order
