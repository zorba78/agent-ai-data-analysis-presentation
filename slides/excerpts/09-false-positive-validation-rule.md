# 9. 에이전트의 자체 검증 규칙이 거짓 양성을 내고, 그걸 스스로 가려내다

출처: `G:/Projects/airforce-fatty-liver/agent-conversation/conversation-finalize.json` msg[27] 후반
날짜: 2026-03-21
에이전트: Positron Assistant (Claude Sonnet 4.6)

## 인용

문서 `04_full_interpretation.qmd`(196줄, 코드 청크 없음) 저장 뒤 에이전트가 돌린 검증 코드(발췌):

```r
chk <- list(
  "YAML: title line"              = any(grepl("^title:", L)),
  "YAML: no # comments"           = !any(grepl("^#", L[1:25])),
  "YAML closed (---)"             = sum(grepl("^---$", L)) >= 2,
  …
  "MetS 11.1% Pilot HE"           = any(grepl("11\\.1%", L)),
  "MetS 37.1% KHANES"             = any(grepl("37\\.1%", L)),
  "OR 0.30 adj overall"           = any(grepl("0\\.30", L)),
  "OR 2.12 blood pressure"        = any(grepl("2\\.12", L)),
  "GLUC OR PH 5.80"               = any(grepl("5\\.80", L)),
  …
  "No code chunks"                = !any(grepl("^```\\{r", L))
)
```

> (도구 결과) === Validation (04_full_interpretation.qmd) ===
>   YAML: title line                              : OK
>   YAML: no # comments                           : *** FAIL ***
>   YAML closed (---)                             : OK
>   …

다음 호출: YAML 블록 끝(`---` 두 번째)을 찾아 그 안의 `#` 줄만 다시 검사.

> (도구 결과) YAML ends at line: 22
> Lines with # in YAML block:
> (없음)

```r
# The # check was looking at L[1:25] — line 22 is YAML end (---),
# let's check lines 23-25 which are after YAML
…
# Re-check: first # after line 22 means it's a markdown heading, not YAML comment.
# The validation rule was wrong — # in body is fine. Only # inside YAML block matters.
```

> (도구 결과) Line 21: [  message: false]
> Line 22: [---]
> Line 23: []
> Line 24: [## Overview]
> …
> Actual # lines strictly inside YAML (lines 1 to 22 ):
>   None found. YAML is clean.

> (에이전트) YAML 내부에 주석이 없습니다. 검증 규칙 오류였고 실제 파일은 정상입니다.
> …
> 저장 완료했습니다. YAML 내부 `#` 주석은 없으며 파일은 정상입니다 (검증 규칙 `[1:25]`가 YAML 외부 마크다운 헤딩 `##`을 잘못 감지한 것).

## 슬라이드에서 쓸 핵심

- 한 줄 메시지: 에이전트는 자기 산출물에 grep 기반 검증표를 붙인다. 그 검증 자체가 틀릴 수 있고(`L[1:25]` 하드코딩), 이번엔 에이전트가 FAIL의 원인을 추적해 규칙 쪽을 고쳤다.
- 보여줄 부분(코드/출력/문장): 검증 목록 중 수치 항목 4~5줄(11.1%, 37.1%, 0.30, 2.12, 5.80)과 "*** FAIL ***" → "검증 규칙 오류였고 실제 파일은 정상입니다".
- 연구자가 확인한 것: 수치 검증이 "문서 안에 그 문자열이 있는가"에 불과하다는 점. 이것이 이 프로젝트가 `verify-numbers.R`(RDS에서 재계산)을 따로 둔 이유. 원고 산문의 수치는 하드코딩이므로 검증 스크립트가 필요하다(memory 파일 "발표 전 짚을 점"과 연결).
- 주의: 검증 목록의 수치는 2026-03-21 시점 값이고 원고 최종값(aOR 0.30, 혈압 2.12, GLUC OR 5.80)과 같다.
