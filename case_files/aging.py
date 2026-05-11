"""Shared aging-effects library for ME case file PDF generation."""
import math, random
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color
from reportlab.lib.units import inch

W, H = letter

PAPER_BG  = Color(0.960, 0.938, 0.862)
GRAIN_CLR = Color(0.700, 0.580, 0.400)
COFFEE_D  = Color(0.400, 0.230, 0.080)
COFFEE_L  = Color(0.560, 0.380, 0.180)
CREASE_D  = Color(0.280, 0.200, 0.100)
CREASE_H  = Color(0.990, 0.970, 0.920)
FOXING    = Color(0.580, 0.420, 0.260)
STAMP_R   = Color(0.720, 0.100, 0.080)
STAMP_B   = Color(0.100, 0.150, 0.600)
HW_BLUE   = Color(0.180, 0.200, 0.680)
HW_PENCIL = Color(0.250, 0.240, 0.230)
TEXT_CLR  = Color(0.075, 0.075, 0.075)
HDR_BG    = Color(0.860, 0.838, 0.780)
ROW1_BG   = Color(0.960, 0.940, 0.880)
ROW2_BG   = Color(0.940, 0.918, 0.858)
GRID_CLR  = Color(0.400, 0.360, 0.300)


def aged_bg(c, seed=42):
    c.saveState()
    c.setFillColor(PAPER_BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    for i in range(0, int(H), 45):
        a = 0.012 + 0.009 * abs(math.sin(i / 190.0 + seed * 0.01))
        c.setFillColor(Color(0.60, 0.50, 0.35, alpha=a))
        c.rect(0, i, W, 45, fill=1, stroke=0)
    rng = random.Random(seed)
    for _ in range(700):
        x = rng.uniform(0, W); y = rng.uniform(0, H)
        sz = rng.uniform(0.3, 2.0)
        a  = rng.uniform(0.008, 0.055)
        c.setFillColor(Color(GRAIN_CLR.red, GRAIN_CLR.green, GRAIN_CLR.blue, alpha=a))
        c.circle(x, y, sz, fill=1, stroke=0)
    for ew, a in [(50, 0.040), (30, 0.030), (15, 0.025)]:
        c.setFillColor(Color(0.38, 0.28, 0.18, alpha=a))
        c.rect(0, H-ew, W, ew, fill=1, stroke=0)
        c.rect(0, 0,    W, ew, fill=1, stroke=0)
        c.rect(0, 0,    ew, H, fill=1, stroke=0)
        c.rect(W-ew, 0, ew, H, fill=1, stroke=0)
    c.restoreState()


def coffee_ring(c, cx, cy, r, seed=1, op=0.22, ry=None):
    if ry is None: ry = r
    c.saveState()
    rng = random.Random(seed)
    for sc in [0.88, 0.68, 0.48, 0.28]:
        a = 0.022 + rng.uniform(-0.004, 0.004)
        c.setFillColor(Color(COFFEE_L.red, COFFEE_L.green, COFFEE_L.blue, alpha=a))
        c.ellipse(cx-r*sc, cy-ry*sc, cx+r*sc, cy+ry*sc, fill=1, stroke=0)
    for rw, a in [(r*0.20, op*0.55), (r*0.13, op*0.80), (r*0.07, op*0.55)]:
        c.setStrokeColor(Color(COFFEE_D.red, COFFEE_D.green, COFFEE_D.blue, alpha=a))
        c.setLineWidth(rw)
        c.ellipse(cx-r, cy-ry, cx+r, cy+ry, fill=0, stroke=1)
    for _ in range(30):
        ang = rng.uniform(0, 2*math.pi)
        d   = rng.uniform(r*0.80, r*1.20)
        dx  = cx + d*math.cos(ang)
        dy  = cy + (ry/r)*d*math.sin(ang)
        sz  = rng.uniform(0.4, 3.5)
        a   = rng.uniform(0.07, 0.30)
        c.setFillColor(Color(COFFEE_D.red, COFFEE_D.green, COFFEE_D.blue, alpha=a))
        c.circle(dx, dy, sz, fill=1, stroke=0)
    c.restoreState()


def crease(c, x1, y1, x2, y2, seed=1, inten=1.0):
    c.saveState()
    rng = random.Random(seed)
    dx, dy = x2-x1, y2-y1
    ln = math.sqrt(dx*dx+dy*dy) or 1
    nx, ny = -dy/ln*2, dx/ln*2
    mx = (x1+x2)/2 + rng.uniform(-10, 10)
    my = (y1+y2)/2 + rng.uniform(-10, 10)
    c.setStrokeColor(Color(CREASE_D.red, CREASE_D.green, CREASE_D.blue, alpha=0.11*inten))
    c.setLineWidth(2.5)
    c.bezier(x1, y1, mx-dx*0.1, my, mx+dx*0.1, my, x2, y2)
    c.setStrokeColor(Color(CREASE_D.red, CREASE_D.green, CREASE_D.blue, alpha=0.07*inten))
    c.setLineWidth(4.5)
    c.bezier(x1, y1, mx-dx*0.1, my, mx+dx*0.1, my, x2, y2)
    c.setStrokeColor(Color(CREASE_H.red, CREASE_H.green, CREASE_H.blue, alpha=0.22*inten))
    c.setLineWidth(0.8)
    c.bezier(x1+nx, y1+ny, mx-dx*0.1+nx, my+ny, mx+dx*0.1+nx, my+ny, x2+nx, y2+ny)
    c.restoreState()


def foxing(c, seed=42, count=40, inten=1.0):
    c.saveState()
    rng = random.Random(seed)
    for _ in range(count):
        x = rng.uniform(0.04*W, 0.96*W); y = rng.uniform(0.04*H, 0.96*H)
        r = rng.uniform(0.8, 5.5)
        a = rng.uniform(0.03, 0.17)*inten
        c.setFillColor(Color(FOXING.red, FOXING.green, FOXING.blue, alpha=a))
        c.circle(x, y, r, fill=1, stroke=0)
        c.circle(x+rng.uniform(-r*0.6, r*0.6), y+rng.uniform(-r*0.6, r*0.6),
                 r*0.6, fill=1, stroke=0)
    c.restoreState()


def staple_marks(c):
    c.saveState()
    bx = 0.72*inch; by = H - 0.52*inch
    for oy in [0, -0.28*inch]:
        sx, sy = bx, by+oy
        c.setFillColor(Color(0.55, 0.35, 0.18, alpha=0.13))
        c.ellipse(sx-5, sy-8, sx+0.30*inch+5, sy+0.05*inch+8, fill=1, stroke=0)
        c.setFillColor(Color(0.22, 0.20, 0.18))
        c.rect(sx, sy, 0.28*inch, 0.038*inch, fill=1, stroke=0)
        c.setFillColor(Color(0.30, 0.25, 0.18, alpha=0.20))
        c.rect(sx+1.5, sy-2, 0.28*inch, 0.038*inch, fill=1, stroke=0)
    c.restoreState()


def rubber_stamp(c, text, x, y, angle=0, clr=None, fsize=18, op=0.62):
    if clr is None: clr = STAMP_R
    c.saveState()
    c.translate(x, y); c.rotate(angle)
    c.setFont('Helvetica-Bold', fsize)
    tw = c.stringWidth(text, 'Helvetica-Bold', fsize)
    px, py = 7, 4; bw, bh = tw+2*px, fsize+2*py
    sc = Color(clr.red, clr.green, clr.blue, alpha=op)
    c.setStrokeColor(sc); c.setFillColor(Color(1,1,1,alpha=0))
    c.setLineWidth(2.2); c.rect(-px, -py, bw, bh, fill=0, stroke=1)
    c.setLineWidth(1.0); c.rect(-px-2, -py-2, bw+4, bh+4, fill=0, stroke=1)
    c.setFillColor(sc); c.drawString(0, 0, text)
    c.restoreState()


def hw_note(c, text, x, y, angle=0, clr=None, fsize=8.5):
    if clr is None: clr = HW_BLUE
    c.saveState()
    c.translate(x, y); c.rotate(angle)
    c.setFillColor(Color(clr.red, clr.green, clr.blue, alpha=0.78))
    c.setFont('Helvetica', fsize); c.drawString(0, 0, text)
    c.restoreState()


def smudge(c, x, y, w=60, h=20, seed=1, op=0.07):
    c.saveState()
    rng = random.Random(seed)
    for _ in range(10):
        ox = x+rng.uniform(-w*0.4, w*0.4); oy = y+rng.uniform(-h*0.4, h*0.4)
        ew = rng.uniform(w*0.3, w);         eh = rng.uniform(h*0.3, h*0.7)
        a  = rng.uniform(0.01, op)
        c.setFillColor(Color(0.18, 0.14, 0.10, alpha=a))
        c.ellipse(ox-ew/2, oy-eh/2, ox+ew/2, oy+eh/2, fill=1, stroke=0)
    c.restoreState()


def make_onpage(doc_seed, doc_name, total_pages, aging):
    """Returns onPage/onLaterPages callback for SimpleDocTemplate."""
    def on_page(c, doc):
        pn = doc.page
        pcfg = aging.get(pn, aging.get('default', {}))
        ps   = doc_seed + pn * 43
        aged_bg(c, seed=ps)
        for cr in pcfg.get('rings',   []): coffee_ring(c, *cr)
        for cr in pcfg.get('creases', []): crease(c, *cr)
        fc = pcfg.get('foxing', {'count': 38, 'inten': 0.85})
        foxing(c, seed=ps+111, count=fc['count'], inten=fc['inten'])
        if pn == 1 and aging.get('staple', True): staple_marks(c)
        for st in pcfg.get('stamps', []): rubber_stamp(c, *st)
        for hn in pcfg.get('hw',     []): hw_note(c, *hn)
        for sm in pcfg.get('smudges',[]): smudge(c, *sm)
        # Footer rule + text
        c.saveState()
        c.setFont('Courier', 7.5)
        c.setFillColor(Color(0.35, 0.30, 0.25))
        ft = (f"Minnehaha County Office of the Medical Examiner  |  Case 2015-ME-0447  |  "
              f"{doc_name}  |  Page {pn} of {total_pages}  |  PRELIMINARY — CAUSE/MANNER DEFERRED")
        c.drawCentredString(W/2, 0.40*inch, ft)
        c.setStrokeColor(Color(0.45, 0.40, 0.35, alpha=0.45))
        c.setLineWidth(0.5)
        c.line(0.78*inch, 0.53*inch, W-0.78*inch, 0.53*inch)
        c.restoreState()
    return on_page
