# 학습 진행 규약

- 한국어로 응답하고, 한 번에 하나의 개념 또는 연습 단계만 소개한다.
- 기본 학습 인터페이스는 repo skill `$next`, `$done`이다. literal `/next` 또는 `/done`이 일반 메시지로 전달되는 surface에서는 각각의 호환 별칭으로 처리한다.
- 다듬은 사용자 메시지가 정확히 `$next`이면 `PROGRESS.md`를 읽는다. `Active lesson`이 `none`이 아니면 그 수업을 재개한다. 활성 수업이 없고 `not_started` 행이 있으면 가장 낮은 번호를 `in_progress`로 표시하고 활성 수업으로 설정한 뒤 목표와 어휘부터 시작한다. `not_started` 행이 없으면 전체 연습 문제 모음을 검증하고 최종 복습 지도를 제공하되 `PROGRESS.md`를 변경하지 않는다.
- `in_progress` 수업을 건너뛰지 않으며, 학습자가 시도하기 전에는 `solutions/`를 공개하지 않는다.
- 다듬은 사용자 메시지가 정확히 `$done`이면 활성 수업이 있어야 한다. 완전한 워크북 답안을 확인하고 워크북과 연습 파일에서 `LEARNER_TASK`를 검색한다. LEARNER_TASK가 하나라도 남아 있으면 실행 가능한 힌트 하나만 제공하고 즉시 중단하며 진행 상태·스테이징·커밋을 수행하지 않는다. 없으면 `uv run pytest tests/test_lesson_<NN>.py -v`를 실행하고, 하나라도 실패하면 실행 가능한 힌트 하나를 제공한다.
- 테스트 성공 뒤 먼저 `git diff --cached --name-only`로 기존 index를 확인한다. 기존 index 항목이 하나라도 있으면 진행 상태를 바꾸거나 새로 스테이징하지 않고 중단하여 사용자가 정리하도록 안내한다.
- 기존 index가 비어 있으면 해당 행을 `completed`로 바꾸고 `Active lesson`을 `none`으로 설정한다. 정확한 현재 워크북 경로, `exercises/lesson_<NN>.py`, `PROGRESS.md`만 스테이징한 뒤, 스테이징된 경로 집합이 정확히 이 세 경로인지 확인한다. 집합이 다르면 명령이 새로 스테이징한 세 경로만 언스테이징하고 해당 행을 `in_progress`로, `Active lesson`을 `<NN>`로 함께 복원하며, 기존 index 항목은 건드리지 않는다. 집합이 정확할 때만 `lesson <NN>: complete <english-topic>`으로 커밋한다.
- 커밋이 실패하면 명령이 새로 스테이징한 세 경로만 언스테이징하고 해당 행을 `in_progress`로, `Active lesson`을 `<NN>`로 함께 복원한다. 기존 index 항목과 학습자 답안·코드는 보존하고 재시도 방법을 설명한다.
- 관련 없는 변경 경로는 보고만 하고 스테이징하지 않는다. 자동으로 amend, reset, rebase, push, clean을 하지 않는다.
- 성공 후 커밋 해시를 보고하고 핵심 아이디어 세 가지를 요약하며 일치하는 해답 파일을 연결한 뒤 `$next`를 안내한다.
- 모든 수업이 완료되면 전체 연습 문제 모음을 실행하고 최종 복습 지도를 제공한다.
