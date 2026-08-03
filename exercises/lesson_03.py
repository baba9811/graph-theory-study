from collections import deque


def bfs(
    graph: dict[str, set[str]], start: str
) -> tuple[dict[str, int], dict[str, str | None]]:
    """시작 정점에서 너비 우선 탐색을 하여 거리와 부모를 반환합니다."""
    raise NotImplementedError("LEARNER_TASK")


def reconstruct_path(
    parents: dict[str, str | None], start: str, goal: str
) -> list[str] | None:
    """부모 딕셔너리를 따라 start부터 goal까지의 경로를 복원합니다."""
    raise NotImplementedError("LEARNER_TASK")
