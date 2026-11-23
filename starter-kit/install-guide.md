# 설치 안내

2026년 11월 기준. 명령과 메뉴 이름은 바뀔 수 있으므로 막히면 각 단계의 공식 문서를 확인.

## 1. R과 Positron

1. R 설치: <https://cran.r-project.org>
2. Positron 설치: <https://positron.posit.co/download.html>
3. Positron에서 프로젝트 폴더 열기(File > Open Folder). 오른쪽 위에서 R 버전 선택
4. PDF 출력이 필요하면 Positron 터미널에서 `quarto install tinytex`
5. 분석 패키지 설치. 사례 연구에서 쓴 것: `install.packages(c("tidyverse", "haven", "readxl", "survey", "gtsummary", "flextable", "officer", "emmeans"))`

## 2. Claude Code

요건: 유료 구독(Pro, Max, Team, Enterprise) 또는 Console 계정. 무료 요금제로는 쓸 수 없음.

1. 명령줄 도구 설치
   - Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`
   - macOS, Linux: `curl -fsSL https://claude.ai/install.sh | bash`
2. 새 터미널을 열고 `claude --version`으로 확인
3. 프로젝트 폴더에서 `claude` 실행. 첫 실행 때 브라우저 로그인
4. Positron 확장(선택): Extensions 창(Ctrl+Shift+X)에서 "Claude Code" 검색 후 설치

공식 문서: <https://code.claude.com/docs>

## 3. Positron MCP(R 세션 연결)

에이전트가 내가 보는 R 세션에서 코드를 실행하고 객체를 조회하게 하는 연결. Positron 2026.10 이상에 들어 있고, 따로 설치할 것은 없음. 실험 기능.

1. Positron 설정(Ctrl+,)에서 `ai.mcp.enabled` 검색 후 켜기
2. 명령 팔레트(Ctrl+Shift+P)에서 "Positron MCP: Add to Coding Agent" 실행
3. Positron에서 새 터미널을 열고 프로젝트 폴더에서 `claude mcp list` 실행. `positron`이 연결됨으로 보이면 완료
4. R 세션을 하나 시작한 뒤 Claude Code에 "현재 R 세션의 객체 목록을 보여줘"라고 요청해 확인

등록은 프로젝트 폴더마다 한 번. Windows에서 `positron`이 목록에 안 보이면 Positron을 최신 판으로 올린 뒤 2번을 다시 실행.

안내 글: <https://opensource.posit.co/blog/2026-11-04_positron-mcp/>

## 4. 문헌 검색 MCP

1. claude.ai에 로그인 > 설정 > 커넥터에서 PubMed 연결. 필요하면 bioRxiv, Clinical Trials, Scholar Gateway도 연결
2. 같은 계정으로 로그인한 Claude Code에서 `claude mcp list` 또는 대화 중 `/mcp`로 확인
3. 확인 요청 예: "PubMed에서 PMID <여기에: 번호>의 서지 정보를 조회해줘"

밖으로 나가는 것은 검색어와 검색 결과. 쓰는 도구만 연결.

## 5. 함께 쓰는 도구

| 도구 | 쓰는 이유 | 시작 |
|---|---|---|
| Git | 에이전트가 바꾼 내용을 기록하고 되돌림 | <https://git-scm.com> 설치 후 프로젝트 폴더에서 `git init` |
| renv | 패키지 버전 고정, 같은 결과 재현 | R에서 `install.packages("renv"); renv::init()` |
| Zotero, Better BibTeX | 실제 문헌 목록과 인용키를 대조할 기준 | <https://www.zotero.org>, `references/references.bib`로 자동 내보내기 |

## 6. 첫 실행 점검

- [ ] `claude --version` 출력 확인
- [ ] `claude mcp list`에 `positron`과 문헌 검색 MCP가 연결됨으로 표시
- [ ] 프로젝트 폴더에 `CLAUDE.md`, `.claude/settings.json`, `docs/progress.md`가 있음
- [ ] 원자료 폴더가 `.gitignore`에 있음
- [ ] Claude Code에 "CLAUDE.md를 읽고 이 프로젝트의 규칙을 요약해줘"라고 요청해 지침이 읽히는지 확인
