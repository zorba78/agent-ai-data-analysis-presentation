# setup-orchestration-annual-report

원본: healthy-aging-project-annual-report/.claude/skills/annual-report/SKILL.md 역할 표와 "지킬 것"; .claude/agents/evidence-analyst.md 14–15행 (마스킹 완료, 2026-10-19)
섹션: 11
보여줄 이유: 보고서 문장은 오케스트레이터가 쓰지 않는다. 근거 분석 / 초안 / 검토를 다른 에이전트에 나누고, 근거표에 없는 내용은 보고서에 들어갈 수 없게 만든 구조

```markdown
# 연차실적·계획서 작성 오케스트레이션
이 스킬을 실행하는 세션이 오케스트레이터다. 오케스트레이터는 근거를 모으고, 워커에게 일을 나누고, 결과를 합치고,
사용자에게 보고한다. 보고서 문장은 워커가 쓴다.
| 역할 | 실행 주체 | 모델 · effort | 정의 |
|---|---|---|---|
| 오케스트레이터 | 메인 세션 | Fable 5.1 · medium | `.claude/settings.json` |
| 근거 분석 | `evidence-analyst` | Opus 5.5 · xhigh | `.claude/agents/evidence-analyst.md` |
| 초안 작성 | `report-writer` | Opus 5.5 · xhigh | `.claude/agents/report-writer.md` |
| 검토 | `report-reviewer` | Opus 5.5 · xhigh | `.claude/agents/report-reviewer.md` |
워커는 Agent 도구의 `subagent_type` 에 위 이름을 넣어 부른다. 호출할 때 `model`·`effort` 를 따로 주지 않는다
(정의 파일 값이 쓰이도록). 범용 에이전트로 보고서 문장을 쓰게 하지 않는다.
…
## 3단계. 검토 (review)
초안마다 `report-reviewer` 를 새로 띄운다. 넘길 것은 검토할 파일 경로뿐이다. 오케스트레이터의 평가나 작성 워커의 설명을 붙이지 않는다.
…
## 지킬 것
- 달성 여부("달성"/"미달성")와 달성도(%)는 사용자가 확인한 값만 넣는다. 워커가 추정한 값은 제안으로만 보고한다.
- <db> 는 `<db>-db` 스킬의 규칙대로만 다룬다. 워커 지시문에 계정·비밀번호를 적지 않는다.
```

`.claude/agents/evidence-analyst.md` 14–15행(근거 분석 워커의 역할 정의):

> 네가 만드는 근거표를 보고 다른 작성자가 보고서 문장을 쓴다. 근거표에 없는 내용은 보고서에 들어가지 못하고,
> 근거표에 틀린 내용이 있으면 그대로 평가 문서에 실린다. 그래서 자료에서 직접 확인한 것만 적는다.

(같은 파일 12–13행의 기관명·과제명·파트명이 든 소개 문장은 뽑지 않았다. frontmatter: `model: claude-opus-5-5`, `effort: xhigh`, `tools: Read, Grep, Glob, Bash, Write`, `skills: <db>-db`)

## 치환 목록
| 종류 | 건수 |
|---|---|
| DB명 → `<db>` (스킬 이름 속 DB명 2곳 포함) | 3 |
| 기관명·과제명·파트명(evidence-analyst.md 12–13행) | 발췌 범위 밖(뽑지 않음) |
| 과제 식별 가능한 항목 ID(S1a–S7)·파일명 | 역할 표 밖이라 뽑지 않음 |
