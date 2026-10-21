# 7. 분석 데이터의 구조: 변수명·자료형·단위만

출처:
- `G:/Projects/airforce-fatty-liver/data/derived-data/afhe-khanes2022-analysis-codebook.rds` (53행 × 3열: `variable_cat`, `variable`, `variable_label`). 메타데이터만 읽음
- 같은 폴더 `afhe-khanes2022-analysis-dataset.rds`에서 `names()`·`class()`·`levels()`·`label` 속성만 추출(3,697행 × 58열). 행 데이터는 읽지도 출력하지도 않음
- 정의 출처: 레포 `CLAUDE.md` 141–166행(파일 목록), 204–260행(정의)
날짜: 2026-10-19 조사
에이전트: 해당 없음(구조 조사)
식별 가능 열 처리: `ID`(Identifier) 열은 아래 목록에서 제외. 검진일·소속에 해당하는 열은 데이터셋에 없음. `SEX`는 전원 남성이라 분석에 쓰이지 않음

## 변수 구조 (화면 노출 규칙 1: 구조만)

| 범주(코드북) | 변수 | 자료형 | 단위 / 수준 |
|---|---|---|---|
| Identifier | GROUP | factor | Pilot HE / KHANES |
| Demographics | AGE | numeric | years |
| Demographics | AGE_GROUP | factor | ≤ 29 / 30-39 / 40-49 / ≥ 50 |
| Vital Signs | HEIGHT, WEIGHT | numeric | cm, kg |
| Vital Signs | BMI | numeric | kg/m² |
| Vital Signs | WAISTCIR | numeric | cm |
| Vital Signs | SYSBP, DIABP | numeric | mmHg |
| Medication | HYPERTENSION, DYSLIP, DIABETES | factor | No / Yes (약물 복용) |
| Disease | C_HYPERTENSION, C_ABOBESE, C_OBESE, C_DIABETES, C_HYPERTG, C_HYPERCHOL, C_DYSLIPIDEMIA | factor | No / Yes (CLAUDE.md 정의 1–7) |
| Disease | METS_new | factor | Normal / MeTS |
| MeTs Criteria | mets_c1 | factor | Abdominal Obesity (waist circumference ≥ 90 cm) |
| MeTs Criteria | mets_c2 | factor | High Triglyceride (TRIG ≥ 150 mg/dL \| medication) |
| MeTs Criteria | mets_c3 | factor | Low HDL Cholesterol (HDL < 40 mg/dL \| medication) |
| MeTs Criteria | mets_c4 | factor | High Blood Pressure (SYSBP ≥ 130 mmHg \| DIABP ≥ 85 mmHg \| medication) |
| MeTs Criteria | mets_c5 | factor | High Fasting Glucose (GLUC ≥ 100 mg/dL \| medication) |
| MeTs Criteria | mets_count | factor | 0 / 1 / 2 / ≥ 3 |
| Substance Use | SMOKING, ALCOHOL | factor | No / Yes |
| Substance Use | EXERCISE | factor | Low / Moderate / High |
| Laboratory Test | WBC, RBC, PLAT | numeric | 10³/μL, 10⁶/μL, 10³/μL |
| Laboratory Test | HGB, HCT | numeric | g/dL, % |
| Laboratory Test | BUN, CREAT | numeric | mg/dL |
| Laboratory Test | URATE | numeric | mg/dL (Uric Acid; 논문 표는 μmol/L, ×59.48) |
| Laboratory Test | AST, ALT | numeric | IU/L |
| Laboratory Test | GLUC | numeric | mg/dL (논문 표는 mmol/L, ÷18.02) |
| Laboratory Test | CHOL, TRIG, HDL, LDL | numeric | mg/dL |
| Laboratory Test | URBLD, URPROT, HBSAGCAT, HCVABCAT | factor | − / + |
| Complex Sample Design | wt_itvex | numeric | Sample Weight (KNHANES) |
| Complex Sample Design | psu | character | PSU (KNHANES) |
| Complex Sample Design | kstrata | numeric | Strata (KNHANES) |
| 파생(코드북 밖) | GROUP2 | factor | KHANES / Pilot HE (참조군을 KHANES로 둔 재배열) |
| 파생(코드북 밖) | C_OBESEB | factor | BMI<23 / 23≤BMI<25 / 25≤BMI<30 / BM≥30 |
| 파생(코드북 밖) | medication, medication_n | factor | No / Yes; 0 / 1 / 2 / 3 |
| 파생(코드북 밖) | WC_GROUP | factor | Q1 / Q2 / Q3 / Q4 (pooled 사분위) |

변수 라벨은 코드북 `variable_label` 그대로(예: "Uric Acid (mg/dL)", "WBC (10^3^/μL)"). 표의 `|`는 라벨 원문의 OR 기호.

## 계약서 쪽 정의 (레포 CLAUDE.md 141–160행)

> | 파일명 | 설명 |
> |--------|------|
> | `afhe-khanes2022-analysis-dataset.rds` | **주요 분석 데이터** (공군 + KHANES 병합, 최종 전처리 완료) |
> | `afhe-khanes2022-mrege_final.csv` | 위 rds의 CSV 버전 |
> …
> **기본 분석 데이터 로드 방법**:
> ```r
> afhe_khanes_final <- readr::read_rds("data/derived-data/afhe-khanes2022-analysis-dataset.rds")
> ```

## 슬라이드에서 쓸 핵심
- 한 줄 메시지: 에이전트가 받은 것은 행이 아니라 구조다. 변수명이 계약서(mets_c1–c5), 코드북, 코드, 표에서 같은 이름으로 이어진다
- 보여줄 부분(코드/출력/문장): 범주별 변수 표(위). 녹화·라이브에서는 `names()`, `sapply(d, class)`, 코드북 표까지만. `head()`·데이터뷰어 금지
- 연구자가 확인한 것: 약물 변수 3개(Medication)와 질병 변수 7개(Disease, `C_` 접두)가 다른 범주라는 점. KNHANES 설계변수 3개가 있지만 쓰지 않기로 한 결정(`08-unweighted-decision.md`)
