# 8. 약물 불균형(이상지질혈증 약 0.7% vs 13.6%)이 보고서 qmd에 표로 남은 모습

(대화 로그 장면은 `08-medication-imbalance.md`. 이 파일은 같은 발견이 Quarto 보고서의 코드 청크·footnote·Limitations에 어떻게 기록됐는지를 뽑은 것)

출처: `G:/Projects/airforce-fatty-liver/quarto/agent_bot/2026-03-10/02-afhe-khanes-analysis-report.qmd` 428–455행(`tbl-dyslip` 청크), 698–705행(요약표 Result 열), 737행(Limitations 목록)
날짜: 2026-03-10
에이전트: DataBot(레포 CLAUDE.md 명칭; 모델 미기재). 대화 로그상 같은 날 에이전트는 Positron Assistant (Claude Sonnet 4.6)
수치 주의: 이 보고서는 분석 중간 단계. 원고 최종값은 아래 병기

## 인용

### `tbl-dyslip` 청크 (428–455행). 표 값이 도출되는 과정이 청크에 남아 있다(CLAUDE.md 행동 규칙 7)

```r
afhe_khanes_final |>
  group_by(GROUP, DYSLIP) |>
  summarise(n=n(),
            CHOL=sprintf("%.1f \u00b1 %.1f",mean(CHOL,na.rm=T),sd(CHOL,na.rm=T)),
            LDL =sprintf("%.1f \u00b1 %.1f",mean(LDL, na.rm=T),sd(LDL, na.rm=T)),
            .groups="drop") |>
  group_by(GROUP) |>
  mutate(N=sum(n), Pct=sprintf("%.1f%%",n/N*100)) |>
  …
  lancet_gt(
    title    = "Table 4. Dyslipidemia Medication Prevalence and Lipid Levels by Group",
    subtitle = "Explaining attenuation of CHOL and LDL significance after medication adjustment (Model 3)",
    footnote = paste0(
      "KHANES medication users (n = 149, 13.6%) show markedly lower CHOL and LDL. ",
      "Pilot HE has only 18 users (0.7%). This ~20-fold imbalance explains why ",
      "CHOL/LDL group differences disappear after medication adjustment."
    )
  )
```

### 요약표 Result 열 (698–705행)

> "Pilot HE lower (11.1% vs 37.1%; adjusted OR = 0.37, p < 0.001)",
> "Higher in Pilot HE only (47.7% vs 38.8%; adjusted OR = 2.16, p < 0.001)",
> …
> "Explained by KHANES dyslipidemia medication imbalance (13.6% vs 0.7% in Pilot HE)",

### Limitations 목록 (737행)

> 3. **Medication imbalance**: KHANES has substantially higher antihypertensive (15.7%), lipid-lowering (13.6%), and antidiabetic (9.6%) medication use versus Pilot HE (<3% for all).

원고 최종값(이 프로젝트 CLAUDE.md 31행, 논문 2 Abstract): MetS 11.1% vs 37.1%, aOR 0.30(중간값 0.37); 혈압 구성요소 aOR 2.12(중간값 2.16). 유병률은 동일, OR은 보정 모형이 달라 중간값과 다르다. 최종 원고에서 CHOL·LDL은 완전 보정 후에도 유의(Δβ 0.20 p=0.049, Δβ 0.24 p=0.022)로 남았으므로 "유의성 소실"은 이 중간 보고서(Model 3 기준) 시점의 해석이다. 약물 비율 자체는 2026-08-16 `verify-numbers.R` (1)절이 재계산했다(`09-verify-numbers-script.md` 참조).

## 슬라이드에서 쓸 핵심
- 한 줄 메시지: 대화에서 찾은 원인이 보고서에서는 표를 만든 청크와 footnote로 남는다. 결론 문장이 아니라 도출 과정이 기록이다
- 보여줄 부분(코드/출력/문장): footnote 3문장과 `group_by → summarise → lancet_gt` 청크
- 연구자가 확인한 것: 18명·149명이라는 셀 크기와 "20배"라는 표현이 과장인지, 그리고 최종 모형에서 CHOL/LDL 결론이 바뀐 점(중간 해석을 그대로 원고에 옮기지 않았다)
