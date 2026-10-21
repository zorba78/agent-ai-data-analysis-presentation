---
name: setup-showcase
description: 다른 프로젝트의 CLAUDE.md, SKILL.md, 에이전트 정의, settings에서 발표(4, 9, 10, 11번 섹션)에 보여줄 부분을 발췌하고 내부 IP, 서버명, DB명, 계정, 과제명, 비밀번호를 마스킹해 slides/excerpts/setup-*.md에 저장한다. "설정 발췌", "CLAUDE.md 예시", "스킬 예시", "마스킹" 요청 시 사용.
---

# 설정 파일 발췌와 마스킹

발표 4번(CLAUDE.md), 9, 10번(스킬 사례), 11번(역할 분리 에이전트)에서 실제 설정 파일을 보여준다. 원본은 `G:/Projects/<프로젝트>/`에 있고 **읽기만 한다.** 발췌본은 `slides/excerpts/setup-<이름>.md`.

## 발췌 대상과 용도

| 섹션 | 원본 | 보여줄 것 |
|---|---|---|
| 4 | `airforce-fatty-liver/CLAUDE.md` | 6블록 구조(목적, 상태 / 역할 / 행동 규칙 / 코딩 규칙 / 윤리 제약 / 저장 규칙). 상태 줄, "표 값이 도출되는 과정을 청크에 남겨라", MetS 정의 블록(253–260행) |
| 4 | 같은 파일 | "없을 때 vs 있을 때" 비교용으로 행동 규칙 1–9번 |
| 9 | `regression-lecture-note/.claude/skills/lecture-review/SKILL.md`, `session-memory/SKILL.md` | 점검, 기억 습관 스킬의 description(트리거 문구)과 절차 |
| 9 | `healthy-aging-project-annual-report/.claude/skills/gard-db/SKILL.md` | "읽기만, 집계값만, 5 미만, 접속정보 Read 금지" 규칙. **마스킹 필수** |
| 10 | `mecasin-phase3-sample-size/.claude/skills/ss-*/SKILL.md` | 작업 단위로 쪼갠 분석 스킬 묶음의 description 5개 |
| 11 | `healthy-aging-project-annual-report/.claude/skills/annual-report/SKILL.md`, `.claude/agents/*.md` | 역할 표(오케스트레이터/근거 분석/초안/검토), 모델, effort 배분, "근거표에 없는 내용은 보고서에 못 들어간다" 문장 |
| 11 | 이 프로젝트의 `CLAUDE.md` 오케스트레이션 절, `scripts/run-worker.ps1` 머리 | 계약서 하나(CLAUDE.md = AGENTS.md), 오케스트레이터 둘, 모델 다양성 |

## 마스킹 규칙

발췌본에 넣기 전에 아래를 치환한다. 치환 목록을 발췌본 끝에 표로 남긴다(원본값은 적지 않고 종류만).

| 종류 | 치환 |
|---|---|
| IP 주소(`\d+\.\d+\.\d+\.\d+`) | `<internal-ip>` |
| 서버, 호스트명, DB명, 스키마, 테이블명 | `<server>`, `<db>`, `<table>` |
| 계정, 비밀번호, 토큰, 접속정보 파일 경로 | `<account>`, `<secret>`, `<env-file>` |
| 과제명, 과제번호, 기관 내부 명칭 | `<project-name>` 또는 일반화("연차보고서 과제") |
| 사용자 홈 경로 | `<path>` |
| 대상자 수처럼 과제 식별이 가능한 세부 수치 | 반올림하거나 `N` |

마스킹 후 발췌본을 `grep`으로 다시 검사한다: IP 패턴, `192.168`, `Users\\`, `.env`, `PWD`, `password`. 하나라도 남으면 저장하지 않는다.

## 발췌본 형식

```markdown
# setup-<이름>

원본: <프로젝트명>/<상대경로> (마스킹 완료, <날짜>)
섹션: <번호>
보여줄 이유: 한 문장

```<언어>
(발췌, 20줄 이하. 길면 `…`로 줄이고 줄임 표시)
```

## 치환 목록
| 종류 | 건수 |
```

## 규칙

1. 발췌는 20줄 이하. 슬라이드 한 장에 들어가는 분량만. 전체 파일이 필요하면 스타터킷 템플릿으로 보낸다.
2. 원본 파일의 문장을 바꾸지 않는다. 마스킹 치환만 한다.
3. 다른 프로젝트의 미완료 작업, 결정 사항, 대상자 정보가 발췌에 섞이면 뺀다.
4. `gard-db` 같은 보안 규칙 스킬은 규칙 문장만 뽑고 서버 정보, 조회 예시는 뽑지 않는다.
