# 7. mediation::mediate()의 환경 오류를 세 번 만에 고치다

출처: `G:/Projects/airforce-fatty-liver/agent-conversation/conversation-finalize.json` msg[9] (사용자 요청은 msg[8])
날짜: 2026-03-19
에이전트: Positron Assistant (Claude Sonnet 4.6)

## 인용

> (사용자) 현재 방향으로 진행한 다음 매개분석(BMI → URATE/GLUC → MeTS) 방향  분석 실시

(집단별 다중회귀와 flextable을 끝낸 뒤)

> (에이전트) <MEMO>I have made 6 tool calls this turn (soft limit: ~3). Proceeding to mediation analysis — this is the second major deliverable requested.</MEMO>

시도 1(executeCode), 함수 안에서 `as.formula(sprintf(...))`로 모형을 적합하고 `mediate()` 호출:

```r
run_mediation <- function(mediator, group_label, sims = 2000) {
  dat <- df_reg |> filter(GROUP2 == group_label) |>
    mutate(METS_bin = as.integer(METS_new == "MeTS"))
  fm_med <- as.formula(sprintf("%s ~ BMI_z + %s", mediator, covs))
  fit_med <- lm(fm_med, data = dat)
  …
  med_out <- mediate(fit_med, fit_out, treat = "BMI_z", mediator = mediator,
                     boot = TRUE, boot.ci.type = "perc", sims = sims)
```

> (도구 결과) mediation: Causal Mediation Analysis
> Version: 4.5.1
> Running mediation analyses (2000 bootstrap replicates each)...
>   [1/4] URATE | KHANES
> Running nonparametric bootstrap
> Error:
> ! object 'fm_med' not found

시도 2, 주석 `# Fix: mediation models must be fit on the SAME data object passed to mediate()`, `as.data.frame()` 추가:

> (도구 결과) Error:
> ! object 'fm_a' not found

시도 3, 주석 `# mediation::mediate() captures the model call env — must use explicit formula objects`:

```r
  fit_a <- eval(bquote(lm(.(as.formula(f_a_chr)), data = dat)))
  fit_b <- eval(bquote(glm(.(as.formula(f_b_chr)), data = dat,
                            family = binomial(link = "logit"))))
```

> (도구 결과) [1/4] URATE | KHANES … [4/4] GLUC | Pilot HE
> Running nonparametric bootstrap
> Done.

> (에이전트) <MEMO>I have made 9 tool calls this turn. Mediation models are complete — proceeding to extract results and build the table/plot, which is the final deliverable.</MEMO>

결과 요약(집계, 중간값):

> (도구 결과) === Mediation Summary ===
> Group    Mediator   ACME  ACME_lo ACME_hi ACME_p … PM
> KHANES   URATE    0.0024 -0.0046  0.0097  0.504 … 0.0116
> Pilot HE URATE    0.0086  0.004   0.0133  0     … 0.0538
> KHANES   GLUC     0.0161  0.0066  0.0282  0     … 0.0832
> Pilot HE GLUC     0.0192  0.0108  0.0279  0     … [생략]

주: 매개분석은 뒤에 사용자가 원고에서 제외했다(finalize msg[24] "RQ4에서 mediation analysis 결과는 추가하지 않을 예정"). 위 수치는 출판 원고에 없다.
제외 이유(사용자 확인 2026-10-20): 초기에 생각했던 분석 방향과 맞지 않는다고 판단. 매개분석 결과는 출판 논문에 없음. 시연 소재로 쓰지 않음.

## 슬라이드에서 쓸 핵심

- 한 줄 메시지: 첫 시도의 오류 진단("같은 데이터 객체")은 틀렸고 두 번째("mediate()가 모형 call의 환경을 캡처한다")가 맞았다. 에이전트는 에러 메시지를 읽고 가설을 바꿔 가며 고쳤다.
- 보여줄 부분(코드/출력/문장): 에러 메시지 2개(`object 'fm_med' not found`, `object 'fm_a' not found`)와 `eval(bquote(...))` 두 줄. 녹화 클립 1(코드·에러 수정) 후보.
- 연구자가 확인한 것: 결과를 쓸지 말지. 결국 매개분석은 원고에서 뺐다. "고쳤다"와 "쓴다"는 다른 결정이라는 점을 12번 섹션에 연결.
- 주의: 에이전트의 `<MEMO>` 자기 제한("soft limit ~3 tool calls")을 넘긴 것을 스스로 기록한 부분은 4번 섹션(규칙·메모리)과 연결 가능.
