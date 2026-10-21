# 8. 허리둘레 보정 시 전 연령군 OR 비유의: 구성요소로 보정하는 것의 순환성

출처:
- `G:/Projects/airforce-fatty-liver/quarto/agent_bot/2026-03-10/02-afhe-khanes-analysis-report.qmd` 563–572행(Table 6 footnote), 641행, 673행, 703행
- `G:/Projects/airforce-fatty-liver/output/agent_bot/2026-08-14/reviewer2-response-plan.md` 406–414행((b) 방어 논거 표), 421행(순환성 메모)
날짜: 2026-03-10(보고서), 2026-08-14(리뷰어 대응안)
에이전트: DataBot(레포 CLAUDE.md 명칭; 모델 미기재)

## 인용

### 2026-03-10 보고서 Table 6 footnote (563–572행)

```r
  lancet_gt(
    title    = "Table 6. Age-stratified MeTS OR: Testing the Healthy Worker Effect",
    subtitle = "Reference = KHANES; sequential adjustment models",
    footnote = paste0(
      "pp = percentage point gap. +WAISTCIR (highlighted orange): +Lifestyle + waist circumference. ",
      "+All Anthro/BP: +Lifestyle + HEIGHT, WEIGHT, BMI, WAISTCIR, SYSBP, DIABP. ",
      "Key finding: WAISTCIR alone eliminates OR in all age strata. ",
      "ns = not significant; ** p<0.01; *** p<0.001."
    )
  )
```

> subtitle="Red-bordered row = WAISTCIR: OR approaches 1.0 in all age strata" (641행)
> subtitle="KHANES consistently exceeds Pilot HE by ~5-7 cm across all age strata" (673행)
> "Waist circumference: KHANES exceeds Pilot HE by 5-7 cm; WAISTCIR alone eliminates OR in all age strata" (703행)

### 2026-08-14 리뷰어 대응안, 층화 변수 선택 논거 (406–414행, 발췌)

> **핵심**: 두 층화 방식 모두 **해당 변수 유형에 대한 문헌 관례**를 따른 것. 서로 다른 논리가 아니라 *같은 논리를 각 변수 유형에 적용*한 결과임. 응답서는 이것만 말하면 되고, 그 이상은 사족.
> …
> | ③ (구현 속성) **pooled** 사분위 | 코드상 `quantile(.)`이 병합 데이터에 `group_by` 없이 적용됨 → 절단값이 집단 공통. 따라서 층 내 OR은 **동일 절대 수준의 남성끼리** 비교한 값. 집단별 사분위였다면 이 해석이 불가능. 각 층 \~25%로 희박 셀 없음 | `manuscript-minor-revision.qmd:1189-1201` |

### 같은 파일, 순환성 메모 (421행, "폐기된 논거" 2번)

> 2.  **"진단 절단값을 층화 기준으로 쓰면 순환성이 최대가 된다"**. 논리적으로는 성립하나 리뷰어가 묻지 않은 쟁점이며, 층화변수 자체가 MetS 구성요소라 **부분적 순환성은 어떤 절단값을 써도 남음**. 먼저 꺼내면 오히려 이 지점을 파고들 빌미가 됨. 리뷰어가 후속으로 제기할 경우에만 대응.

## 슬라이드에서 쓸 핵심
- 한 줄 메시지: 허리둘레를 보정하면 집단 차이가 사라진다. 그런데 허리둘레는 MetS 정의의 일부다. 무엇을 보정할지는 통계가 아니라 인과 구조의 문제다
- 보여줄 부분(코드/출력/문장): "WAISTCIR alone eliminates OR in all age strata"와 "부분적 순환성은 어떤 절단값을 써도 남음" 두 문장
- 연구자가 확인한 것: 최종 원고의 주 모형은 연령·생활습관(+BMI·약물)만 보정하고 MetS 구성요소는 보정 변수가 아니라 층화 변수로만 썼다(논문 2 Statistical analysis). 순환성 논점은 리뷰어가 묻지 않았으므로 응답서에 선제적으로 넣지 않기로 했다
