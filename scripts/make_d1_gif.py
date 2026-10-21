"""Render a ~20 s replay of a real agent log as an animated GIF (no screen recording).
Scene: slides/excerpts/07-factor-prevalence-zero.md (2026-03-21, Positron Assistant).
Quoted lines are verbatim from the excerpt; rows are omitted, never edited.
Final prevalences match the published MetS paper (Table, component prevalence).
Usage: python -I scripts/make_d1_gif.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "demo", "clips", "D1-error-fix-sample.gif")
PREVIEW_DIR = os.environ.get("D1_PREVIEW_DIR")  # optional: write still frames here
os.makedirs(os.path.dirname(OUT), exist_ok=True)

W, H = 1280, 720
FPS = 10
DUR = 20.0

KR = r"C:\Windows\Fonts\malgun.ttf"
KRB = r"C:\Windows\Fonts\malgunbd.ttf"
MONO = r"C:\Windows\Fonts\consola.ttf"
f_krb = ImageFont.truetype(KRB, 21)
f_mono = ImageFont.truetype(MONO, 20)
f_small = ImageFont.truetype(KR, 18)
f_title = ImageFont.truetype(KRB, 26)
f_cap = ImageFont.truetype(KRB, 23)
f_cap2 = ImageFont.truetype(KR, 20)

BG = (247, 247, 242)
PANEL = (255, 255, 255)
BAR = (238, 241, 245)
INK = (20, 33, 61)
INK2 = (74, 85, 104)
MUTED = (106, 113, 121)
BLUE = (11, 95, 165)
ORANGE = (217, 119, 6)
RED = (180, 35, 24)
GREEN = (22, 128, 61)
CODEBG = (243, 246, 250)
ERRBG = (253, 236, 234)
OKBG = (231, 246, 236)

# (start_sec, kind, text, chars_per_sec or None for instant)
EV = [
    (0.3, "user", "> afhe-khanes-analysis-report-word.qmd 의 전체 분석 결과 해석. …", 28),
    (2.8, "agent", "숫자 코딩을 가정하고 유병률 계산", None),
    (3.1, "code", "mutate(across(mets_c1:mets_c5, ~ as.integer(as.character(.x) == \"1\" |", 90),
    (4.3, "out", "   GROUP2   name        n total   pct", None),
    (4.6, "err", " 1 KHANES   mets_c1     0  1093     0", None),
    (5.2, "err", "Warning message: There were 5 warnings in `mutate()`. … ! NAs introduced by coercion", None),
    (6.0, "out", "mets_c1 class: factor", None),
    (7.6, "agent", "전부 0% → 자료형 확인 후 factor 기준으로 수정", None),
    (7.9, "comment", "# Correct approach for factor \"Yes\"/\"No\"", 70),
    (8.7, "code", "mutate(across(mets_c1:mets_c5, ~ as.integer(.x == \"Yes\")))", 70),
    (10.3, "out", "   GROUP2   name        n total   pct", None),
    (10.6, "ok", " 1 KHANES   mets_c1   495  1093  45.3", None),
    (10.9, "ok", " 4 KHANES   mets_c4   424  1093  38.8", None),
    (11.2, "ok", " 6 Pilot HE mets_c1   339  2604  13", None),
    (11.5, "ok", " 9 Pilot HE mets_c4  1242  2604  47.7", None),
]
CAPTION_AT = 14.0

X0, Y0 = 60, 92
PW, PH = W - 120, 502
LINE_X = X0 + 34
TOP = Y0 + 60


def font_for(kind):
    return f_krb if kind in ("user", "agent") else f_mono


def color_for(kind):
    return {"user": INK, "agent": BLUE, "code": INK, "comment": (90, 120, 90),
            "out": INK2, "err": RED, "ok": GREEN}[kind]


def height_for(kind):
    return 33 if kind in ("user", "agent") else 27


def frame(t):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.text((60, 26), "③ 분석 실행: 이상한 값을 보고 고치기", font=f_title, fill=INK)
    d.rounded_rectangle((W - 360, 26, W - 60, 62), radius=18, fill=(220, 234, 247))
    d.text((W - 210, 44), "실제 로그 재현, 2026-03-21", font=f_small, fill=BLUE, anchor="mm")
    d.rounded_rectangle((X0 + 4, Y0 + 10, X0 + PW + 4, Y0 + PH + 10), radius=20, fill=(225, 229, 236))
    d.rounded_rectangle((X0, Y0, X0 + PW, Y0 + PH), radius=20, fill=PANEL, outline=(217, 222, 231))
    d.rounded_rectangle((X0, Y0, X0 + PW, Y0 + 44), radius=20, fill=BAR)
    d.rectangle((X0, Y0 + 24, X0 + PW, Y0 + 44), fill=BAR)
    for i, c in enumerate([(224, 91, 91), (240, 182, 64), (91, 192, 106)]):
        d.ellipse((X0 + 22 + i * 22, Y0 + 16, X0 + 34 + i * 22, Y0 + 28), fill=c)
    d.text((X0 + 110, Y0 + 12), "Positron  |  에이전트가 R 세션에서 실행", font=f_small, fill=MUTED)

    y = TOP
    last = None
    for start, kind, text, cps in EV:
        if t < start:
            break
        n = len(text) if cps is None else min(len(text), int((t - start) * cps))
        shown = text[:n]
        f = font_for(kind)
        if kind in ("err", "ok"):
            w = d.textlength(text, font=f)
            d.rounded_rectangle((LINE_X - 10, y - 3, LINE_X + w + 14, y + 24), radius=7,
                                fill=ERRBG if kind == "err" else OKBG)
        if kind in ("code", "comment"):
            d.rectangle((LINE_X - 10, y - 3, X0 + PW - 30, y + 24), fill=CODEBG)
        if kind == "agent":
            d.rounded_rectangle((LINE_X - 10, y + 2, LINE_X - 4, y + 26), radius=3, fill=BLUE)
            d.text((LINE_X + 6, y), shown, font=f, fill=color_for(kind))
        else:
            d.text((LINE_X, y), shown, font=f, fill=color_for(kind))
        last = (kind, y, d.textlength(shown, font=f), n < len(text))
        y += height_for(kind)
    if last and last[3] and int(t * 4) % 2 == 0:
        kind, ly, lw, _ = last
        x = LINE_X + (6 if kind == "agent" else 0) + lw + 3
        d.rectangle((x, ly + 2, x + 10, ly + 24), fill=BLUE)

    if t >= CAPTION_AT:
        a = min(1.0, (t - CAPTION_AT) / 0.6)
        al = int(255 * a)
        cy = Y0 + PH + 18
        ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        od = ImageDraw.Draw(ov)
        od.rounded_rectangle((60, cy, 700, cy + 92), radius=18, fill=(255, 255, 255, al), outline=(217, 222, 231, al))
        od.rectangle((60, cy + 14, 66, cy + 78), fill=BLUE + (al,))
        od.text((86, cy + 14), "에이전트가 한 일", font=f_cap, fill=BLUE + (al,))
        od.text((86, cy + 52), "불가능한 값(전부 0%) 확인, 자료형 점검 후 수정", font=f_cap2, fill=INK + (al,))
        od.rounded_rectangle((720, cy, W - 60, cy + 92), radius=18, fill=(255, 247, 237, al), outline=(240, 196, 138, al))
        od.rectangle((720, cy + 14, 726, cy + 78), fill=ORANGE + (al,))
        od.text((746, cy + 14), "연구자의 몫", font=f_cap, fill=(180, 83, 9, al))
        od.text((746, cy + 52), "자명한 오류는 에이전트가, 그럴듯한 오류는 사람이", font=f_cap2, fill=INK + (al,))
        im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    return im


frames = [frame(i / FPS) for i in range(int(DUR * FPS))]
out, durs = [], []
for fr in frames:
    if out and fr.tobytes() == out[-1].tobytes():
        durs[-1] += 1000 // FPS
    else:
        out.append(fr)
        durs.append(1000 // FPS)
pal = frames[-1].quantize(colors=128, method=Image.Quantize.MEDIANCUT)
q = [f.quantize(palette=pal, dither=Image.Dither.NONE) for f in out]
q[0].save(OUT, save_all=True, append_images=q[1:], duration=durs, loop=0, optimize=True, disposal=1)
if PREVIEW_DIR:
    for t in (2.0, 6.5, 12.0, 19.9):
        frame(t).save(os.path.join(PREVIEW_DIR, f"d1v2_t{t}.png"))
print(OUT, len(q), "frames", sum(durs) / 1000, "s", os.path.getsize(OUT) // 1024, "KB")
