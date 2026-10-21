# 9. 손 계산으로 emmeans를 재현하다: regrid("logit")의 OR과 "OR의 OR"

출처: `G:/Projects/airforce-fatty-liver/agent-conversation/conversation-probit-logit-prob.json` msg[10–13]
날짜: 2026-03-17
에이전트: Positron Assistant (Claude Sonnet 4.6)

## 인용

> (사용자) regrid(em1, "logit")인 경우 odds ratio가 계산되는데 어떤 과정을 통해 계산되는지 위와 같이 상세히 설명.

> (에이전트) 수동 계산으로 단계별로 확인하겠습니다.

```r
em1_raw <- summary(emmeans(m1, ~ GROUP2 * AGE_GROUP))  # type="link" default
```

> (도구 결과) GROUP2   AGE_GROUP  emmean     SE  df asymp.LCL asymp.UCL
>  KHANES   ≤ 29      -1.0545 0.1290 Inf    -1.306   -0.8025
>  Pilot HE ≤ 29      -1.6494 0.0834 Inf    -1.813   -1.4859
>  … Results are given on the probit (not the response) scale.

```r
prob      <- pnorm(lp_probit)          # probit LP → probability
logit_val <- log(prob / (1 - prob))    # probability → logit
log_OR    <- logit_Pilot - logit_KHANES
OR        <- exp(log_OR)
```

> (에이전트) 수동 계산값이 emmeans 결과와 정확히 일치합니다. …
>
> | AGE | logit(Pilot) | logit(KHANES) | log(OR) | **OR** | emmeans OR |
> | ≤ 29 | −2.9543 | −1.7677 | −1.1866 | **0.305** | 0.305 ✓ |
> | 30–39 | −2.2896 | −0.8996 | −1.3900 | **0.249** | 0.249 ✓ |
> | 40–49 | −1.6373 | −0.4424 | −1.1949 | **0.303** | 0.303 ✓ |
> | ≥ 50 | −1.1820 | −0.0493 | −1.1327 | **0.322** | 0.322 ✓ |
>
> > `regrid(em1, "logit")`은 모델의 **고유 링크(probit)**를 무시하고, 예측 확률 $\hat{p}$을 **logit으로 재변환**한 새로운 선형 공간을 만드는 것입니다.
>
> 따라서 이 OR은 **probit 모델에서 도출된 근사 OR**이며, logit 모델의 OR과 개념은 같지만 **모델 계수와 직접 대응하지 않습니다.** 모델 계수로부터 OR을 직접 구하려면 처음부터 `family = binomial(link = "logit")`으로 적합해야 합니다.

> (사용자) 내가 궁금한건  contrast(regrid(em1, "logit"), interaction = c("pairwise", "trt.vs.ctrl"),type = "response")에서 도출한 odds ratio 결과야.

> (도구 결과) GROUP2_pairwise   AGE_GROUP_trt.vs.ctrl odds.ratio    SE  df null z.ratio p.value
>  KHANES / Pilot HE (30-39) / ≤ 29             1.226 0.422 Inf    1   0.592  0.5539
>  KHANES / Pilot HE (40-49) / ≤ 29             1.008 0.347 Inf    1   0.024  0.9810
>  KHANES / Pilot HE ≥ 50 / ≤ 29                0.948 0.325 Inf    1  -0.157  0.8751

> (도구 결과) (30-39) - (≤29): 1.3900 - 1.1866 = 0.2034  (= log OR ratio)
> …
> (30-39)/(≤29): exp(0.2034) = 1.2256  | emmeans: 1.226
> (40-49)/(≤29): exp(0.0083) = 1.0083  | emmeans: 1.008
> (≥50)  /(≤29): exp(-0.0539) = 0.9475  | emmeans: 0.948

> (에이전트) $$\underbrace{\eta_{\text{probit}}}_{\text{em1 내부}} \xrightarrow{\Phi(\cdot)} \hat{p} \xrightarrow{\log\frac{\hat{p}}{1-\hat{p}}} \underbrace{\eta_{\text{logit}}}_{\text{regrid("logit")}} \xrightarrow{\Delta_{\text{GROUP}}} \log(\text{OR}) \xrightarrow{\Delta_{\text{AGE}}} \log(\text{OR ratio}) \xrightarrow{\exp(\cdot)} \underbrace{\text{OR ratio}}_{\text{type="response"}}$$
> …
> > `type="response"`의 결과값은 **"OR의 OR"**, 즉 **Odds Ratio Ratio** 입니다.
> > 모든 연령대에서 OR ratio ≈ 1이고 **p > 0.5** → 연령대가 바뀌어도 KHANES/Pilot 간의 OR 차이는 **통계적으로 유의하지 않음** (상호작용 없음).

(이 흐름은 이후 `05_statistical_analysis_methods.qmd`의 RQ2 Statistical Analysis 절 "Probit binomial GLM … regrid("logit") → revpairwise 로 OR 산출; OR ratio = exp(δ_j) 정의"로 들어갔다. finalize msg[31] 요약.)

## 슬라이드에서 쓸 핵심

- 한 줄 메시지: 패키지 출력(emmeans)을 믿지 않고 `pnorm`/`log`/`exp` 네 줄로 재현하게 했다. 에이전트가 검산한 것이고, 검산을 시킨 것은 연구자다.
- 보여줄 부분(코드/출력/문장): 변환 사슬 수식 한 줄(probit → p → logit → ΔGROUP → ΔAGE → exp), 재현 표의 "emmeans OR ✓" 열, 그리고 "probit 모델에서 도출된 근사 OR … 모델 계수와 직접 대응하지 않습니다" 문장.
- 연구자가 확인한 것: 원고 Methods에 적을 정의(OR ratio = exp(δ_j))가 코드에서 실제 계산되는 양과 같은지. 검증 보고서 녹화(9번)의 대본으로 쓸 수 있다.
