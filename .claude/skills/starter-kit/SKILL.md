---
name: starter-kit
description: 청중 배포용 스타터킷(starter-kit/)을 만든다. CLAUDE.md 템플릿, SKILL.md 템플릿, 에이전트 정의 템플릿, 폴더 구조 템플릿, 결과 검증 체크리스트, 프롬프트 치트시트 1장. "스타터킷", "배포물", "템플릿", "청중에게 줄 것" 요청 시, 그리고 슬라이드 12–13번이 확정된 뒤 사용.
---

# 스타터킷

청중이 발표 다음 날 자기 프로젝트에 그대로 넣을 수 있는 파일 묶음. 대상은 통계분석에 익숙한 연구자이므로 설명은 짧게, 파일은 바로 쓸 수 있게.
출력은 `starter-kit/`. 슬라이드 13번 마지막 장의 QR은 이 폴더를 올린 공개 레포 주소로 한다(주소는 사용자가 정한다).

## 구성

| 파일 | 내용 | 원본 |
|---|---|---|
| `README.md` | 10줄. 무엇이 들어 있고 어디에 넣는지 | |
| `CLAUDE.md` | 연구 프로젝트용 계약서 템플릿. 6블록(목적, 상태 / 역할 / 행동 규칙 / 코딩 규칙 / 윤리 제약 / 저장 규칙) + 화면 노출 규칙 + memory 규칙. 괄호 안은 채울 자리 | 사용자의 CLAUDE.md 공통 블록을 일반화 |
| `AGENTS.md` | "CLAUDE.md와 같은 내용을 두라"는 안내 3줄 + 동일 복사 | |
| `folder-structure.md` | `data/{rawdata,derived-data/{user,agent}}`, `code/{user,agent}`, `quarto/{user,agent}`, `output/{user,agent}/YYYY-MM-DD`, `memory/`, `references/`. 각 폴더 한 줄 설명 | 사용자의 저장 규칙 |
| `.claude/skills/_template/SKILL.md` | frontmatter(name, description에 트리거 문구 넣는 법, argument-hint) + 본문 골격(먼저 읽을 것 / 할 일 / 출력 / 하지 않는 것) | 이 프로젝트 스킬들의 공통 골격 |
| `.claude/agents/_template.md` | frontmatter(name, description, model, effort, tools) + "먼저 읽을 것 / 할 일 / 출력 / 하지 않는 것" | `slide-writer.md` 골격 |
| `verification-checklist.md` | 결과 검증 체크리스트(9번 섹션). 표본 수 / 결측 / 변수 정의 / 가중치 / 모형 척도 / 이상치 / 수치 재계산 / 렌더 성공 ≠ 그림 있음 / 인용 DOI 실존 | 레포 `verify-numbers.R`과 2026-08-16 교훈 |
| `prompt-cheatsheet.md` | 한 장. 단계별 프롬프트 뼈대 6개(계획, 사전, 코드, 검증, 표그림, 원고)와 각 프롬프트에 꼭 넣는 한 줄("가정을 명시하고 불확실하면 물어라", "행 단위 출력 금지" 등) | 발표 6–11번 슬라이드의 프롬프트 |
| `run-worker.ps1` | 이 프로젝트의 디스패처에서 모델명을 변수로 뺀 버전. 주석으로 교체 지점 표시 | `scripts/run-worker.ps1` |

## 규칙

1. 사용자의 실제 프로젝트에서 가져오는 문장은 `setup-showcase`의 마스킹 규칙을 그대로 적용한다. 과제명, 서버, 계정, 대상자 수는 넣지 않는다.
2. 템플릿의 채울 자리는 `[ ]`가 아니라 `<여기에: …>` 형식으로 통일한다.
3. 설명은 한국어, 코드, 파일명, frontmatter 키는 영어. em-dash와 AI 문체를 쓰지 않는다.
4. 모든 파일을 합쳐 A4 10쪽 이내. 넘으면 치트시트와 체크리스트를 우선하고 나머지를 줄인다.
5. 라이선스 표시: 사용자가 정한다. 정해지기 전에는 `LICENSE`를 만들지 않는다.
6. 완성 후 `starter-kit/`를 통째로 `grep`한다: IP, `192.168`, `Users\\`, `.env`, `password`, 과제번호 패턴. 남으면 배포하지 않는다.

## 하지 않는 것

- 사용자의 실제 CLAUDE.md를 그대로 복사하지 않는다. 일반화한 템플릿만 넣는다.
- 특정 도구 버전에 묶인 플래그 설명을 길게 쓰지 않는다. 바뀐다. 명령은 최소로, 공식 문서 링크로 대신한다.
