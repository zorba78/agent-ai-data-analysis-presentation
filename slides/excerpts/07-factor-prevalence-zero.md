# 7. factor 열을 숫자처럼 더해 유병률이 전부 0%로 나온 뒤 고치다

출처: `G:/Projects/airforce-fatty-liver/agent-conversation/conversation-finalize.json` msg[27] (사용자 요청은 msg[26])
날짜: 2026-03-21
에이전트: Positron Assistant (Claude Sonnet 4.6)

## 인용

> (사용자) afhe-khanes-analysis-report-word.qmd 의 전체 분석 결과 해석.  결과 해석 문서는 새롭게 영문으로 작성. 결과해석 내용만 생성(테이블, 그림 생성 필요 없음)

> (에이전트) 먼저 전체 분석 결과 수치를 재확인하겠습니다.

시도 1: 패키지 미로드.

> (도구 결과) Error in `count()`: ! could not find function "count"

시도 2: `library(tidyverse)` 후 `summarise(n = sum(value, na.rm=TRUE), …)`로 mets_c1~c5 유병률 계산. 시도 3에서 다음으로 바꿈:

```r
mutate(across(mets_c1:mets_c5, ~ as.integer(as.character(.x) == "1" |
                                               .x == TRUE |
                                               as.numeric(as.character(.x)) == 1)))
```

> (도구 결과) === MeTS component prevalence ===
>    GROUP2   name        n total   pct
>  1 KHANES   mets_c1     0  1093     0
>  2 KHANES   mets_c2     0  1093     0
>  … (10행 모두 n = 0, pct = 0)
> Warning message: There were 5 warnings in `mutate()`. … ! NAs introduced by coercion
> mets_c1 class: fa[ctor] …

시도 4:

```r
# Correct approach for factor "Yes"/"No"
mutate(across(mets_c1:mets_c5, ~ as.integer(.x == "Yes")))
```

> (도구 결과) === MeTS component prevalence ===
>    GROUP2   name        n total   pct
>  1 KHANES   mets_c1   495  1093  45.3
>  2 KHANES   mets_c2   531  1093  48.6
>  3 KHANES   mets_c3   207  1093  18.9
>  4 KHANES   mets_c4   424  1093  38.8
>  5 KHANES   mets_c5   468  1093  42.8
>  6 Pilot HE mets_c1   339  2604  13
>  7 Pilot HE mets_c2   526  2604  20.2
>  8 Pilot HE mets_c3    98  2604   3.8
>  9 Pilot HE mets_c4  1242  2604  47.7
> 10 Pilot HE mets_c5   720  2604  27.6

(원고 최종값과 일치: 논문 2 Table의 구성요소 유병률. 복부비만 13.0% vs 45.3%, 혈압 47.7% vs 38.8%)

## 슬라이드에서 쓸 핵심

- 한 줄 메시지: 코드북에 "mets_c1~c5 = factor(No/Yes)"라고 적혀 있었는데도 에이전트는 숫자 코딩을 가정했다. 0%라는 말이 안 되는 값이 나오자 `class()`를 확인하고 고쳤다.
- 보여줄 부분(코드/출력/문장): "모두 0, NAs introduced by coercion" 출력 한 덩어리와 `as.integer(.x == "Yes")` 한 줄. 같은 세션 msg[3](add-analysis)에서 에이전트 자신이 "mets_c1~c5 → factor(0="No", 1="Yes")"라고 요약했던 점을 발표자 노트에.
- 연구자가 확인한 것: 자명한 오류(전부 0%)는 에이전트가 스스로 잡지만, 그럴듯한 오류는 못 잡는다. 코드북과 자료형을 CLAUDE.md에 적어 두는 이유(4번 섹션)와 연결.
