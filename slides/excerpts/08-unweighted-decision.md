# 8. 가중치 미적용 결정: 비교 목적이면 한쪽만 가중할 수 없다

출처:
- `G:/Projects/airforce-fatty-liver/memory/agent_bot/2026-05-09/session-summary.md` §5(52–60행), §7(72–78행)
- `G:/Projects/airforce-fatty-liver/quarto/agent_bot/2026-08-16/manuscript-minor-revision-r2.qmd` 422행(Limitations 단락 마지막 부분)
날짜: 2026-05-09(원고 개정 세션), 2026-08-16(r2)
에이전트: DataBot(레포 CLAUDE.md 명칭). session-summary에 모델명 미기재

## 인용

### 2026-05-09 세션 요약 §5 "수정 적용 후 manuscript 현재 스냅샷"

> - **Sixth limitation** (압축 후 ~95 단어):
>   > Sixth, KNHANES uses a stratified, multi-stage clustered probability sampling design with individual-level survey weights for nationally representative inference on the non-institutionalised Korean civilian population, whereas the Pilot HE cohort is a near-census of active-duty male ROKAF pilots and is not a probability sample. We performed an unweighted analysis throughout because the primary analytic aim is comparative rather than absolute, and applying KNHANES weights to only one side of the comparison would weight the two samples to incompatible target populations and complicate the interpretation of the resulting odds ratios. Consequently, the KNHANES-side prevalences reported here should not be read as nationally representative estimates of Korean male MetS, and the between-group ORs reflect a contrast between the two sampled cohorts rather than a survey-weighted population contrast.

### 같은 파일 §7 "주요 의사결정 / 사용자 피드백"

> 1. **표·그림 미포함**: 사용자 명시 — "qmd 파일에 결과 테이블 및 그림은 포함시키지 않고 논문 내용만 작성"
> 2. **em-dash 지양**: 사용자 명시 — "진행하되 문장에 하이픈 사용 지양 (예: --rather than ... --)"
> 3. **저자 문체 유지**: 사용자 명시 — "저자의 문맥, 문체, 주장 등을 유지하면서 초안의 부족한 부분을 수정"
> 4. **압축 우선**: Abstract, Limitations 모두 길이 압축 요청 두 차례

### 최종 원고 r2 Limitations (422행, 발췌)

> … Finally, KNHANES uses a complex probability sampling design, whereas the pilot cohort represents a near-census of active-duty male ROKAF pilots; we therefore conducted unweighted analyses, as our aim was comparative rather than absolute, and weighting only one group would target incompatible populations. Accordingly, the KNHANES prevalences reported here are not nationally representative, and the ORs reflect contrasts between the two sampled cohorts rather than population-level estimates.

## 슬라이드에서 쓸 핵심
- 한 줄 메시지: 가중치를 쓸지 말지는 연구자의 설계 판단이고, 에이전트는 그 판단을 Limitations 문장으로 끝까지 밀고 갔다
- 보여줄 부분(코드/출력/문장): 5월 초안(~95단어)과 8월 r2(2문장)의 같은 논거. 데이터셋에 `wt_itvex`, `psu`, `kstrata`가 있는데도 쓰지 않은 이유
- 연구자가 확인한 것: 비교 연구에서 한쪽만 가중하면 두 표본의 목표 모집단이 달라진다는 점. KNHANES 측 유병률을 국가 대표값으로 읽지 말라는 단서를 직접 요구해 압축시켰다
