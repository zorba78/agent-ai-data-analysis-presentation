# 9/13. Δβ 부호 오독: β = Pilot − KHANES인데 "KHANES가 더 크다"로 읽음

출처: `G:/Projects/airforce-fatty-liver/agent-conversation/conversation-add-analysis.json` msg[8–9]; 대조는 msg[20](사용자 표), `conversation-finalize.json` msg[27](qmd 산문)
날짜: 2026-03-10 (오독), 2026-03-21 (바른 산문)
에이전트: Positron Assistant (Claude Sonnet 4.6)

## 인용

> (사용자) GLUC와 URATE에 대해 그룹별 대사증후군 연관성을 시각화하는 상호작용 그래프 그리기. 제목, 부제목, 캡션 등 텍스트는 모두 영어로 작성

도구 호출(executeCode): ggplot2 + patchwork. 그림 부제에 에이전트가 직접 쓴 정의:

```r
subtitle = paste0(
  "Mean ± 95% CI of GLUC and URATE by MeTS status, stratified by group (Pilot HE vs. KHANES 2022).\n",
  "Interaction β: difference in log-OR slope between Pilot HE and KHANES per 1 SD increase (from logistic regression)."
),
```

> (에이전트) 그래프가 생성되었습니다. 주요 해석을 정리합니다.
>
> ### Fasting Glucose (GLUC) — 좌측 패널
> - **두 그룹 모두 MeTS군에서 혈당이 상승**하지만, **KHANES(주황)의 기울기가 훨씬 가파름**
>   - KHANES: Non-MeTS ~96 → MeTS ~115 mg/dL (+19)
>   - Pilot HE: Non-MeTS ~95 → MeTS ~104 mg/dL (+9)
> - 상호작용 $\beta$ = 1.010 (95% CI: 0.695–1.325, p<0.001): **KHANES에서 GLUC 1 SD 증가 시 대사증후군 위험 증가폭이 Pilot HE보다 유의하게 큼**
> …
> ### Uric Acid (URATE) — 우측 패널
> …
> - 두 그룹 모두 MeTS군에서 요산이 상승하나, **Pilot HE의 기울기가 더 가파름**
> - 상호작용 $\beta$ = 0.305 (95% CI: 0.133–0.477, p<0.001): …

왜 오독인가: 스크립트 정의(add-analysis msg[21] 도구 주석)는 "차이 β : Pilot 기울기(log-OR) - KHANES 기울기(log-OR)". β = +1.010이면 조종사의 GLUC 1-SD 기울기가 더 크다. 그래프의 평균 혈당 차이(+19 vs +9, 원 척도 평균)와 로지스틱 기울기 OR(표준화 1-SD당)은 다른 양인데, 에이전트는 그림의 인상으로 β 부호를 읽었다. 같은 메시지 안에서 URATE는 "Pilot HE의 기울기가 더 가파름"이라 해 부호 해석이 일관되지도 않다.

채팅에서는 아무도 지적하지 않았다. 열흘 뒤 사용자가 붙여 넣은 표(msg[20], 조정3 모델)와 에이전트의 qmd 산문은 맞는 방향이다:

> (사용자, msg[20]) GLUC      2.330 (1.839, 2.953)            5.764 (4.245, 7.827)            0.906 (0.527, 1.285)            4.687 (<0.001) ***

> (에이전트, finalize msg[27] qmd 본문) **Fasting glucose (GLUC)** showed the largest and most robust group difference across all adjustment stages. In the unadjusted model, $\Delta\beta$ = 1.01 (95% CI: 0.69--1.33, *p* < 0.001); this remained essentially unchanged after full adjustment ($\Delta\beta$ = 0.98, 95% CI: 0.64--1.32, *p* < 0.001) … Within groups, the per-SD OR for glucose was substantially higher in Pilot HE (OR = 5.80, 95% CI: 4.35--7.74) than in KHANES (OR = 2.17, 95% CI: 1.79--2.64) after full adjustment.

중간값 표기: msg[9]의 β 1.010/0.305는 비보정 모형, msg[20]의 5.764/2.330은 3월 10일 시점 조정3 모형. 원고 최종값: 완전 보정 후 GLUC OR 5.80 vs 2.17, Δβ 0.98 (finalize msg[27]); 요산 Δβ 0.27 (p = 0.009) (CLAUDE.md).

## 슬라이드에서 쓸 핵심

- 한 줄 메시지: 에이전트가 그림 캡션에 β의 정의를 정확히 적어 놓고도, 바로 아래 해석에서 부호를 반대로 읽었다. 최종 원고는 맞았지만 그건 나중 단계의 재계산 덕이지 채팅에서 잡힌 게 아니다.
- 보여줄 부분(코드/출력/문장): 캡션 정의 한 줄("difference in log-OR slope between Pilot HE and KHANES") 옆에 해석 한 줄("KHANES에서 … 증가폭이 Pilot HE보다 유의하게 큼")을 나란히.
- 연구자가 확인한 것: 대비 방향(Pilot − KHANES)을 코드에서 읽어야 한다. 9번 섹션의 `verify-numbers.R`처럼 수치를 RDS에서 재계산하는 단계가 왜 필요한지의 근거. 13번 한계: "일관되게 틀리지 않는다. 같은 메시지 안에서도 방향이 바뀐다".
