# 녹화 환경과 설치 슬라이드 결정 2026-10-21

- 녹화는 Hyper-V Windows 11 VM에서 설치부터 진행(사용자 결정). 현재 PC 화면에 API 키 메모, Recent 서버명 등 노출 위험이 있어 깨끗한 VM 사용
- 호스트: Windows 11 Enterprise, RAM 128GB, 24코어, C 드라이브 1.6TB 여유. Hyper-V 기능은 2026-10-21 기준 꺼져 있었음(설정 → 시스템 → 고급 → 가상 작업 영역에서 켜기, 재부팅 필요)
- VM 설치 원본: 사용자 보유 Win11.iso. 빠른 만들기 → 로컬 설치 원본 → "이 가상 컴퓨터에서 Windows 실행" 체크(2세대, TPM). 메모리 16GB, CPU 4+. 정품 키는 호스트 키 재사용 금지, 키 없이 설치 가능
- VM 설정 후: 향상된 세션 1920×1080, 배율 125%, Windows 업데이트 완료, 체크포인트 3개(clean / 도구 설치 후 / 프로젝트 투입 후)
- 분석 장면 데이터: 공군 데이터는 VM에 복사하지 않음. 합성 데이터 또는 공개 데이터(미정)
- 슬라이드 9(Positron: 설치와 구동), 11(Claude Code: 설치와 구동)로 개정. 설치 정보는 2026-10-21 공식 문서 확인. 영상 자리: demo/clips/positron-first-run.mp4(사용자 제작). Claude Code 설치 영상도 추가 예정(11번)
- 11번 하단 카드(읽기/쓰기/실행/권한): 설치 후 에이전트가 할 수 있는 일. 사용자가 목적을 물었고 유지 여부 미결
- 다음: VM용 설정 묶음(CLAUDE.md, 폴더 구조, 합성 데이터, 코드북) + 녹화 런북(demo-runbook 스킬)
- 2026-10-28: 저장소 공개 전환(사용자 결정), GitHub Pages 켬. 주소 https://zorba78.github.io/agent-ai-data-analysis-presentation/slides/ (루트는 slides/로 리다이렉트). 렌더 결과(slides/index.html, index_files)를 커밋해야 Pages가 갱신됨. 영상(demo/clips)은 git 제외라 Pages에서는 재생 안 됨 → Release 첨부 또는 별도 호스팅 필요
