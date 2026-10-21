---
name: talk-orchestration
description: 1시간 발표자료(13섹션)를 소재 발췌 → 아웃라인 → 슬라이드 → 독립 검토 → 수치 검증 → 수정 순서로 만드는 오케스트레이션 절차. 발표자료, 슬라이드, 아웃라인, 발표자 노트 작성이나 수정, 검토 요청, 진행 상태 점검을 요청받으면 사용.
argument-hint: "[status | outline | draft <섹션번호…> | review [섹션번호…] | verify | all]"
model: claude-fable-5-1
effort: medium
---

# 발표자료 작성 오케스트레이션

이 스킬을 실행하는 세션이 오케스트레이터 A(작성 허브)다. 오케스트레이터는 소재를 모으고, 워커에게 일을 나누고, 검토 결과를 반영하고, 사용자에게 보고한다. 슬라이드 본문은 워커가 쓴다.

| 역할 | 실행 주체 | 모델, effort | 정의 |
|---|---|---|---|
| 오케스트레이터 A | 메인 세션 | Fable 5.1, medium | `.claude/settings.json` |
| 슬라이드 작성 | `slide-writer` | Opus 5.5, xhigh | `.claude/agents/slide-writer.md` |
| 수치, 인용 검증 | `fact-checker` | Opus 5.5, xhigh | `.claude/agents/fact-checker.md` |
| 독립 검토 | Terra | GPT-5.6, high | `scripts/run-worker.ps1 -Worker terra` |
| 독립 검토(세션형) | Astra | GPT-6.0, medium | 사용자가 `copilot`으로 직접 엶. `prompts/astra-session.md` |

Claude 워커는 Agent 도구의 `subagent_type`에 위 이름을 넣어 부른다. `model`, `effort`는 따로 주지 않는다(정의 파일 값이 쓰이도록). 범용 에이전트로 슬라이드를 쓰게 하지 않는다.
Terra는 반드시 `scripts/run-worker.ps1`로 부른다. 직접 `codex exec`를 치지 않는다(한도 소진 시 Opus 대체와 수행 모델 기록이 스크립트에 있다).

## 인자

- `status`(기본값): 아래 "상태 점검"만 하고 보고한다.
- `outline`: 1–2단계.
- `draft <섹션번호…>`: 지정한 섹션만 3단계.
- `review [섹션번호…]`: 4단계만.
- `verify`: 5단계만.
- `all`: 1–6단계 전부. 단계 사이에 사용자 확인을 받는다.

## 상태 점검

1. `memory/MEMORY.md`를 읽는다. `review/`에서 가장 최근 날짜 폴더의 파일을 읽는다.
2. `slides/outline.md`가 있는지, `slides/index.qmd`에 어떤 섹션이 들어 있는지, 각 섹션의 검토, 검증 상태를 본다.
3. 섹션별로 "아웃라인 / 초안 / 검토 반영 / 검증 통과"를 표로 보고하고, 다음 할 일을 한 줄로 제안한다.

## 단계

### 1. 소재 발췌 (오케스트레이터가 직접)

`repo-excerpt` 스킬로 레포의 대화 메시지, 코드, qmd를 `slides/excerpts/<섹션번호>-<이름>.md`에, `setup-showcase` 스킬로 다른 프로젝트의 설정 파일을 `slides/excerpts/setup-*.md`에 뽑는다. 둘 다 원본은 읽기만 하고, 화면 노출 규칙과 마스킹 규칙은 각 스킬에 있다.

### 2. 아웃라인 (`slide-writer`)

`slide-writer`에게 CLAUDE.md의 구성(13섹션, 시간)과 `slides/excerpts/`를 주고 `slides/outline.md`를 쓰게 한다. 슬라이드별 제목, 한 줄 메시지, 할당 시간, 시각자료 유형, 발표자 노트 초안, 출처.
받은 뒤 시간 합계가 53분 이내인지, 섹션 8, 9가 통계 청중 수준인지 확인하고 사용자에게 보여준다. 사용자 확인 전에는 3단계로 가지 않는다.

### 3. 초안 (`slide-writer`)

섹션 단위로 `slide-writer`를 부른다. 한 번에 한 섹션. 입력은 `slides/outline.md`의 해당 섹션과 `slides/excerpts/`. 출력은 `slides/index.qmd`의 해당 섹션 블록(`## ` 구분)과 발표자 노트(`::: {.notes}`).
여러 섹션을 병렬로 부를 때는 서로 다른 섹션만 맡긴다.

### 4. 독립 검토 (Terra 또는 Astra)

초안이 된 섹션을 `scripts/run-worker.ps1 -Worker terra -Task <작업파일>`로 Terra에 넘긴다. 작업 파일은 `prompts/review-terra.md`를 바탕으로 검토 대상 섹션 번호와 파일 경로를 채워 `output/agent/YYYY-MM-DD/`에 만든다.
결과는 `review/YYYY-MM-DD/section-<번호>-terra.md`에 저장된다. 결과 머리의 `worker:` 줄로 실제 수행 모델을 확인한다. Opus로 대체됐으면 "같은 계열 검토"임을 사용자에게 알린다.
사용자가 Astra 세션을 따로 열어 검토한 결과도 같은 폴더에 `-astra.md`로 들어온다. 둘 다 읽는다.
검토 지적을 그대로 반영하지 않는다. 지적마다 "반영 / 반영 안 함(이유)"를 정해 사용자에게 표로 보고하고, 반영분만 `slide-writer`에게 수정시킨다.

### 5. 수치, 인용 검증 (`fact-checker`)

`fact-checker`에게 `slides/index.qmd` 전체와 `references/`, 레포의 `verify-numbers.R` 경로를 주고 검증표(`output/agent/YYYY-MM-DD/fact-check.md`)를 받는다. 항목: 슬라이드 번호 / 주장 또는 수치 / 근거 위치 / 상태(일치, 불일치, 확인 불가).
불일치와 확인 불가는 사용자에게 보고한다. 수치를 오케스트레이터가 임의로 고치지 않는다.

### 6. 렌더와 마무리

`revealjs-deck` 스킬로 렌더하고 넘침, 깨진 그림, 노트 누락, 화면 노출을 점검한다. 결정 사항을 `memory/`에 남기고 `MEMORY.md`를 갱신한다.

### 이후 (슬라이드 확정 뒤)

- `demo-runbook`: 시연 3개의 런북과 녹화 전 점검표.
- `starter-kit`: 청중 배포물. 12–13번 슬라이드가 확정된 뒤.

## 하지 않는 것

- 레포 `airforce-fatty-liver`와 `references/`를 수정하지 않는다.
- `review/`에 쓰지 않는다. 읽기만 한다.
- Claude 한도가 떨어지면 API 과금으로 넘기지 않는다. 상태를 `memory/`에 남기고 멈춘다.
- 오류 장면을 각색하지 않는다.
