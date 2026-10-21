# 발표 아웃라인: 연구 생산성 향상을 위한 Agent AI 기반 워크플로우: 데이터 분석에서 논문 작성까지

작성: 2026-10-19, slide-writer(Claude Opus 5.5). 상태: 아웃라인 초안, 사용자 확인 전(talk-orchestration 2단계)
근거: `CLAUDE.md`(구성, 노출 규칙, 서지), `memory/talk-scenes-from-repo.md`, `slides/excerpts/` 33개(장면 26 + setup 7)

## 총계

| 섹션 | 막 | 슬라이드 수 | 분 |
|---|---|---|---|
| 1 병목 | 1막 | 5 (표지 포함) | 3.0 |
| 2 기존 vs Agentic | 1막 | 2 | 2.0 |
| 3 파이프라인 한 장 | 1막 | 2 | 2.0 |
| **1막 소계** | | **9** | **7.0** |
| 4 환경 + CLAUDE.md | 2막 | 6 | 6.0 |
| 5 연구 질문 | 2막 | 2 | 2.0 |
| 6 계약서 + 코드북 → 설계안 → 결정 | 2막 | 4 | 6.0 |
| 7 전처리, 코드 (녹화 D1) | 2막 | 4 | 6.0 |
| 8 분석 설계, probit | 2막 | 7 | 7.0 |
| 9 검증 (녹화 D2) | 2막 | 6 | 5.0 |
| 10 표, 그림 (라이브 D3) | 2막 | 3 | 4.0 |
| 11 원고 + 역할 분리 에이전트 | 2막 | 5 | 5.0 |
| **2막 소계** | | **37** | **41.0** |
| 12 통제 지점 | 3막 | 5 | 3.0 |
| 13 효과, 한계 | 3막 | 4 | 2.0 |
| **3막 소계** | | **9** | **5.0** |
| **본 발표 총계** | | **55** | **53.0** |
| Q&A (부록 5장, 시간 미배정) | | (5) | 7.0 |

시간 버퍼는 0분이다. 넘칠 때 줄일 순서는 문서 끝 "넘칠 때 줄일 순서"에 적었다.

## 작성 규칙 (이 아웃라인 전체)

- 번호 `S01`–`S55`는 덱 전체 순번, 괄호 안 `4-2`는 섹션-순서.
- 각 섹션의 첫 슬라이드가 `slides/index.qmd`의 섹션 블록 시작이다. 블록 제목은 `## <섹션번호>. <메시지 제목>`으로 쓰고 상단에 파이프라인 진행바(질문 → 데이터 이해 → 분석 → 검증 → 논문 → 재현)를 둔다.
- 3단 열 이름은 "프롬프트 / 에이전트가 한 일 / 연구자가 확인한 것"으로 고정. 프롬프트 원문이 로그에 없는 memory, qmd 장면은 첫 칸을 "맥락(프롬프트 원문 없음)"으로 쓴다.
- 에이전트 표기 두 가지를 섞지 않는다. 대화 로그(json) 장면은 **Positron Assistant(Claude Sonnet 4.6)**, memory, qmd 장면은 **DataBot(모델 미기재)**.
- 인용은 발췌본 원문 그대로. 줄일 때만 `…`. 오류 장면은 다듬지 않는다.
- 중간값은 노트에 "중간값, 원고 최종값 …"으로 병기. 출처 없는 수치는 쓰지 않고 "확인 필요"로 남긴다.
- 노트는 "말할 내용"(2–4문장)과 필요하면 "질문 대비"(통계 청중의 예상 질문), "확인 필요"로 나눈다.
- 두 논문 PDF(`references/`)는 암호 보호로 이번 작업에서 열리지 않았다. 출판본 수치는 발췌본의 pypdf 추출 문장과 `CLAUDE.md` 서지를 근거로 했다.

---

## 1막 왜

### 섹션 1. 병목 (3.0분)

| 번호 | 제목 | 분 | 유형 |
|---|---|---|---|
| S01 | 표지 | 0.25 | 텍스트 |
| S02 (1-1) | (후보) 분석 판단보다 그 판단을 코드, 표, 원고로 옮기는 일에 시간이 더 든다 | 1.0 | 다이어그램 |
| S03 (1-2) | (후보) 같은 숫자를 네 번 옮기면 틀릴 기회도 네 번 생긴다 | 0.75 | 다이어그램 |
| S04 (1-3) | 사례는 출판된 두 논문이고, 장면은 모두 실제 작업 로그에서 왔다 | 0.5 | 텍스트 |
| S05 (1-4) | 판단은 연구자가, 그 판단을 끝까지 밀고 가는 반복 노동은 에이전트가 | 0.5 | 텍스트 |

#### S01. 표지
- 시간 0.25분, 유형: 텍스트(YAML 자동 생성)
- 한 줄 메시지: 발표 제목과 사례.
- 화면: title "연구 생산성 향상을 위한 Agent AI 기반 워크플로우: 데이터 분석에서 논문 작성까지", subtitle "국민건강영양조사 vs 공군 조종사 건강검진: 대사증후군, 지방간 위험 비교 사례"
- 노트 초안: `<여기에: 자기소개 한 줄(소속, 역할)>`. 오늘 보여드릴 장면은 모두 한 레포의 실제 대화 로그, memory, 코드에서 왔고, 데이터는 구조와 집계만 화면에 올린다고 먼저 말한다.
- 출처: `.claude/skills/revealjs-deck/SKILL.md`(YAML 골격), `CLAUDE.md` 화면 노출 규칙

#### S02 (1-1). (후보 제목) 분석 판단보다 그 판단을 코드, 표, 원고로 옮기는 일에 시간이 더 든다
- 블록 제목: `## 1. <확정 제목>`
- 시간 1.0분, 유형: 다이어그램(단계별 체감 시간 막대) 또는 텍스트
- 한 줄 메시지: 연구자의 병목은 판단이 아니라 판단을 옮기는 반복 노동이다.
- 화면(6줄 이하): `<여기에: 논문 한 편 기준 단계별 체감 시간 비율. 예: 설계 / 코드 / 표, 그림 / 원고 / 리뷰어 대응>`
- 노트 초안: 발췌본이 없는 자리다. 사용자의 실제 경험(논문 한 편을 낼 때 어디서 시간이 샜는지)을 1–2문장으로 넣는다. 숫자를 넣으면 체감치라고 밝힌다. 제목도 사용자의 경험에 맞게 확정한다.
- 출처: 사용자 경험(발췌 없음)

#### S03 (1-2). (후보 제목) 같은 숫자를 네 번 옮기면 틀릴 기회도 네 번 생긴다
- 시간 0.75분, 유형: 다이어그램(R 출력 → 표 → 원고 산문 → 리뷰어 응답서)
- 한 줄 메시지: 수치가 문서 사이를 옮겨 다닐 때마다 오류가 들어올 자리가 생긴다.
- 화면: 4단 화살표 + `<여기에: 수치를 옮기다 생긴 실제 사례 1건. 논문명, 수치 없이>`
- 노트 초안: 사용자의 경험 한 건을 넣는다. 이 사슬의 마지막(응답서가 약속한 숫자를 원고에 넣기 전 재계산)은 9번 `verify-numbers.R`, 산문 숫자의 하드코딩 문제는 11번에서 다시 나온다고 예고한다.
- 출처: 사용자 경험(발췌 없음). 예고 대상: `09-verify-numbers-script.md`, `11-methods-draft-and-number-sourcing.md`

#### S04 (1-3). 사례는 출판된 두 논문이고, 장면은 모두 실제 작업 로그에서 왔다
- 시간 0.5분, 유형: 텍스트
- 한 줄 메시지: 연출이 아니라 출판까지 간 실제 작업의 로그다.
- 화면:
  - Song DH, Ku B. Aerosp Med Hum Perform 2025: 공군 1,044명, MAFLD
  - Ku B, Song DH. BMJ Mil Health 2026: 조종사 2,604 vs KNHANES 1,093, 24–61세 남성, MetS
  - 레포: 대화 로그 4개, memory, qmd, code (2026-03 ~ 2026-08)
- 노트 초안: 두 논문 모두 출판됐다. 레포의 대화 로그 4개(`conversation-finalize`, `conversation-add-analysis`, `conversation-probit-logit-prob`, 루트의 `conversation-export`)와 memory, qmd, 코드에서 장면을 골랐고, 오류 장면도 문장 그대로 보여준다.
- 출처: `CLAUDE.md` 사례 논문(doi:10.3357/AMHP.6646.2025, doi:10.1136/military-2026-003444), `memory/talk-scenes-from-repo.md` 3행, 36행

#### S05 (1-4). 판단은 연구자가, 그 판단을 끝까지 밀고 가는 반복 노동은 에이전트가
- 시간 0.5분, 유형: 텍스트
- 한 줄 메시지: 발표 전체의 주장 한 문장.
- 화면: 주장 한 줄 + "에이전트가 틀린 장면도 각색 없이 보여드립니다"
- 노트 초안: 오늘의 주장은 하나다. 분석 설계 판단은 연구자가 하고, 그 판단을 코드, 검증, 문서로 끝까지 밀고 가는 반복 노동은 에이전트가 한다. 이 주장이 이 사례에서 완전히 지켜지지 않은 지점도 13번에서 제가 먼저 꺼낸다.
- 출처: `CLAUDE.md` 목적 3, 행동 규칙 3

### 섹션 2. 기존 vs Agentic (2.0분)

| 번호 | 제목 | 분 | 유형 |
|---|---|---|---|
| S06 (2-1) | (후보) 채팅창은 코드를 건네고, 에이전트는 내 세션에서 실행하고 결과를 읽는다 | 1.0 | 표 |
| S07 (2-2) | 실행력이 커진 만큼 틀린 전제를 끝까지 밀고 가는 힘도 커졌다 | 1.0 | 텍스트 |

#### S06 (2-1). (후보 제목) 채팅창은 코드를 건네고, 에이전트는 내 세션에서 실행하고 결과를 읽는다
- 블록 제목: `## 2. <확정 제목>`
- 시간 1.0분, 유형: 표(2열)
- 한 줄 메시지: 차이는 코드 품질이 아니라 실행과 관찰을 누가 하느냐다.
- 에이전트: Positron Assistant(Claude Sonnet 4.6), 2026-03-19
- 화면(표 3행):

  | 일 | 기존 방식 | Positron Assistant 로그 |
  |---|---|---|
  | 변수명 확인 | `<여기에>` | "Column `DYSLIPIDEMIA` doesn't exist." → `names()`로 `DYSLIP` 확인 |
  | 세션 객체 확인 | `<여기에>` | `exists("reg_results")`, `file.exists(png_path)` |
  | 에러 수정 | `<여기에>` | `object 'fm_med' not found` → 세 번째 시도에서 해결 |

- 노트 초안: 왼쪽 칸은 사용자의 이전 방식으로 채운다(예: 채팅창 코드를 콘솔에 붙여넣고 에러를 다시 복사해 붙이는 왕복). 오른쪽은 모두 같은 날 로그에 있는 도구 호출이다. 장면 전체는 6, 7번에서 본다.
- 출처: `06-design-proposal-choice.md`(finalize msg[6–8]), `07-knit-failure-three-causes.md`(finalize msg[18–21]), `07-mediation-env-error.md`(finalize msg[9])

#### S07 (2-2). 실행력이 커진 만큼 틀린 전제를 끝까지 밀고 가는 힘도 커졌다
- 시간 1.0분, 유형: 텍스트(인용 2줄 + 한 줄)
- 한 줄 메시지: 에이전트는 틀린 전제 위에서도 끝까지 일한다. 멈추는 것은 연구자다.
- 에이전트: Positron Assistant(Claude Sonnet 4.6), 2026-03-10
- 화면:
  - (사용자) "결과 해석이 이상한데?"
  - (에이전트) "확인했습니다. 이전 해석에 오류가 있었습니다."
  - 그 사이 에이전트는 틀린 전제 위에 Healthy Worker Effect 서사와 논문 서술 제안까지 썼다
- 노트 초안: 9번의 미리보기다. 이 장면은 사용자 질문 자체에 전제 오류가 있었고, 에이전트가 그것을 바로잡지 않고 따라간 경우다. 전체 흐름과 두 OR의 차이는 9번에서 본다.
- 출처: `09-two-odds-ratios-confused.md`(add-analysis msg[18–21])

### 섹션 3. 파이프라인 한 장 (2.0분)

| 번호 | 제목 | 분 | 유형 |
|---|---|---|---|
| S08 (3-1) | 질문에서 재현까지 여섯 단계, 단계마다 연구자가 확인하는 지점이 있다 | 1.0 | 다이어그램 |
| S09 (3-2) | 모든 단계는 같은 세 칸으로 본다: 프롬프트, 에이전트가 한 일, 연구자가 확인한 것 | 1.0 | 다이어그램 |

#### S08 (3-1). 질문에서 재현까지 여섯 단계, 단계마다 연구자가 확인하는 지점이 있다
- 블록 제목: `## 3. 질문에서 재현까지 여섯 단계, 단계마다 연구자가 확인하는 지점이 있다`
- 시간 1.0분, 유형: 다이어그램(진행바 + 시간축)
- 한 줄 메시지: 발표의 지도. 2막의 섹션이 각 단계에 대응한다.
- 화면:
  - 진행바: 질문(5) → 데이터 이해(6) → 분석(7, 8) → 검증(9) → 논문(10, 11) → 재현(7 knit 자급자족, 9 재계산, 10 내보내기)
  - 시간축: 2026-03-10 기존 스크립트 감사 → 03-17 probit 척도 → 03-19 RQ4 회귀, knit → 03-21 해석 문서, Methods 초안 → 05-09 원고 개정 → 08-14~16 리뷰어 대응, `verify-numbers.R`
- 노트 초안: 오늘 보여드릴 장면을 단계와 날짜에 올려 둔 그림이다. 3월은 분석, 5월은 원고, 8월은 리뷰어 대응이었다. 단계 이름이 사용자의 실제 워크플로와 다르면 `<여기에: 사용자 단계명>`으로 바꾼다.
- 출처: `.claude/skills/revealjs-deck/SKILL.md`(진행바 6단계). 날짜: `06-script-audit-questions.md`, `08-probit-logit-probability-scale.md`, `06-design-proposal-choice.md`, `07-factor-prevalence-zero.md`, `08-unweighted-decision.md`, `09-verify-numbers-script.md`

#### S09 (3-2). 모든 단계는 같은 세 칸으로 본다: 프롬프트, 에이전트가 한 일, 연구자가 확인한 것
- 시간 1.0분, 유형: 다이어그램(3단 견본)
- 한 줄 메시지: 장면을 읽는 형식과 두 에이전트 표기를 먼저 정한다.
- 화면:
  - 3칸 견본: 프롬프트 | 에이전트가 한 일 | 연구자가 확인한 것
  - 대화 로그 장면: Positron Assistant(Claude Sonnet 4.6)
  - memory, qmd 장면: DataBot(모델 미기재)
  - 오류 장면은 로그 문장 그대로, 데이터는 구조와 집계만
- 노트 초안: 대화 로그(json)에는 모델명이 기록돼 있지만 memory, qmd 산출물은 저자란이 "Databot (Agent Analysis)"일 뿐 모델이 적혀 있지 않다. 그래서 둘을 같은 모델로 가정하지 않고 표기를 나눈다. 프롬프트 원문이 없는 장면은 첫 칸을 "맥락"으로 쓴다.
- 출처: `memory/talk-scenes-from-repo.md` 3행, 37행, `08-probit-choice-reason.md`(qmd 저자란), `CLAUDE.md` 화면 노출 규칙, 행동 규칙 3

---

## 2막 어떻게

### 섹션 4. 환경 + CLAUDE.md (6.0분)

| 번호 | 제목 | 분 | 유형 |
|---|---|---|---|
| S10 (4-1) | 에이전트는 내 R 세션 안에서 다섯 가지 도구로 일한다 | 1.0 | 다이어그램 |
| S11 (4-2) | CLAUDE.md는 프롬프트가 아니라 계약서다: 여섯 블록 | 1.0 | 코드 |
| S12 (4-3) | 규칙 두 줄이 이후 모든 검증의 바탕이 된다: "표 값이 도출되는 과정을 남겨라" | 1.0 | 텍스트 |
| S13 (4-4) | MetS 정의 다섯 줄이 계약서에서 코드 변수 mets_c1–c5로 그대로 이어진다 | 1.0 | 코드 |
| S14 (4-5) | 정의를 적어 두면 에이전트는 묻지 않고, 적지 않은 자리는 에이전트가 채운다 | 1.25 | 표 |
| S15 (4-6) | 결정은 대화가 아니라 memory/ 파일에 남는다 | 0.75 | 코드 |

#### S10 (4-1). 에이전트는 내 R 세션 안에서 다섯 가지 도구로 일한다
- 블록 제목: `## 4. 에이전트는 내 R 세션 안에서 다섯 가지 도구로 일한다`
- 시간 1.0분, 유형: 다이어그램
- 한 줄 메시지: Positron의 에이전트는 채팅창이 아니라 세션, 파일, 터미널에 손이 닿는다.
- 에이전트: Positron Assistant(Claude Sonnet 4.6), 2026-03
- 화면: Positron 창(편집기 / R 콘솔, 세션 / 파일 / 터미널)과 도구 다섯 개 `todoWrite`, `executeCode`, `read`, `write`, `bash`. 도구마다 로그 예시 한 줄(할 일 4항목, `names(afhe_khanes_final)`, 스크립트 721줄 읽기, 파일 저장, `cat`)
- 노트 초안: 도구 이름은 2026-03 로그에 기록된 그대로다. 경계도 있다: `read`가 "ENOPRO: No file system provider found"로 실패하자 `bash`의 `cat`으로 읽었고, `write`가 "outside the workspace and not currently open in an editor"로 실패하자 `bash`로 파일을 만들었다. 연구자는 에이전트가 경계에서 우회한다는 사실을 알고 있어야 한다.
- 확인 필요: 도구 이름과 동작은 발표 1주 전 최신 Positron과 다시 대조(`CLAUDE.md` 행동 규칙 4).
- 출처: `06-design-proposal-choice.md`(finalize msg[6–8]), `06-script-audit-questions.md`(add-analysis msg[2–3]), `07-knit-failure-three-causes.md`(finalize msg[18–21]), `07-user-cancels-tool-call.md`(finalize msg[12–15])

#### S11 (4-2). CLAUDE.md는 프롬프트가 아니라 계약서다: 여섯 블록
- 시간 1.0분, 유형: 코드(마크다운 헤더 발췌)
- 한 줄 메시지: 세션마다 같은 조건으로 시작하게 하는 문서는 여섯 블록으로 짠다.
- 화면: 헤더 발췌 `## 프로젝트 개요`(상태 줄) / `## 역할` / `## 행동 규칙` / `## 코딩 규칙` / `## 윤리적 제약` / `## 생성 파일 저장 공간`, 그리고 상태 줄 "상태: 데이터 전처리 완료, 기초 및 최종 분석 완료, Quarto 분석 보고서 작성 완료"
- 노트 초안: 원본 381행 중 헤더만 보여준다. 역할 블록은 "통계학 전문가(이론, 실무 모두)", "의학(내과, 내분비학)/역학/생리학 전문가"로 시작한다. 상태 줄은 새 세션의 에이전트가 어디서부터 이어갈지를 정한다. 이 발표 프로젝트도 같은 구조를 쓴다(11번).
- 확인 필요: 대화 로그의 에이전트는 "AGENTS.md 규칙"을 언급한다(`07-user-cancels-tool-call.md`). 레포의 AGENTS.md와 CLAUDE.md가 같은 내용인지 확인.
- 출처: `setup-claude-md-six-blocks.md`(레포 CLAUDE.md 1, 3, 5, 10, 20–23, 26… 행), `06-contract-mets-definition.md`(레포 CLAUDE.md 5행)

#### S12 (4-3). 규칙 두 줄이 이후 모든 검증의 바탕이 된다: "표 값이 도출되는 과정을 남겨라"
- 시간 1.0분, 유형: 텍스트(인용)
- 한 줄 메시지: 규칙은 오류를 막지 않는다. 오류를 찾을 길을 남긴다.
- 화면(인용):
  - "7. quarto 문서에서 테이블 및 그림 생성 시 사용하기 위해 만든 데이터셋은 quarto 문서 청크에 남김"
  - "- 직접 테이블을 생성하지 말고 테이블 값이 도출되는 과정을 반드시 남김"
  - "9. 모든 수치 결과는 그 도출 과정을 문서에 포함"
  - "1. 결과 생성 및 해석 시 추론은 최대한 배제하고 근거에 기반한 답변 도출"
- 노트 초안: 규칙 7, 9 때문에 8번의 약물 불균형 표가 `group_by → summarise → lancet_gt` 청크로 남았고, 9번의 `verify-numbers.R`이 같은 데이터에서 다시 계산할 수 있었다. 규칙 1이 있었는데도 9번의 두 OR 혼동은 일어났다. 규칙의 역할은 예방이 아니라 추적 가능성이다.
- 출처: `06-contract-mets-definition.md`(레포 CLAUDE.md 26–39행), `08-medication-imbalance-report.md`(2026-03-10 보고서 qmd 428–455행), `09-verify-numbers-script.md`

#### S13 (4-4). MetS 정의 다섯 줄이 계약서에서 코드 변수 mets_c1–c5로 그대로 이어진다
- 시간 1.0분, 유형: 코드(인용) + 화살표
- 한 줄 메시지: 정의와 변수명이 계약서, 코드북, 코드, 표에서 같은 이름으로 이어진다.
- 화면(인용, 레포 CLAUDE.md 252–260행):
  - "복부비만 : 남성: ≥ 90cm / 여성: ≥ 85cm (허리둘레): mets_c1"
  - "중성지방 : ≥ 150 mg/dL 또는 이상지질혈증 약물 복용 중 :mets_c2"
  - "HDL : 남성: < 40 mg/dL / 여성: < 50 mg/dL 또는 약물 복용 중 :mets_c3"
  - "혈압 : 고혈압 약물 복용중 또는 수축기 혈압  ≥ 130 또는 이완기 혈압  ≥ 85 :mets_c4"
  - "공복혈당 : ≥ 100 mg/dL 또는 당뇨병 약물 복용 중 :mets_c5"
  - → 코드북 라벨 `mets_c1` "Abdominal Obesity (waist circumference ≥ 90 cm)"
- 노트 초안: 허리둘레 90 cm와 혈압 130/85는 연구자가 정해 적은 기준이고, 에이전트는 이 정의를 바꾸지 않았다. 같은 절의 표본 흐름(조종사 2,827 → 2,604, KNHANES 6,265 → 1,093)은 논문 2 최종값과 같다. 정의마다 "또는 약물 복용 중"이 붙어 있다는 점은 8번 약물 보정에서 다시 쓴다.
- 출처: `06-contract-mets-definition.md`(레포 CLAUDE.md 192–202, 252–260행), `07-data-structure.md`(코드북 `variable_label`)

#### S14 (4-5). 정의를 적어 두면 에이전트는 묻지 않고, 적지 않은 자리는 에이전트가 채운다
- 시간 1.25분, 유형: 표("없을 때 vs 있을 때")
- 한 줄 메시지: 계약서가 말한 곳에서는 에이전트가 어긋남을 찾고, 침묵한 곳에서는 에이전트가 이유를 지어 넣는다.
- 화면(표):

  | | 에이전트의 행동 | 장면 |
  |---|---|---|
  | 있을 때: MetS 정의 | 로그 3종에 정의, 허리둘레 기준, 공복 질문 0건. 대신 "`demo_tbl`에 MeTS 기준 항목이 포함되지 않음 → 의도적인지 확인 필요" | 6번 |
  | 있을 때: 저장 위치 | "AGENTS.md 규칙에 따라 `code/agent_bot/2026-03-19/` 폴더에" | 12번 |
  | 없을 때: 모형 선택 이유 | "The probit link was chosen to match the visual representation conventions used in the companion figure" | 8번 |
  | 없을 때: 재현성 trade-off | 매개분석 결과값을 "하드코딩한 `med_summary` tibble로" | 7번 |

  선택 행: `<여기에: 계약서 없이 일했던 시기의 경험 1건>`
- 노트 초안: 계약서에 정의가 있던 곳에서 에이전트는 정의를 되묻지 않았고, 대신 표에서 기준 행이 빠진 것을 짚었다. 계약서가 말하지 않은 곳에서는 에이전트가 모형 선택 이유를 지어 넣었고, 재현성과 실행 시간 사이의 trade-off도 스스로 정했다. 아래 두 칸은 7번과 8번에서 다시 본다.
- 확인 필요: 레포 CLAUDE.md(381행)에 모형 선택 근거나 재현성 관련 규칙이 정말 없었는지. 발췌본은 일부 행만 담고 있다.
- 출처: `06-contract-mets-definition.md`(memory/talk-scenes-from-repo.md 10행 인용), `06-script-audit-questions.md`(add-analysis msg[3]), `07-user-cancels-tool-call.md`(finalize msg[12–15]), `08-probit-choice-reason.md`(05_statistical_analysis_methods.qmd 96–112행), `07-knit-failure-three-causes.md`(finalize msg[21])

#### S15 (4-6). 결정은 대화가 아니라 memory/ 파일에 남는다
- 시간 0.75분, 유형: 코드(두 발췌 나란히)
- 한 줄 메시지: 계약서는 고정되고, 세션의 결정과 교훈은 memory 파일로 쌓인다.
- 화면:
  - 왼쪽(사례 레포 `memory/agent_bot/2026-05-09/session-summary.md` §7 "주요 의사결정 / 사용자 피드백"의 항목명): "표, 그림 미포함", "em-dash 지양", "저자 문체 유지", "압축 우선"
  - 오른쪽(기억 스킬 규칙): "**파일당 사실 1건.**" / "상대 날짜("어제", "다음 주")는 절대 날짜(YYYY-MM-DD)로 변환해 기록." / "이미 repo가 기록하는 내용(코드 구조, CLAUDE.md 내용, 파일 목록)은 저장하지 않는다."
- 노트 초안: 사례 레포의 2026-05-09 요약에는 사용자가 요구한 문체 규칙이, 2026-08-16 요약에는 "exit code만으로 성공을 판단하면 안 됨" 같은 교훈이 남았다(9번). 오른쪽은 다른 프로젝트(회귀분석 강의 노트)에서 쓰는 기억 스킬의 규칙이다. 다음 세션의 에이전트는 대화가 아니라 이 파일을 읽고 이어간다.
- 출처: `08-unweighted-decision.md`(session-summary 2026-05-09 §7), `setup-skill-session-memory.md`, `09-render-success-missing-figure.md`(session-summary 2026-08-16 §5-3)
- 메모: `setup-skill-session-memory.md`는 섹션 9로 표시돼 있으나 4번으로 옮겼다.

### 섹션 5. 연구 질문 (2.0분)

| 번호 | 제목 | 분 | 유형 |
|---|---|---|---|
| S16 (5-1) | 논문 1의 부차적 발견이 논문 2의 질문이 됐다: 조종사에서 두드러진 요산 | 1.0 | 다이어그램 |
| S17 (5-2) | 요산을 왜 넣었는지 리뷰어가 물었고, 답한 것은 연구자다 | 1.0 | 텍스트 |

#### S16 (5-1). 논문 1의 부차적 발견이 논문 2의 질문이 됐다: 조종사에서 두드러진 요산
- 블록 제목: `## 5. 논문 1의 부차적 발견이 논문 2의 질문이 됐다: 조종사에서 두드러진 요산`
- 시간 1.0분, 유형: 다이어그램(두 논문 화살표)
- 한 줄 메시지: 연구 질문은 에이전트가 아니라 앞 논문에 남은 의문에서 나왔다.
- 화면:
  - 논문 1 (Aerosp Med Hum Perform 2025): 공군 1,044명, MAFLD. 조종사 하위군 다변량 로지스틱 회귀에서 요산 OR 1.83 (95% CI 1.32–2.55). 비조종사에서는 유의하지 않음
  - → 논문 2 (BMJ Mil Health 2026): 조종사 2,604 vs KNHANES 1,093. MetS 11.1% vs 37.1%, aOR 0.30
  - 요산: 일반 남성에서는 MetS와 유의한 연관 없음, 조종사에서 per-SD OR 1.35 (95% CI 1.17–1.55). 집단 차이 Δβ 0.27 (p = 0.009)
- 노트 초안: 논문 2 Discussion이 이 연결을 직접 쓴다: "The urate finding is particularly notable given our prior work." 지방간 논문에서 조종사에게만 두드러졌던 요산이 "일반 남성과 비교하면 어떤가"라는 다음 질문이 됐다. 이 단계에서 에이전트의 몫은 거의 없었다.
- 확정(사용자 2026-10-20): OR 1.83은 조종사 하위군 다변량 로지스틱 회귀의 추정치다. 논문 1 Abstract도 "among pilots, … uric acid (OR = 1.83)"로 적는다.
- 확인 필요: (2) per-SD OR 1.35는 r2 qmd 416행 기준, 출판본 대조 필요(fact-checker 단계). (3) 일반 남성의 per-SD OR 수치는 발췌에 없어 쓰지 않았다. (4) MAFLD 27.7% vs 34.7%는 어느 쪽이 조종사인지 발췌에 명시가 없어 화면에서 뺐다.
- 출처: `05-urate-origin.md`(논문 2 Introduction, Discussion, r2 qmd 352, 416, 426행, 출판본 Abstract 대조), `CLAUDE.md` 28–31행, doi:10.3357/AMHP.6646.2025, doi:10.1136/military-2026-003444

#### S17 (5-2). 요산을 왜 넣었는지 리뷰어가 물었고, 답한 것은 연구자다
- 시간 1.0분, 유형: 텍스트(인용)
- 한 줄 메시지: 질문의 정당화는 연구자의 맥락에서 나온다.
- 에이전트: DataBot(모델 미기재). r2 원고를 저자 문체로 재작성
- 화면:
  - "Serum urate is not a conventional MetS screening test, so its inclusion warrants explanation."
  - "Aircrew differ in that urate is already in the standard aeromedical diagnostic panel at no added cost, …"
  - Reviewer 2 항목 R2-3 "Urate 사용 근거 상술"에 답해 r2에서 추가
- 노트 초안: 요산은 MetS 선별검사가 아니라서 리뷰어가 근거를 물었다. 답의 두 축(항공의학 표준 패널에 이미 들어 있다, 선행 ROKAF 코호트에서 최상위 사분위 신호가 있었다)은 저자의 연구 맥락이다. 문장은 DataBot이 다듬었지만 논거는 연구자가 가져왔다.
- 출처: `05-urate-origin.md`(논문 2 Introduction 2쪽, `output/agent_bot/2026-08-14/reviewer2-response-plan.md` 131행)

### 섹션 6. 계약서 + 코드북 → 설계안 → 결정 (6.0분)

| 번호 | 제목 | 분 | 유형 |
|---|---|---|---|
| S18 (6-1) | 에이전트가 받는 것은 행이 아니라 구조와 정의다 | 1.25 | 표 |
| S19 (6-2) | 에이전트의 첫 일은 코드를 쓰는 게 아니라 기존 스크립트에 "의도인가"를 되묻는 것이었다 | 1.5 | 3단 |
| S20 (6-3) | 에이전트는 설계안을 내고 멈췄고, 방향은 연구자가 골랐다 | 2.0 | 3단 |
| S21 (6-4) | 제안된 설계 중 집단별 회귀는 출판본에 남았고, 매개분석은 연구자가 뺐다 | 1.25 | 다이어그램 |

#### S18 (6-1). 에이전트가 받는 것은 행이 아니라 구조와 정의다
- 블록 제목: `## 6. 에이전트가 받는 것은 행이 아니라 구조와 정의다`
- 시간 1.25분, 유형: 표
- 한 줄 메시지: 데이터는 변수명, 자료형, 단위로만 에이전트와 청중에게 간다.
- 화면(범주 요약, 6행):

  | Category | Variables (type, unit) |
  |---|---|
  | Group, Demographics | GROUP (Pilot HE / KHANES), AGE (years), AGE_GROUP |
  | Vital signs | HEIGHT, WEIGHT, BMI (kg/m²), WAISTCIR (cm), SYSBP, DIABP (mmHg) |
  | Medication / Disease | HYPERTENSION, DYSLIP, DIABETES / C_* (7), METS_new |
  | MetS criteria | mets_c1–mets_c5 (factor No/Yes), mets_count |
  | Laboratory | URATE, GLUC, CHOL, TRIG, HDL, LDL (mg/dL), AST, ALT (IU/L) … |
  | Complex sample design | wt_itvex, psu, kstrata (KNHANES) |

- 노트 초안: 분석 데이터 3,697행 중 변수명, 자료형, 단위만 보여준다. ID 열은 목록에서 뺐고 검진일, 소속에 해당하는 열은 없다. 약물 변수(Medication)와 질병 변수(Disease, `C_` 접두)가 다른 범주라는 점, KNHANES 설계변수 3개가 있지만 쓰지 않은 점(8번)을 짚는다. 논문 표의 단위는 URATE μmol/L(×59.48), GLUC mmol/L(÷18.02)로 바뀐다.
- 메모: 코드북 원문은 GROUP을 "Identifier" 범주로 둔다. 식별 열과 혼동되지 않도록 화면 범주명을 "Group"으로 바꿀지 결정 필요(바꾸면 노트에 밝힌다). 열 수는 코드북 53, 데이터셋 58(파생 변수 GROUP2, C_OBESEB, medication, medication_n, WC_GROUP).
- 출처: `07-data-structure.md`(`afhe-khanes2022-analysis-codebook.rds`, 데이터셋 `names()`, `class()`, `levels()`), `CLAUDE.md` 화면 노출 규칙 1, 3
- 메모: `07-data-structure.md`는 섹션 7 표시이나 6번 제목(코드북)에 맞춰 옮겼다.

#### S19 (6-2). 에이전트의 첫 일은 코드를 쓰는 게 아니라 기존 스크립트에 "의도인가"를 되묻는 것이었다
- 시간 1.5분, 유형: 3단
- 한 줄 메시지: 감사(audit)부터 시킨 덕에 에이전트가 연구자에게 질문을 돌려줬다.
- 에이전트: Positron Assistant(Claude Sonnet 4.6), 2026-03-10
- 화면:
  - 프롬프트: "현재 02-afhe-khanes-analysis-script.R 수행 내요 검증 및 결과 요약. output 파일 생성하지 않음."
  - 에이전트가 한 일: 스크립트 721줄 읽기 → 세션 객체 구조만 확인(`nrow`/`ncol`, `table(GROUP)`) → 모형 4단계 요약 unadj `METS_new ~ GROUP2 * value_scaled` / adj1 + 생활습관 / adj2 + 신체계측, 혈압 / adj3 + 약물
  - 연구자가 확인한 것(에이전트가 되물은 두 항목): "… 포화 모델이 작성되어 있으나, 다중공선성 위험이 있어 결과 해석 시 주의 필요" / "… `demo_tbl`에 MeTS 기준 항목이 포함되지 않음 → 의도적인지 확인 필요"
- 노트 초안: 에이전트는 파일을 만들지 말라는 지시를 지키고 읽기와 구조 확인만 했다. 모형 4단계 구성은 8번의 약물 보정 장면에서 다시 나온다. 사용자가 두 검토 사항에 어떻게 답했는지는 로그 발췌에 없으므로 답을 지어내지 않는다. 같은 메시지의 MetS 보정 OR 0.37, 혈압 구성요소 2.16은 중간값, 원고 최종값 aOR 0.30, 2.12.
- 메모: 프롬프트 원문의 오타("내요")는 그대로 둔다.
- 출처: `06-script-audit-questions.md`(add-analysis msg[2–3]), `CLAUDE.md` 31행(최종값)

#### S20 (6-3). 에이전트는 설계안을 내고 멈췄고, 방향은 연구자가 골랐다
- 시간 2.0분, 유형: 3단
- 한 줄 메시지: 설계의 선택지는 에이전트가 정리하고, 선택은 연구자가 한다.
- 에이전트: Positron Assistant(Claude Sonnet 4.6), 2026-03-19
- 화면:
  - 프롬프트: "URATE와 GLUC에 대해 연구목적 4번에 대한 분석 실시"
  - 에이전트가 한 일: `todoWrite` 4항목 → `select()` 에러 "Column `DYSLIPIDEMIA` doesn't exist." → `names()`로 `DYSLIP` 확인 → 설계안 "**종속변수**: URATE, GLUC (각각) / **독립변수**: AGE, BMI, SMOKING, ALCOHOL, EXERCISE, medication + GROUP2 / **방법**: 집단별(Pilot HE / KHANES) **다중선형회귀** + 집단 간 **회귀계수 비교(상호작용)**" → "이 방향으로 진행할까요? 아니면 다른 접근(예: 매개분석, 경로분석 등)을 원하시는지 알려 주세요."
  - 연구자가 확인한 것: "현재 방향으로 진행한 다음 매개분석(BMI → URATE/GLUC → MeTS) 방향  분석 실시"
- 노트 초안: 에이전트는 계약서의 연구목적 4번을 읽고 변수 구조를 확인한 뒤 제안에서 멈췄다. 변수명 오류(`DYSLIPIDEMIA`)는 `names()`로 스스로 바로잡았다. 연구자는 회귀와 매개분석 가운데 하나가 아니라 둘을 순서대로 골랐고, 그 결과는 다음 장에서 본다.
- 질문 대비: "집단별 회귀 + 계수 비교"와 "합동 모형의 상호작용 검정"은 같은가. 출판본은 "Linear regression examined determinants of urate and fasting glucose, with pooled-model interaction tests."로 합동 모형 상호작용을 썼다.
- 출처: `06-design-proposal-choice.md`(finalize msg[6–8]), `08-probit-choice-reason.md`(논문 2 Statistical analysis)

#### S21 (6-4). 제안된 설계 중 집단별 회귀는 출판본에 남았고, 매개분석은 연구자가 뺐다
- 시간 1.25분, 유형: 다이어그램(결정 나무)
- 한 줄 메시지: "고쳤다"와 "쓴다"는 다른 결정이고, 뒤의 결정은 연구자의 몫이다.
- 화면:
  - 설계안 → (a) 집단별 다중선형회귀 + 상호작용 → 출판본 "Linear regression examined determinants of urate and fasting glucose, with pooled-model interaction tests."
  - 설계안 → (b) 매개분석 BMI → URATE/GLUC → MeTS → 세 번 만에 실행(7번) → (사용자) "RQ4에서 mediation analysis 결과는 추가하지 않을 예정"
- 노트 초안: 에이전트가 끝까지 돌려 놓은 매개분석을 연구자가 원고에서 뺐다. 매개분석 수치는 출판 원고에 없으므로 화면에 올리지 않는다. 뺀 이유: `<여기에: 사용자가 매개분석을 뺀 이유 한 문장>`.
- 출처: `07-mediation-env-error.md`(finalize msg[24]), `08-probit-choice-reason.md`(논문 2 Statistical analysis 4쪽), `06-design-proposal-choice.md`

### 섹션 7. 전처리, 코드 (6.0분, 녹화 D1)

| 번호 | 제목 | 분 | 유형 |
|---|---|---|---|
| S22 (7-1) | 에이전트는 에러를 읽고 가설을 바꿔 가며 고쳤다: 첫 진단은 틀렸고 두 번째가 맞았다 | 1.5 | 3단(코드) |
| S23 (7-2) | "세션에서는 되는데 knit은 안 된다"의 세 원인을 한 번에 진단하고 문서를 세션 독립적으로 다시 썼다 | 1.5 | 3단 |
| S24 (7-3) | [녹화 D1] 에이전트는 코드를 쓰기 전에 세션에 무엇이 있는지부터 확인한다 | 1.75 | 녹화 |
| S25 (7-4) | 말이 안 되는 값(전부 0%)은 에이전트가 스스로 잡지만, 그 전에 자료형을 가정했다 | 1.25 | 3단(코드) |

#### S22 (7-1). 에이전트는 에러를 읽고 가설을 바꿔 가며 고쳤다: 첫 진단은 틀렸고 두 번째가 맞았다
- 블록 제목: `## 7. 에이전트는 에러를 읽고 가설을 바꿔 가며 고쳤다: 첫 진단은 틀렸고 두 번째가 맞았다`
- 시간 1.5분, 유형: 3단(코드)
- 한 줄 메시지: 에이전트의 디버깅은 에러 메시지 → 가설 → 재시도의 반복이고, 가설이 틀릴 수도 있다.
- 에이전트: Positron Assistant(Claude Sonnet 4.6), 2026-03-19
- 화면:
  - 프롬프트: "현재 방향으로 진행한 다음 매개분석(BMI → URATE/GLUC → MeTS) 방향  분석 실시"
  - 에이전트가 한 일: 시도 1 `object 'fm_med' not found` → 시도 2 주석 `# Fix: mediation models must be fit on the SAME data object passed to mediate()` → `object 'fm_a' not found` → 시도 3 `fit_a <- eval(bquote(lm(.(as.formula(f_a_chr)), data = dat)))` → "Done."
  - 연구자가 확인한 것: 결과를 원고에 쓸지. 쓰지 않았다(6-4).
- 노트 초안: 두 번째 시도의 가설("같은 데이터 객체")은 틀렸고, 세 번째 시도의 주석 `# mediation::mediate() captures the model call env`(원문 앞부분)가 맞는 진단이었다. 함수 안에서 문자열로 만든 formula 객체의 이름을 `mediate()`가 bootstrap 중 찾지 못한 것으로 보이고, `eval(bquote())`로 formula를 call 안에 직접 넣어 해결했다. 에이전트는 "<MEMO>I have made 6 tool calls this turn (soft limit: ~3)."를 스스로 기록하고 계속 진행했다. 매개분석 결과 수치는 출판본에 없어 화면에 올리지 않는다.
- 확인 필요: 원인 설명(bootstrap 중 call 재평가)은 로그의 주석에서 추론한 것이므로 발표자가 확인 후 말한다.
- 출처: `07-mediation-env-error.md`(finalize msg[8–9], msg[24])

#### S23 (7-2). "세션에서는 되는데 knit은 안 된다"의 세 원인을 한 번에 진단하고 문서를 세션 독립적으로 다시 썼다
- 시간 1.5분, 유형: 3단
- 한 줄 메시지: knit 실패 진단은 에이전트가 빠르다. 재현성과 실행 시간의 trade-off는 연구자가 받아들일지 정한다.
- 에이전트: Positron Assistant(Claude Sonnet 4.6), 2026-03-19
- 화면:
  - 프롬프트: "knit 실행 시 오류. 분석 결과는 현재 작업공간에 저장된 결과를 기반으로 통계량 값들을 추출해서 테이블을 재생성하고, …"
  - 에이전트가 한 일: `read` 실패(ENOPRO) → `bash`의 `cat` → "1. **YAML 안 `#` 주석** → 파싱 오류 / 2. **knit 환경은 세션과 독립** → `ft_urate`, `ft_gluc`, `ft_med` 객체가 없음. … / 3. **`fig_path`** → 저장된 PNG를 `knitr::include_graphics()`로 삽입" → (응답 끊김, 사용자 "재실행") → 자급자족 qmd, 자체 점검 "Overall: PASS"
  - 연구자가 확인한 것: 매개분석은 "결과값을 **하드코딩**한 `med_summary` tibble로 `ft_med` 재생성". 2,000 bootstrap을 knit마다 돌리지 않는 선택
- 노트 초안: 세 원인은 Quarto 사용자라면 한 번씩 겪는 것들이다. 에이전트는 회귀표를 setup 청크에서 데이터 로드부터 다시 계산하게 바꾸고, 매개분석 값만 하드코딩했다. 이 trade-off는 에이전트가 정했고 연구자가 받아들였다(12번). 중간에 응답이 끊겨 사용자가 "재실행"을 친 것도 그대로 보여준다.
- 출처: `07-knit-failure-three-causes.md`(finalize msg[18–21])

#### S24 (7-3). [녹화 D1] 에이전트는 코드를 쓰기 전에 세션에 무엇이 있는지부터 확인한다
- 시간 1.75분, 유형: 녹화(90초, 대기 구간 2–4배속, 자막)
- 한 줄 메시지: 세션 확인 → 코드 → 에러 → 수정의 한 바퀴를 실제 속도로 본다.
- 화면: `{{< video demo/clips/D1-knit-fix.mp4 >}}` (파일명 가칭)
- 노트 초안: 대본은 7-2의 knit 장면을 모델로 한다: 세션 객체 확인(`exists()`, `file.exists()`) → 코드 작성 → 에러 → 수정. 클립 앞뒤로 "지금 에이전트가 하는 일"을 한 문장씩 말한다. 녹화가 끝나면 실제 흐름에 맞춰 제목과 노트를 고친다. 연출된 실수는 넣지 않는다.
- 확인 필요: 녹화는 발췌 장면이 아니라 새로 찍는 시연이다. `demo/runbook.md` 미작성. 녹화 전 점검표(데이터뷰어 닫기, 콘솔 지우기, 터미널 경로, 환경변수 탭, API 키)
- 출처: `.claude/skills/demo-runbook/SKILL.md`(D1), `07-knit-failure-three-causes.md`, `CLAUDE.md` 화면 노출 규칙 1, 5

#### S25 (7-4). 말이 안 되는 값(전부 0%)은 에이전트가 스스로 잡지만, 그 전에 자료형을 가정했다
- 시간 1.25분, 유형: 3단(코드)
- 한 줄 메시지: 자명한 오류는 에이전트가 잡는다. 그럴듯한 오류는 9번의 몫이다.
- 에이전트: Positron Assistant(Claude Sonnet 4.6), 2026-03-21
- 화면:
  - 프롬프트: "afhe-khanes-analysis-report-word.qmd 의 전체 분석 결과 해석.  결과 해석 문서는 새롭게 영문으로 작성. …"
  - 에이전트가 한 일: `as.integer(as.character(.x) == "1" | .x == TRUE | as.numeric(as.character(.x)) == 1)` → 10행 모두 `n = 0`, "NAs introduced by coercion", `mets_c1 class: fa[ctor]` → `mutate(across(mets_c1:mets_c5, ~ as.integer(.x == "Yes")))`
  - 연구자가 확인한 것: 고친 결과가 원고 최종값과 같다(복부비만 13.0% vs 45.3%, 혈압 47.7% vs 38.8%, Pilot HE vs KHANES)
- 노트 초안: 열하루 전 다른 대화(2026-03-10, add-analysis msg[3])에서 에이전트 자신이 "mets_c1~c5 → factor(0="No", 1="Yes")"라고 요약했는데도 숫자 코딩을 가정했다. 전부 0%라는 값이 나오자 `class()`를 보고 고쳤다. 0%는 누구나 이상하다고 느끼는 값이다. 그럴듯한 값이 틀렸을 때는 어떻게 되는지가 9번이다.
- 출처: `07-factor-prevalence-zero.md`(finalize msg[26–27]), `06-script-audit-questions.md`(add-analysis msg[3])

### 섹션 8. 분석 설계, probit (7.0분)

| 번호 | 제목 | 분 | 유형 |
|---|---|---|---|
| S26 (8-1) | 주 분석은 logistic, 효과 수정 검정은 probit 상호작용 모형: 두 모형은 역할이 다르다 | 0.75 | 다이어그램(수식) |
| S27 (8-2) | 연구자의 손계산 0.1009와 emmeans의 0.1779는 서로 다른 척도에서 잰 값이었다 | 1.0 | 3단 |
| S28 (8-3) | 같은 모형, 같은 추정치인데 상호작용의 p는 probit 척도에서 0.33–0.60, 확률 척도에서 0.001–0.019다 | 1.5 | 표(3단 요약) |
| S29 (8-4) | 모형 선택 이유를 에이전트가 쓰면 "그림과 맞추려고"가 된다 | 0.75 | 3단 |
| S30 (8-5) | 가중치를 쓰지 않은 것은 연구자의 설계 판단이고, 에이전트는 그 판단을 Limitations 두 문장까지 밀고 갔다 | 1.0 | 3단 |
| S31 (8-6) | "왜 보정하면 사라지나"에 에이전트는 복약률 차이로 답했고, 그 해석은 원고에 가지 않았다 | 1.0 | 3단 |
| S32 (8-7) | 허리둘레를 보정하면 집단 차이가 사라진다. 그런데 허리둘레는 MetS 정의의 일부다 | 1.0 | 3단 |

#### S26 (8-1). 주 분석은 logistic, 효과 수정 검정은 probit 상호작용 모형: 두 모형은 역할이 다르다
- 블록 제목: `## 8. 주 분석은 logistic, 효과 수정 검정은 probit 상호작용 모형: 두 모형은 역할이 다르다`
- 시간 0.75분, 유형: 다이어그램 + 수식
- 한 줄 메시지: 이 사례에는 링크 함수가 둘이고, 층별 OR은 probit 적합값을 logit으로 다시 옮겨 얻었다.
- 에이전트: 수식은 DataBot(모델 미기재) Methods 초안(2026-03-21)
- 화면:
  - Main: logistic regression, adjusted for age, smoking, alcohol, physical activity → aOR
  - Effect modification: $\Phi^{-1}[P(\text{MetS}_i = 1)] = \beta_0 + \beta_1 \text{GROUP2}_i + \beta_2 V_i + \beta_3 (\text{GROUP2}_i \times V_i)$, LRT
  - V: age group, pooled-sample quartiles of WC, SBP, DBP, HDL, TRIG, GLUC
  - Stratum OR: `regrid(..., "logit")` → `contrast(..., method = "revpairwise", by = V)`
- 노트 초안: 출판본 Statistical analysis는 "MetS prevalence, components and adjusted associations were compared using logistic regression …"과 "Effect modification … was tested using probit-binomial models with interaction terms and likelihood-ratio tests (LRTs)."로 두 모형을 나눈다. 사분위 절단값은 병합 표본 3,697명에서 구했기 때문에 층 안의 비교는 같은 절대 수준의 남성끼리다. 층별 OR은 probit 적합 확률을 logit으로 옮긴 값이라 logistic 계수의 OR과 같지 않다(9번에서 에이전트 스스로 "근사 OR"이라 부른다).
- 출처: `08-probit-choice-reason.md`(05_statistical_analysis_methods.qmd 86–120행, 논문 2 Statistical analysis 4쪽), `08-waist-adjustment-circularity.md`(reviewer2-response-plan.md 406–414행, pooled 사분위), `09-hand-calculation-check.md`

#### S27 (8-2). 연구자의 손계산 0.1009와 emmeans의 0.1779는 서로 다른 척도에서 잰 값이었다
- 시간 1.0분, 유형: 3단
- 한 줄 메시지: 패키지 출력이 손계산과 다를 때, 먼저 의심할 것은 척도다.
- 에이전트: Positron Assistant(Claude Sonnet 4.6), 2026-03-17
- 화면:
  - 프롬프트: "… 30세 이하의 KHANES - Pilot = 0.1458 - 0.0495 = 0.0963, 30세 이상 40세 이하 KHANES - Pilot = 0.2892 - 0.0920 = 0.1972.  두 값의 차이는 1.009 정도인데 int_cntr의 (30-39) - (20-29)는 0.1779 임."
  - 에이전트가 한 일: "핵심을 정확히 짚으셨습니다. **스케일 차이** 때문입니다." → `probit_vals <- qnorm(probs)` → "int_cntr (30-39) - (≤29) on PROBIT scale = 0.1777" / "int_cntr reported value = 0.1779"
  - 연구자가 확인한 것: `int_cntr`는 확률이 아니라 probit(선형 예측) 척도의 이중 대비다. 확률 척도 0.1972 − 0.0963 = 0.1009, probit 척도 0.7728 − 0.5951 = 0.1777
- 노트 초안: 출발점은 연구자의 손계산이었다. 사용자의 "1.009"는 0.1009의 오타이고, 에이전트는 지적하지 않은 채 0.1009로 받아 계산했다. 0.1777과 0.1779의 차이는 네 자리로 반올림한 확률에서 다시 계산했기 때문으로 보인다. 수치는 2026-03-17 탐색 단계 값이다.
- 출처: `08-probit-logit-probability-scale.md`(probit-logit-prob msg[6–7])

#### S28 (8-3). 같은 모형, 같은 추정치인데 상호작용의 p는 probit 척도에서 0.33–0.60, 확률 척도에서 0.001–0.019다
- 시간 1.5분, 유형: 표 + 3단 요약 한 줄
- 한 줄 메시지: 상호작용은 척도에 의존한다. 이것은 non-collapsibility가 아니다.
- 에이전트: Positron Assistant(Claude Sonnet 4.6), 2026-03-17
- 화면(6줄):

  | Interaction contrast | Probit scale | p | Probability scale | p |
  |---|---|---|---|---|
  | (30-39) − ≤29 | 0.1779 | 0.328 | 0.101 | 0.019 |
  | (40-49) − ≤29 | 0.1116 | 0.543 | 0.132 | 0.003 |
  | (≥50) − ≤29 | 0.0977 | 0.595 | 0.157 | 0.001 |

  - 프롬프트 "확률 스케일에서 상호작용을 검정" → 에이전트 `regrid(em1, transform = "response")` + "이는 통계학에서 잘 알려진 **"non-collapsibility"** 문제입니다."
  - 연구자: 계산은 맞고 이름이 틀렸다. 상호작용의 척도 의존성(scale dependence of interaction)이다
- 노트 초안: probit 척도에서 집단 차이는 연령대 사이에 거의 일정하다. Φ가 비선형이라 기저 유병률이 높은 연령대일수록 같은 probit 차이가 더 큰 위험차로 바뀌고, 그래서 "링크 척도에서 상호작용 없음"과 "가법(위험차) 척도에서 상호작용 있음"이 동시에 참이다. non-collapsibility는 교란이 없어도 공변량에 대해 주변화한 OR(또는 probit 계수)이 조건부 값과 달라지는 성질이라 여기서 일어난 일과 다르다. 에이전트의 권고("probit 모델에서는 **probit 스케일(int_cntr)**이 상호작용 검정의 올바른 기준입니다.")도 그대로 받지 않는다: 어느 척도가 맞는지는 질문이 정한다.
- 질문 대비:
  - "확률 척도 유의는 비선형 변환의 산물 아닌가?" 에이전트도 "확률 스케일의 유의성(p < 0.05)은 **비선형 변환의 수학적 산물**로, 실제 그룹 간 효과 수정(effect modification)의 증거로 보기 어렵습니다."라고 썼다. 그러나 위험차 척도의 상호작용은 공중보건적으로 의미 있는 효과 수정이다. "유병률 격차가 나이가 들수록 커지는가"가 질문이면 확률 척도가 맞다.
  - 표의 probit 값은 KHANES − Pilot 방향이다. glm 계수(`GROUP2Pilot HE:AGE_GROUP30-39 -0.1779`)는 부호가 반대다.
  - 출판본은 probit 모형과 LRT로 효과 수정을 검정했다. 위 p는 Wald z 기반 탐색 단계 값이다.
- 확정(사용자 2026-10-20): 위 노트의 입장(척도 선택은 질문이 정한다, 위험차 척도의 상호작용도 의미 있는 효과 수정이다)을 유지한다. 질문 대비에 "출판본은 링크 척도(probit) + LRT로 보고했다"를 사실로 덧붙인다.
- 확인 필요: 출판본 LRT p값(발췌에 없음). 출판본에 "non-collapsibility" 표현이 들어갔는지.
- 출처: `08-probit-logit-probability-scale.md`(probit-logit-prob msg[2–3], msg[8–9]), `memory/talk-scenes-from-repo.md` 19행, 31행

#### S29 (8-4). 모형 선택 이유를 에이전트가 쓰면 "그림과 맞추려고"가 된다
- 시간 0.75분, 유형: 3단(두 문장 나란히)
- 한 줄 메시지: 링크 함수를 고른 이유는 연구자가 써야 하고, 이 사례는 그 이유가 약하다.
- 에이전트: DataBot(모델 미기재), Methods 초안 2026-03-21
- 화면:
  - 맥락(프롬프트 원문 없음): RQ2 Statistical Analysis 절 초안
  - 에이전트가 쓴 것: "The probit link was chosen to match the visual representation conventions used in the companion figure (forest plot of EMM-based prevalence)."
  - 연구자가 남긴 것(출판본): "Effect modification across age groups and pooled-sample quartiles of continuous risk factors was tested using probit-binomial models with interaction terms and likelihood-ratio tests (LRTs)."
- 노트 초안: 그림 관례는 링크 함수를 고르는 이유가 될 수 없다. 출판본은 이유를 지우고 무엇을 했는지만 남겼다. 그래서 "왜 probit인가"라는 질문에 원고는 지금도 답하지 않는다. 이 약점은 13번에서 제가 다시 꺼낸다.
- 질문 대비: "logit으로 적합했어도 결론이 같았나?" 레포에 logit 재적합 비교가 있는지 확인 필요. 층별 OR을 probit에서 regrid로 얻은 구조 자체도 같은 질문을 부른다.
- 출처: `08-probit-choice-reason.md`(05_statistical_analysis_methods.qmd 96–112행, 논문 2 Statistical analysis 4쪽)

#### S30 (8-5). 가중치를 쓰지 않은 것은 연구자의 설계 판단이고, 에이전트는 그 판단을 Limitations 두 문장까지 밀고 갔다
- 시간 1.0분, 유형: 3단
- 한 줄 메시지: 추정 대상(estimand)을 고르는 것은 연구자, 그 선택의 대가를 원고에 적는 것은 에이전트.
- 에이전트: DataBot(모델 미기재), 2026-05-09 초안 / 2026-08-16 r2
- 화면:
  - 맥락(프롬프트 원문 없음): 데이터에 `wt_itvex`, `psu`, `kstrata`가 있다. memory에 남은 사용자 지시 "저자 문체 유지", "압축 우선"(Abstract, Limitations 압축 요청 두 차례)
  - 에이전트가 한 일: 5월 Sixth limitation(약 95단어) → 8월 r2: "we therefore conducted unweighted analyses, as our aim was comparative rather than absolute, and weighting only one group would target incompatible populations."
  - 연구자가 확인한 것: "Accordingly, the KNHANES prevalences reported here are not nationally representative, and the ORs reflect contrasts between the two sampled cohorts rather than population-level estimates."
- 노트 초안: KNHANES는 층화, 다단계 집락 확률표본이고, 조종사 자료는 5월 초안의 표현대로 "a near-census of active-duty male ROKAF pilots"다. 한쪽만 가중하면 두 표본이 서로 다른 목표 모집단을 갖게 되어 OR 해석이 흐려진다는 것이 저자의 논거다. 그 대가로 KNHANES 유병률 37.1%를 국가 대표값으로 읽지 말라는 단서를 원고에 남겼다.
- 질문 대비:
  - "KNHANES를 가중해 '한국 남성 모집단 대비 조종사'를 추정하는 것도 정당한 추정 대상 아닌가?" 맞다. 저자는 두 표본 코호트의 대비를 택했고, 그 선택과 한계를 Limitations에 적었다.
  - "가중치를 안 쓰더라도 psu, kstrata를 무시하면 분산이 과소추정될 수 있지 않나?" 설계 기반 분산 민감도 분석이 레포에 있는지 확인 필요(발췌에 없음).
- 출처: `08-unweighted-decision.md`(session-summary 2026-05-09 §5 52–60행, §7 72–78행, r2 qmd 422행), `07-data-structure.md`(설계변수)

#### S31 (8-6). "왜 보정하면 사라지나"에 에이전트는 복약률 차이로 답했고, 그 해석은 원고에 가지 않았다
- 시간 1.0분, 유형: 3단(표)
- 한 줄 메시지: 원인 탐색의 순서는 좋았지만 결론은 과했고, 최종 모형은 다른 답을 냈다.
- 에이전트: Positron Assistant(Claude Sonnet 4.6), 2026-03-10
- 화면:
  - 프롬프트: "CHOL, LDL의 조정3 유의성 소실 원인을 복약력 분포 비교로 확인하기"
  - 에이전트가 한 일: `count(GROUP, DYSLIP)` → 이상지질혈증 약 Pilot HE 18/2,604 (0.7%) vs KHANES 149/1,093 (13.6%) → 복약 여부별 CHOL, LDL 평균, t-test, violin plot → "조정3의 유의성 소실은 **방법론적으로 타당하며**, 복약 보정 후 실질적 그룹 차이는 존재하지 않음을 시사합니다."
  - 연구자가 확인한 것: 최종 원고에서 LDL Δβ 0.24 (p = 0.022), total cholesterol Δβ 0.20 (p = 0.049)로 완전 보정 후에도 유의. 3월의 "소실" 해석은 원고로 옮기지 않았다
- 노트 초안: 분포 → 층별 평균 → 검정 → 그림의 순서는 연구자가 할 순서와 같았다. 그러나 비복약자 CHOL이 196.5 vs 200.9(p = 0.002)인데 "두 그룹의 수치가 거의 동일"이라 했고, 도구 출력의 `cat()` 서식은 p = 0.002를 "p < 0.001"로 찍었다(다음 요약에서는 p=0.002로 바르게 적음). 같은 발견은 보고서 qmd에 `tbl-dyslip` 청크와 footnote로 남았다. 3월 결과는 중간값, 원고 최종값 LDL Δβ 0.24, TC Δβ 0.20 유의. 복약률 0.7%, 13.6%는 데이터 사실이고 2026-08-16 `verify-numbers.R`이 다시 계산했다.
- 질문 대비:
  - 약물은 교란인가, 결과의 결과인가: 지질이 높아서 약을 먹고, 약이 측정 지질을 낮춘다.
  - (사용자 결정 2026-10-20) 약물 보정의 순환성 논점은 슬라이드, 노트에서 다루지 않는다.
- 출처: `08-medication-imbalance.md`(add-analysis msg[6–7]), `08-medication-imbalance-report.md`(2026-03-10 보고서 qmd 428–455, 698–705, 737행), `05-urate-origin.md`(출판본 Abstract Δβ), `09-verify-numbers-script.md`

#### S32 (8-7). 허리둘레를 보정하면 집단 차이가 사라진다. 그런데 허리둘레는 MetS 정의의 일부다
- 시간 1.0분, 유형: 3단
- 한 줄 메시지: 무엇을 보정할지는 통계가 아니라 추정 대상과 인과 구조의 문제다.
- 에이전트: DataBot(모델 미기재), 2026-03-10 보고서 / 2026-08-14 리뷰어 대응안
- 화면:
  - 맥락(프롬프트 원문 없음): 연령층화 순차 보정 표 "Table 6. Age-stratified MeTS OR: Testing the Healthy Worker Effect"
  - 에이전트가 한 일: footnote "Key finding: WAISTCIR alone eliminates OR in all age strata." → 8월 대응안 "층화변수 자체가 MetS 구성요소라 **부분적 순환성은 어떤 절단값을 써도 남음**"
  - 연구자가 확인한 것: 최종 주 모형은 연령, 생활습관만 보정(바이오마커 모형은 BMI, 약물 추가)하고, MetS 구성요소는 보정 변수가 아니라 pooled 사분위 층화 변수로만 썼다
- 노트 초안: mets_c1이 허리둘레 90 cm 이상이므로 허리둘레를 보정하면 결과 정의의 일부를 공변량으로 넣는 셈이다. 동시에 허리둘레는 집단에서 MetS로 가는 경로 위에 있을 수 있어서, 보정하면 총효과가 아니라 그 경로를 막은 효과를 추정하게 된다. 순환성 논점은 리뷰어가 묻지 않아 응답서에 먼저 넣지 않기로 했다(12번).
- 질문 대비: Model 2의 BMI 보정도 허리둘레와 상관이 높아 같은 질문을 받을 수 있다. 3월 보고서의 허리둘레 차이 수치는 중간 보고서 값이라 쓰지 않는다.
- 출처: `08-waist-adjustment-circularity.md`(2026-03-10 보고서 qmd 563–572, 641, 673, 703행, reviewer2-response-plan.md 406–414, 421행), `08-probit-choice-reason.md`(출판본 Statistical analysis), `memory/talk-scenes-from-repo.md` 35행(출처 정정)

### 섹션 9. 검증 (5.0분, 녹화 D2)

| 번호 | 제목 | 분 | 유형 |
|---|---|---|---|
| S33 (9-1) | 혼동은 질문에서 시작됐고, 에이전트는 바로잡는 대신 그 위에 서사를 지었다 | 1.0 | 3단 |
| S34 (9-2) | 그림 캡션에 β의 정의를 정확히 적고도, 바로 아래 해석에서 부호를 반대로 읽었다 | 0.75 | 3단 |
| S35 (9-3) | 패키지 출력을 믿지 않고 pnorm, log, exp 네 줄로 재현하게 했다 | 0.75 | 3단(코드) |
| S36 (9-4) | 문서에 그 숫자가 있는지 보는 것은 검증이 아니다: 같은 데이터에서 다시 계산한다 | 1.0 | 코드(두 열) |
| S37 (9-5) | [녹화 D2] 원고 수치를 데이터에서 다시 꺼내 대조한다 | 1.0 | 녹화 |
| S38 (9-6) | 종료 코드 0은 검증이 아니다: 렌더는 "성공"했는데 Figure 1이 없었다 | 0.5 | 텍스트 |

#### S33 (9-1). "오즈비" 한 단어가 두 표를 가리켰다. 에이전트는 묻지 않고 하나를 골라 서사를 지었다
- 블록 제목: `## 9. "오즈비" 한 단어가 두 표를 가리켰다. 에이전트는 묻지 않고 하나를 골라 서사를 지었다`
- 시간 1.0분, 유형: 3단
- 한 줄 메시지: 그럴듯한 설명은 통계 지식이 아니라 질문의 틀을 따라간다. 모호한 용어는 에이전트가 물어야 한다.
- 에이전트: Positron Assistant(Claude Sonnet 4.6), 2026-03-10
- 화면:
  - 프롬프트: "공군 pilot 집단의 요산의 연령에 따른 감소속도가 더 빠르다 라는 결과와 맨 처음 로지스틱 회귀모형 결과 보정 후에도 대사증후군에 대한 공군 집단의 오즈비가 일반 인구 집단보다 높게 나타난 사실과 어떻게 연결을 할 수 있지? …"
  - 에이전트가 한 일: "즉, **생활습관으로 설명되지 않는 잔여 OR 차이**와 **연령에 따른 URATE 감소 둔화** 모두, 조종사 집단에 내재된 **건강 근로자 효과(Healthy Worker Effect)**로 수렴하는 공통 설명이 가능합니다." + 논문 서술 제안
  - 연구자가 확인한 것: "결과 해석이 이상한데? 로지스틱 회귀모형 결과는 작업 공간의 tbl_result_mets_lbtest 결과를 확인해." → (에이전트) "확인했습니다. 이전 해석에 오류가 있었습니다." 두 OR 분리: 집단 간 유병 OR(`tbl_data_mets_component`) vs 집단 안 1-SD 기울기 OR(`tbl_result_mets_lbtest`)
- 노트 초안: 분석 중의 탐색적 질문이었다. 질문의 "오즈비"는 집단 내 검사값 OR 표(`tbl_result_mets_lbtest`, 요산 Pilot 1.27 vs KHANES 0.98)를 가리켰는데, 에이전트는 어느 표인지 묻지 않고 집단 간 유병 OR로 받았다. 첫 답에서 "Pilot HE의 대사증후군 OR이 KHANES 대비 **0.37 (95% CI: 0.30–0.46)로 낮음**"이라고 맞게 적고도 "보정 후에도 높다"는 틀 위에 HWE 서사와 논문 문장까지 지었다. 연구자가 표 이름을 짚어 바로잡았고, 이 연결 시도는 원고에 올리지 않았다: 출판 논문은 요산의 연령 기울기와 OR을 연결하지 않는다. 수치는 중간값, 원고 최종값 aOR 0.30, 요산 Δβ 0.27 (p = 0.009), 조종사 per-SD OR 1.35.
- 메모: 발표자의 질문이 모호했던 점은 숨기지 않되(`CLAUDE.md` 행동 규칙 3), "전제 오류"가 아니라 "모호한 용어를 에이전트가 묻지 않음"으로 서술한다. 사용자 확인 2026-10-20.
- 출처: `09-two-odds-ratios-confused.md`(add-analysis msg[18–21]), `memory/talk-scenes-from-repo.md` 7행(연령 상호작용 p = 0.003)

#### S34 (9-2). 그림 캡션에 β의 정의를 정확히 적고도, 바로 아래 해석에서 부호를 반대로 읽었다
- 시간 0.75분, 유형: 3단(코드와 인용 나란히)
- 한 줄 메시지: 에이전트는 일관되게 틀리지 않는다. 같은 메시지 안에서도 방향이 바뀐다.
- 에이전트: Positron Assistant(Claude Sonnet 4.6), 2026-03-10
- 화면:
  - 프롬프트: "GLUC와 URATE에 대해 그룹별 대사증후군 연관성을 시각화하는 상호작용 그래프 그리기. …"
  - 에이전트가 한 일: 캡션 `"Interaction β: difference in log-OR slope between Pilot HE and KHANES per 1 SD increase (from logistic regression)."` / 해석 "상호작용 $\beta$ = 1.010 (95% CI: 0.695–1.325, p<0.001): **KHANES에서 GLUC 1 SD 증가 시 대사증후군 위험 증가폭이 Pilot HE보다 유의하게 큼**"
  - 연구자가 확인한 것: 채팅에서는 아무도 지적하지 않았다. 최종 원고: 완전 보정 후 per-SD OR Pilot HE 5.80 vs KHANES 2.17, Δβ 0.98
- 노트 초안: 스크립트의 정의는 Pilot 기울기 − KHANES 기울기라서 β = +1.010은 조종사의 기울기가 더 크다는 뜻이다. 에이전트는 원 척도 평균 혈당 차이(+19 vs +9 mg/dL) 그림의 인상으로 부호를 읽었고, 같은 메시지에서 URATE는 "Pilot HE의 기울기가 더 가파름"이라 해 해석 방향도 일관되지 않았다. 최종 원고가 맞은 것은 뒤 단계의 재계산 덕이지 채팅에서 잡힌 것이 아니다. β 1.010은 비보정 모형 중간값, 원고 최종값 Δβ 0.98(완전 보정).
- 출처: `09-delta-beta-sign.md`(add-analysis msg[8–9], msg[20–21], finalize msg[27]), `05-urate-origin.md`(출판본 Abstract Δβ 0.98)

#### S35 (9-3). 패키지 출력을 믿지 않고 pnorm, log, exp 네 줄로 재현하게 했다
- 시간 0.75분, 유형: 3단(코드)
- 한 줄 메시지: 검산한 것은 에이전트이고, 검산을 시킨 것은 연구자다.
- 에이전트: Positron Assistant(Claude Sonnet 4.6), 2026-03-17
- 화면:
  - 프롬프트: "regrid(em1, "logit")인 경우 odds ratio가 계산되는데 어떤 과정을 통해 계산되는지 위와 같이 상세히 설명."
  - 에이전트가 한 일:
    ```r
    prob      <- pnorm(lp_probit)          # probit LP → probability
    logit_val <- log(prob / (1 - prob))    # probability → logit
    log_OR    <- logit_Pilot - logit_KHANES
    OR        <- exp(log_OR)
    ```
    → 0.305 / 0.249 / 0.303 / 0.322, 모두 "emmeans OR ✓"
  - 연구자가 확인한 것: "이 OR은 **probit 모델에서 도출된 근사 OR**이며, logit 모델의 OR과 개념은 같지만 **모델 계수와 직접 대응하지 않습니다.**" Methods에 쓸 OR ratio = exp(δ_j)가 코드의 양과 같은지
- 노트 초안: 연령층별 OR 0.25–0.32는 원고 최종값과 같다. 이어서 사용자가 이중 대비의 OR(OR ratio)을 묻자 1.226 / 1.008 / 0.948(p > 0.5)이 손계산과 일치했다. 이 흐름이 그대로 Methods의 "OR ratio = exp(δ_j)" 정의가 됐다.
- 질문 대비: 같은 연령 상호작용이 세 척도에서 다르게 나온다. probit 링크 p 0.33–0.60, logit으로 재격자한 OR ratio p 0.55–0.98, 확률(위험차) p 0.001–0.019. 척도를 밝히지 않은 "상호작용 유의/비유의"는 정보가 없다(부록 A4).
- 출처: `09-hand-calculation-check.md`(probit-logit-prob msg[10–13], finalize msg[31]), `08-probit-logit-probability-scale.md`(finalize msg[27] "Age strata OR 0.25-0.32")

#### S36 (9-4). 문서에 그 숫자가 있는지 보는 것은 검증이 아니다: 같은 데이터에서 다시 계산한다
- 시간 1.0분, 유형: 코드(두 열)
- 한 줄 메시지: 검증은 문자열 확인이 아니라 재계산이고, 판정 기준은 미리 적는다.
- 에이전트: 왼쪽 Positron Assistant(Claude Sonnet 4.6), 2026-03-21 / 오른쪽 DataBot(모델 미기재), 2026-08-14~16
- 화면:
  - 왼쪽(에이전트 자체 검증): `"OR 0.30 adj overall" = any(grepl("0\\.30", L))` / "YAML: no # comments : *** FAIL ***" → "YAML 내부에 주석이 없습니다. 검증 규칙 오류였고 실제 파일은 정상입니다."
  - 오른쪽(`verify-numbers.R`): "Nothing here changes any analysis; it recomputes from the same analysis dataset the manuscript already uses." / 판정 기준 "전환 후 Table 2, 3, 4의 OR, Δβ, 95% CI, p가 기존 값과 **완전히 동일**해야 함." / 결과 "약물/유병률 12개, BMI 6단계, Table 4 SI 계수 전부 일치"
- 3단 요약(노트용): 맥락(프롬프트 원문 없음) Reviewer 2 comments 2.7, 2.8, 2.9가 원고에 넣기로 약속한 수치 → 에이전트가 같은 RDS에서 재계산 → 연구자가 미리 적은 판정 기준과 대조
- 노트 초안: 왼쪽 규칙 `L[1:25]`는 본문 `## Overview`를 YAML 주석으로 오탐했고, 에이전트가 원인을 추적해 규칙 쪽을 고쳤다. 그래도 grep은 "0.30이라는 글자가 문서에 있는가"만 본다. 오른쪽은 분석 데이터 RDS를 다시 읽어 계산한다. SI 변환은 결과변수에 상수를 곱하는 것이라 계수와 CI는 같은 배수로 바뀌고 p는 그대로여야 한다는 기준을 먼저 적었고, 이 스크립트 출력이 이 발표의 수치 대조 기준이다.
- 출처: `09-false-positive-validation-rule.md`(finalize msg[27]), `09-verify-numbers-script.md`(verify-numbers.R 1–14, 22–36, 68–87행, reviewer2-response-plan.md §D 558–561행, session-summary 2026-08-16 §5 39행), `CLAUDE.md` 행동 규칙 2

#### S37 (9-5). [녹화 D2] "검증 보고서 써줘": 에이전트가 점검표를 쓰고, 사람이 읽는다
- 시간 1.0분, 유형: 녹화(60초)
- 한 줄 메시지: 검증을 시키는 것도 일이다. 점검표가 나오면 읽는 것은 연구자다.
- 화면: `{{< video demo/clips/D2-verification-report.mp4 >}}` (파일명 가칭)
- 노트 초안: (사용자 결정 2026-10-20: 후보 B) "검증 보고서 써줘" 프롬프트로 n, 결측, 변수 정의, 가중치, 모형 척도 점검표가 나오는 장면. 화면에는 집계 출력(n, 결측 수, 비율, 계수)만 둔다. 에이전트의 자체 검증이 문자열 grep에 그쳐 오탐을 낸 장면(`09-false-positive-validation-rule.md`)과 대비시켜, "보고서가 나왔다"와 "검증됐다"가 다름을 말한다. `verify-numbers.R`은 S36에서 스크립트로 보여 주고, 여기서는 돌리지 않는다. 녹화 후 실제 흐름에 맞춰 제목과 노트를 고친다.
- 확인 필요: `demo/runbook.md` 미작성. 프롬프트 원문은 런북에서 확정.
- 출처: `.claude/skills/demo-runbook/SKILL.md`(D2), `09-false-positive-validation-rule.md`, `09-verify-numbers-script.md`

#### S38 (9-6). 종료 코드 0은 검증이 아니다: 렌더는 "성공"했는데 Figure 1이 없었다
- 시간 0.5분, 유형: 텍스트(인용)
- 한 줄 메시지: 산출물을 열어 그림 개수와 캡션 번호를 세는 것까지가 검증이다.
- 에이전트: DataBot(모델 미기재), 2026-08-16 밤
- 화면:
  - "knitr `error = TRUE` 때문에 렌더가 "성공"하면서 Figure 1이 빠지고 stratified 그림이 Figure 1로 번호가 밀린 docx가 두 차례(23:09, 23:28) 생성됐음"
  - 교훈: "knitr `error = TRUE` 문서는 exit code만으로 성공을 판단하면 안 됨. 렌더 후 docx에서 "Error" 문단, 그림 개수, 캡션 번호를 반드시 확인"
- 노트 초안: 원인은 R 4.6.1 사용자 라이브러리에 DiagrammeR, webshot2, chromote가 없어 CONSORT 그림이 실패한 것이다. docx를 열어 보기 전까지는 실패를 알 수 없었다. 이 교훈이 memory에 남아 다음 세션의 점검 항목이 됐고, 청중에게 드릴 체크리스트의 "렌더 성공 ≠ 그림 있음" 항목이 여기서 왔다.
- 출처: `09-render-success-missing-figure.md`(session-summary 2026-08-16 §5-3 59–63행), `.claude/skills/starter-kit/SKILL.md`(verification-checklist)

### 섹션 10. 표, 그림 (4.0분, 라이브 D3)

| 번호 | 제목 | 분 | 유형 |
|---|---|---|---|
| S39 (10-1) | 표와 그림은 코드에서 나온다: 양식은 연구자가 정의했고 에이전트는 그 양식을 따랐다 | 0.75 | 3단(코드) |
| S40 (10-2) | [라이브 D3] Quarto 청크 하나에서 Table 1을 렌더한다 | 2.75 | 라이브 |
| S41 (10-3) | 리뷰어가 그림을 고치라 해도 모형은 건드리지 않는다: 바뀌는 것은 표시뿐이다 | 0.5 | 3단(코드) |

#### S39 (10-1). 표와 그림은 코드에서 나온다: 양식은 연구자가 정의했고 에이전트는 그 양식을 따랐다
- 블록 제목: `## 10. 표와 그림은 코드에서 나온다: 양식은 연구자가 정의했고 에이전트는 그 양식을 따랐다`
- 시간 0.75분, 유형: 3단(코드)
- 한 줄 메시지: 표, 그림은 코드에서 나오고, 산문의 숫자는 스크립트로 검증된다.
- 에이전트: DataBot(모델 미기재), 2026-08-16 r2
- 화면:
  - 맥락(프롬프트 원문 없음): 계약서 규칙 "8. 테이블은 Lancet 논문 포맷 적용" + 사용자 함수 `lancet_ft(df, caption, footnote, bold_rows, fill_rows, span_cols, center_cols)` (`code/funs/helpers.R`)
  - 에이전트가 한 일: `tbl_summary(by = GROUP, …)` → `as_flex_table()` → `border_remove()` → `hline_top(border = fp_border(width = 2), part = "all")` → `flextable::font(fontname = "Arial", part = "all")`
  - 연구자가 확인한 것: 소수점 규칙(|x| ≥ 10 → 1자리, |x| < 10 → 2자리)이 표와 산문에서 같은지
- 노트 초안: `helpers.R`은 사용자가 쓴 함수이고(agent_bot 폴더가 아님), 에이전트는 그 양식을 따랐다. 이 섹션의 메시지는 "모든 숫자가 코드에서 나온다"가 아니다. 표와 그림은 코드에서 나오고, 산문의 숫자는 스크립트로 검증된다(11번). 바로 이어 라이브로 Table 1을 렌더한다.
- 출처: `10-table-figure-automation.md`(r2 qmd 493–527, 579–599행, helpers.R 9–17, 93행), `06-contract-mets-definition.md`(규칙 8), `memory/talk-scenes-from-repo.md` 31행

#### S40 (10-2). [라이브 D3] Quarto 청크 하나에서 Table 1을 렌더한다
- 시간 2.75분, 유형: 라이브(실패 시 D3 백업 녹화로 즉시 전환)
- 한 줄 메시지: 데이터에서 문서의 표까지 한 줄기로 이어지는 것을 실시간으로 본다.
- 화면: Positron 창. 백업 `{{< video demo/clips/D3-table1.mp4 >}}` (파일명 가칭)
- 노트 초안: 짚을 점 세 가지: 에이전트가 데이터 행을 출력하지 않고 구조만 확인하는지, `tbl_summary` 결과가 Lancet 양식으로 이어지는지, 표 값이 청크 안에서 도출되는지(계약서 규칙 7). 데이터뷰어와 `head()`는 열지 않는다. 실패하면 설명하지 말고 바로 백업 녹화로 넘어간다.
- 확인 필요: (1) 렌더 전에 Table 1에 5명 미만 셀이 있는지 확인(조종사 약물 변수 등). 있으면 "5 미만"으로 바꾸거나 라이브에서 해당 행을 뺀다(`CLAUDE.md` 화면 노출 규칙 2). (2) 런북은 D3를 3분으로 잡았다. 여기서는 2.75분. (3) `demo/runbook.md` 미작성.
- 출처: `.claude/skills/demo-runbook/SKILL.md`(D3), `10-table-figure-automation.md`, `CLAUDE.md` 화면 노출 규칙 1–2

#### S41 (10-3). 리뷰어가 그림을 고치라 해도 모형은 건드리지 않는다: 바뀌는 것은 표시뿐이다
- 시간 0.5분, 유형: 3단(코드)
- 한 줄 메시지: 그림 수정과 재분석을 스크립트 머리에서부터 구분한다.
- 에이전트: DataBot(모델 미기재), 2026-08-15~16
- 화면:
  - 맥락(프롬프트 원문 없음): Reviewer 2 item 14(Figure 2 재배치), comment 12(중복 범례)
  - 에이전트가 한 일: `figure2-stratified-3col.R` 헤더 "The underlying models, estimates and contrasts are untouched; only the display changes." + `plot_layout(heights = c(1, 1), guides = "collect")` + 제출용 PNG 600 dpi, TIFF 300 dpi
  - 연구자가 확인한 것: 그림 개수와 캡션 번호(9-6의 교훈)
- 노트 초안: 그림 요청을 받았을 때 모형을 다시 돌리지 않고 표시 계층만 바꿨다는 사실을 스크립트 머리에 적었다. 내보내기 스크립트도 "The figures are identical in content … only the output device and resolution differ."라고 적었다. Figure 1 CONSORT는 `DiagrammeR::grViz()`로 그린다.
- 출처: `10-table-figure-automation.md`(figure2-stratified-3col.R 헤더, export-submission-figures.R 1–7, 22–25, 48행, r2 qmd 1264–1273, 1815–1830행)

### 섹션 11. 원고 + 역할 분리 에이전트 (5.0분)

| 번호 | 제목 | 분 | 유형 |
|---|---|---|---|
| S42 (11-1) | 원고 초안은 에이전트가 쓰되, 문체와 길이의 기준은 연구자가 memory에 남겼다 | 1.0 | 3단 |
| S43 (11-2) | 원고 산문의 숫자는 R 객체가 아니라 글자다: 그래서 표와 스크립트로 따로 대조한다 | 1.0 | 3단 |
| S44 (11-3) | "완료되었습니다!"와 올바름은 다르다: 쓰는 에이전트와 검토하는 에이전트를 나누는 이유 | 1.0 | 3단(코드) |
| S45 (11-4) | 보고서 문장은 오케스트레이터가 쓰지 않는다: 근거 분석, 초안, 검토를 다른 에이전트에 나눈다 | 1.0 | 다이어그램 |
| S46 (11-5) | 계약서 하나, 오케스트레이터 둘, 모델 다양성: 쓰는 모델과 검토하는 모델의 계열을 다르게 한다 | 1.0 | 다이어그램 |

#### S42 (11-1). 원고 초안은 에이전트가 쓰되, 문체와 길이의 기준은 연구자가 memory에 남겼다
- 블록 제목: `## 11. 원고 초안은 에이전트가 쓰되, 문체와 길이의 기준은 연구자가 memory에 남겼다`
- 시간 1.0분, 유형: 3단
- 한 줄 메시지: 표준 문단은 에이전트가 빠르게 채우고, 기준은 연구자가 준다.
- 에이전트: DataBot(모델 미기재), 2026-03-21 Methods 초안 / 2026-05-09 원고 개정
- 화면:
  - 프롬프트(memory에 기록된 사용자 지시): "저자의 문맥, 문체, 주장 등을 유지하면서 초안의 부족한 부분을 수정" / "qmd 파일에 결과 테이블 및 그림은 포함시키지 않고 논문 내용만 작성"
  - 에이전트가 한 일: Methods Overview 초안(author "Databot (Agent Analysis)"): "All statistical analyses were performed in R (version 4.5.2; R Core Team, 2025) using the tidyverse suite (Wickham et al., 2019) …"
  - 연구자가 확인한 것: 출판본은 "R (V.4.5.3)". Abstract와 Limitations는 두 차례 압축을 요구했다
- 노트 초안: 소프트웨어, 기술통계, 집단 비교 검정 같은 표준 문단은 에이전트가 패키지 인용까지 채운다. 기준은 연구자가 준다: 문체 유지, 표, 그림 분리, em-dash 지양이 memory에 "사용자 명시"로 남았다. R 버전처럼 작은 사실도 초안과 출판본 사이에 바뀌었다.
- 출처: `11-methods-draft-and-number-sourcing.md`(05_statistical_analysis_methods.qmd 1–5, 21–34행), `08-unweighted-decision.md`(session-summary 2026-05-09 §7), `08-probit-choice-reason.md`(출판본 "R (V.4.5.3)")

#### S43 (11-2). 원고 산문의 숫자는 R 객체가 아니라 글자다: 그래서 표와 스크립트로 따로 대조한다
- 시간 1.0분, 유형: 3단
- 한 줄 메시지: 산문 숫자의 출처를 문장으로 남기고, 교차검증을 절차로 둔다.
- 에이전트: DataBot(모델 미기재), 2026-08-15~16
- 화면:
  - 맥락(프롬프트 원문 없음): 리뷰어 응답서 작성
  - 에이전트가 한 일: "the Results sentence now ends **"(adjusted ORs 0.18-0.79, all p ≤ 0.009)"**. The added p value is the largest adjusted p among those components, taken from Table 2; no reanalysis was required."
  - 연구자가 확인한 것: "답변서의 원고 인용문 전부 r2 qmd/docx와 대조 → 일치" + `verify-numbers.R` 재실행 전부 일치. "all p ≤ 0.009"가 Table 2 다섯 구성요소 중 가장 큰 보정 p인지
- 노트 초안: 표와 그림은 코드에서 나오지만, 산문의 "0.18-0.79"는 누군가 표에서 옮겨 적은 글자다. 이 레포는 산문 수치를 하드코딩했고, 대신 출처를 응답서에 문장으로 남기고 표와 검증 스크립트로 대조했다. 이것은 13번에서 제가 꺼낼 한계이기도 하다.
- 확인 필요: "adjusted ORs 0.18-0.79, all p ≤ 0.009"를 출판본과 대조(PDF 암호 보호로 이번 작업에서 미확인).
- 출처: `11-methods-draft-and-number-sourcing.md`(responses-to-reviewers.qmd 128행, responses-to-reviewers-v2.qmd 174행, session-summary 2026-08-16 §5 39–40행), `memory/talk-scenes-from-repo.md` 23행

#### S44 (11-3). "완료되었습니다!"와 올바름은 다르다: 쓰는 에이전트와 검토하는 에이전트를 나누는 이유
- 시간 1.0분, 유형: 3단(코드)
- 한 줄 메시지: 혼자 쓰고 혼자 끝낸 에이전트의 결과는 아무도 확인하지 않는다.
- 에이전트: Positron Assistant(Claude Sonnet 4.6), 2026-03-12
- 화면:
  - 프롬프트: "현재 작업공간 contrast(emm1, "revpairwise", by = c("GROUP2", "C_ABOBESE"))의 결과에서 각 집단의 contrast 간 차이 검정"
  - 에이전트가 한 일: 다섯 번의 시도 끝에
    ```r
    est_diff <- cont_df$estimate[1] - cont_df$estimate[2]
    se_diff  <- sqrt(cont_df$SE[1]^2 + cont_df$SE[2]^2)
    ```
    주석 `# METS_new is the outcome (binary), not a predictor` → "완료되었습니다!"
  - 연구자가 확인한 것: 로그에 확인 흔적이 없다(대화가 여기서 끝남)
- 노트 초안: 두 대비는 같은 모형에서 나온 추정치라 공분산이 0이 아닐 수 있는데, SE를 `sqrt(SE1² + SE2²)`로 계산해 Var(a − b) = Var(a) + Var(b) − 2Cov(a, b)의 마지막 항을 버렸다. 또 `emm1`(METS_new를 예측변수로 둔 모형으로 보임)과 MetS를 결과로 둔 로지스틱 모형 사이를 오가며 "URATE-MeTS 연관성"으로 결론지었다. 결과는 그럴듯했지만 산출 경로가 틀렸고, 검토한 사람이 없었다. 수치는 출판 원고에 없는 탐색 결과라 화면에는 코드 패턴만 올린다.
- 확인 필요: `emm1`의 모형식은 로그에 없다(t-ratio와 df = 3681로 추정). 이 결과가 원고에 들어갔는지 레포 qmd에서 확인 후 말한다.
- 출처: `11-mets-new-outcome-not-predictor.md`(레포 루트 `conversation-export.json` msg[32–33])

#### S45 (11-4). 보고서 문장은 오케스트레이터가 쓰지 않는다: 근거 분석, 초안, 검토를 다른 에이전트에 나눈다
- 시간 1.0분, 유형: 다이어그램
- 한 줄 메시지: 쓰는 쪽과 검토하는 쪽을 나누고, 검토자에게는 파일만 넘긴다.
- 화면:
  - 오케스트레이터(근거 수집, 분배, 통합, 보고) → `evidence-analyst`(근거표) → `report-writer`(초안) → `report-reviewer`(초안마다 새로 띄움)
  - "근거표에 없는 내용은 보고서에 들어가지 못하고, 근거표에 틀린 내용이 있으면 그대로 평가 문서에 실린다. 그래서 자료에서 직접 확인한 것만 적는다."
  - "넘길 것은 검토할 파일 경로뿐이다. 오케스트레이터의 평가나 작성 워커의 설명을 붙이지 않는다."
- 노트 초안: 다른 프로젝트(연차보고서 작성)의 구성이다. 앞 장의 "완료되었습니다!"처럼 쓴 쪽이 스스로 끝내지 않도록 역할을 갈랐다. 다만 이 구성은 워커 셋이 모두 Opus 5.5라서 쓰는 모델과 검토하는 모델이 같은 계열이다. 다음 장의 구성은 그 점을 바꿨다.
- 메모: 프로젝트 폴더명은 화면에 쓰지 않고 "연차보고서 프로젝트"로 일반화한다. `<db>` 마스킹 유지. 강의 노트 프로젝트의 점검 스킬("지적만 하고 수정은 하지 않는다.")은 부록 A3로 뺐다.
- 출처: `setup-orchestration-annual-report.md`(annual-report SKILL.md 역할 표, 3단계, evidence-analyst.md 14–15행), `setup-skill-lecture-review.md`

#### S46 (11-5). 계약서 하나, 오케스트레이터 둘, 모델 다양성: 쓰는 모델과 검토하는 모델의 계열을 다르게 한다
- 시간 1.0분, 유형: 다이어그램
- 한 줄 메시지: 공유 상태는 대화가 아니라 레포이고, 검토는 다른 계열의 모델이 한다.
- 화면:
  - 중앙: CLAUDE.md = AGENTS.md, `memory/`, `review/`, git ("공유 상태는 대화가 아니라 레포다")
  - 왼쪽: 오케스트레이터 A 작성 허브 Claude Fable 5.1 → `slide-writer`, `fact-checker` (Claude Opus 5.5)
  - 오른쪽: 오케스트레이터 B 검토 허브 GPT-6.0 Astra, 독립 검토 워커 GPT-5.6 Terra
  - 규칙 2 "쓰는 모델과 검토하는 모델은 계열을 다르게 한다." / `run-worker.ps1`: "the header says "fallback from terra""
- 노트 초안: 지금 보시는 슬라이드가 이 구조로 만들어지고 있다. 이 아웃라인은 Opus가 썼고 Terra 또는 Astra가 검토한다. Terra가 한도에 걸리면 같은 작업을 Opus로 다시 돌리고 결과 머리에 실제 수행 모델을 적는다: 같은 계열 검토가 된 사실을 숨기지 않기 위해서다.
- 확인 필요: 도구 기능(Claude Code, Codex, Copilot CLI)은 발표 1주 전 최신 버전과 다시 대조(`CLAUDE.md` 행동 규칙 4). `memory/orchestration-decisions.md`의 미확인 항목(Copilot CLI `--agent` 등)은 말하지 않는다.
- 출처: `setup-orchestration-this-project.md`(CLAUDE.md 66–83행, `scripts/run-worker.ps1` 1–16행)

---

## 3막 그래서

### 섹션 12. 통제 지점 (3.0분)

| 번호 | 제목 | 분 | 유형 |
|---|---|---|---|
| S47 (12-1) | 연구자의 통제 지점은 네 곳이다: 실행 전, 데이터 노출, 빼는 결정, 저자 검토 | 0.75 | 다이어그램 |
| S48 (12-2) | ① 실행 전 승인: 연구자는 도구 호출을 거부하고 범위를 다시 정했다 | 0.5 | 텍스트 |
| S49 (12-3) | ② 노출 규칙: 데이터가 에이전트와 화면으로 가는 길을 규칙으로 미리 좁힌다 | 0.5 | 텍스트 |
| S50 (12-4) | ③ 빼는 결정: 사실이어도 설계 시점의 이유가 아니면 응답서에 넣지 않는다 | 0.5 | 텍스트 |
| S51 (12-5) | ④ 저자 검토: "중복 인용"으로 지운 다섯 편을 저자가 되살렸다 | 0.75 | 텍스트 |

#### S47 (12-1). 연구자의 통제 지점은 네 곳이다: 실행 전, 데이터 노출, 빼는 결정, 저자 검토
- 블록 제목: `## 12. 연구자의 통제 지점은 네 곳이다: 실행 전, 데이터 노출, 빼는 결정, 저자 검토`
- 시간 0.75분, 유형: 다이어그램(S55에서 재사용)
- 한 줄 메시지: 앞의 장면들은 연구자가 멈추거나 되돌린 네 지점으로 묶인다.
- 화면: 파이프라인 진행바 위에 표지 4개. ① 실행 전 승인(분석) ② 노출 규칙(데이터 이해) ③ 빼는 결정(논문) ④ 저자 검토(논문)
- 노트 초안: 네 지점의 공통점은 에이전트가 할 수 있는 일을 연구자가 멈추거나 되돌리는 순간이라는 것이다. 지점마다 로그 장면 하나씩을 본다. 이 그림으로 발표를 닫는다.
- 출처: S48–S51의 출처

#### S48 (12-2). ① 실행 전 승인: 연구자는 도구 호출을 거부하고 범위를 다시 정했다
- 시간 0.5분, 유형: 텍스트(인용 3줄)
- 한 줄 메시지: 승인 단계에서 멈추면 잘못된 파일이 생기지 않는다.
- 에이전트: Positron Assistant(Claude Sonnet 4.6), 2026-03-19
- 화면:
  - (도구 결과) `{"type": "error-text", "value": "User declined to execute tool."}`
  - (에이전트) "**Tool execution canceled by user.** What would you like me to do instead?"
  - (사용자) "내가 원했던건 연구질문 4와 관련한 분석 스크립트를 새로운 R 파일로 작성하라는 것이야."
- 노트 초안: 원래 요청은 "분석 결과 도출을 위해 생성했던 스크립트들을 새로운 파일로 저장"이었고, 에이전트는 이를 넓게 해석해 flextable 스크립트부터 저장하려 했다. 연구자가 실행을 거부하고 범위를 다시 정했다. 다시 시작한 에이전트는 계약서 규칙의 저장 위치(`code/agent_bot/2026-03-19/`)에 RQ4 스크립트 두 개를 만들었다.
- 출처: `07-user-cancels-tool-call.md`(finalize msg[12–15])

#### S49 (12-3). ② 노출 규칙: 데이터가 에이전트와 화면으로 가는 길을 규칙으로 미리 좁힌다
- 시간 0.5분, 유형: 텍스트(두 열)
- 한 줄 메시지: 무엇을 보여줄지가 아니라 무엇이 나갈 수 있는지를 먼저 정한다.
- 화면:
  - 왼쪽(이 발표의 `CLAUDE.md` 화면 노출 규칙): "조종사 데이터는 구조만 보여준다" / "집계값만 쓴다. 5명 미만 셀은 "5 미만"" / "식별 가능 열(ID, 검진일, 소속)은 변수명조차 띄우지 않는다"
  - 오른쪽(임상 DB 프로젝트의 접근 스킬): "**읽기만 한다.**" / "**집계값만 꺼낸다.**" / "**접속 정보를 옮겨 적지 않는다.** … 이 파일을 `Read` 로 열지 않고"
- 노트 초안: 오늘 화면의 데이터는 모두 변수명, 자료형, 단위, 집계값이었다. 임상 DB에 에이전트를 붙인 다른 프로젝트는 같은 원칙을 스킬로 고정했다: 읽기 전용 세션, 집계만, 5 미만, 접속 정보 파일은 에이전트가 열지도 않는다.
- 확인 필요: 사례 레포의 계약서에 같은 노출 규칙이 있었는지(런북 스킬은 "없으면 시연용 프롬프트에 직접 쓴다"고 적고 있음).
- 출처: `CLAUDE.md` 화면 노출 규칙 1–3, `setup-skill-db-access-rules.md`(규칙 1, 2, 4), `.claude/skills/demo-runbook/SKILL.md` 점검표 5
- 메모: `setup-skill-db-access-rules.md`는 섹션 9 표시이나 12번으로 옮겼다. 전문은 부록 A2.

#### S50 (12-4). ③ 빼는 결정: 사실이어도 설계 시점의 이유가 아니면 응답서에 넣지 않는다
- 시간 0.5분, 유형: 텍스트(인용)
- 한 줄 메시지: 통제는 무엇을 더하느냐만이 아니라 무엇을 빼느냐에도 있다.
- 에이전트: DataBot(모델 미기재), 리뷰어 대응안
- 화면: "**"사분위 상한이 MetS 진단 절단값과 거의 일치한다"** … 사실이지만 **이 표본에서만 성립하는 우연의 일치**이며 사후 관찰임. 설계 시점의 사유가 아니므로 "왜 사분위를 썼는가"에 대한 답이 될 수 없고, 응답서에 넣으면 사후 정당화로 읽힘."
- 노트 초안: Reviewer 2가 "연령은 10년 구간인데 왜 다른 변수는 사분위인가"를 물었다. 1차 개정안에 들어갔던 절단값 일치표(WC 89.1 vs 90 등)는 폐기됐고, 채택한 논거는 연속형 지표를 사분위로 나누는 관례와 원고가 이미 인용하던 선행 ROKAF 연구(rhee2015)였다. 사실인 표라도 설계 시점의 이유가 아니면 답이 아니다.
- 확인 필요: 폐기를 사용자가 지시했는지 에이전트가 먼저 제안했는지는 발췌에 없다. 파일은 `2026-08-14` 폴더인데 본문은 "2026-08-15 1차 개정안"을 언급한다(파일이 이후 갱신된 것으로 보임).
- 출처: `12-posthoc-argument-dropped.md`(reviewer2-response-plan.md 410–412, 416–424행)

#### S51 (12-5). ④ 저자 검토: "중복 인용"으로 지운 다섯 편을 저자가 되살렸다
- 시간 0.75분, 유형: 텍스트(인용)
- 한 줄 메시지: 규칙을 기계적으로 적용하면 해석 틀의 근거가 사라진다. 저자 검토가 마지막 관문이다.
- 에이전트: DataBot(모델 미기재), 2026-08-16
- 화면:
  - "We anchor our findings within the framework of the healthy-worker effect (HWE) in aviation [@cairns2020; @houston2011; @koterov2025; @park2024; @pizzi2008] …"
  - "해석 틀을 도입하는 문장에 근거가 없어지는 것은 중복 제거가 아님."
  - 교훈: "각 문장이 자체 근거를 필요로 하는지 먼저 볼 것"
- 노트 초안: 오전 세션이 Discussion 재인용과 중복이라며 Introduction의 인용 다섯 편을 지웠고, 저녁에 사용자 검토 후 복원했다. 같은 날 반대 방향도 있었다: 새로 넣은 Table 3 각주 문장은 사용자 지적으로 진짜 중복이라 삭제했다. 렌더 결과 참고문헌 36편 불변, 복원 5편은 [17–21].
- 출처: `12-hwe-citations-restored.md`(session-summary 2026-08-16 §5-1 44–48행, r2 qmd 352행)

### 섹션 13. 효과, 한계 (2.0분)

| 번호 | 제목 | 분 | 유형 |
|---|---|---|---|
| S52 (13-1) | 에이전트가 줄인 것은 판단이 아니라 판단을 옮기는 노동이다 | 0.5 | 텍스트 |
| S53 (13-2) | 이 사례의 약점 세 가지를 제가 먼저 말씀드린다 | 0.75 | 텍스트 |
| S54 (13-3) | 에이전트의 한계는 일관되지 않다는 데 있다: 전제를 따라가고, 부호를 뒤집고, 완료를 선언한다 | 0.5 | 텍스트 |
| S55 (13-4) | 판단은 연구자가, 그 판단을 끝까지 밀고 가는 노동은 에이전트가 | 0.25 | 다이어그램(S47 재사용) |

#### S52 (13-1). 에이전트가 줄인 것은 판단이 아니라 판단을 옮기는 노동이다
- 블록 제목: `## 13. 에이전트가 줄인 것은 판단이 아니라 판단을 옮기는 노동이다`
- 시간 0.5분, 유형: 텍스트
- 한 줄 메시지: 로그로 말할 수 있는 효과는 "무엇을 맡겼는가"까지다.
- 화면:
  - 맡긴 것: 기존 스크립트 감사, 설계안 초안, 에러 수정, knit 재작성, 표, 그림 파이프라인, 수치 재계산(약물, 유병률 12개, BMI 6단계, Table 4 SI 계수)
  - `<여기에: 체감 효과 한 줄. 예: 리뷰어 대응에 든 기간>`
- 노트 초안: 시간 절약 같은 정량 효과는 로그에 없으므로 사용자의 경험으로 채운다. 로그에서 확인되는 것은 위 목록이다. 이 목록에 설계 판단은 하나도 없다.
- 출처: `06-script-audit-questions.md`, `06-design-proposal-choice.md`, `07-mediation-env-error.md`, `07-knit-failure-three-causes.md`, `10-table-figure-automation.md`, `09-verify-numbers-script.md`

#### S53 (13-2). 이 사례의 약점 세 가지를 제가 먼저 말씀드린다
- 시간 0.75분, 유형: 텍스트(목록 3)
- 한 줄 메시지: 에이전트가 만든 문장과 구조라도 받아들인 책임은 저자에게 있다.
- 화면:
  1. "non-collapsibility"는 틀린 이름이다. 척도 의존성이다 (8-3)
  2. 원고 산문의 수치는 하드코딩이다. 표와 `verify-numbers.R`로 교차검증했지만 코드에서 자동으로 나오지는 않는다 (11-2)
  3. probit을 고른 근거가 약하다. 초안의 이유는 "to match the visual representation conventions", 출판본에는 이유가 없다 (8-4)
- 노트 초안: 1은 에이전트의 용어를 검토 없이 받으면 생기는 종류의 오류이고, 2는 "표, 그림은 코드에서 나온다"는 메시지의 경계이며, 3은 "판단은 연구자가"라는 주장이 이 사례에서 완전히 지켜지지 않은 지점이다. 청중이 먼저 묻기 전에 제가 꺼낸다.
- 확인 필요: 출판본에 "non-collapsibility" 표현이 들어갔는지(PDF 미확인).
- 출처: `memory/talk-scenes-from-repo.md` 31행, `08-probit-logit-probability-scale.md`, `11-methods-draft-and-number-sourcing.md`, `08-probit-choice-reason.md`

#### S54 (13-3). 에이전트의 한계는 일관되지 않다는 데 있다: 전제를 따라가고, 부호를 뒤집고, 완료를 선언한다
- 시간 0.5분, 유형: 텍스트(목록 3)
- 한 줄 메시지: 자명한 오류는 에이전트가 잡고, 그럴듯한 오류는 연구자와 재계산이 잡는다.
- 에이전트: Positron Assistant(Claude Sonnet 4.6) 장면 모음
- 화면:
  - 질문의 전제를 따라간다 (9-1, 두 OR)
  - 같은 메시지 안에서 해석 방향이 바뀐다 (9-2, Δβ 부호)
  - 검토 없이 "완료되었습니다!" (11-3, 공분산 누락)
- 노트 초안: 전부 0%(7-4)나 YAML 오탐(9-4)처럼 자명한 오류는 에이전트가 스스로 잡았다. 그럴듯한 오류는 연구자가 멈추거나 뒤 단계의 재계산이 잡았고, 하나는 아무도 잡지 않았다. 그래서 검증은 에이전트의 자기 보고가 아니라 데이터에서 다시 계산하는 절차여야 한다.
- 출처: `09-two-odds-ratios-confused.md`, `09-delta-beta-sign.md`, `11-mets-new-outcome-not-predictor.md`, `07-factor-prevalence-zero.md`, `09-false-positive-validation-rule.md`

#### S55 (13-4). 판단은 연구자가, 그 판단을 끝까지 밀고 가는 노동은 에이전트가
- 시간 0.25분, 유형: 다이어그램(S47 통제 지점 그림 재사용) + QR
- 한 줄 메시지: 네 통제 지점으로 돌아와 닫는다.
- 화면: S47 그림 + 스타터킷 `<여기에: 공개 레포 주소와 QR>`
- 노트 초안: 처음의 주장으로 돌아온다. 네 지점을 쥐고 있으면 나머지 반복 노동은 맡길 수 있다. 스타터킷에는 계약서 템플릿, 스킬, 에이전트 템플릿, 검증 체크리스트가 들어 있다. 이어서 질문을 받는다.
- 출처: `CLAUDE.md` 목적 3, `.claude/skills/starter-kit/SKILL.md`

---

## 부록 (Q&A 대비, 시간 미배정)

| 번호 | 제목 | 유형 | 출처 |
|---|---|---|---|
| A1 | 표본크기 산출 하나를 여섯 스킬로 쪼갠다: description에 트리거 문구를 넣는다 | 코드 | `setup-skills-ss-bundle.md`(마스킹 유지: `<project-name>`, `<indication>`) |
| A2 | 임상 DB에 에이전트를 붙일 때의 규칙 일곱 개 | 텍스트 | `setup-skill-db-access-rules.md` |
| A3 | 점검 스킬은 지적만 하고 고치지 않는다 | 코드 | `setup-skill-lecture-review.md` |
| A4 | 같은 연령 상호작용, 세 척도, 세 결론: probit 링크 / logit 재격자 OR ratio / 확률 | 표 | `08-probit-logit-probability-scale.md`, `09-hand-calculation-check.md` |
| A5 | 표 값이 도출되는 과정: `tbl-dyslip` 청크와 footnote | 코드 | `08-medication-imbalance-report.md` |

부록 노트(공통): 질문이 나왔을 때만 띄운다. A4의 수치는 2026-03-17 탐색 단계 값(probit p 0.328 / 0.543 / 0.595, OR ratio p 0.5539 / 0.9810 / 0.8751, 확률 척도 p 0.019 / 0.003 / 0.001). A5의 "유의성 소실"은 2026-03-10 Model 3 기준 중간 해석이고 원고 최종값은 LDL Δβ 0.24 (p = 0.022), TC Δβ 0.20 (p = 0.049).

---

## 발췌본 사용 현황 (33개)

| 발췌 파일 | 사용 슬라이드 |
|---|---|
| 05-urate-origin | S16, S17, S31, S34(최종값) |
| 06-contract-mets-definition | S11, S12, S13, S14, S31(질문 대비), S39 |
| 06-design-proposal-choice | S06, S10, S20, S21, S52 |
| 06-script-audit-questions | S10, S14, S19, S25(노트), S52 |
| 07-data-structure | S18, S13, S30 |
| 07-knit-failure-three-causes | S06, S10, S14, S23, S24, S52 |
| 07-user-cancels-tool-call | S10, S11, S14, S48 |
| 07-mediation-env-error | S06, S21, S22, S52 |
| 07-factor-prevalence-zero | S25, S54 |
| 08-probit-logit-probability-scale | S27, S28, S35, S53, A4 |
| 08-probit-choice-reason | S09, S14, S20, S26, S29, S42, S53 |
| 08-unweighted-decision | S15, S30, S42 |
| 08-medication-imbalance | S31 |
| 08-medication-imbalance-report | S12, S31, A5 |
| 08-waist-adjustment-circularity | S26, S32 |
| 09-two-odds-ratios-confused | S07, S33, S54 |
| 09-delta-beta-sign | S34, S54 |
| 09-hand-calculation-check | S26, S35, A4 |
| 09-verify-numbers-script | S12, S21, S31, S36, S37, S52 |
| 09-render-success-missing-figure | S15, S38 |
| 09-false-positive-validation-rule | S36, S54 |
| 10-table-figure-automation | S39, S40, S41, S52 |
| 11-methods-draft-and-number-sourcing | S42, S43, S53 |
| 11-mets-new-outcome-not-predictor | S44, S54 |
| 12-hwe-citations-restored | S51 |
| 12-posthoc-argument-dropped | S50 |
| setup-claude-md-six-blocks | S11 |
| setup-skill-lecture-review | S45(노트), A3 |
| setup-skill-session-memory | S15 |
| setup-skills-ss-bundle | A1(본 발표 미사용) |
| setup-orchestration-this-project | S46 |
| setup-skill-db-access-rules | S49, A2 |
| setup-orchestration-annual-report | S45 |

## 넘칠 때 줄일 순서

본 발표 총계가 정확히 53.0분이라 버퍼가 없다. 리허설에서 넘치면 아래 순서로 줄인다(필수 요구 장면은 건드리지 않는 순서).

1. S15 memory(0.75) → S11 노트로 합침
2. S21 매개분석 결정(1.25) → 삭제, 한 줄("매개분석은 연구자가 원고에서 뺐다")만 S20 노트로
3. S41 그림 수정(0.5) → 삭제, 내용은 S39 노트로
4. S54 에이전트 한계(0.5) → S53에 한 줄로 합침
5. S40 라이브 D3(2.75) → 2.25분으로 줄이고 바로 백업 녹화 사용
