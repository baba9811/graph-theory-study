from pathlib import Path


def test_progress_starts_with_one_state_per_lesson():
    progress = Path("PROGRESS.md").read_text(encoding="utf-8")
    assert "- Active lesson: none" in progress
    assert progress.count("| not_started |") == 18


def test_agent_contract_defines_both_commands_and_safe_commit_scope():
    contract = Path("AGENTS.md").read_text(encoding="utf-8")
    assert "`/next`" in contract
    assert "`/done`" in contract
    assert "LEARNER_TASK" in contract
    assert "PROGRESS.md" in contract
    assert "관련 없는 변경" in contract


def test_done_stops_before_state_changes_when_learner_work_remains():
    contract = Path("AGENTS.md").read_text(encoding="utf-8")
    assert "완전한 워크북 답안" in contract
    assert "LEARNER_TASK가 하나라도 남아 있으면" in contract
    assert "즉시 중단" in contract
    assert "진행 상태·스테이징·커밋을 수행하지 않는다" in contract


def test_readme_expands_np_on_its_first_use():
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "NP (Nondeterministic Polynomial, 비결정론적 다항식)" in readme
