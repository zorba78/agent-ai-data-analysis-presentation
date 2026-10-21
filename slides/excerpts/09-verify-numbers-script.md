# 9. verify-numbers.R: 원고에 들어갈 수치를 같은 데이터에서 다시 계산한다

출처:
- `G:/Projects/airforce-fatty-liver/code/agent_bot/2026-08-16/verify-numbers.R` 1–14행(헤더), 22–36행((1) 약물·유병 비율), 68–87행((3) SI 변환 후 계수)
- `G:/Projects/airforce-fatty-liver/output/agent_bot/2026-08-14/reviewer2-response-plan.md` §D 558–561행
- 실행 결과 기록: `memory/agent_bot/2026-08-16/session-summary.md` §5 39행
날짜: 2026-08-14(§D), 2026-08-16(스크립트)
에이전트: DataBot(레포 CLAUDE.md 명칭; 모델 미기재)

## 인용

### 스크립트 헤더 (1–14행)

```r
# =============================================================================
# Date    : 2026-08-16
# File    : verify-numbers.R
# Purpose : Verify every number that the response letter promises to insert into
#           the manuscript, before it is written into
#           quarto/agent_bot/2026-08-16/manuscript-minor-revision-r2.qmd.
#           Nothing here changes any analysis; it recomputes from the same
#           analysis dataset the manuscript already uses.
#             (1) medication use and prevalent-condition prevalences (comment 2.7)
#             (2) the full BMI distribution, Korean and WHO criteria (comment 2.9)
#             (3) Table 4 regression coefficients after SI conversion of the two
#                 outcomes, urate and fasting glucose (comment 2.8)
# Usage   : Rscript code/agent_bot/2026-08-16/verify-numbers.R
# =============================================================================
```

### 대표 검사 (1): 약물 복용·유병 비율 (22–36행)

```r
d <- read_rds("data/derived-data/afhe-khanes2022-analysis-dataset.rds")
cat("N =", nrow(d), " by GROUP:\n"); print(table(d$GROUP))

pct <- function(v) {
  tb <- table(d$GROUP, v)
  yes <- tb[, "Yes"]
  sprintf("%s %.1f%% (n=%d)", rownames(tb), 100 * yes / rowSums(tb), yes)
}
for (v in c("HYPERTENSION", "DYSLIP", "DIABETES",
            "C_HYPERTENSION", "C_DIABETES", "C_DYSLIPIDEMIA", "C_OBESE")) {
  if (!v %in% names(d)) { cat(v, ": ABSENT\n"); next }
  cat(sprintf("%-16s : %s\n", v, paste(pct(d[[v]]), collapse = " | ")))
}
```

### 대표 검사 (3): SI 변환 후 Table 4 계수 (68–87행, 발췌)

```r
# The two outcomes are rescaled: urate mg/dL -> umol/L (x 59.48), glucose
# mg/dL -> mmol/L (/ 18.02). The predictors are untouched, so every coefficient
# and confidence bound is multiplied by the same factor and every p value is
# unchanged. Printed here so the Results prose can quote the converted values.
fm <- "%s ~ GROUP2 * (AGE_z + BMI_z + SMOKING + ALCOHOL + EXERCISE + medication)"
for (out in c("URATE", "GLUC")) {
  fac <- if (out == "URATE") 59.48 else 1 / 18.02
  m <- lm(as.formula(sprintf(fm, out)), data = reg_dat)
  tt <- broom::tidy(m) %>%
    filter(str_detect(term, "AGE_z|SMOKINGYes|medicationYes")) %>%
    transmute(term, conventional = round(estimate, 3), SI = round(estimate * fac, 3),
              p = format.pval(p.value, digits = 3, eps = 1e-16))
  …
}
```

### SI 변환 불변 규칙 (reviewer2-response-plan.md §D)

> 2.  **SI 전환 검증 기준**: 전환 후 Table 2·3·4의 OR·Δβ·95% CI·p가 기존 값과 **완전히 동일**해야 함. 달라지면 변환 오류이므로 반드시 확인.

같은 §D 1번: "**최종 표·그림은 반드시 R에서 재생성할 것.** §A의 수치는 Python으로 산출한 검증·설계용 값이며(`code/agent_bot/2026-08-14/reviewer2-bmi-category-pooled-sd.py`), 원고 표는 기존 `gt`/`flextable` 파이프라인으로 만들어야 서식이 유지됨."

### 실행 결과 (2026-08-16 session-summary §5)

> - `verify-numbers.R` 재실행: 약물/유병률 12개, BMI 6단계, Table 4 SI 계수 전부 일치. BMI 카이제곱은 비보정 기준(p = 0.096, χ² = 69.4) → Table 1(gtsummary)과 동일

## 슬라이드에서 쓸 핵심
- 한 줄 메시지: 답변서가 약속한 숫자는 원고에 쓰기 전에 스크립트로 다시 계산한다. 검증 기준은 "단위를 바꿔도 OR·p는 그대로"처럼 미리 정한다
- 보여줄 부분(코드/출력/문장): 헤더의 "Nothing here changes any analysis; it recomputes from the same analysis dataset" 두 줄, (3)절의 주석 4줄, §D 2번 규칙
- 연구자가 확인한 것: 검증 수치가 Python(설계용)과 R(원고용) 두 경로에서 같은지. 변환 계수 59.48과 1/18.02가 맞는지. 이 스크립트 출력이 이 발표의 수치 대조 기준이다(이 프로젝트 CLAUDE.md 행동 규칙 2)
