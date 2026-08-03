import re
from pathlib import Path


def test_progress_state_obeys_course_invariants():
    progress = Path("PROGRESS.md").read_text(encoding="utf-8")
    active_match = re.search(r"^- Active lesson: (none|\d+)$", progress, re.MULTILINE)
    rows = re.findall(r"^\|\s*(\d+)\s*\|\s*([a-z_]+)\s*\|$", progress, re.MULTILINE)

    assert active_match is not None
    assert len(rows) == 18
    assert {int(number) for number, _ in rows} == set(range(1, 19))
    assert all(status in {"not_started", "in_progress", "completed"} for _, status in rows)

    in_progress = [int(number) for number, status in rows if status == "in_progress"]
    assert len(in_progress) <= 1
    active = active_match.group(1)
    assert in_progress == ([] if active == "none" else [int(active)])


def test_agent_contract_defines_both_commands_and_safe_commit_scope():
    contract = Path("AGENTS.md").read_text(encoding="utf-8")
    assert "`$next`" in contract
    assert "`$done`" in contract
    assert "LEARNER_TASK" in contract
    assert "PROGRESS.md" in contract
    assert "관련 없는 변경" in contract


def test_next_handles_a_completed_course_without_changing_progress():
    contract = Path("AGENTS.md").read_text(encoding="utf-8")
    assert "`not_started` 행이 없으면" in contract
    assert "전체 연습 문제 모음" in contract
    assert "최종 복습 지도" in contract
    assert "`PROGRESS.md`를 변경하지 않는다" in contract


def test_done_requires_an_exact_staged_set_and_preserves_existing_index():
    contract = Path("AGENTS.md").read_text(encoding="utf-8")
    assert "기존 index" in contract
    assert "스테이징된 경로 집합이 정확히" in contract
    assert "명령이 새로 스테이징한 세 경로만" in contract
    assert "기존 index 항목은 건드리지 않는다" in contract


def test_done_failure_branches_restore_the_active_progress_invariant():
    contract = Path("AGENTS.md").read_text(encoding="utf-8")
    lines = contract.splitlines()
    branches = [
        next(line for line in lines if marker in line)
        for marker in ("집합이 다르면", "커밋이 실패하면")
    ]

    assert all("`in_progress`" in branch for branch in branches)
    assert all("`Active lesson`" in branch for branch in branches)
    assert all("`<NN>`" in branch for branch in branches)


def test_done_stops_before_state_changes_when_learner_work_remains():
    contract = Path("AGENTS.md").read_text(encoding="utf-8")
    assert "완전한 워크북 답안" in contract
    assert "LEARNER_TASK가 하나라도 남아 있으면" in contract
    assert "즉시 중단" in contract
    assert "진행 상태·스테이징·커밋을 수행하지 않는다" in contract


def test_readme_expands_np_on_its_first_use():
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "NP (Nondeterministic Polynomial Time, 비결정적 다항 시간)" in readme


def test_readme_documents_supported_repo_skill_invocation():
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "`$next`" in readme
    assert "`$done`" in readme
    assert "`/skills`" in readme
    assert "새 채팅" in readme or "재시작" in readme


def test_repo_skills_delegate_to_the_authoritative_course_state_machine():
    interfaces = {
        "next": (
            'display_name: "Next Graph Lesson"',
            'short_description: "Start the next graph theory lesson"',
            "$next",
        ),
        "done": (
            'display_name: "Finish Graph Lesson"',
            'short_description: "Validate and finish the active graph lesson"',
            "$done",
        ),
    }
    for name, interface_values in interfaces.items():
        skill_path = Path(f".agents/skills/{name}/SKILL.md")
        agent_path = Path(f".agents/skills/{name}/agents/openai.yaml")
        skill = skill_path.read_text(encoding="utf-8")
        frontmatter = skill.split("---", 2)[1]
        agent = agent_path.read_text(encoding="utf-8")

        assert set(
            line.split(":", 1)[0]
            for line in frontmatter.splitlines()
            if line.strip()
        ) == {"name", "description"}
        assert f"name: {name}" in frontmatter
        assert "AGENTS.md" in skill
        assert "PROGRESS.md" in skill
        assert all(value in agent for value in interface_values)
