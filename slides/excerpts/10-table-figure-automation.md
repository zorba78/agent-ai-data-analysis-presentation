# 10. 표·그림 자동화: gtsummary → flextable Lancet 양식, emmeans + patchwork, DiagrammeR CONSORT, 600 dpi 내보내기

출처:
- `G:/Projects/airforce-fatty-liver/quarto/agent_bot/2026-08-16/manuscript-minor-revision-r2.qmd` 493–527행(Table 1 gtsummary), 579–599행(as_flex_table Lancet 양식), 1264–1273행(CONSORT), 1486–1494행(emmeans), 1815–1830행(patchwork)
- `G:/Projects/airforce-fatty-liver/code/funs/helpers.R` 9–17행(`lancet_ft()`), 93행(`lancet_gt()`)
- 그림 스크립트: `code/agent_bot/2026-08-15/figure2-stratified-3col.R`, `code/agent_bot/2026-08-16/export-submission-figures.R`
날짜: 2026-08-15, 2026-08-16
에이전트: DataBot(레포 CLAUDE.md 명칭; 모델 미기재). `helpers.R`는 사용자 작성 함수(`code/funs/`, agent_bot 폴더 아님)

## 인용

### Table 1: gtsummary → flextable Lancet 양식 (r2 qmd 507–527행, 579–599행; 20줄로 압축)

```r
  tbl_summary(
    by = GROUP,
    statistic = list(
      all_continuous() ~ "{mean} ({sd})",
      all_categorical() ~ "{n} ({p}%)"
    ),
    # Magnitude-aware decimal placement matching the tbl-reg-urate-gluc rule
    # (|x| >= 10 -> 1 dp; |x| < 10 -> 2 dp). …
    digits = list(
      all_continuous() ~ 1,
      c(WBC, RBC, GLUC, CHOL, TRIG, HDL, LDL) ~ 2,
      c(HGB, URATE) ~ 0
    )
  ) %>%
  …
demo_lancet_ft <- demo_tbl %>%
  as_flex_table() %>%
  # 2a. Lancet border skeleton
  border_remove() %>%
  hline_top(border = fp_border(width = 2), part = "all") %>%
  hline_bottom(border = fp_border(width = 1), part = "header") %>%
  hline_bottom(border = fp_border(width = 2), part = "body") %>%
  # 2b. Typography
  flextable::font(fontname = "Arial", part = "all") %>%
  fontsize(size = 9, part = "body") %>%
```

### 사용자 헬퍼 함수 시그니처 (`code/funs/helpers.R`)

```r
lancet_ft <- function(
  df,
  caption = NULL,
  footnote = NULL,
  bold_rows = NULL, # integer vector of row indices to bold
  fill_rows = NULL, # named list: list(rows=c(1,2), color="#FFF3E0")
  span_cols = NULL, # named list: list(cols=c(4,5,6,7), label="Spanner")
  center_cols = NULL
) {
…
lancet_gt <- function(gt_tbl, title = NULL, subtitle = NULL, footnote = NULL) {
```

### Figure 2: emmeans 추정 → patchwork 조립 (r2 qmd 1491행, 1815–1830행)

```r
            emmeans(mod, as.formula(em_fmla), type = "response")
…
library(patchwork)
make_panel <- function(i) {
  prev$plt_prev[[i]] /
    prev_odds_test$plt_ortest[[i]] +
    plot_layout(heights = c(1.8, 1))
}
## The seven duplicate legends are collected into one shared legend at the foot
## of the figure (reviewer 2, comment 12). Layout is unchanged: 4 columns x
## 2 rows, the eighth cell empty.
(
  (make_panel(1) | make_panel(2) | make_panel(3) | make_panel(4)) /
  (make_panel(5) | make_panel(6) | make_panel(7) | patchwork::plot_spacer())
) +
  plot_layout(heights = c(1, 1), guides = "collect") +
```

### Figure 1: CONSORT (r2 qmd 1264–1273행)

```r
#| dpi: 300
# Date: 2026-03-15
# This diagram shows:
# 1) Initial sample sizes for AFHE and KNHANES
# 2) Stepwise exclusions with explicit counts
# 3) Final analytic sample sizes for each source
# 4) Final combined dataset size after merging
DiagrammeR::grViz("
digraph consort_diagram {
```

### 제출용 내보내기 스크립트 헤더 (`export-submission-figures.R` 1–7행, 22–25행, 48행)

```r
# Date    : 2026-08-16
# File    : export-submission-figures.R
# Purpose : Produce Figure 1 and Figure 2 as stand-alone high-resolution files
#           for separate upload to BMJ Military Health, in PNG, TIFF and SVG.
#           The figures are identical in content to those in
#           quarto/agent_bot/2026-08-16/manuscript-minor-revision-r2.qmd; only
#           the output device and resolution differ.
…
#           Resolutions: 600 dpi for PNG, 300 dpi for TIFF. …
PNG_DPI  <- 600
```

`figure2-stratified-3col.R` 헤더(2026-08-15): "Redraw Figure 2 in response to Reviewer 2, item 14. The underlying models, estimates and contrasts are untouched; only the display changes."

## 슬라이드에서 쓸 핵심
- 한 줄 메시지: 표와 그림은 데이터에서 문서까지 코드 한 줄기로 이어진다. 리뷰어가 그림을 고치라 해도 모형은 건드리지 않는다
- 보여줄 부분(코드/출력/문장): `tbl_summary → as_flex_table → border/hline` 흐름 10줄, `make_panel` + patchwork 조립 6줄. 라이브 데모(Table 1)의 대본이 된다
- 연구자가 확인한 것: Lancet 양식(상단 2pt, 헤더 아래 1pt, 하단 2pt 선, Arial 9/10pt)은 사용자가 `helpers.R`에 먼저 정의했고 에이전트는 그 양식을 따랐다. 소수점 자리수 규칙(|x| ≥ 10 → 1자리)이 표와 산문에서 같은지
