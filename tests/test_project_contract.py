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
