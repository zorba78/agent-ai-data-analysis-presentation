# 8/9. probit → logit → 확률 척도: 상호작용 검정 결과가 척도에 따라 뒤집힌다

출처: `G:/Projects/airforce-fatty-liver/agent-conversation/conversation-probit-logit-prob.json` msg[2–9]
날짜: 2026-03-17
에이전트: Positron Assistant (Claude Sonnet 4.6)

## 인용

### 모형과 연령대별 OR (msg[2–3])

> (사용자) 현재 작업공간 em1 <- emmeans(m1, ~ GROUP2 * AGE_GROUP, type = "response") 에서 각 연령대 별 pilot 대비 KHANES odds ratio 계산

> (도구 결과) Call: glm(formula = as.formula(fm_string), family = binomial(link = "probit"), data = afhe_khanes_strat)
> …
> GROUP2Pilot HE                 -0.5949     0.1532  -3.882 0.000103 ***
> …
> GROUP2Pilot HE:AGE_GROUP30-39  -0.1779     0.1820  -0.977 0.328408
> GROUP2Pilot HE:AGE_GROUP40-49  -0.1116     0.1835  -0.608 0.542883
> GROUP2Pilot HE:AGE_GROUP≥ 50   -0.0977     0.1839  -0.531 0.595 …

> (에이전트) probit 스케일로 나오고 있네요. `regrid()`로 확률 스케일로 전환 후 OR을 계산하겠습니다.

첫 시도 `regrid(em1, transform = "log.odds")`:

> (도구 결과) Error in `match.arg()`: ! 'arg' should be one of "response", "mu", "unlink", "none", "pass", "logit", "probit", …

`regrid(em1, transform = "logit")` 후 `contrast(…, "revpairwise", by = "AGE_GROUP", type = "response")`:

> (에이전트) | 연령대 | OR (Pilot HE / KHANES) | 95% CI | z | p |
> | ≤ 29 | **0.305** | 0.170–0.547 | -3.99 | < 0.001 |
> | 30–39 | **0.249** | 0.178–0.349 | -8.07 | < 0.001 |
> | 40–49 | **0.303** | 0.216–0.424 | -6.95 | < 0.001 |
> | ≥ 50 | **0.322** | 0.231–0.449 | -6.68 | < 0.001 |

(원고 최종값: 연령층화 OR 0.25–0.32, finalize msg[27] 검증 목록 "Age strata OR 0.25-0.32"와 일치)

### 사용자의 손 계산 (msg[6])

> (사용자) emmeans()로 추정한 각 그룹별 연령에 따른 MeTS 추정 유병률은  GROUP2   AGE_GROUP   prob …
>  KHANES   ≤ 29      0.1458 …
>  Pilot HE ≤ 29      0.0495 …
>  KHANES   30-39     0.2892 …
>  Pilot HE 30-39     0.0920 …
> … 여기에서 GROUP2 차이, 예를 들어 30세 이하의 KHANES - Pilot = 0.1458 - 0.0495 = 0.0963, 30세 이상 40세 이하 KHANES - Pilot = 0.2892 - 0.0920 = 0.1972.  두 값의 차이는 1.009 정도인데 int_cntr의 (30-39) - (20-29)는 0.1779 임.

(사용자의 "1.009"는 0.1009의 오타. 에이전트는 이를 지적하지 않고 0.1009로 받아 계산했다.)

> (에이전트) 핵심을 정확히 짚으셨습니다. **스케일 차이** 때문입니다. …
> `em1`의 확률값은 **probit → 확률**로 back-transform된 값이고,
> `int_cntr`는 back-transform **이전**, 즉 **probit(선형 예측값) 스케일**에서 대비를 계산합니다.

```r
probit_vals <- qnorm(probs)
…
int_probit <- diff_3039 - diff_le29
```

> (도구 결과) ≤29:   KHANES probit(0.1458) - Pilot probit(0.0495) = 0.5951
> 30-39: KHANES probit(0.2892) - Pilot probit(0.0920) = 0.7728
> int_cntr (30-39) - (≤29) on PROBIT scale = 0.1777
> int_cntr reported value                  = 0.1779

> (에이전트) | | ≤ 29 GROUP 차이 | 30–39 GROUP 차이 | **이중 대비 (int_cntr)** |
> | **확률 스케일** | 0.1458 − 0.0495 = 0.0963 | 0.2892 − 0.0920 = 0.1972 | **0.1009** |
> | **Probit 스케일** | Φ⁻¹(0.1458) − Φ⁻¹(0.0495) = 0.5951 | Φ⁻¹(0.2892) − Φ⁻¹(0.0920) = 0.7728 | **0.1777 ≈ int_cntr** |

### 확률 척도에서 검정 (msg[8–9])

> (사용자) 확률 스케일에서 상호작용을 검정

```r
em1_prob <- regrid(em1, transform = "response")
int_cntr_prob <- contrast(em1_prob, interaction = c("pairwise", "trt.vs.ctrl"))
```

> (에이전트) | 연령대 | Probit scale estimate | p | Prob scale estimate | p |
> | (30-39) − ≤29 | 0.1779 | 0.328 | **0.101** | **0.019** |
> | (40-49) − ≤29 | 0.1116 | 0.543 | **0.132** | **0.003** |
> | (≥50) − ≤29 | 0.0977 | 0.595 | **0.157** | **0.001** |
>
> **probit 스케일**에서는 그룹 차이가 선형 예측값 기준으로 연령대 간 거의 일정 → 상호작용 **유의하지 않음**
> **확률 스케일**에서는 비선형 변환($\Phi$) 때문에 유병률이 높은 구간(고령)일수록 확률 차이가 자동으로 커짐 → 상호작용 **유의함**
> …
> 이는 통계학에서 잘 알려진 **"non-collapsibility"** 문제입니다.
> …
> > **권장**: probit 모델에서는 **probit 스케일(int_cntr)**이 상호작용 검정의 올바른 기준입니다.
> > 확률 스케일의 유의성(p < 0.05)은 **비선형 변환의 수학적 산물**로, 실제 그룹 간 효과 수정(effect modification)의 증거로 보기 어렵습니다.

## 슬라이드에서 쓸 핵심

- 한 줄 메시지: 같은 모형, 같은 추정치인데 상호작용의 p가 probit 척도에서 0.33–0.60, 확률 척도에서 0.001–0.019. 에이전트는 계산은 정확히 재현했지만 이름을 틀렸다. 이것은 non-collapsibility가 아니라 상호작용의 척도 의존성(scale dependence of interaction)이다.
- 보여줄 부분(코드/출력/문장): 사용자의 손 계산 한 줄(0.1972 − 0.0963 = 0.1009) vs `qnorm` 재현(0.7728 − 0.5951 = 0.1777 ≈ 0.1779), 그리고 척도별 p 비교표 3행.
- 연구자가 확인한 것: (1) emmeans의 `int_cntr`가 어느 척도에서 계산되는지, (2) 어느 척도가 연구 질문("효과 수정이 있는가" vs "유병률 차이가 커지는가")에 맞는지, (3) 용어. 발표에서 "non-collapsibility" 오용을 짚을 것(memory 파일 "발표 전 짚을 점"). probit 선택 근거가 "시각적 표현과 맞추기 위해"로 기록된 점(`05_statistical_analysis_methods.qmd` 111행)과 함께 8번 섹션에서 다룬다.
