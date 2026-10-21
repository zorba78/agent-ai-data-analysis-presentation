# setup-skills-ss-bundle

원본: <project-name>-phase3-sample-size/.claude/skills/*/SKILL.md 의 frontmatter description 5개 (마스킹 완료, 2026-10-19)
섹션: 10
보여줄 이유: 표본크기 산출이라는 한 과업을 "문헌 추출 / 벤치마크 / 공식 계산 / 시뮬레이션 / 민감도 / 보고서"로 쪼개고, 각 스킬의 description에 트리거 문구를 넣은 묶음

```yaml
# ref-extract
description: references/ 폴더의 참고문헌(hwpx IB, docx 초안, pdf 프로토콜·SAP)에서 텍스트를 추출하고 핵심 수치(효과크기, SD, n, 방문, 분석법)의 위치를 찾는다. "IB에서 … 찾아", "프로토콜 어디에", "SAP의 MMRM 모형", "새 참고문헌 추가" 요청에 사용.
# <indication>-benchmark
description: 다른 <indication> 2/3상 시험의 1차 변수·효과크기·SD·표본크기·탈락율을 조사해 <project-name> 3상 가정의 타당성을 뒷받침하는 벤치마크 표를 만든다. ClinicalTrials.gov(c-trials MCP), PubMed MCP, Consensus를 사용. "다른 <indication> 3상은 몇 명", "FVC를 1차로 쓴 시험", "위약군 FVC 감소율 문헌값" 요청에 사용.
# ss-continuous
description: 연속형 1차 유효성 변수(기저치 대비 변화량, ANCOVA)에 대한 공식 기반 표본크기 산출. 효과크기(Cohen's d 또는 Δ/SD), 탈락 보정, 배분비, ANCOVA 분산감소를 다룬다. "표본크기 계산", "군당 몇 명", "d=0.35로 다시", "2:1 배정이면" 같은 요청에 사용.
# ss-mmrm-sim
description: 반복측정 1차 분석(MMRM, 선형혼합모형)에 맞춘 시뮬레이션 기반 검정력·표본크기. 방문별 평균 궤적, 공분산 구조(UN/AR1/CS), 탈락 패턴(MCAR/MAR)을 지정해 nlme로 검정력을 추정한다. "MMRM 기준 검정력", "시뮬레이션으로 확인", "탈락이 중간에 생기면" 요청에 사용.
# ss-sensitivity
description: 표본크기 민감도 분석. 효과크기(d 또는 Δ/SD), 검정력, 탈락율, 배분비를 격자로 바꿔 표와 그림(검정력 곡선, 히트맵)을 만든다. "민감도 표", "시나리오별", "d를 0.25~0.5로", "power 90%면" 요청에 사용.
# ss-report
description: 프로토콜·SAP·IND 제출용 "표본크기 산정(Sample Size Determination)" 절 작성. 한국어 본문 + 영문 병기, 근거·가정·공식·시나리오별 결과를 규제 문서 양식으로 정리하고 Quarto(.qmd)로 작성해 Word(.docx)로 렌더링한다. 표는 flextable. "보고서로 정리", "프로토콜 문구", "IND용 문서", "docx로" 요청에 사용.
```

(스킬 폴더는 6개. `ss-*` 4개 + 참고문헌 추출 + 벤치마크. 섹션 10에서 "분석 스킬 묶음 5개"로 보여줄 때는 `ref-extract`를 빼거나 벤치마크를 빼면 된다)

## 치환 목록
| 종류 | 건수 |
|---|---|
| 시험약·과제명 → `<project-name>` | 2 (description 1곳, 원본 경로 1곳) |
| 적응증(질환명) → `<indication>` | 4 (스킬 이름 1곳, description 3곳) |
