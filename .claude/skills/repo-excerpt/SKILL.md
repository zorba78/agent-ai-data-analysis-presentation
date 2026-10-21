---
name: repo-excerpt
description: 사례 레포(airforce-fatty-liver)의 대화 로그, memory, 코드, qmd에서 발표 장면을 인용 단위로 뽑아 slides/excerpts/에 저장한다. "발췌", "장면 뽑아줘", "msg[18] 인용", "레포에서 가져와" 요청 시, 그리고 talk-orchestration 1단계에서 사용.
---

# 레포 발췌

사례 레포 `G:/Projects/airforce-fatty-liver`는 **읽기 전용**이다. 발췌본은 이 프로젝트의 `slides/excerpts/<섹션번호>-<이름>.md`에 쓴다.
장면 목록과 출처는 `memory/talk-scenes-from-repo.md`에 있다. 거기 없는 장면을 새로 찾으면 그 파일에 한 줄 추가한다.

## 대화 로그 읽는 법

`agent-conversation/*.json`은 Positron Assistant 내보내기(`messages[]` 배열, 항목마다 `message.lmMessage[]`). `.html`은 같은 내용이므로 열지 않는다. 레포 루트의 `conversation-export.json`은 `conversation-add-analysis.json`과 거의 같고 msg[32–33]만 더 있다.
json을 통째로 읽지 않는다. 메시지 번호로 뽑는다.

```powershell
python -I .claude/skills/repo-excerpt/scripts/extract_msg.py G:\Projects\airforce-fatty-liver\agent-conversation\conversation-add-analysis.json 18-21
python -I .claude/skills/repo-excerpt/scripts/extract_msg.py <json> --grep "결과 해석이 이상한데"
```

콘솔 인코딩이 cp949라 한글이 깨지면 `> output/agent/YYYY-MM-DD/msg.txt`로 UTF-8 파일에 쓴 뒤 읽는다(스크립트가 stdout을 UTF-8로 바꾸지만 PowerShell 5.1 리디렉션은 BOM을 붙인다. Read 도구로 읽으면 문제없다).

## 발췌본 형식

```markdown
# <섹션번호>. <장면 이름>

출처: <파일 경로> msg[<n>] (또는 파일, 줄)
날짜: <로그 timestamp를 날짜로>
에이전트: Positron Assistant (Claude Sonnet 4.6)   ← 로그에 적힌 대로

## 인용
> (사용자) ...
> (에이전트) ...

## 슬라이드에서 쓸 핵심
- 한 줄 메시지:
- 보여줄 부분(코드/출력/문장):
- 연구자가 확인한 것:
```

## 규칙

1. 인용은 글자 그대로. 줄임은 `…`로 표시하고 뜻이 바뀌지 않게 한다. 다듬지 않는다.
2. 도구 결과(tool-result)는 집계, 구조, 에러 메시지만 옮긴다. 행 단위 데이터가 보이면 그 부분을 `[행 데이터 생략]`으로 바꾼다. ID, 검진일, 소속 열은 변수명도 옮기지 않는다.
3. 경로에 든 사용자 홈 디렉터리, 내부 서버명은 `<path>`로 바꾼다.
4. 수치가 포함된 인용은 `references/`의 논문 값과 다를 수 있다(분석 중간 단계). 발췌본에 "원고 최종값: …"을 병기하거나 "중간값"이라고 적는다.
5. 발췌본 하나에 장면 하나. 섹션 번호를 파일명 앞에 붙인다.
