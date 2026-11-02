---
name: setting-video-youtube-2026-11-02
description: 프로젝트 설정 녹화(setting-01)는 YouTube 링크로 참조, 기존 설치 영상 링크는 유지
metadata:
  type: project
---

- 원본: C:/Users/Boncho/Videos/화면 녹화/setting-01.mp4(35분, 4K, 8.9GB). 2배속 압축본 setting-01-2x.mp4(17분 32초, 4K, 90MB, H.264 CRF 26)
- 내용: 폴더 생성 목적, CLAUDE.md, 스킬셋, 오케스트레이션 설정 실제 작업
- 슬라이드 참조 방식: YouTube 링크(사용자 결정 2026-11-02). act2.qmd "시연: 프로젝트 설정" 장(30/52), 오케스트레이션 구성 다음. 주소 https://www.youtube.com/watch?v=HFQgLpBmv88 (2026-11-02 반영, 업로드 파일 setting-01-2x.mp4(4K 2배속 CRF 26, 90MB))
- "시연: 설치와 첫 실행" 장의 기존 영상(로컬 clip + GitHub Release v0.1-demo)은 그대로 유지(사용자 결정)
- 미완료: 발표용 재생 구간, 커밋. 3막 영상 6개(YOUTUBE_ID_1–6)는 녹화 후

**Why:** 영상이 커서 git, Release 대신 YouTube로 호스팅
**How to apply:** 주소를 받으면 YOUTUBE_ID 교체 후 렌더, index.html 커밋(Pages 갱신). [[vm-recording-plan-2026-10-21]]
- YouTube embed는 file://로 열면 Error 153(Referer 없음). quarto preview, 로컬 http 서버, GitHub Pages로 열면 정상(사용자 확인 2026-11-02). 발표 당일도 http로 열 것. iframe에 referrerpolicy="strict-origin-when-cross-origin" 명시
- setting-01-low.mp4는 화질 불량으로 미사용(사용자 2026-11-02). 인코딩 기준은 4K 유지, libx264 CRF 26 preset fast, 2배속, aac 96k
- 2026-11-02 3막 영상 5개 연결: ① SxZpKwva5qo / ②③ _SwO-ve6bFY / ④ xnLV1XTcu_E / ⑤ WXJjkJ09R6U / ⑥ PijAcm--Ngc. 모두 referrerpolicy iframe. 재생 구간 미정
