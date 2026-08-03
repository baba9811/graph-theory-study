def degree_map(graph: dict[str, set[str]]) -> dict[str, int]:
    return {vertex: len(neighbors) for vertex, neighbors in graph.items()}


def is_valid_path(graph: dict[str, set[str]], path: list[str]) -> bool:
    if not path or len(path) != len(set(path)):
        return False
    if any(vertex not in graph for vertex in path):
        return False
    return all(target in graph[source] for source, target in zip(path, path[1:]))
