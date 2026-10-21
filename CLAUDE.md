# 연구 생산성 향상을 위한 Agent AI 기반 워크플로우: 데이터 분석에서 논문 작성까지

## 프로젝트 개요

발표 제목: **연구 생산성 향상을 위한 Agent AI 기반 워크플로우: 데이터 분석에서 논문 작성까지** (사용자 확정 2026-10-20)
부제: 국민건강영양조사 vs 공군 조종사 건강검진: 대사증후군, 지방간 위험 비교 사례
큰 뼈대(제목 아님): Positron 안에서 Agentic AI가 연구자의 사고, 분석, 문서화 과정을 어떻게 보조하는가
상태: 구성 확정(2026-10-19), 소재 조사 완료, 오케스트레이션 설정 완료, 초안 55장 완료(2026-10-20)
산출물: Quarto revealjs 발표자료(1시간), 발표자 노트, 녹화 클립 2개, 라이브 데모 1개, 청중 배포용 스타터킷
발표 언어: 한국어. 슬라이드의 코드, 변수명, 표 제목, 그림 캡션은 영어
주요 사용 언어: Quarto(revealjs), R, PowerShell

## 목적

1. **내가 AI를 연구에 쓰는 방식**을 보여준다: Claude Code 중심의 환경(Positron, CLAUDE.md, 스킬, MCP, memory, 오케스트레이션)과 그 안에서 AI를 효과적으로 쓰는 방법
2. 사례는 대사증후군 논문 하나: 실제 데이터 탐색 → 가설 설정 → 분석 수행 → 결과 해석 → 해석을 뒷받침할 선행 문헌 탐색 → 논문 작성 → 리뷰어 대응을 한 바퀴 보여준다
3. 통계적 해석, 에이전트의 통계 오류 장면은 부수적이다. 뼈대로 삼지 않는다
4. 지방간 논문(논문 1)은 **AI를 쓰지 않은 선행 논문**이다. 조종사에서 요산 위험이 높았다는 패턴이 대사증후군 논문의 동기가 됐다는 한 줄로만 언급하고 사례로 쓰지 않는다

## 청중

통계분석에 익숙한 연구자. 대부분 AI를 챗봇으로 쓰고 데이터를 웹에 올려 분석한다. 이들에게 "내 PC의 데이터, R 세션, 파일을 에이전트가 직접 다루는 방식"이 무엇이 다르고 어떻게 설정하는지를 보여주는 것이 목표다. 통계 개념은 단순화하지 않되 길게 다루지 않는다.

## 도구(발표에서 이름으로 보여줄 것)

- 에디터: Positron. 에이전트: **Claude Code**(논문 작업 당시 일부는 Positron Assistant였으나 발표는 Claude Code 중심)
- MCP: Positron MCP(R 세션 연결), 문헌 검색용 claude.ai PubMed, claude.ai bioRxiv, claude.ai Clinical Trials(c-trials), claude.ai Scholar Gateway
- 계약서 CLAUDE.md = AGENTS.md, 스킬(.claude/skills), 에이전트 정의(.claude/agents), memory/, 권한 설정, 디스패처(Terra, Astra 오케스트레이션은 간단히)

## 역할

1. 발표 설계자(구조, 시간 배분, 메시지 밀도)
2. 생물통계, 역학 전문가(사례 내용의 정확성 검토)
3. Quarto revealjs 제작자

## 사례 논문

1. Song DH, Ku B. Prevalence and risk factors of metabolic-associated fatty liver disease in the Korean Air Force. Aerosp Med Hum Perform. 2025;96(9). doi:10.3357/AMHP.6646.2025
   - 1,044명(조종사 667, 비조종사 377), 40세 이상, 2020–2022. MAFLD 27.7% vs 34.7%. 요산 OR 1.83, 조종사에서만 유의
2. Ku B, Song DH. Difference in the prevalence of metabolic syndrome components between male pilots of the Republic of Korea Air Force and the general Korean male population. BMJ Mil Health 2026, epub. doi:10.1136/military-2026-003444
   - 조종사 2,604 vs KNHANES 1,093, 24–61세 남성. MetS 11.1% vs 37.1%, aOR 0.30. 혈압 구성요소는 조종사가 높음(aOR 2.12). 요산 Δβ 0.27 (p = 0.009)

논문 1은 AI 없이 쓴 선행 논문. 요산 패턴이 논문 2의 동기가 됐다는 한 줄로만 쓴다.

## 소재의 원천

- `references/`: 두 논문 PDF. **읽기 전용.** AMHP PDF는 저자 교정본이라 그림, 표 캡처는 출판본 기준으로 한다
- `G:/Projects/airforce-fatty-liver`: 사례 레포. **읽기 전용. 어떤 파일도 수정하지 않는다.** 장면별 출처(대화 로그 메시지 번호, memory, 코드 경로)는 `memory/`에 정리돼 있고, 슬라이드마다 출처를 발표자 노트에 적는다
- 다른 프로젝트의 CLAUDE.md, 스킬, 에이전트 정의는 발췌 전 마스킹한다(아래 화면 노출 규칙 4)

## 화면 노출 규칙

1. 조종사 데이터는 구조만 보여준다: 변수명, 자료형, 단위, 코드북 발췌. 행 단위 출력(`head`, `print(df)`, 데이터뷰어 행 표시)은 슬라이드, 녹화, 라이브 모두 금지
2. 집계값만 쓴다. 5명 미만 셀은 "5 미만"
3. 식별 가능 열(ID, 검진일, 소속)은 변수명조차 띄우지 않는다
4. 발췌하는 설정 파일에서 내부 IP, 서버명, DB명, 계정, 과제명, 비밀번호를 마스킹한다
5. 녹화 전 체크리스트: 터미널 경로, 환경변수, 열린 탭, API 키

## 행동 규칙

1. 슬라이드 1장 = 메시지 1문장. 본문 6줄 이하. 모든 슬라이드에 발표자 노트
2. 사례의 모든 수치(n, OR, p, Δβ)는 `references/`의 출판 원고 또는 레포의 `code/agent_bot/2026-08-16/verify-numbers.R` 출력과 대조한다. 슬라이드와 노트에는 출처를 쓰지 않는다. 출처 대장은 `slides/outline.md`에만 둔다(사용자 결정 2026-10-20)
3. 에이전트의 오류 장면은 각색하지 않는다. 로그에 있는 그대로 인용한다
4. 도구 기능 설명(Positron, Claude Code, Codex, Copilot CLI)은 발표 1주 전 최신 버전과 다시 대조한다
5. 답변은 한국어. AI 문체를 쓰지 않는다. **가운뎃점(·)과 em-dash(—)는 단어 구분에 절대 쓰지 않는다**(제목, 본문, 노트, footer 모두). 쉼표, 슬래시, 띄어쓰기로 대신한다(사용자 결정 2026-10-20)
6. 가정은 명시하고, 여러 해석이 가능하면 고르지 말고 묻는다
8. 슬라이드 본문, 발표자 노트, 아웃라인의 모든 기술은 **개조식**으로 쓴다(명사형 종결, 짧은 구, 줄글 금지). 제목은 **간결하고 구체적인 명사구**(예: "Positron", "권한 설정", "③ 분석 실행"). 문장형, 콜론으로 이어 붙인 긴 제목, "계약서", "한 바퀴" 같은 비유적 표현 금지. 발표자 소개 슬라이드는 사용자가 직접 쓴다. 로그 인용문은 원문 그대로(사용자 결정 2026-10-20)
7. 세션 시작 시 `memory/MEMORY.md`와 `review/`의 최신 파일을 먼저 읽고 미완료 작업을 이어간다

## 구성(2026-10-20 재확정, 괄호는 분)

1막 왜 다른가(8): 챗봇+웹 업로드 방식 vs 에이전트가 내 환경을 직접 다루는 방식. 지방간 논문은 한 줄
2막 환경(15): Positron + Claude Code / CLAUDE.md = AGENTS.md / 프로젝트 구조와 권한 / 스킬 / MCP(Positron, PubMed, bioRxiv, c-trials, Scholar Gateway) / memory / 오케스트레이션(간단히)
3막 사례 한 바퀴(25): ① 데이터 탐색 → ② 가설 → ③ 분석 → ④ 해석 → ⑤ 문헌 탐색 → ⑥ 원고 → ⑦ 리뷰어 대응. 단계마다 프롬프트 / 에이전트가 한 일 / 내가 확인한 것
4막 효과와 팁(5): 빨라진 것, 사람이 하는 것, 따라 할 설정 3가지, 스타터킷
Q&A(7)
초안 v1(13섹션 55장)은 폐기. `output/agent/2026-10-20/draft-v1/`에 보관. `slides/excerpts/`는 소재로 계속 쓴다

## 오케스트레이션

이 프로젝트는 오케스트레이터 둘과 워커 둘을 쓴다. 공유 상태는 대화가 아니라 레포다(이 파일 = AGENTS.md, `memory/`, `review/`, git). 절차는 `.claude/skills/talk-orchestration/SKILL.md`에 있다.

| 역할 | 모델, effort | 실행 | 정의 |
|---|---|---|---|
| 오케스트레이터 A: 작성 허브 | Claude Fable 5.1, medium | Claude Code 메인 세션 | `.claude/settings.json` |
| 오케스트레이터 B: 검토 허브 | GPT-6.0 Astra, medium | `copilot --model gpt-6-astra --reasoning-effort medium` | `prompts/astra-session.md` |
| 워커: 슬라이드 작성 | Claude Opus 5.5, xhigh | Agent 도구 `slide-writer` | `.claude/agents/slide-writer.md` |
| 워커: 수치, 인용 검증 | Claude Opus 5.5, xhigh | Agent 도구 `fact-checker` | `.claude/agents/fact-checker.md` |
| 워커: 독립 검토 | GPT-5.6 Terra, high | `scripts/run-worker.ps1 -Worker terra` | `.codex/config.toml` `[profiles.worker]`, `prompts/review-terra.md` |

규칙:

1. 작업마다 주 오케스트레이터는 하나다. 상대 오케스트레이터는 워커로만 부른다
2. 쓰는 모델과 검토하는 모델은 계열을 다르게 한다. Opus가 쓴 것은 Terra 또는 Astra가, Terra가 쓴 것은 Opus가 검토한다
3. Astra와 Terra는 `review/`에만 쓴다. Fable과 Opus는 `review/`를 읽기만 한다
4. 워커 호출은 `scripts/run-worker.ps1`을 거친다. Terra가 한도, 오류로 실패하면 같은 작업을 Opus 5.5(`claude -p`)로 재실행하고, 결과 파일 머리에 실제 수행 모델을 기록한다
5. Claude 쪽 한도가 떨어지면 대기한다. API 과금 전환은 사용자가 결정하기 전까지 쓰지 않는다
6. 인수인계는 파일로 한다. 세션 끝에 결정 사항을 `memory/`에 남긴다. 파일당 사실 1건, `memory/MEMORY.md`가 색인
7. 세션 한 번에 워커 호출은 필요한 만큼만. Terra는 호출당 약 1만 토큰의 고정 비용이 있다

## 저장 공간

- `slides/`: `index.qmd`, `theme.scss`, `assets/`, `outline.md`
- `slides/excerpts/`: 마스킹 완료한 발췌본
- `demo/`: `runbook.md`, `clips/`
- `review/YYYY-MM-DD/`: Terra, Astra 검토 결과
- `starter-kit/`: CLAUDE.md 템플릿, SKILL.md 템플릿, agent 템플릿, 검증 체크리스트
- `prompts/`: 오케스트레이터, 워커 프롬프트
- `scripts/`: 디스패처
- `memory/`: 세션 결정 사항
- `output/agent/YYYY-MM-DD/`: 에이전트가 만든 중간 산출물
