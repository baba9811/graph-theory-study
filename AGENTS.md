# 학습 진행 규약

- 한국어로 응답하고, 한 번에 하나의 개념 또는 연습 단계만 소개한다.
- 다듬은 사용자 메시지가 정확히 `/next`이면 `PROGRESS.md`를 읽는다. `Active lesson`이 `none`이 아니면 그 수업을 재개하고, 그렇지 않으면 가장 낮은 번호의 `not_started` 수업을 골라 `in_progress`로 표시하고 활성 수업으로 설정한 뒤 목표와 어휘부터 시작한다.
- `in_progress` 수업을 건너뛰지 않으며, 학습자가 시도하기 전에는 `solutions/`를 공개하지 않는다.
- 다듬은 사용자 메시지가 정확히 `/done`이면 활성 수업이 있어야 한다. 해당 워크북과 연습 파일에서 `LEARNER_TASK`를 검색하고 `uv run pytest tests/test_lesson_<NN>.py -v`를 실행한다. 하나라도 실패하면 실행 가능한 힌트 하나를 제공한다.
- 성공하면 해당 행을 `completed`로 바꾸고 `Active lesson`을 `none`으로 설정한다. 정확한 현재 워크북 경로, `exercises/lesson_<NN>.py`, `PROGRESS.md`만 스테이징하고, 스테이징된 경로 목록을 확인한 뒤 `lesson <NN>: complete <english-topic>`으로 커밋한다.
- 커밋이 실패하면 그 정확한 경로들을 언스테이징하고 진행 상태만 `in_progress`로 복원한다. 학습자 답안과 코드는 보존하고 재시도 방법을 설명한다.
- 관련 없는 변경 경로는 보고만 하고 스테이징하지 않는다. 자동으로 amend, reset, rebase, push, clean을 하지 않는다.
- 성공 후 커밋 해시를 보고하고 핵심 아이디어 세 가지를 요약하며 일치하는 해답 파일을 연결한 뒤 `/next`를 안내한다.
- 모든 수업이 완료되면 전체 연습 문제 모음을 실행하고 최종 복습 지도를 제공한다.
