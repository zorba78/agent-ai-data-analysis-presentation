# 발표 아웃라인 v2: 연구 생산성 향상을 위한 Agent AI 기반 워크플로우: 데이터 분석에서 논문 작성까지

작성 2026-10-20. v1(13섹션 55장) 폐기. 축은 "내가 AI를 연구에 쓰는 방식"이고 대사증후군 논문은 그 방식을 끝까지 보여주는 실.
모든 기술은 개조식. 가운뎃점, em-dash 금지. 제목은 간결하고 구체적인 명사구. 로그 인용은 원문 그대로. 슬라이드와 노트에는 출처를 쓰지 않고, 아래 각 장의 "출처" 줄이 출처 대장이다. 발표자 소개는 사용자가 직접 쓴다(S01 제외). 슬라이드 제목은 `slides/sections/*.qmd`가 기준(2026-10-20 개정).
에이전트 표기: 대화 로그 장면 중 2026-03월은 Positron Assistant(Claude Sonnet 4.6), 2026-05월 이후(문헌, 원고, 리뷰어 대응)는 Claude Code. 발표는 Claude Code 중심.

## 총계

| 막 | 장 | 분 |
|---|---|---|
| 1 왜 다른가 | 7 | 8.5 |
| 2 환경 | 15 | 20 |
| 3 사례 | 17 | 27 |
| 4 효과와 팁 | 7 | 8 |
| 합계(표지 제외) | 46 | 63.5 |

2026-10-20 S02, S08b 추가로 1.5분 초과. 2026-10-22 S08c Quarto, S08d TinyTeX 추가로 총 5.5분 초과(58.5분, S09b 시연 2분 포함). 3막 또는 Q&A에서 조정 필요.
| Q&A | | 7 |

시연: 녹화 D1(3막 ③ 분석 실행, 90초), 녹화 D2(3막 ⑤ 문헌 탐색, 60초), 라이브 D3(2막 Claude Code 세션 열기 + 데이터 구조 질문, 2분). 백업 녹화 필수.

---

## 1막. 왜 다른가 (8분)

### S01 발표자 (0.5)
- 유형: 텍스트. `[여기에: 소속, 역할 한 줄]`
- 노트: 통계학자, 두 논문 공저자, AI는 2025년부터 연구에 투입

### S02 AI 활용 방식 4가지 (1.5) [2026-10-20 추가]
- 유형: 그림(`assets/figs/s01-ai-usage-modes.svg`, 4칸 카드 + 축)
- 본문: 1 웹 챗봇 질문 / 2 파일 업로드 분석 / 3 에디터 자동완성 / 4 에이전트(오늘 주제). 축: 수작업 비중 높음 → 에이전트 자율성 높음. 카드별 칩: 연구자 역할
- 노트: 네 방식 모두 같은 모델. 다른 것은 AI가 내 작업 환경에 얼마나 닿는가. 청중 다수는 1과 2

### S02b 챗봇 방식 (1)
- 유형: 그림(`assets/figs/s02-chatbot-flow.svg`, 업로드 → 질문 → 복사)
- 본문: 챗봇에 질문 / 웹에 데이터 업로드 / 결과를 손으로 옮김
- 노트: 앞 장의 1과 2를 한 그림으로. 비난이 아니라 출발점. 한계는 다음 장

### S03 그 방식의 비용: 데이터가 밖으로 나가고, 맥락은 매번 사라지고, 숫자는 손으로 옮겨진다 (1.5)
- 유형: 3칸 카드(보안 / 맥락 / 재현)
- 본문: 원자료 외부 전송(IRB, 군 자료) / 대화마다 설명 반복 / 코드와 결과와 원고가 끊김
- 노트: `[여기에: 본인이 겪은 사례 1건]`

### S04 내 방식: 에이전트가 내 PC의 데이터, R 세션, 파일을 직접 다룬다 (2)
- 유형: 다이어그램(Positron 창 안에 Claude Code, R 세션, 파일, MCP)
- 본문: 데이터는 PC에 / 에이전트가 코드 작성, 실행, 수정 / 결과는 파일로 남음 / 규칙은 계약서로
- 노트: 챗봇과의 차이 세 가지: 실행, 파일, 기억. 이 발표 전체가 이 그림의 설명

### S05 연구 워크플로우 6단계 (1.5) [2026-11-02 개정: 전처리 → 탐색 → 가설 → 분석 → 문헌 → 초안]
- 유형: 파이프라인 7단계 진행바 + 한 줄씩
- 본문: 7단계. 모든 단계에서 에이전트가 일하고, 사람이 결정
- 노트: 3막에서 이 순서 그대로. 단계마다 "프롬프트 / 에이전트가 한 일 / 내가 확인한 것"

### S06 사례: 공군 조종사 vs 국민건강영양조사, 대사증후군 (1)
- 유형: 텍스트 + 논문 서지
- 본문: 조종사 2,604 vs KNHANES 1,093, 남성 24–61세 / 출판: BMJ Mil Health 2026 / 동기: AI 없이 쓴 선행 논문(지방간, AMHP 2025)에서 조종사의 요산 위험이 높았음 → 대사증후군에서도 같은 패턴인가
- 노트: 지방간 논문은 여기 한 줄. 분석은 비교적 단순한 로지스틱 회귀가 중심이라 1시간 사례로 적합
- 출처: CLAUDE.md 사례 논문, 05-urate-origin

## 2막. 환경 (15분)

### S07 2. 환경은 다섯 층이다: 에디터, 에이전트, 계약서, 도구, 기억 (1.5)
- 유형: 층 다이어그램
- 본문: Positron / Claude Code / CLAUDE.md = AGENTS.md / 스킬, MCP / memory
- 노트: 각 층 한 장씩. 층이 빠지면 생기는 문제를 같이 말함

### S08 Positron: 설치와 구동 (1) [2026-10-21 개정]
- 유형: 그림(`assets/figs/s09-positron-install.svg`, 내려받기 / R 연결 / 첫 화면) + 3칸(설치 직후 설정: 인터프리터 / RStudio 단축키 / 확장). 영상은 S09b로 이동(2026-10-22)
- 출처: positron.posit.co/download(2026-10-21 확인, 버전 2026.10.1-2)
- 본문: 에이전트가 쓰는 R 세션 = 내가 보는 R 세션 / Positron MCP로 연결, 실행 코드가 내 콘솔에 표시 / 결과 객체, 그림, 데이터는 Positron 창에서 직접 확인
- 노트: 메시지 한 줄 "에이전트와 내가 같은 R 세션을 본다". 화면 노출 규칙. 스크린샷은 합성 데이터나 집계 화면

### S08c Quarto: 문서 생성 (1) [2026-10-22 추가]
- 유형: 그림(`assets/figs/s10-quarto-flow.svg`, qmd → Quarto → docx/pdf/html/revealjs) + 3칸
- 본문: 한 원고, 여러 형식 / 숫자는 코드에서 / 에이전트와 궁합
- 출처: quarto.org/docs/get-started, docs/download(2026-10-22 확인, Positron 번들 1.10.18)

### S08d TinyTeX: LaTeX 설치 (1) [2026-10-22 추가]
- 유형: 그림(`assets/figs/s10-tinytex-install.svg`, 설치 A quarto / B R / TinyTeX 설명) + `quarto check` 출력
- 본문: pdf 출력 전 확인 한 줄
- 출처: quarto.org/docs/output-formats/pdf-engine.html, yihui.org/tinytex(2026-10-22 확인). codepanel은 이 PC 실제 출력

### S08b Positron + Claude Code vs 웹 Code (1) [2026-10-20 추가]
- 유형: 그림(`assets/figs/s09-positron-vs-web.svg`, 4행 2열 비교)
- 본문: R 실행 / 결과 확인 / 기록 / 고치는 방식. 왼쪽 Positron + Claude Code, 오른쪽 웹 Code 단독(클라우드 VM)
- 노트: 같은 엔진, 차이는 작업 화면. 웹이 나은 경우(설치 없음, 비동기, 휴대폰)도 말함. 결국 선호의 문제
- 출처: 세션 논의 2026-10-20(claude.ai/code는 GitHub 레포를 클라우드 VM에 복제, 데스크톱 앱 Code 탭은 로컬 폴더). 발표 1주 전 재확인

### S09 Claude Code: 설치와 구동 (1.5) [2026-10-21 개정]
- 유형: 그림(`assets/figs/s11-claude-code-install.svg`, CLI 설치 명령 + Positron 확장) + 4칸(읽기 / 쓰기 / 실행 / 권한)
- 출처: code.claude.com/docs/en/setup, code.claude.com/docs/en/vs-code(2026-10-21 확인)
- 유형: 코드(세션 시작 화면) + 3칸(읽기 / 쓰기 / 실행)
- 본문: `claude` 한 줄로 시작 / 파일 읽기, 편집, 쉘 실행, R 실행(Positron MCP) / 권한은 도구별 승인
- 노트: 논문 작업 당시 일부는 Positron Assistant. 지금은 Claude Code로 통일. 라이브 D3 예고

### S09b 시연: 설치와 첫 실행 (2) [2026-10-22 추가]
- 유형: 3칸(Positron / Claude Code CLI / 확장) + 사용자 제작 영상 `demo/clips/install-positron-claude.mp4`(Hyper-V VM 녹화)
- 노트: 로그인 화면 편집, 전체 3~4분 녹화 후 2분 편집

### S10 (삭제, 2026-10-23) 라이브 D3는 3막 ① 데이터 탐색(S20)으로 이동. 2막 후반은 "개념과 역할 / 작성 요점 / 예시" 구조로 재작성(2026-10-23)
- 새 장: 지침 파일의 역할(1.5) / CLAUDE.md 개념(1.5) + 행동 규칙 예시(1.5, 2026-10-30 추가) + 예시 2장 / 경계: 폴더와 권한(1.5, 2026-10-30 3장→1장) / 스킬 개념(1.5) + 예시 / CLAUDE.md와 스킬의 차이(1.5, 2026-10-30 추가, 스킬 뒤) / MCP 개념(1.5) + 구성 / memory 개념(1) + 예시 / 오케스트레이션 개념(1) + 구성 / 에이전트 연구의 이득과 조건(1.5)
- 시간 재계산 필요. 2막 약 29분, 전체 약 68분. 3막 또는 2막 예시 장 축소로 조정
- 2026-10-30 추가: CLAUDE.md 개념 장 수정(작성자: 사람 또는 에이전트 초안 후 사람 확정 / 작성 요점 첫 줄: 목적과 역할, 둘째 줄: 실패 양상을 겨눈 행동 규칙). 새 장 "행동 규칙 예시: 네 가지 실패 양상"
  - 출처: Karpathy X 게시글 2026-01-26(status 2015883857489522876, 원문 전체 미확인, 두 조각은 TechTimes 2026-05-18, aibuilderclub 2차 인용) / forrestchang/andrej-karpathy-skills CLAUDE.md(Forrest Chang, 2026-01-27, 약 22만 스타). 카파시 본인 파일 아님, 공개 지지 미확인

### (구) S10 라이브 D3: 세션을 열고 "이 데이터가 어떻게 생겼는지" 묻는다 (2)
- 유형: 라이브(백업 녹화 `../demo/clips/D3-session-open.mp4`)
- 본문: 프롬프트 "분석 데이터셋의 변수 구조와 결측을 집계로만 요약" / 기대: 변수명, 자료형, 단위, n, 결측 수 / 행 데이터 출력 없음
- 노트: 집계만 출력하는 규칙이 계약서에 있음을 다음 장에서 연결

### S11 CLAUDE.md = AGENTS.md: 프롬프트가 아니라 계약서 (1.5)
- 유형: 설정 발췌(setup-claude-md-six-blocks)
- 본문: 6블록: 목적과 상태 / 역할 / 행동 규칙 / 코딩 규칙 / 윤리 제약 / 저장 규칙 / 같은 내용을 두 파일로(Claude Code, Codex, Copilot 공용)
- 노트: 세션마다 읽힘. 교정이 생기면 여기 적음. 레포 CLAUDE.md 상태 줄 예시

### S12 계약서에 정의를 적어 두면 에이전트는 묻지 않는다: MetS 정의 다섯 줄 (1)
- 유형: 설정 발췌(06-contract-mets-definition) + 코드 변수 `mets_c1–c5`
- 본문: 허리둘레 ≥ 90 cm / TG ≥ 150 / HDL < 40 / BP ≥ 130/85 또는 약물 / 공복혈당 ≥ 100 또는 약물
- 노트: 대화 로그 3건 어디에도 정의를 묻는 장면 없음

### S13 경계: 폴더와 권한 (1.5) (2026-10-30 S13, S14 통합. 개념 장, 폴더 트리 장, 권한 JSON 장 → 1장)
- 유형: 폴더 트리 축약 + 권한 원칙 3줄 + 장면 1줄
- 본문: 좌 agent_bot 날짜 폴더 트리 5줄 / 우 읽기 전용, 산출물과 외부 폴더 명시, 파괴적 명령은 매번 승인, `Bash(rm -f *.pdf)` 잔존
- 노트: allow 목록(curl, WebFetch europepmc, PubMed MCP 2개, additionalDirectories)은 노트로. 출처: 레포 settings.local.json(마스킹), CLAUDE.md 136–137행
- 이유: 통계 청중에게 settings.json 문법은 불필요. 원칙과 장면만 남김. 약 2분 절감

### S15 스킬: 같은 지시를 세 번 하면 파일로 만든다 (1.5)
- 유형: 설정 발췌(setup-skill-lecture-review, setup-skill-session-memory, setup-skills-ss-bundle 중 2개)
- 본문: SKILL.md = 트리거 문구(description) + 절차 + 출력 위치 / 예: 점검 스킬, 세션 메모리 스킬, 분석 묶음 스킬
- 노트: description에 사용자 말투를 넣어 자동 발동
- 2026-10-30 변경: 개념 장 본문은 원칙만(예시는 노트). 예시 장은 타 프로젝트(lecture-review, ss 묶음) 발췌 대신 사례 기반 가상 스킬 verify-numbers로 교체. 사례 레포에 스킬이 없으므로 "가상 예, 실제 파일 아님"을 label로 명시
  - 출처: 09-verify-numbers-script(스크립트 헤더, 실행 결과), 11-methods-draft-and-number-sourcing(§D 절차). description 발동 문구는 발표 전 로그 원문 확인

### S15b CLAUDE.md와 스킬의 차이 (1.5) (2026-10-30 추가, 스킬 개념과 예시 뒤. 스킬을 본 다음 비교)
- 유형: 비교표 4행(읽히는 때 / 담는 것 / 개수 / 넣는 기준) + 예 1줄
- 본문: 항상 vs 발동 시 / 목적, 역할, 정의, 규칙 vs 절차, 체크리스트, 출력 / 하나 vs 여럿 / "모든 작업에 해당하는가" vs "세 번째 시키는가" / 예: 집계값만 출력 → CLAUDE.md, 표본크기 민감도 표 → 스킬
- 노트: 잘못 넣었을 때의 양상(규칙을 스킬에: 다른 작업에서 빠짐 / 절차를 CLAUDE.md에: 파일이 길어져 뒤쪽 규칙 무시). 비유는 구두로만
- 이유: 프롬프트 설정이 낯선 청중이 둘의 차이를 가장 먼저 물음(사용자 지적 2026-10-30)

### S15c 하네스: 개념과 역할 (1.5) (2026-11-16 추가, 비교 장 뒤)
- 본문: 모델을 감싸고 돌리는 프로그램, Claude Code 자체가 하네스 / 루프: 모델 호출 → 도구 실행 → 결과 반환 / 여섯 요소: 실행, 도구, 컨텍스트, 상태, 수명주기, 검증 / 지침 파일, 스킬, MCP, memory는 하네스 입력 / 설정 창구: settings.json, 지침 파일, MCP 등록 / 훅
- 노트: 챗봇과 Claude Code는 같은 모델, 1막의 차이는 하네스 차이. 깊이 들어가지 않음
- 출처: 여섯 요소 H=(E,T,C,S,L,V)는 "Agent Harness for LLM Agents: A Survey" preprints.org 202604.0428(2026-04), 레포 Gloriaameng/Awesome-Agent-Harness / "도구에서 플랫폼으로"는 "Harness Engineering: A Source-Code Study of Eleven Systems" arXiv:2609.00006(2026-07) / "같은 모델, 다른 결과"는 같은 논문이 인용한 Harness-Bench(2026) / 훅 예는 일반 예(이 레포에 훅 설정 없음, 2026-10-21 비밀 검사는 수동) / 재대조 규칙은 이 발표 CLAUDE.md 행동 규칙 4
- 확인 필요: 발표 1주 전 Claude Code 훅, settings.json 항목명 최신판과 대조

### S15d 하네스와 지침 파일의 차이 (1) (2026-11-16 추가)
- 본문: 표 3열(하네스 / CLAUDE.md / 스킬) x 5행(무엇인가, 누가 만드나, 정하는 것, 바꾸는 법, 없으면) / 사례: 집계값 규칙은 파일, 매 세션 읽어 넣고 행 출력 명령을 권한 창에 멈추는 것은 하네스
- 노트: SKILL.md는 공개 표준이라 Claude Code, Codex, Cursor에서 동작. CLAUDE.md는 AGENTS.md로 이름만 바꾸면 Codex가 읽음
- 출처: Agent Skills 표준 호환 범위는 K-Dense scientific-agent-skills README(2026-10 확인) / AGENTS.md 호환은 이 발표 CLAUDE.md "CLAUDE.md = AGENTS.md" / 권한 창 예는 이 발표 CLAUDE.md 화면 노출 규칙 1
- 시간: 2막에 2.5분 추가. 전체 시간 조정은 보류(부록 삭제 때와 같은 처리)

### S16 MCP: 에이전트가 외부 도구를 직접 호출한다 (1.5)
- 유형: 카드 5개
- 본문: Positron MCP(R 세션) / PubMed / bioRxiv / Clinical Trials / Scholar Gateway
- 노트: 문헌 단계(3막 ⑤)에서 실제 사용. `claude mcp list`로 연결 상태 확인. 데이터는 밖으로 나가지 않고 검색 질의만 나감

### S17 memory: 결정은 대화가 아니라 파일에 남는다 (1)
- 유형: 설정 발췌(레포 `memory/agent_bot/2026-05-06/MEMORY.md` 4줄)
- 본문: 파일당 사실 1건 / `MEMORY.md`가 색인 / 세션 시작 시 먼저 읽음 / 예: 출력 폴더 규칙, 프로젝트 상태 스냅샷
- 노트: 2026-05-06 세션에서 에이전트가 스스로 만든 memory 발췌. 다음 세션이 이어받은 근거

### S18 오케스트레이션(간단히): 쓰는 모델과 검토하는 모델을 다르게 둔다 (1)
- 유형: 다이어그램(계약서 하나, 오케스트레이터 둘, 워커 둘)
- 본문: Claude Code(Fable) + Copilot(Astra) / 워커 Opus, Terra / 검토는 다른 계열 모델 / 디스패처가 한도 소진 시 대체
- 노트: 이 발표자료 자체가 이 구조로 만들어짐. 깊이 들어가지 않음. 질문 나오면 구두로 보충

## 3막. 사례 (25분) [2026-11-02 재구성]

research-example 폴더에서 처음부터 다시 진행한 작업 녹화가 소재. 리뷰어 대응 제외, 해석은 분석에 포함. 이전 3막(로그 회고형 17장)은 `output/agent/2026-11-02/act3-v2-archive/`에 보관. 각 장의 `[녹화 후]` 자리는 녹화와 로그 확인 뒤 채움.

| 장 | 제목 | 분 |
|---|---|---|
| S20 | 출발 상태와 규칙 | 1 |
| S21, S21b, S21v | ① 전처리 / ① 확인 요청: 재산출 MetS와 원 변수의 불일치 / ① 영상: 자료 정제 | 2.5 + 1.5 + 1 |
| S22 | ② 탐색 | 2.5 |
| S23, S23b | ③ 가설 설정 / ③ 설계 검토: 순환성과 희소 셀 | 2.5 + 1.5 |
| S23v | ②③ 영상: 탐색과 분석계획서(한 영상, 2026-11-02 구조 변경) | 1 |
| S24, S24b, S24v | ④ 분석 / ④ 결과와 해석 / ④ 영상: 분석 | 2.5 + 2 + 1 |
| S25, S25b | ⑤ 참고문헌 수집 / ⑤ 규칙 위반: 참고 금지 논문 | 2 + 1.5 |
| S26, S26v | ⑥ 초안 작성 / ⑥ 영상: 원고 초안 | 2 + 1 |
| S27 | 연구자 확인 지점 | 1.5 |
| 합계 | | 27 |

- 출처: research-example `CLAUDE.md`, `docs/analysis-plan.md`, `.claude/skills/research-orchestration/SKILL.md`(2026-11-02 확인). 녹화 후 run 폴더(`agent/<날짜>_<작업요약>/`)와 `docs/progress.md`를 출처로 추가
- 수치: 재분석 결과라 출판본과 다를 수 있음. 대조 기준 결정 필요(CLAUDE.md 행동 규칙 2)
- 영상: 장마다 YouTube 1개, ID 자리 `YOUTUBE_ID_1`–`6`
- S21, S21b 출처(2026-11-02 채움): research-example 세션 로그(2026-11-02 03:15–04:41 KST, 오케스트레이터 Claude Fable 5.1, 워커 stats-analyst Claude Opus 5.5). 프롬프트 인용은 사용자 메시지 원문, 에이전트 인용은 오케스트레이터 보고 메시지 원문
- S21 수치: `code/agent/2026-11-02_공군자료정제/output/01_clean_airforce_flow.csv`(2,827 → 2,739), `2026-11-02_KNHANES정제/output/02_clean_knhanes_flow.csv`(6,265 → 1,174), `2026-11-02_자료병합/output/03_merge_datasets_summary.md`(3,913 × 55, MetS 11.2% vs 39.6%, 연령 36.3 vs 44.1). 리코딩 검증 14/14은 공군 README
- S21b 수치: `2026-11-02_공군자료정제/output/mets_components_af.csv`(METS_new 308, METS_orig 290), `mets_discordance_af.csv`(30 / 5 / 17), 공군 summary.md(SBP 임계값 탐색 최소 21건)
- 영상: `C:/Users/Boncho/Videos/화면 녹화/data-preprocessing.mp4` 63분 → `data-preprocessing-2x.mp4`
- S22, S23, S23b 출처(2026-11-02 채움): 세션 로그 578f1270(KST 05:01–05:15, 탐색과 완전사례), 4511cebe(KST 05:22–05:51, SAP v2.0–2.2). 프롬프트와 에이전트 인용은 원문. 수치: `code/agent/2026-11-02_완전사례/README.md`(3,823 × 48, 2,738 / 1,085, 89명 중 71명 GPAQ), SAP v2.0 보고(검출 가능 6 pp, d ≈ 0.19, 60세 이상 25명), v2.2 보고(72%, WC Q2 139명, TG Q1 117명), `docs/analysis-plan.md` v2.2
- S23 혼선 장면(2026-11-02 반영): 세션 4511cebe KST 06:12–06:29. 연령표준화 질문 → §5-4 보강 → "H2에서는 보정이 필요가 없어" → H2 전체 비보정 → 재확인 메시지(06:28) → H2a 보정 OR 복원, 연령군 모형 H1→H2b 이동. progress.md 마지막 두 줄, SAP §1 표, §6.2, §13(미결 8개)
- S24–S27 출처(2026-11-02 채움): 세션 4511cebe. 분석 KST 06:36–08:55, 문헌 09:03–09:30, 초안 09:35–09:50. 사용자 메시지 원문(대기열 입력 포함: "해당 논문은 참고하지 않는다라는 규칙을 줬는데" 09:22, "지금 분석은 해당 논문을 재현하기 위함이야" 09:23, "알아 AI를 이용한 논문작성에 대한 예시로 쿼리를 준거야" 09:36). 로그 타임스탬프는 UTC, 9시간 더해 KST
- S24, S24b 수치: research-example `output/tables/table2_prevalence_or.csv`(MetS 0.19 → 0.27 (0.23–0.33), 혈압 1.41 → 2.09), `table3_subgroups.csv`(연령군 LR p 0.914), `table5_biomarker_interaction.csv`(요산 OR 1.59 vs 1.25, Δβ 0.24 (0.07–0.42) p 0.006, Model 2 Δβ 0.26 p 0.012), 오케스트레이터 보고(지질약 복용자 LDL 93.5, MetS 91%)
- S24b 출판본 대조(노트 전용): 출판 aOR 0.30, 혈압 2.12(CLAUDE.md 사례 논문). 재현은 0.27, 2.09
- S25 수치: `docs/progress.md`(문헌 4 run 232편), 오케스트레이터 보고(59 / 87 / 26 / 60). Lee JH 2018 doi:10.3346/jkms.2018.33.e172, Schulze 2000 doi:10.1023/a:1011020823807, Choi 2022 doi:10.1002/pds.5437
- S25b: 워커 보고 원문 "같은 비교가 이미 출판되어 있습니다."(문헌 A 워커, 09:22). 규칙 부재 근거: 2026-11-02 새벽 research-example grep 결과 없음, CLAUDE.md 92행 규칙 줄과 파일 수정 시각 09:49, progress.md 39행
- S26: 오케스트레이터 보고 09:36(저널 추천), 09:41(투고 규정), 09:50(원고 인프라). `docs/journal-shortlist.md`, `docs/journal-guidelines.md`. 원고 미완성
- 선행 지방간 논문 서지 정정: PubMed 기준 Aerosp Med Hum Perform 2025;96(10):894–902, PMID 41043813(research-example 문헌 워커 확인). 슬라이드 노트 반영, 이 프로젝트 CLAUDE.md는 96(9)로 남음

## 4막. 효과와 팁 (5분)

### S38 4. 빨라진 것과 그대로인 것 (1.5)
- 카드 2개: 에이전트에게 간 것(코드, 표, 문헌 정리, 숫자 검증, 초안) / 사람에게 남은 것(질문, 설계, 해석, 인용 판단, 최종 검토)
- 노트: `[여기에: 체감 효과, 예: 리뷰어 대응 기간]`

### S39 내일 바로 할 수 있는 설정 3가지 (1.5)
- 본문: CLAUDE.md 한 장 쓰기(6블록) / 산출물 폴더 나누기 / 숫자 검증 스크립트 하나
- 노트: 스타터킷에 템플릿

### S40 AI 활용 논문의 윤리 (1) [2026-11-02 교체: 로그 장면 3개 → 일반 윤리]
- 본문: 저자 자격 / 사용 공개 / 최종 책임. 미공개 사용은 정정 또는 부정행위
- 출처: ICMJE Recommendations, AI Use by Authors https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html (2026-11-02 확인)
- 이전 내용(묻지 않고 고름, non-collapsibility, 완료 선언)은 `output/agent/2026-11-02/act4-before-limits.qmd`

### S40b 최근 이슈 1: 가짜 참고문헌 (1) [2026-11-02 추가, 11-02 3장으로 분할]
- 본문: PubMed 전수 조사 / 증가 추세 / 학계 밖(Deloitte)
- 출처: Retraction Watch 2026-05-07 https://retractionwatch.com/2026/05/07/one-in-277-pubmed-indexed-papers-in-2026-shows-fabricated-references-says-analysis/ (Topaz 외, Lancet 서한. 250만 편, 9,710만 건, 4,046건/2,810편, 1/2,828 → 1/458 → 1/277)
- 출처: NeurIPS 2025 가짜 인용 100건 arXiv 2602.05930. CS 학회 2.6%(2025) vs 0.3%(2024)는 2차 보도(SciCampus가 Nature 분석 인용), 1차 미확인
- 출처: Deloitte 환불 AP 보도 2025-10-07 https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ , Fortune https://fortune.com/2025/10/07/deloitte-ai-australia-government-report-hallucinations-technology-290000-refund (계약 A$440,000, GPT-4o 기반 도구 공개, 마지막 분할금 환불)

### S40c 최근 이슈 2: AI 심사와 숨은 프롬프트 (1)
- 본문: 심사자가 AI를 씀(ICLR 2026, NIH) / 저자가 AI 심사자를 노림(Nikkei) / 결과
- 출처: Pangram Labs ICLR 2026 분석, 2차 보도 https://news.bensbites.com/posts/52410-pangram-labs-21-of-the-75800-peer-reviews-submitted-for-iclr-2026-a-major-ml-conference-were-fully-ai-generated-and-50-contained-signs-of-ai-use . 다른 탐지기(Sem-Detect)는 5%로 추정(arXiv 2605.21713). 1차 보고서 미확인, 발표 전 확인
- 출처: NIH NOT-OD-23-149 https://grants.nih.gov/grants/guide/notice-files/NOT-OD-23-149.html (2023-06-23)
- 출처: Nikkei 조사 2차 보도 TechCrunch 2025-07-06 https://techcrunch.com/2025/07/06/researchers-seek-to-influence-peer-review-with-hidden-ai-prompts , The Decoder https://the-decoder.com/researchers-hide-prompts-in-scientific-papers-to-sway-ai-powered-peer-review/ (17편, 14개 대학). Lin Z. arXiv 2507.06185(18편), CACM https://cacm.acm.org/opinion/hidden-prompts-in-manuscripts-exploit-ai-assisted-peer-review/ . 72% 설문: Research Integrity and Peer Review https://link.springer.com/article/10.1186/s41073-025-00187-7
- 편수 불일치: Nikkei 17편, Lin 18편. 슬라이드는 Nikkei 기준, 노트에 Lin 기준 병기

### S40d 최근 이슈 3: 워터마크와 표시 의무 (1)
- 본문: 법(한국, EU) / Claude 텍스트 워터마크 / 한계
- 출처: Anthropic https://www.anthropic.com/news/claude-text-watermark (2026-08-14, 09-01 갱신), 지원 문서 https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content
- 출처: EU AI Act 50조 2026-08-02 시행, 실천강령 서명(2차 보도, 1차 EU 문서 미확인)
- 출처, 원리 노트: Dathathri 외. Scalable watermarking for identifying large language model outputs. Nature 2024;634:818–823. doi:10.1038/s41586-024-08025-4 / 참조 구현 https://github.com/google-deepmind/synthid-text (창 4, 깊이 30, Threefry, 63비트 키는 논문과 구현 기준) / Nemecek 외. arXiv 2609.09604
- 출처: 한국 AI 기본법 2026-01-22 시행, 과태료 최대 3천만 원, 1년 이상 유예. Korea JoongAng Daily https://www.koreajoongangdaily.com/business/koreas-groundbreaking-ai-law-requires-watermarks-on-generated-content-but-enforcement-gaps-remain/12094830 . 유예 연장 법안 처리 여부 미확인

### S41 함께 쓰면 좋은 도구 (1) [2026-11-02 교체: 스타터킷 → 도구 권고]
- 본문: Git, GitHub / renv / Zotero. 각 카드에 "왜"를 첫 줄로. 마지막 줄 공통점(추적, 되돌림, 재현)
- 출처: research-example `.gitignore`와 git 저장소 없음(2026-11-02 확인), `docs/progress.md` run 폴더 기록 규칙. renv, Zotero Better BibTeX는 일반 기능 설명. Claude Code 체크포인트 범위는 발표 1주 전 공식 문서 재확인
- 이전 스타터킷 장 내용(QR 자리, 통제 지점 카드 4개)은 git 이력에 남음
