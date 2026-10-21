# 9. 렌더는 "성공"했는데 Figure 1이 없다: error=TRUE의 함정

출처: `G:/Projects/airforce-fatty-liver/memory/agent_bot/2026-08-16/session-summary.md` §5-3 59–63행
날짜: 2026-08-16 밤
에이전트: DataBot(레포 CLAUDE.md 명칭; 모델 미기재). 렌더 환경은 R 4.6.1 사용자 라이브러리

## 인용

> ## 5-3. 렌더 환경 문제 발견·해결 (같은 날 밤)
>
> - 이 작업 사본의 R 4.6.1 사용자 라이브러리에 `DiagrammeR`·`webshot2`·`chromote`가 없어 fig-consort(Figure 1)가 실패, knitr `error = TRUE` 때문에 렌더가 "성공"하면서 Figure 1이 빠지고 stratified 그림이 Figure 1로 번호가 밀린 docx가 두 차례(23:09, 23:28) 생성됐음 → 세 패키지를 CRAN에서 설치 후 재렌더, Figure 1·2 정상 확인
> - git-ignore된 `output/user/mets_lbtest_models.rds`가 없어 문서 맨 앞에 `Error in readRDS()` 문단이 찍혔음 → r2 qmd에서 `file.exists()` 조건부 로드(문서 내 미사용 객체)
> - 교훈: knitr `error = TRUE` 문서는 exit code만으로 성공을 판단하면 안 됨. 렌더 후 docx에서 "Error" 문단·그림 개수·캡션 번호를 반드시 확인

관련 코드 맥락: Figure 1은 `DiagrammeR::grViz()`로 그리는 CONSORT 흐름도(`manuscript-minor-revision-r2.qmd` 1273행). 같은 날 `export-submission-figures.R` 헤더에도 "DiagrammeRsvg and rsvg are not installed and CRAN is unreachable from this machine"라는 환경 제약이 적혀 있다(10–15행).

## 슬라이드에서 쓸 핵심
- 한 줄 메시지: 종료 코드 0은 검증이 아니다. 산출물(docx)에서 그림 개수와 캡션 번호를 세어야 한다
- 보여줄 부분(코드/출력/문장): 첫 번째 글머리 한 줄("렌더가 '성공'하면서 Figure 1이 빠지고 stratified 그림이 Figure 1로 번호가 밀린 docx가 두 차례 생성")과 교훈 한 줄
- 연구자가 확인한 것: 두 차례 생성된 docx를 열어 보기 전까지 실패를 몰랐다는 점. 교훈이 memory에 기록돼 다음 세션의 체크리스트가 됐다
