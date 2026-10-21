# 12. 에이전트가 HWE 인용 5편을 "중복"으로 삭제, 저자가 복원

출처:
- `G:/Projects/airforce-fatty-liver/memory/agent_bot/2026-08-16/session-summary.md` §5-1 44–48행
- 복원된 문장: `quarto/agent_bot/2026-08-16/manuscript-minor-revision-r2.qmd` 352행
날짜: 2026-08-16 저녁
에이전트: DataBot(레포 CLAUDE.md 명칭; 모델 미기재)

## 인용

> ## 5-1. 사용자 검토 후 원고 r2 수정 (같은 날 저녁, 재렌더 완료)
>
> - **HWE 인용 복원**: Introduction "We anchor our findings within the framework of the healthy-worker effect (HWE) in aviation" 문장의 `[@cairns2020; @houston2011; @koterov2025; @park2024; @pizzi2008]` — 오전 세션이 "Discussion 재인용과 중복"으로 삭제했던 것을 복원. 해석 틀을 도입하는 문장에 근거가 없어지는 것은 중복 제거가 아님. 렌더 결과 참고문헌 36편 불변, 복원 5편은 [17–21]
> - **Table 3 각주 중복 제거**(사용자 지적): 새로 넣었던 "All estimates are per 1-SD …" 문장이 기존 "OR = odds ratio for MetS per 1-SD increase in the biomarker (standardized)"와 중복 → 새 문장 삭제, 기존 정의를 "(standardized on the pooled sample, N = 3,697)"로 확장. 답변서 comment 11도 이에 맞춰 수정
> - 교훈: "중복 인용" 판단은 같은 문헌이 여러 문장에 붙는 것을 자동으로 중복으로 보면 안 됨. 각 문장이 자체 근거를 필요로 하는지 먼저 볼 것

복원된 문장(r2 qmd 352행):

> We anchor our findings within the framework of the healthy-worker effect (HWE) in aviation [@cairns2020; @houston2011; @koterov2025; @park2024; @pizzi2008] and link them to our prior work on metabolic dysfunction-associated fatty liver disease (MAFLD) [@songku2025].

## 슬라이드에서 쓸 핵심
- 한 줄 메시지: 리뷰어의 "중복 인용" 지적을 에이전트가 기계적으로 적용하면 해석 틀의 근거가 사라진다. 저자 검토가 통제 지점이다
- 보여줄 부분(코드/출력/문장): "해석 틀을 도입하는 문장에 근거가 없어지는 것은 중복 제거가 아님"과 교훈 한 줄. 같은 날 반대 방향(사용자 지적으로 진짜 중복인 각주 삭제)도 함께
- 연구자가 확인한 것: 참고문헌 수(36편)가 불변인지, 복원 5편의 번호([17–21])가 렌더 결과와 맞는지. 오류 장면은 각색하지 않고 memory 문장 그대로 쓴다(이 프로젝트 CLAUDE.md 행동 규칙 3)
