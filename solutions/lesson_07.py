def strongly_connected_components(graph: dict[str, set[str]]) -> list[set[str]]:
    if any(neighbor not in graph for neighbors in graph.values() for neighbor in neighbors):
        raise ValueError("모든 정점은 graph의 키여야 합니다")

    visited = set()
    finish_order = []

    def visit(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visit(neighbor)
        finish_order.append(vertex)

    for vertex in graph:
        if vertex not in visited:
            visit(vertex)

    reversed_graph = {vertex: set() for vertex in graph}
    for source, neighbors in graph.items():
        for target in neighbors:
            reversed_graph[target].add(source)

    visited.clear()
    components = []

    def collect(vertex, component):
        visited.add(vertex)
        component.add(vertex)
        for neighbor in reversed_graph[vertex]:
            if neighbor not in visited:
                collect(neighbor, component)

    for vertex in reversed(finish_order):
        if vertex not in visited:
            component = set()
            collect(vertex, component)
            components.append(component)
    return components
