# 8. probit 선택 근거가 "시각적 표현과 맞추기 위해"로 기록됨: 약한 근거

출처:
- `G:/Projects/airforce-fatty-liver/quarto/agent_bot/2026-03-19/05_statistical_analysis_methods.qmd` 86–94행(층화 변수), 96–112행(probit GLM과 선택 이유), 114–120행(OR 도출)
- 대조: `references/military-2026-003444.full.pdf` Statistical analysis 절(4쪽, pypdf 추출)
날짜: 2026-03-21(qmd `date`), 출판본 2026
에이전트: qmd 저자란 "Databot (Agent Analysis)" (모델 미기재)

## 인용

### 에이전트 초안의 Methods (05_statistical_analysis_methods.qmd)

> Seven variables were used to stratify participants: age group (AGE) and
> six continuous MetS-component variables (waist circumference [WC], systolic
> blood pressure [SBP], diastolic blood pressure [DBP], HDL cholesterol, TRIG,
> and GLUC). … The six continuous variables were
> each divided into quartiles (Q1--Q4) using cut-points derived from the
> **pooled** distribution of all 3,697 participants, ensuring that the
> group-comparison reference is a common population scale.
>
> ### Probit binomial generalised linear model for prevalence estimation
>
> Within each stratification variable $V$, MetS prevalence was estimated via
> a probit binomial GLM:
>
> $$
> \Phi^{-1}\!\left[P(\text{MetS}_i = 1)\right]
> = \beta_0 + \beta_1 \text{GROUP2}_i
> + \beta_2 V_i
> + \beta_3 (\text{GROUP2}_i \times V_i)
> $$
>
> where $\Phi^{-1}$ is the probit (inverse normal CDF) link function.
> Estimated marginal means (EMMs) on the response (probability) scale were
> obtained from `emmeans::emmeans(..., type = "response")`, yielding
> model-adjusted prevalence estimates with 95% CIs for each GROUP2 × stratum
> cell. The probit link was chosen to match the visual representation
> conventions used in the companion figure (forest plot of EMM-based
> prevalence).
>
> ### Odds ratios and OR ratios
>
> Between-group ORs (Pilot HE vs KHANES) within each stratum were derived
> from pairwise contrasts on the **logit**-scale EMMs, using
> `emmeans::regrid(..., "logit")` followed by
> `emmeans::contrast(..., method = "revpairwise", by = V)`.

### 출판본 Statistical analysis (논문 2, 4쪽; 추출 텍스트의 줄바꿈 하이픈은 이어 붙임)

> Analyses were performed using R (V.4.5.3). Continuous variables are reported as mean±SD and categorical variables as percentages; groups were compared using Welch's t-test and Pearson's χ2 or Fisher's exact tests. MetS prevalence, components and adjusted associations were compared using logistic regression with adjustment for age, smoking, alcohol use and physical activity. Effect modification across age groups and pooled-sample quartiles of continuous risk factors was tested using probit-binomial models with interaction terms and likelihood-ratio tests (LRTs). For 15 z-scored biomarkers, nested logistic regression estimated group-specific ORs for MetS per 1-SD increase: Model 0 included group, biomarker and their interaction; Model 1 added lifestyle covariates and Model 2 further adjusted for BMI and medications. Interactions were assessed using Wald-type z statistics. Linear regression examined determinants of urate and fasting glucose, with pooled-model interaction tests. All tests were two-sided, with p<0.05 considered statistically significant.

## 슬라이드에서 쓸 핵심
- 한 줄 메시지: 모형 선택 이유를 에이전트가 쓰면 "그림과 맞추려고"가 된다. 출판본은 이유를 빼고 무엇을 했는지만 남겼다. 이유는 연구자의 몫이다
- 보여줄 부분(코드/출력/문장): "The probit link was chosen to match the visual representation conventions used in the companion figure" 한 문장과, 출판본의 "tested using probit-binomial models with interaction terms and likelihood-ratio tests" 한 문장을 나란히
- 연구자가 확인한 것: probit로 적합하고 OR은 logit 척도로 regrid해 뽑는 2단계 구조가 맞는지. 상호작용이 probit에서 비유의, 확률 척도에서 유의로 갈린 척도 의존성 장면(`conversation-probit-logit-prob.json` msg[3–13], 다른 발췌)과 연결된다. 발표 전 짚을 점: 이 근거를 그대로 옹호하지 않는다(`memory/talk-scenes-from-repo.md` 27행)
