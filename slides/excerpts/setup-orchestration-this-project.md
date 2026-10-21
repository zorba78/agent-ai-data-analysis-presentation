# setup-orchestration-this-project

원본: agent-ai-data-analysis-presentation/CLAUDE.md 오케스트레이션 절(66–83행), scripts/run-worker.ps1 머리 주석(1–16행) (마스킹 완료, 2026-10-19)
섹션: 11
보여줄 이유: 계약서 하나(CLAUDE.md = AGENTS.md)를 두 회사의 오케스트레이터가 공유하고, 쓰는 모델과 검토하는 모델의 계열을 다르게 하며, 워커 호출은 스크립트가 실제 수행 모델을 기록한다

```markdown
## 오케스트레이션
이 프로젝트는 오케스트레이터 둘과 워커 둘을 쓴다. 공유 상태는 대화가 아니라 레포다(이 파일 = AGENTS.md, `memory/`, `review/`, git).
| 역할 | 모델 · effort | 실행 | 정의 |
|---|---|---|---|
| 오케스트레이터 A: 작성 허브 | Claude Fable 5.1 · medium | Claude Code 메인 세션 | `.claude/settings.json` |
| 오케스트레이터 B: 검토 허브 | GPT-6.0 Astra · medium | `copilot --model gpt-6-astra --reasoning-effort medium` | `prompts/astra-session.md` |
| 워커: 슬라이드 작성 | Claude Opus 5.5 · xhigh | Agent 도구 `slide-writer` | `.claude/agents/slide-writer.md` |
| 워커: 수치·인용 검증 | Claude Opus 5.5 · xhigh | Agent 도구 `fact-checker` | `.claude/agents/fact-checker.md` |
| 워커: 독립 검토 | GPT-5.6 Terra · high | `scripts/run-worker.ps1 -Worker terra` | `.codex/config.toml` `[profiles.worker]`, `prompts/review-terra.md` |
규칙:
1. 작업마다 주 오케스트레이터는 하나다. 상대 오케스트레이터는 워커로만 부른다
2. 쓰는 모델과 검토하는 모델은 계열을 다르게 한다. Opus가 쓴 것은 Terra 또는 Astra가, Terra가 쓴 것은 Opus가 검토한다
3. Astra와 Terra는 `review/`에만 쓴다. Fable과 Opus는 `review/`를 읽기만 한다
4. 워커 호출은 `scripts/run-worker.ps1`을 거친다. Terra가 한도·오류로 실패하면 같은 작업을 Opus 5.5(`claude -p`)로 재실행하고, 결과 파일 머리에 실제 수행 모델을 기록한다
```

```powershell
<#
.SYNOPSIS
  Worker dispatcher for the talk project (2026-10-19).
  Runs a task file through a worker model and saves the response with a header
  recording which model actually did the work.
.DESCRIPTION
  -Worker terra : GPT-5.6 Terra via Codex CLI, profile "worker" (.codex/config.toml, effort high, read-only sandbox).
                  If Codex exits non-zero or prints a usage/rate-limit message, the same task is re-run with
                  -Worker opus and the header says "fallback from terra".
  -Worker opus  : Claude Opus 5.5 via `claude -p`. No further fallback: if the Claude subscription limit is hit,
                  the script stops and reports (CLAUDE.md orchestration rule 5).
#>
```

## 치환 목록
| 종류 | 건수 |
|---|---|
| 없음(.EXAMPLE 줄의 경로는 프로젝트 상대 경로라 홈 디렉터리 없음. 그 줄은 20줄 제한으로 생략) | 0 |
