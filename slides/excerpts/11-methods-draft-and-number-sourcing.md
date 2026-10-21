# 11. Methods 초안과 산문 수치의 출처: 숫자는 하드코딩하되 표·스크립트와 대조한다

출처:
- `G:/Projects/airforce-fatty-liver/quarto/agent_bot/2026-03-19/05_statistical_analysis_methods.qmd` 1–5행(YAML), 21–34행(Overview)
- `G:/Projects/airforce-fatty-liver/quarto/agent_bot/2026-08-15/responses-to-reviewers.qmd` 128행; `quarto/agent_bot/2026-08-16/responses-to-reviewers-v2.qmd` 174행(같은 문장)
- `G:/Projects/airforce-fatty-liver/memory/agent_bot/2026-08-16/session-summary.md` §5 39–40행
날짜: 2026-03-21(Methods 초안), 2026-08-15/16(답변서)
에이전트: qmd 저자란 "Databot (Agent Analysis)" (모델 미기재)

## 인용

### Methods 초안 머리 (05_statistical_analysis_methods.qmd, 15줄 이내)

```yaml
title: "Statistical Analysis Methods"
subtitle: "Air Force Pilot vs. KHANES 2022 — Metabolic Syndrome Comparative Study"
author: "Databot (Agent Analysis)"
date: "2026-03-21"
```

> ## Overview
>
> All statistical analyses were performed in R (version 4.5.2; R Core Team, 2025)
> using the tidyverse suite (Wickham et al., 2019) for data manipulation,
> the broom package (Robinson et al., 2023) for model tidying, and the emmeans
> package (Lenth, 2024) for estimated marginal means and contrast estimation.
> Regression tables were produced with the flextable package (Gohel & Skintzos, 2024).
> A two-sided significance level of $\alpha = 0.05$ was applied throughout.
> Continuous variables are summarised as mean ± SD and categorical variables as
> frequency (percentage). Baseline comparisons between groups used Welch's
> two-sample *t*-test for continuous variables and Pearson's $\chi^2$ test (or
> Fisher's exact test when any expected cell count was less than 5) for
> categorical variables.

(출판본은 "R (V.4.5.3)". 초안과 출판본 사이에 R 버전이 올라갔다)

### 산문 수치가 하드코딩이며 표에서 가져온다는 기록 (responses-to-reviewers.qmd 128행)

> **Response.** All three changes made. The Abstract now reads **"Logistic regression was used to determine crude and adjusted odds ratios (ORs) for overall MetS and for each of the five individual MetS criteria"**, and the Results sentence now ends **"(adjusted ORs 0.18-0.79, all p ≤ 0.009)"**. The added p value is the largest adjusted p among those components, taken from Table 2; no reanalysis was required.

### 답변서 인용문과 원고의 교차검증 (2026-08-16 session-summary §5)

> - 답변서의 원고 인용문 전부 r2 qmd/docx와 대조 → 일치 (Table 1 각주·Table 2 라벨은 렌더된 docx에서 확인)
> - `verify-numbers.R` 재실행: 약물/유병률 12개, BMI 6단계, Table 4 SI 계수 전부 일치. …

## 슬라이드에서 쓸 핵심
- 한 줄 메시지: 원고 산문의 숫자는 R 객체가 아니라 글자다. 그래서 표와 검증 스크립트로 대조하는 절차가 따로 필요하다
- 보여줄 부분(코드/출력/문장): Overview 첫 문단(패키지 인용까지 에이전트가 채움)과 "taken from Table 2; no reanalysis was required" 한 문장
- 연구자가 확인한 것: "all p ≤ 0.009"가 Table 2의 다섯 구성요소 중 가장 큰 보정 p인지. 발표 전 짚을 점: 10번 메시지를 "코드에서 나오거나 스크립트로 검증된다"로 바꿔 말한다(`memory/talk-scenes-from-repo.md` 27행)
