---
name: revealjs-deck
description: 발표용 Quarto revealjs 덱(slides/index.qmd, theme.scss)의 골격 생성, 렌더, 넘침, 깨진 그림, 발표자 노트 누락 점검. "렌더", "슬라이드 빌드", "테마", "넘침 확인", "qmd 골격" 요청 시, 그리고 talk-orchestration 6단계에서 사용.
---

# Quarto revealjs 덱

## 골격 (`slides/index.qmd`가 없을 때)

YAML 헤더:

```yaml
---
title: "연구 생산성 향상을 위한 Agent AI 기반 워크플로우: 데이터 분석에서 논문 작성까지"
subtitle: "국민건강영양조사 vs 공군 조종사 건강검진: 대사증후군, 지방간 위험 비교 사례"
author: "구본초"
date: last-modified
lang: ko
format:
  revealjs:
    theme: [default, theme.scss]
    slide-number: c/t
    width: 1600
    height: 900
    code-line-numbers: false
    code-overflow: scroll
    highlight-style: github
    footer: "Positron + Agentic AI, 2026"
    menu: true
    chalkboard: false
    preview-links: false
    embed-resources: false
    transition: none
    fig-cap-location: bottom
execute:
  echo: true
  eval: false
---
```

- `eval: false`가 기본. 슬라이드에서 코드를 실제로 돌리지 않는다(라이브 데모는 Positron에서 한다). 돌려야 하는 청크만 `#| eval: true`.
- 본문 섹션은 `## <번호>. <제목>`로 시작하고, 섹션 안 슬라이드는 `### `가 아니라 `## `로 나눈다(revealjs는 `##`가 슬라이드).
- 모든 슬라이드 끝에 `::: {.notes}` 블록.

## 레이아웃 3종

1. **개념**: 제목 + 다이어그램(SVG 또는 Mermaid) + 1문장.
2. **3단 단계**: `:::: {.columns}` 세 칸. 프롬프트 / 에이전트가 한 일 / 연구자가 확인한 것. 6–11번 섹션에 쓴다.
3. **코드, 결과**: 왼쪽 코드(`.r` 또는 `.text`), 오른쪽 출력 또는 그림. 코드 블록 12줄 이하, 넘으면 `{.scrollable}`가 아니라 잘라서 두 장.

파이프라인 진행바: `theme.scss`의 `.pipeline` 클래스로 상단에 6단계(질문 → 데이터 이해 → 분석 → 검증 → 논문 → 재현)를 그리고 현재 단계를 `.active`로 표시한다. 섹션 첫 슬라이드마다 넣는다.

## `theme.scss`

```scss
/*-- scss:defaults --*/
$font-family-sans-serif: "Pretendard", "Noto Sans KR", sans-serif;
$font-family-monospace: "JetBrains Mono", "D2Coding", monospace;
$presentation-font-size-root: 34px;
$code-block-font-size: 0.65em;
$body-color: #1f2328;
$link-color: #0b5fa5;
/*-- scss:rules --*/
.reveal .pipeline { display: flex; gap: .4em; font-size: .5em; margin-bottom: .6em; }
.reveal .pipeline span { padding: .15em .6em; border: 1px solid #ccc; border-radius: 1em; }
.reveal .pipeline span.active { background: #0b5fa5; color: #fff; border-color: #0b5fa5; }
.reveal .notes-only { display: none; }
```

폰트는 로컬 설치를 전제한다. 설치 여부는 사용자에게 확인한다. 웹폰트를 넣으면 발표장 네트워크에 의존하므로 넣지 않는다.

## 렌더와 점검

```powershell
# Quarto는 PATH에 없다. Positron 번들을 쓴다.
& "C:\Program Files\Positron\resources\app\quarto\bin\quarto.exe" render slides/index.qmd
```

렌더 전 grep: `slides/sections/*.qmd`에 `, `, `—`, raw HTML 블록 태그(`^\s*</?(div|p|h3)\b`, 파이프라인 줄 제외), 슬라이드 안 `^### `가 0건이어야 한다.

렌더 후 브라우저 측정(`python -I -m http.server 8765`를 slides/에서 띄우고 Chrome 탭에서 JS 실행):
- `Reveal.getTotalSlides()` = `##` 슬라이드 수, `.slides section section` = 0(세로 슬라이드 없음)
- 슬라이드마다 `.src`와 notes를 뺀 모든 요소의 최하단이 캔버스 높이(900) − 45 이하
- 육안 확인은 헤드리스 Chrome: `chrome --headless=new --user-data-dir=<임시> --window-size=1600,900 --screenshot=<png> "http://127.0.0.1:8765/index.html#/<번호>"`

렌더 후 점검 항목과 방법:

1. **넘침**: 렌더된 html을 열어(`quarto preview` 또는 브라우저) 슬라이드마다 세로 스크롤이 생기는지. 자동 점검은 Chrome DevTools 없이 어려우므로 본문 6줄, 코드 12줄 규칙을 qmd에서 센다: `## ` 블록별 줄 수를 세어 초과 블록을 보고한다.
2. **깨진 그림**: qmd의 `![](...)`와 `{{< video >}}` 경로가 `slides/assets/`에 실제로 있는지 `Test-Path`.
3. **발표자 노트 누락**: `## ` 블록 수와 `::: {.notes}` 수가 같은지.
4. **화면 노출**: 렌더 산출물에서 `\d{6}-\d{7}`(주민번호형), IP(`\d+\.\d+\.\d+\.\d+`), `C:\\Users\\`, 내부 서버명을 grep. 하나라도 나오면 사용자에게 보고하고 멈춘다.
5. **시간**: `slides/outline.md`의 시간 합계가 53분 이내인지.

점검 결과는 `output/agent/YYYY-MM-DD/render-check.md`에 표로 남긴다.

## 하지 않는 것

- 슬라이드 내용을 고치지 않는다(그건 `slide-writer`). 골격, 테마, 렌더, 점검만 한다.
- `embed-resources: true`로 바꾸지 않는다(녹화 영상이 들어가면 파일이 커진다). 배포본이 필요하면 사용자에게 묻는다.
