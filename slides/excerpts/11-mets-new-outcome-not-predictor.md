# 11/13. "METS_new는 결과변수지 예측변수가 아니다": 대비의 대비를 손으로 짜다 공분산을 빠뜨리다

출처: `G:/Projects/airforce-fatty-liver/conversation-export.json` msg[32–33] (파일은 `agent-conversation/` 밖 레포 루트에 있음)
날짜: 2026-03-12
에이전트: Positron Assistant (Claude Sonnet 4.6)

## 인용

> (사용자) 현재 작업공간 contrast(emm1, "revpairwise", by = c("GROUP2", "C_ABOBESE"))의 결과에서 각 집단의 contrast 간 차이 검정

> (에이전트) … 이는 **interaction contrast** (contrast-of-contrasts) 분석입니다.

> (도구 결과) GROUP2 = KHANES, C_ABOBESE = No:
>  contrast      estimate    SE   df t.ratio p.value
>  MeTS - Normal   0.3203 0.168 3681   1.909  0.0564
> GROUP2 = Pilot HE, C_ABOBESE = No:
>  MeTS - Normal   0.6360 0.125 3681   5.074 <0.0001
> GROUP2 = KHANES, C_ABOBESE = Yes:
>  MeTS - Normal   0.0389 0.127 3681   0.305  0.7601
> GROUP2 = Pilot HE, C_ABOBESE = Yes:
>  MeTS - Normal   0.1200 0.139 3681   0.862  0.3890
> Results are averaged over the levels of: SMOKING, ALCOHOL, EXERCISE, HYPERTENSION, DYSLIP, DIABETES

시도 1 `contrast(cont1, interaction = c("consec","consec"), by = NULL)` → `nonEst NA`.
시도 2 `contrast(cont1, list(... = c(-1, 1, 0, 0)))`:

> (도구 결과) Error in `contrast.emmGrid()`: ! Nonconforming number of contrast coefficients

시도 3 `contrast(emm1, interaction = list(METS_new = "revpairwise", GROUP2 = "revpairwise"), by = "C_ABOBESE")`:

> (도구 결과) C_ABOBESE = No:  MeTS - Normal  Pilot HE - KHANES  0.3157 0.208 3681  1.516  0.1296
> C_ABOBESE = Yes: MeTS - Normal  Pilot HE - KHANES  0.0811 0.187 3681  0.434  0.6643

시도 4, 3원 상호작용을 두 추정치의 차이로 직접 계산:

```r
est_diff <- cont_df$estimate[1] - cont_df$estimate[2]
se_diff  <- sqrt(cont_df$SE[1]^2 + cont_df$SE[2]^2)
t_stat   <- est_diff / se_diff
p_val    <- 2 * pt(-abs(t_stat), df = df_val)
```

> (도구 결과) Estimate (No - Yes): 0.2346
> SE: 0.2798
> t-statistic: 0.838
> p-value: 0.4019

시도 5 `interaction = list(METS_new, GROUP2, C_ABOBESE 모두 "revpairwise")` → 3원 대비가 나오지 않음. 이어서 모형을 확인:

> (도구 결과) Original model formula:
> METS_new ~ GROUP2 * C_ABOBESE * URATE + AGE + SMOKING + ALCOHOL + EXERCISE
> …
> Interaction terms: "GROUP2Pilot HE:C_ABOBESEYes" "GROUP2Pilot HE:URATE" "C_ABOBESEYes:URATE" "GROUP2Pilot HE:C_ABOBESEYes:URATE"

```r
# The model has GROUP2 × C_ABOBESE × URATE, not METS_new
# METS_new is the outcome (binary), not a predictor
# So we're testing if URATE's effect on MeTS differs by GROUP2 and C_ABOBESE
```

> (에이전트) 완료되었습니다!
> …
> **Level 3 (3-way interaction):** ★
> - **Estimate**: 0.235 (SE=0.280)
> - **t-statistic**: 0.838
> - **p-value**: **0.402 (비유의)**
>
> 복부비만 여부(C_ABOBESE)에 따라 두 집단(Pilot HE vs KHANES) 간 URATE-MeTS 연관성 차이가 **유의하게 달라지지 않습니다** (p=0.40).

## 슬라이드에서 쓸 핵심

- 한 줄 메시지: `emm1`(t-ratio와 df=3681로 보아 METS_new를 예측변수로 둔 선형모형의 emmeans로 추정. 로그에 모형식은 없음)과 `m5`(MeTS를 결과로 둔 로지스틱)는 다른 모형인데 에이전트는 둘을 오가며 "URATE-MeTS 연관성"으로 결론을 지었고, 3원 상호작용은 두 추정치의 공분산을 무시한 SE(`sqrt(SE1² + SE2²)`)로 손계산했다. 결과 p = 0.40은 그럴듯하지만 산출 경로가 틀렸다.
- 보여줄 부분(코드/출력/문장): 손계산 4줄과 주석 "METS_new is the outcome (binary), not a predictor", 그리고 "완료되었습니다!" 결론.
- 연구자가 확인한 것: 확인한 흔적이 로그에 없다(대화가 여기서 끝남). 이 장면은 11번(역할 분리: 쓰는 에이전트와 검토하는 에이전트를 분리하는 이유)과 13번(한계: 완료 선언과 올바름은 다르다)에 쓴다. 발표에서는 "이 결과가 원고에 들어갔는가"를 레포 qmd에서 확인한 뒤 말할 것(요산 × 복부비만 층화는 `reviewer2-response-plan.md`의 허리둘레 보정 논의와 연결 가능).
- 주의: 이 수치들은 출판 원고에 없는 탐색 결과다. 슬라이드에는 수치보다 코드 패턴만 올린다.
