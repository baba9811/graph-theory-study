def degree_map(graph: dict[str, set[str]]) -> dict[str, int]:
    """각 정점의 차수를 딕셔너리로 반환합니다.

    전제: `graph`는 무방향 인접 리스트입니다.
    예: `degree_map({"A": {"B"}, "B": {"A"}})` → `{"A": 1, "B": 1}`
    """
    raise NotImplementedError("LEARNER_TASK")


def is_valid_path(graph: dict[str, set[str]], path: list[str]) -> bool:
    """반복 정점 없이 인접한 정점들로만 이루어진 경로인지 확인합니다.

    전제: 경로 후보의 정점은 문자열이며 `graph`의 키여야 합니다.
    예: `is_valid_path({"A": {"B"}, "B": {"A"}}, ["A", "B"])` → `True`
    """
    raise NotImplementedError("LEARNER_TASK")
