# 6. 계약서(CLAUDE.md)에 MetS 정의가 미리 있었기에 에이전트는 묻지 않았다

출처: `G:/Projects/airforce-fatty-liver/CLAUDE.md` 5행(상태), 26–39행(행동 규칙 1–9), 252–260행(MetS 진단 기준 블록), 190–202행(분석 데이터 설명)
날짜: 파일 기준 2026-03-18(CLAUDE.md "주요 분석 결과 요약 (2026-03-18 기준)")
에이전트: 해당 없음(사용자가 쓴 계약서). 대화 로그(`agent-conversation/*.json`, Positron Assistant, Claude Sonnet 4.6)에 MetS 정의·허리둘레 기준·공복 여부를 묻는 장면이 없음(`memory/talk-scenes-from-repo.md` 10행)

## 인용

### 상태 줄 (5행)

> 상태: 데이터 전처리 완료, 기초 및 최종 분석 완료, Quarto 분석 보고서 작성 완료

### 행동 규칙 1–9 (26–39행)

> ## 행동 규칙
>
> 1.  결과 생성 및 해석 시 추론은 최대한 배제하고 근거에 기반한 답변 도출
> 2.  생성한 코드에 대한 주석은 영어로 상세하게 작성
> 3.  최상단에 작성날짜, 작업개요, 파일명을 주석으로 생성
> 4.  결과 보고서 작성 시 수식이 필요한 경우 모두 삽입. 아울러 수식에 대한 상세 설명 추가
> 5.  답변은 한국어로 생성. 단, 생성한 표, 그림의 제목, 캡션, footnote 등은 영어로 작성
> 6.  논문 manuscript는 영어로 작성. 문서 생성은 quarto -\> word_docx 변환
> 7.  quarto 문서에서 테이블 및 그림 생성 시 사용하기 위해 만든 데이터셋은 quarto 문서 청크에 남김
>     -   직접 테이블을 생성하지 말고 테이블 값이 도출되는 과정을 반드시 남김
>     -   quarto 문서에 수식 사용 시 $$...$$ 또는 $...$ 사용
>     -   문헌 인용 시 인용한 부분의 내용을 발췌\
> 8.  테이블은 Lancet 논문 포맷 적용
> 9.  모든 수치 결과는 그 도출 과정을 문서에 포함

### MetS 진단 기준 블록 (252–260행, "사전 정보" 절 안)

> 8. 대사증후군 (Metabolic Syndrome, MeTS) 진단 기준
>
>     - 복부비만 : 남성: ≥ 90cm / 여성: ≥ 85cm (허리둘레): mets_c1
>     - 중성지방 : ≥ 150 mg/dL 또는 이상지질혈증 약물 복용 중 :mets_c2
>     - HDL : 남성: < 40 mg/dL / 여성: < 50 mg/dL 또는 약물 복용 중 :mets_c3
>     - 혈압 : 고혈압 약물 복용중 또는 수축기 혈압  ≥ 130 또는 
>              이완기 혈압  ≥ 85 :mets_c4
>     - 공복혈당 : ≥ 100 mg/dL 또는 당뇨병 약물 복용 중 :mets_c5

같은 "사전 정보" 절에는 고혈압·복부비만·비만·당뇨·고중성지방·고콜레스테롤·이상지질혈증 7개 정의(204–250행)와 표본 흐름(192–202행)이 함께 있다:

> 1. Health examination data from Air force pilot (aged from 24 to 61)
>    From total of 2827 cases
>     - Exclude Female cases (N = 88) 2739
>     - Exclude missing cases (N = 135) 2604 (final)
> 2. KHANES data 
>    From total of 6265 (2022) cases
>     - Exclude Female cases (N = 3468)  2797
>     - Exclude age not in 24-61 (N = 1498) 1299
>     - Exclude missing cases (N = 207) 1093 (final)

### 에이전트가 정의를 묻지 않은 근거

대화 로그 3종(`conversation-finalize.json`, `conversation-add-analysis.json`, `conversation-probit-logit-prob.json`)을 2026-10-19에 조사한 결과(`memory/talk-scenes-from-repo.md` 10행):

> MetS 정의·허리둘레 기준·공복을 묻는 장면은 없음. CLAUDE.md 253–260행에 미리 적혀 있었음 → 4번과 연결

반대로 에이전트가 정의와 코드의 불일치를 먼저 짚은 장면은 있다(같은 파일 9행, `conversation-add-analysis.json` msg[3]):

> 스크립트 감사: 포화모형 다중공선성 가능, MetS 기준 행 주석 처리 "의도적인지 확인 필요"

## 슬라이드에서 쓸 핵심
- 한 줄 메시지: 정의를 계약서에 적어 두면 에이전트는 묻는 대신 그 정의와 코드의 불일치를 찾는다
- 보여줄 부분(코드/출력/문장): MetS 블록 5줄(mets_c1–c5)과 규칙 7·9. 변수명(mets_c1–c5)이 계약서에서 코드로 그대로 이어진 점
- 연구자가 확인한 것: 허리둘레 기준(남 ≥ 90 cm)과 혈압 기준(≥ 130/85)이 한국 기준임을 연구자가 결정해 적었고, 에이전트는 그 결정을 바꾸지 않았다. 표본 흐름 수치(2,604 / 1,093)는 논문 2 최종값과 같다
