# 5. 논문 1의 요산 발견이 논문 2의 연구 질문이 되다

출처:
- `references/military-2026-003444.full.pdf` Introduction(2쪽, "Serum urate is not a conventional MetS screening test…" 문단), Discussion(6쪽, "The urate finding is particularly notable given our prior work…" 문단). 텍스트는 pypdf로 추출
- `G:/Projects/airforce-fatty-liver/quarto/agent_bot/2026-08-16/manuscript-minor-revision-r2.qmd` 352행, 416행, 426행(`@songku2025` 인용 3곳)
- 두 논문 요약 수치: 이 프로젝트 `CLAUDE.md` 28–31행
날짜: 2026-08-16(원고 r2), 논문 2 출판 2026(epub)
에이전트: 해당 없음(출판 원고 인용). 원고 r2 qmd는 DataBot(레포 CLAUDE.md 명칭)이 저자 문체로 재작성한 것

## 인용

### 논문 2 Introduction, 요산을 쓴 이유 (출판본)

> Serum urate is not a conventional MetS screening test, so its inclusion warrants explanation. Hyperinsulinaemia reduces renal urate excretion, so urate rises with insulin resistance and visceral adiposity; a meta-analysis of prospective cohorts reported a pooled HR of 1.55 (95% CI 1.40 to 1.70) for incident MetS in the highest versus lowest urate category, with a dose-response of 1.05 per 1 mg/dL.13 This association is weaker in men than women,14 which is why urate is not screened for this purpose in most health systems. Aircrew differ in that urate is already in the standard aeromedical diagnostic panel at no added cost, and the ROKAF cohort mentioned above showed its strongest MetS signal in the highest quartiles of urate, white cell count and ALT.12

(이 문단은 Reviewer 2 항목 R2-3 "Urate 사용 근거 상술"에 답해 r2에서 추가된 것. `output/agent_bot/2026-08-14/reviewer2-response-plan.md` 131행)

### 논문 2 Discussion, 선행 MAFLD 논문 인용 (r2 qmd 416행)

> The urate finding is particularly notable given our prior work. Urate was not significantly associated with MetS in the general male population but was clearly associated in pilots (per-SD OR 1.35, 95% CI 1.17–1.55). … In our prior MAFLD analysis of Korean Air Force personnel, urate was an independent risk factor (OR 1.83, 95% CI 1.32–2.55) and a particularly strong predictor among pilots [@songku2025]. … This consistency across independent aviation cohorts supports [the inclusion of urate]{custom-style="ChangeMark"} in routine aeromedical monitoring [even in the absence of]{custom-style="ChangeMark"} classical MetS criteria.

### 논문 2 Introduction 끝, 연구 틀 문장 (r2 qmd 352행)

> We anchor our findings within the framework of the healthy-worker effect (HWE) in aviation [@cairns2020; @houston2011; @koterov2025; @park2024; @pizzi2008] and link them to our prior work on metabolic dysfunction-associated fatty liver disease (MAFLD) [@songku2025].

### 논문 2 Conclusions (r2 qmd 426행)

> … consistent evidence linking urate to both MetS [@malpica2023; @rhee2015] and MAFLD [@songku2025] supports incorporating routine urate screening and structured hyperuricemia follow-up into Pilot Health Examinations.

### 두 논문의 핵심 수치 (이 프로젝트 CLAUDE.md 28–31행)

> 1. Song DH, Ku B. Prevalence and risk factors of metabolic-associated fatty liver disease in the Korean Air Force. Aerosp Med Hum Perform. 2025;96(9). doi:10.3357/AMHP.6646.2025
>    - 1,044명(조종사 667, 비조종사 377), 40세 이상, 2020–2022. MAFLD 27.7% vs 34.7%. 요산 OR 1.83, 조종사에서만 유의
> 2. Ku B, Song DH. Difference in the prevalence of metabolic syndrome components between male pilots of the Republic of Korea Air Force and the general Korean male population. BMJ Mil Health 2026, epub. doi:10.1136/military-2026-003444
>    - 조종사 2,604 vs KNHANES 1,093, 24–61세 남성. MetS 11.1% vs 37.1%, aOR 0.30. 혈압 구성요소는 조종사가 높음(aOR 2.12). 요산 Δβ 0.27 (p = 0.009)

출판본 Abstract 대조(pypdf 추출): "fasting glucose (Δβ 0.98, p<0.001), urate (Δβ 0.27, p=0.009), low-density lipoprotein cholesterol (LDL-C) (Δβ 0.24, p=0.022), and total cholesterol (Δβ 0.20, p=0.049)". 혈압 구성요소 "47.7% vs 38.8%; adjusted OR 2.12 (95% CI 1.80 to 2.52), p<0.001". 수치 일치.

## 슬라이드에서 쓸 핵심
- 한 줄 메시지: 연구 질문은 에이전트가 아니라 전 논문의 남은 의문(조종사에서만 유의했던 요산)에서 나왔다
- 보여줄 부분(코드/출력/문장): 논문 1 "요산 OR 1.83, 조종사에서만 유의" → 논문 2 "per-SD OR 1.35(조종사) vs 1.02(일반인), Δβ 0.27, p = 0.009". Introduction의 "Serum urate is not a conventional MetS screening test, so its inclusion warrants explanation" 한 문장
- 연구자가 확인한 것: 요산이 MetS 선별검사가 아닌데도 넣은 이유를 리뷰어가 물었고(R2-3), 저자가 항공의학 패널에 이미 포함돼 있다는 점과 선행 코호트 근거로 답했다
