# 오케스트레이션 결정 (2026-10-19)

| 역할 | 모델 · effort | 실행 | 확인 |
|---|---|---|---|
| 오케스트레이터 A 작성 허브 | Claude Fable 5.1 · medium | Claude Code, `.claude/settings.json` | 이 세션 |
| 오케스트레이터 B 검토 허브 | GPT-6.0 Astra · medium | `copilot --model gpt-6-astra --reasoning-effort medium` | `copilot -p "reply ok" --model gpt-6-astra -s` → ok |
| 워커 slide-writer, fact-checker | Claude Opus 5.5 · xhigh | `.claude/agents/*.md` | |
| 워커 독립 검토 | GPT-5.6 Terra · high | `codex exec -p worker` (`.codex/config.toml`) | `codex exec -m gpt-5.6-terra` → ok, 종료코드 0, 호출당 약 10.7k 토큰 |

- 한도 소진: Terra 실패 → `scripts/run-worker.ps1`이 Opus 5.5로 재실행하고 결과 머리에 기록. Claude 쪽 한도는 Fable과 Opus가 공유하므로 대체 불가 → 대기.
- **미결정**: Claude 한도 소진 시 API 과금(`ANTHROPIC_API_KEY`) 전환 여부. 결정 전까지 쓰지 않는다.
- 사용자가 Codex에서 안 쓰는 스킬·플러그인을 껐다(2026-10-19).
- Copilot CLI `--agent`가 `.github/agents/*.md`를 읽는지, `settings.json`에 effort 기본값을 둘 수 있는지는 미확인.
- Codex `exec`는 stdin이 TTY가 아니면 추가 입력을 기다린다. 스크립트는 `cmd /c codex ... < NUL`로 EOF를 준다.
- Codex는 프로젝트 `.codex/config.toml`의 `[profiles]`를 무시한다. 모델·effort·샌드박스는 스크립트가 플래그로 넘긴다.
- Codex `exec`는 최종 답만 stdout에, 배너·토큰 수·경고는 stderr에 쓴다. 스크립트는 stdout만 결과로 저장한다.
- 디스패처 시험(2026-10-19): Terra 경로 정상(모델·effort high·read-only 확인), Terra 실패 시 Opus 대체 경로도 정상. 호출당 약 20k 토큰(스킬·플러그인 정리 후에도).
- `.claude/settings.json`의 `Write(...)` deny 규칙은 무효(Edit 규칙이 모든 편집 도구를 덮음). 사용자가 직접 지워야 함. 워크스페이스 신뢰 대화상자도 한 번 수락 필요.
