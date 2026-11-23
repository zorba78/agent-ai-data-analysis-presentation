# 프로젝트 폴더 구조

발표에서 다룬 대사증후군 연구(공군 조종사 대 국민건강영양조사)의 프로젝트 폴더를 그대로 본뜬 구조.

원칙 세 가지

- 원자료는 읽기 전용
- 에이전트의 산출물은 날짜와 작업 이름이 붙은 실행 폴더에만 저장
- 연구자가 확인한 것만 정식 폴더로 옮기고, 옮긴 내용을 진행 기록에 남김

```text
my-project/
├── CLAUDE.md                     # project instructions, read at session start
├── .claude/
│   └── settings.json             # permissions
├── data/
│   ├── rawdata/                  # raw data, read-only
│   └── derived-data/             # cleaned and merged data, after verification
├── code/
│   ├── user/                     # researcher's scripts
│   └── agent/
│       └── YYYY-MM-DD_task-name/ # one run folder per task
│           ├── README.md         # goal, input, how to run, outputs
│           ├── scripts/
│           ├── output/           # tables, figures, logs of this run
│           └── data/             # datasets made in this run
├── output/
│   ├── tables/                   # Table 1 to N (docx, csv)
│   ├── figures/                  # figures (300 dpi tiff, png) with source code
│   └── logs/                     # run logs
├── quarto/                       # reports rendered for the researcher
├── manuscript/                   # manuscript draft, cover letter, checklist
├── docs/
│   ├── analysis-plan.md          # statistical analysis plan, fixed before analysis
│   ├── progress.md               # one line per finished task
│   └── literature/               # literature notes with PMID or DOI
├── references/                   # PDFs
└── .gitignore                    # exclude raw data and personal information
```

## 사례의 실행 폴더

대사증후군 연구에서 에이전트가 하루 동안 만든 실행 폴더 이름. 작업 순서와 내용이 폴더 이름만으로 보임.

```text
code/agent/
├── 2026-11-02_공군자료정제/
├── 2026-11-02_KNHANES정제/
├── 2026-11-02_완전사례/
├── 2026-11-02_분석계획서/
├── 2026-11-02_기술통계/
├── 2026-11-02_유병률비교/
├── 2026-11-02_하위집단분석/
├── 2026-11-02_바이오마커/
├── 2026-11-02_문헌_요산/
├── 2026-11-02_결과해석/
└── 2026-11-02_원고초안/
```

## 실행 폴더의 README.md 양식

사례의 `2026-11-02_기술통계/README.md` 구성. 에이전트에게 실행 폴더마다 이 양식으로 쓰게 함.

```markdown
# <YYYY-MM-DD>_<작업 이름>: <분석계획서의 해당 단계>

작성: <에이전트 이름 또는 연구자>, <날짜>

## 목표
<분석계획서의 어느 절을 수행하는지, 무엇을 만드는지>

## 입력
| 파일 | 내용 |
|---|---|
| data/derived-data/04_analysis_cc.rds | 3,823 × 48, 결측 없음. md5 기록 |

## 실행
Rscript code/agent/<실행 폴더>/scripts/05_derive_table1.R
종료 코드, 경고 수, stopifnot() 통과 여부

## 산출물
| 파일 | 내용 |
|---|---|
| scripts/05_derive_table1.R | 파생, 검증, Table 1 |
| output/tables/table1.csv, table1.docx | Table 1 |
| output/logs/…_flow.csv | 단계별 대상자 수 |
| output/logs/…_session.txt | sessionInfo() |
```

## 진행 기록(docs/progress.md) 양식

작업 하나에 한 줄. 날짜, 한 일, 실행 폴더, 검증 결과, 정식 폴더로 옮긴 파일, 남은 문제. 사례의 실제 기록 두 줄(일부 생략).

```text
- 2026-11-02: 사용자 확정. 결측은 완전사례 분석(다중대체 없음). 남은 결정: 연령표준화 기준인구
- 2026-11-02: run 06 완료(code/agent/2026-11-02_유병률비교/): Table 2. 오케스트레이터 독립 재계산으로
  OR 전부 일치. 반영: output/tables/table2_prevalence_or.*. 미결: 공군 혈압 측정 횟수 사용자 확인
```

이 기록이 있으면 새 세션의 에이전트가 지난 결정과 남은 문제를 이어받음.

## 폴더 만들기

프로젝트 폴더에서 R로 한 번 실행.

```r
dirs <- c(
  "data/rawdata", "data/derived-data", "code/user", "code/agent",
  "output/tables", "output/figures", "output/logs",
  "quarto", "manuscript", "docs/literature", "references", ".claude"
)
invisible(lapply(dirs, dir.create, recursive = TRUE, showWarnings = FALSE))
if (!file.exists("docs/progress.md")) writeLines("# Progress", "docs/progress.md")
if (!file.exists(".gitignore")) {
  writeLines(
    c("data/rawdata/", "data/derived-data/", "*.sas7bdat", "*.xlsx",
      "output/logs/", ".Rhistory", ".RData"),
    ".gitignore"
  )
}
```

`.gitignore` 내용은 사례 프로젝트와 같음. 원자료, 전처리 자료, 로그를 저장소에서 제외.

## 원자료 보호

- `.gitignore`에 원자료 폴더와 자료 파일 확장자 등록
- 권한 설정(`.claude/settings.json`)에서 원자료 폴더 편집 금지
- 추가로 운영체제에서 원자료 폴더를 읽기 전용으로 설정. 권한 설정은 편집 도구만 막고, R 코드로 쓰는 것까지 막지는 못함
