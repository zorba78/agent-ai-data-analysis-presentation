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

.EXAMPLE
  powershell -File scripts/run-worker.ps1 -Worker terra -Task output/agent/2026-10-19/review-task-section-8.md -Out review/2026-10-19/section-8-terra.md
#>
param(
  [Parameter(Mandatory = $true)][ValidateSet('terra', 'opus')][string]$Worker,
  [Parameter(Mandatory = $true)][string]$Task,
  [Parameter(Mandatory = $true)][string]$Out,
  [switch]$NoFallback
)

$ErrorActionPreference = 'Continue'
$projectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $projectRoot

if (-not (Test-Path $Task)) { Write-Error "Task file not found: $Task"; exit 2 }
$prompt = Get-Content -Path $Task -Raw -Encoding UTF8
$outDir = Split-Path -Parent $Out
if ($outDir -and -not (Test-Path $outDir)) { New-Item -ItemType Directory -Force -Path $outDir | Out-Null }

# Patterns that mean "the subscription window is exhausted", not "the task failed".
$limitPattern = 'usage limit|rate limit|rate_limit|quota|429|too many requests|limit reached|exceeded'

function Invoke-Terra([string]$p) {
  # Codex ignores project-level [profiles] in .codex/config.toml, so model, effort and sandbox are passed
  # explicitly here. Codex reads extra input from stdin when stdin is not a TTY, so stdin is redirected
  # from NUL via cmd.exe (the codex.ps1 wrapper does not forward a PowerShell pipe as EOF reliably).
  $tmpOut = [System.IO.Path]::GetTempFileName()
  $tmpErr = [System.IO.Path]::GetTempFileName()
  $args = "exec -m gpt-5.6-terra -c model_reasoning_effort=high -s read-only --skip-git-repo-check -C `"$projectRoot`" `"$($p -replace '"','\"')`""
  $proc = Start-Process -FilePath 'cmd.exe' -ArgumentList "/c codex $args < NUL" -NoNewWindow -Wait -PassThru `
            -RedirectStandardOutput $tmpOut -RedirectStandardError $tmpErr
  $out = Get-Content -Path $tmpOut -Raw -Encoding UTF8
  $err = Get-Content -Path $tmpErr -Raw -Encoding UTF8
  Remove-Item $tmpOut, $tmpErr -Force -ErrorAction SilentlyContinue
  # codex exec writes only the final answer to stdout; the session banner, "tokens used" and warnings go to stderr.
  # Empty stdout means failure; the caller then gets stderr for diagnosis.
  $body = "$out".Trim()
  return @{ exit = $proc.ExitCode; text = $body; stderr = "$err" }
}

function Invoke-Opus([string]$p) {
  $raw = $p | claude -p --model claude-opus-5-5 --output-format text 2>&1
  $text = ($raw | ForEach-Object { "$_" }) -join "`n"
  return @{ exit = $LASTEXITCODE; text = $text }
}

function Save-Result([string]$modelLabel, [string]$note, [string]$body) {
  $header = @(
    "<!-- worker: $modelLabel -->",
    "<!-- task: $Task -->",
    "<!-- run: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') -->",
    "<!-- note: $note -->",
    ""
  ) -join "`n"
  [System.IO.File]::WriteAllText((Join-Path $projectRoot $Out), $header + $body, (New-Object System.Text.UTF8Encoding $false))
}

$usedWorker = $Worker
$note = 'primary'

if ($Worker -eq 'terra') {
  $r = Invoke-Terra $prompt
  $hitLimit = (($r.text + $r.stderr) -match $limitPattern)
  if ($r.exit -eq 0 -and -not $hitLimit -and $r.text.Length -gt 0) {
    Save-Result 'gpt-5.6-terra (codex exec, effort high, read-only sandbox)' $note $r.text
    Write-Output "OK terra -> $Out"
    exit 0
  }
  Write-Warning "Terra failed (exit $($r.exit); limit pattern matched: $hitLimit)."
  if ($NoFallback) { Save-Result 'gpt-5.6-terra (FAILED)' "exit $($r.exit)" ($r.text + "`n" + $r.stderr); exit 1 }
  $usedWorker = 'opus'
  $note = "fallback from terra (exit $($r.exit); limit pattern matched: $hitLimit). Same model family as the writer: not an independent review."
}

if ($usedWorker -eq 'opus') {
  $r = Invoke-Opus $prompt
  $hitLimit = ($r.text -match $limitPattern)
  if ($r.exit -eq 0 -and -not $hitLimit) {
    Save-Result 'claude-opus-5-5 (claude -p)' $note $r.text
    Write-Output "OK opus -> $Out  [$note]"
    exit 0
  }
  Save-Result 'claude-opus-5-5 (FAILED)' "exit $($r.exit); limit pattern matched: $hitLimit. No further fallback: Claude limit, wait (CLAUDE.md rule 5)." $r.text
  Write-Error "Opus failed (exit $($r.exit); limit pattern matched: $hitLimit). Stopping: no API-billing fallback configured."
  exit 1
}
