"""
ME Case 2015-ME-0447 — Crime Scene Diagram (Floor Plan of Suite 712)
Generates a hand-sketch-style overhead floor plan as a PDF.
"""

import os, math, random
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import Color
from reportlab.pdfgen.canvas import Canvas

OUT = os.path.join(os.path.dirname(__file__), "photos")
os.makedirs(OUT, exist_ok=True)

W, H  = letter
PAPER = Color(0.960, 0.938, 0.862)
INK   = Color(0.08,  0.08,  0.10)
DIM_C = Color(0.35,  0.32,  0.28)
RED   = Color(0.72,  0.10,  0.08)
BLUE  = Color(0.10,  0.15,  0.60)
GRID  = Color(0.75,  0.72,  0.65)


def aged_bg(c, seed=77):
    rng = random.Random(seed)
    c.saveState()
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    for i in range(0, int(H), 50):
        a = 0.010 + 0.008 * abs(math.sin(i/180.0))
        c.setFillColor(Color(0.60, 0.50, 0.35, alpha=a))
        c.rect(0, i, W, 50, fill=1, stroke=0)
    for _ in range(500):
        x = rng.uniform(0, W); y = rng.uniform(0, H)
        sz = rng.uniform(0.3, 1.8); a = rng.uniform(0.008, 0.05)
        c.setFillColor(Color(0.70, 0.58, 0.40, alpha=a))
        c.circle(x, y, sz, fill=1, stroke=0)
    for ew, a in [(40,0.035),(20,0.025),(10,0.02)]:
        c.setFillColor(Color(0.38, 0.28, 0.18, alpha=a))
        c.rect(0, H-ew, W, ew, fill=1, stroke=0)
        c.rect(0, 0, W, ew, fill=1, stroke=0)
        c.rect(0, 0, ew, H, fill=1, stroke=0)
        c.rect(W-ew, 0, ew, H, fill=1, stroke=0)
    c.restoreState()


def sketchy_rect(c, x, y, w, h, lw=1.2, passes=2, rng=None, fill=None):
    """Draw a rectangle with a hand-sketched, slightly wobbly line."""
    if rng is None: rng = random.Random()
    if fill:
        c.saveState()
        c.setFillColor(fill)
        c.rect(x, y, w, h, fill=1, stroke=0)
        c.restoreState()
    c.saveState()
    c.setStrokeColor(INK)
    c.setLineWidth(lw)
    c.setLineCap(1)
    for _ in range(passes):
        wobble = lw * 0.6
        def wp(): return rng.uniform(-wobble, wobble)
        c.lines([
            (x+wp(), y+wp(), x+w+wp(), y+wp()),
            (x+w+wp(), y+wp(), x+w+wp(), y+h+wp()),
            (x+w+wp(), y+h+wp(), x+wp(), y+h+wp()),
            (x+wp(), y+h+wp(), x+wp(), y+wp()),
        ])
    c.restoreState()


def sketchy_line(c, x1, y1, x2, y2, lw=0.9, rng=None):
    if rng is None: rng = random.Random()
    c.saveState()
    c.setStrokeColor(INK)
    c.setLineWidth(lw)
    c.setLineCap(1)
    w = lw * 0.5
    def wp(): return rng.uniform(-w, w)
    mx = (x1+x2)/2 + rng.uniform(-4,4)
    my = (y1+y2)/2 + rng.uniform(-4,4)
    c.bezier(x1+wp(), y1+wp(), mx, my, mx, my, x2+wp(), y2+wp())
    c.restoreState()


def label(c, x, y, text, size=7.5, bold=False, color=None, angle=0):
    c.saveState()
    if color: c.setFillColor(color)
    else:     c.setFillColor(INK)
    c.translate(x, y)
    if angle: c.rotate(angle)
    font = 'Courier-Bold' if bold else 'Courier'
    c.setFont(font, size)
    c.drawCentredString(0, 0, text)
    c.restoreState()


def dim_line(c, x1, y1, x2, y2, dim_text, offset=10, rng=None):
    """Draw a dimension line with text."""
    if rng is None: rng = random.Random()
    c.saveState()
    c.setStrokeColor(DIM_C)
    c.setFillColor(DIM_C)
    c.setLineWidth(0.6)
    # offset perpendicular
    dx, dy = x2-x1, y2-y1
    ln = math.sqrt(dx*dx+dy*dy) or 1
    nx, ny = -dy/ln*offset, dx/ln*offset
    # dim line
    c.line(x1+nx, y1+ny, x2+nx, y2+ny)
    # tick marks
    for px, py in [(x1,y1),(x2,y2)]:
        c.line(px+nx-dx/ln*4, py+ny-dy/ln*4,
               px+nx+dx/ln*4, py+ny+dy/ln*4)
    # text
    mid_x = (x1+x2)/2 + nx
    mid_y = (y1+y2)/2 + ny
    ang = math.degrees(math.atan2(dy, dx))
    c.translate(mid_x, mid_y)
    c.rotate(ang)
    c.setFont('Courier', 6.5)
    c.drawCentredString(0, 3, dim_text)
    c.restoreState()


def north_arrow(c, x, y, size=28):
    c.saveState()
    c.translate(x, y)
    c.setStrokeColor(INK)
    c.setFillColor(INK)
    c.setLineWidth(1.0)
    # Arrow shaft
    c.line(0, -size//2, 0, size//2)
    # Arrowhead
    p = c.beginPath()
    p.moveTo(0, size//2)
    p.lineTo(-6, size//2-14)
    p.lineTo(6,  size//2-14)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.setFont('Courier-Bold', 9)
    c.drawCentredString(0, size//2+6, 'N')
    c.restoreState()


def evidence_marker(c, x, y, letter, rng):
    """Draw a circled letter evidence marker."""
    c.saveState()
    r = 9
    # Drop shadow
    c.setFillColor(Color(0.3,0.3,0.3,alpha=0.25))
    c.circle(x+1.5, y-1.5, r, fill=1, stroke=0)
    # Circle
    c.setFillColor(Color(0.92, 0.90, 0.82))
    c.setStrokeColor(RED)
    c.setLineWidth(1.2)
    c.circle(x, y, r, fill=1, stroke=1)
    # Letter
    c.setFillColor(RED)
    c.setFont('Courier-Bold', 9)
    c.drawCentredString(x, y-3, letter)
    c.restoreState()


def body_marker(c, x, y):
    """Draw a body position indicator (X with dashed outline ellipse)."""
    c.saveState()
    # Dashed outline
    c.setStrokeColor(RED)
    c.setLineWidth(0.8)
    c.setDash([3,3])
    c.ellipse(x-18, y-28, x+18, y+10, fill=0, stroke=1)
    c.setDash([])
    # X mark
    c.setLineWidth(1.4)
    c.line(x-8, y-18, x+8, y-2)
    c.line(x+8, y-18, x-8, y-2)
    # Label
    c.setFillColor(RED)
    c.setFont('Courier-Bold', 7)
    c.drawCentredString(x, y+14, 'DECEDENT')
    c.drawCentredString(x, y+22, 'POSITION')
    c.restoreState()


def build():
    path = os.path.join(OUT, "ME-0447-SD-01-Scene-Diagram.pdf")
    c = Canvas(path, pagesize=letter)

    rng = random.Random(712)
    aged_bg(c, seed=712)

    # ── Title Block ──────────────────────────────────────────────────────
    c.saveState()
    c.setFillColor(INK)
    c.setFont('Courier-Bold', 11)
    c.drawCentredString(W/2, H - 0.50*inch, 'CRIME SCENE DIAGRAM — SUITE 712')
    c.setFont('Courier', 8.5)
    c.drawCentredString(W/2, H - 0.68*inch,
        '4200 S. Western Ave., 7th Floor (SW Corner)  |  Sioux Falls, SD 57105')
    c.setFont('Courier', 8)
    c.drawCentredString(W/2, H - 0.84*inch,
        'Case 2015-ME-0447  |  MARSH, Eleanor Anne  |  Scene Date: 10/13–14/2015')
    c.setFont('Courier', 7.5)
    c.drawCentredString(W/2, H - 0.99*inch,
        'Diagram prepared by: S.L. Kowalczyk, MEI-09  |  Reviewed: Det. M.J. Orre, SFPD')
    c.setFont('Courier-Bold', 7)
    c.setFillColor(RED)
    c.drawCentredString(W/2, H - 1.13*inch,
        'PRELIMINARY — NOT TO SCALE — FOR INVESTIGATIVE USE ONLY')
    c.restoreState()

    # Title underline
    c.saveState()
    c.setStrokeColor(INK)
    c.setLineWidth(0.8)
    c.line(0.75*inch, H-1.20*inch, W-0.75*inch, H-1.20*inch)
    c.restoreState()

    # ── Room layout: scale: 1 inch = 3 feet  →  18×15 ft room ──────────
    # Room origin (bottom-left of diagram)
    scale    = inch            # 1 inch = 1 "unit" (we'll use feet-ish)
    room_w   = 6.0 * inch     # 18 ft wide → 6 in
    room_h   = 5.0 * inch     # 15 ft deep → 5 in
    orig_x   = (W - room_w) / 2 - 0.2*inch
    orig_y   = 1.50 * inch

    room_fill = Color(0.96, 0.94, 0.88)

    # Outer building wall (thick)
    c.saveState()
    c.setStrokeColor(INK)
    c.setFillColor(Color(0.82, 0.78, 0.72))
    c.setLineWidth(2.5)
    c.rect(orig_x-8, orig_y-8, room_w+16, room_h+16, fill=1, stroke=1)
    c.restoreState()

    # Interior floor
    sketchy_rect(c, orig_x, orig_y, room_w, room_h, lw=1.6, passes=2, rng=rng,
                 fill=room_fill)

    # South wall (windows) — bottom of diagram (rooms faces south = bottom)
    # Mark window openings on south wall (bottom wall)
    win_margin = 0.4*inch
    win_w      = 1.3*inch
    win_y      = orig_y - 8
    for wx in [orig_x + win_margin, orig_x + room_w - win_margin - win_w]:
        c.saveState()
        c.setFillColor(Color(0.72, 0.80, 0.88))
        c.setStrokeColor(Color(0.40,0.42,0.50))
        c.setLineWidth(0.8)
        c.rect(wx, win_y, win_w, 16, fill=1, stroke=1)
        c.setFillColor(INK)
        c.setFont('Courier', 5.5)
        c.drawCentredString(wx + win_w/2, win_y+4, 'WIN.')
        c.restoreState()

    # Label south wall
    label(c, orig_x + room_w/2, orig_y - 22, '← SOUTH WALL / WINDOWS →', 7, color=DIM_C)
    label(c, orig_x + room_w/2, orig_y - 32, '(floor-to-ceiling glass, blinds open at discovery)', 6.5, color=DIM_C)

    # North wall — top — entry door
    door_x   = orig_x + room_w/2 - 0.45*inch
    door_w   = 0.90*inch
    door_y   = orig_y + room_h
    c.saveState()
    c.setFillColor(room_fill)
    c.setStrokeColor(room_fill)
    c.rect(door_x, door_y-1, door_w, 18, fill=1, stroke=0)
    c.setStrokeColor(INK)
    c.setLineWidth(0.7)
    c.line(door_x, door_y+8, door_x, door_y+16)
    c.line(door_x+door_w, door_y+8, door_x+door_w, door_y+16)
    # Door swing arc
    c.setDash([3,3])
    c.arc(door_x, door_y - door_w + 8, door_x + 2*door_w, door_y + 8,
          startAng=90, extent=90)
    c.setDash([])
    c.setFillColor(INK)
    c.setFont('Courier', 6.5)
    c.drawCentredString(door_x+door_w/2, door_y+20, 'ENTRY DOOR')
    c.drawCentredString(door_x+door_w/2, door_y+28, '(open at discovery)')
    c.restoreState()

    # ── FURNITURE ────────────────────────────────────────────────────────

    # Main executive desk (center, facing north — occupant faces N/toward door)
    # Desk: ~6ft wide × 3ft deep (2in × 1in at scale)
    dk_w  = 2.0*inch
    dk_h  = 1.0*inch
    dk_x  = orig_x + room_w/2 - dk_w/2
    dk_y  = orig_y + 1.6*inch
    sketchy_rect(c, dk_x, dk_y, dk_w, dk_h, lw=1.2, passes=2, rng=rng,
                 fill=Color(0.88,0.82,0.74))
    label(c, dk_x+dk_w/2, dk_y+dk_h/2-3, 'EXEC. DESK', 6.5, bold=True)

    # Credenza behind desk (against south wall approx)
    cr_w  = 2.5*inch
    cr_h  = 0.5*inch
    cr_x  = orig_x + room_w/2 - cr_w/2
    cr_y  = orig_y + 0.55*inch
    sketchy_rect(c, cr_x, cr_y, cr_w, cr_h, lw=1.0, passes=2, rng=rng,
                 fill=Color(0.84,0.78,0.68))
    label(c, cr_x+cr_w/2, cr_y+cr_h/2-3, 'CREDENZA', 6.5, bold=True)

    # Chair position (south side of desk — occupant faces N)
    ch_cx = dk_x + dk_w/2 + 0.18*inch   # slightly right of center (chair had rotated)
    ch_cy = dk_y + dk_h/2
    c.saveState()
    c.setFillColor(Color(0.78,0.72,0.64))
    c.setStrokeColor(INK)
    c.setLineWidth(0.8)
    c.circle(ch_cx, ch_cy-0.12*inch, 0.28*inch, fill=1, stroke=1)
    c.setFont('Courier', 5.5)
    c.setFillColor(INK)
    c.drawCentredString(ch_cx, ch_cy-0.12*inch-3, 'CHAIR')
    c.drawCentredString(ch_cx, ch_cy-0.12*inch-10, '(rotated ~15° E)')
    c.restoreState()

    # Conference table (east side)
    ct_w  = 1.8*inch
    ct_h  = 0.8*inch
    ct_x  = orig_x + room_w - 2.0*inch
    ct_y  = orig_y + 2.2*inch
    sketchy_rect(c, ct_x, ct_y, ct_w, ct_h, lw=1.0, passes=2, rng=rng,
                 fill=Color(0.86,0.80,0.70))
    label(c, ct_x+ct_w/2, ct_y+ct_h/2-3, 'CONF. TABLE', 6)
    label(c, ct_x+ct_w/2, ct_y+ct_h/2+6, '(6 chairs)', 5.5)
    # 6 chair circles
    for ci in range(3):
        c.saveState()
        c.setFillColor(Color(0.82,0.76,0.66))
        c.setStrokeColor(INK)
        c.setLineWidth(0.5)
        cy1 = ct_y + (ci+0.5)*(ct_h/3)
        c.circle(ct_x-0.22*inch, cy1, 0.14*inch, fill=1, stroke=1)  # left side
        c.circle(ct_x+ct_w+0.22*inch, cy1, 0.14*inch, fill=1, stroke=1)  # right side
        c.restoreState()

    # Lateral filing cabinet (antechamber / west side, near north wall)
    fc_w  = 0.6*inch
    fc_h  = 0.4*inch
    fc_x  = orig_x + 0.20*inch
    fc_y  = orig_y + room_h - 0.65*inch
    sketchy_rect(c, fc_x, fc_y, fc_w, fc_h, lw=0.9, passes=2, rng=rng,
                 fill=Color(0.80,0.76,0.70))
    label(c, fc_x+fc_w/2, fc_y+fc_h/2-3, 'FILE CAB.', 5.5)

    # Secondary workstation (antechamber)
    sw_w  = 0.8*inch
    sw_h  = 0.4*inch
    sw_x  = orig_x + 0.15*inch
    sw_y  = orig_y + room_h - 1.25*inch
    sketchy_rect(c, sw_x, sw_y, sw_w, sw_h, lw=0.9, passes=2, rng=rng,
                 fill=Color(0.82,0.78,0.68))
    label(c, sw_x+sw_w/2, sw_y+sw_h/2-3, 'ASST.', 5.5)
    label(c, sw_x+sw_w/2, sw_y+sw_h/2+6, 'DESK', 5.5)

    # Antechamber dividing line (dotted — open doorway)
    c.saveState()
    c.setStrokeColor(DIM_C)
    c.setLineWidth(0.7)
    c.setDash([4,4])
    c.line(orig_x + 1.4*inch, orig_y+room_h, orig_x + 1.4*inch, orig_y+room_h - 1.5*inch)
    c.setDash([])
    c.setFont('Courier', 5.5)
    c.setFillColor(DIM_C)
    c.drawCentredString(orig_x + 0.70*inch, orig_y + room_h - 1.60*inch, 'ANTE-')
    c.drawCentredString(orig_x + 0.70*inch, orig_y + room_h - 1.72*inch, 'CHAMBER')
    c.restoreState()

    # ── BODY POSITION ─────────────────────────────────────────────────────
    body_marker(c, ch_cx, ch_cy - 0.20*inch)

    # ── EVIDENCE MARKERS ─────────────────────────────────────────────────
    # A: Laptop on desk
    evidence_marker(c, dk_x + 0.55*inch, dk_y + dk_h - 0.18*inch, 'A', rng)
    # B: Coffee mug and notepad
    evidence_marker(c, dk_x + 0.22*inch, dk_y + dk_h - 0.20*inch, 'B', rng)
    # C: Purse (credenza post)
    evidence_marker(c, cr_x + cr_w - 0.15*inch, cr_y + cr_h + 0.12*inch, 'C', rng)
    # D: Notepad w/ pen
    evidence_marker(c, dk_x + dk_w - 0.22*inch, dk_y + dk_h - 0.18*inch, 'D', rng)
    # E: Phone handset
    evidence_marker(c, dk_x + dk_w - 0.12*inch, dk_y + 0.20*inch, 'E', rng)

    # ── DIMENSION LINES ───────────────────────────────────────────────────
    dim_line(c, orig_x, orig_y, orig_x+room_w, orig_y, "18 ft (approx.)",
             offset=-22, rng=rng)
    dim_line(c, orig_x+room_w, orig_y, orig_x+room_w, orig_y+room_h, "15 ft (approx.)",
             offset=28, rng=rng)

    # ── NORTH ARROW ──────────────────────────────────────────────────────
    north_arrow(c, orig_x + room_w + 0.90*inch, orig_y + room_h/2, size=30)
    label(c, orig_x + room_w + 0.90*inch, orig_y + room_h/2 - 0.55*inch,
          '(building N)', 6, color=DIM_C)

    # ── SCALE BAR ─────────────────────────────────────────────────────────
    sb_x  = orig_x
    sb_y  = orig_y - 0.60*inch
    sb_len = 1.0*inch   # = 3 ft
    c.saveState()
    c.setStrokeColor(INK)
    c.setFillColor(INK)
    c.setLineWidth(1.0)
    c.line(sb_x, sb_y, sb_x+sb_len, sb_y)
    c.line(sb_x, sb_y-4, sb_x, sb_y+4)
    c.line(sb_x+sb_len, sb_y-4, sb_x+sb_len, sb_y+4)
    c.setFont('Courier', 6.5)
    c.drawCentredString(sb_x + sb_len/2, sb_y + 6, '3 FEET (approx.)')
    c.drawCentredString(sb_x + sb_len/2, sb_y - 12, 'NOT TO SCALE — INVESTIGATIVE REFERENCE ONLY')
    c.restoreState()

    # ── LEGEND ────────────────────────────────────────────────────────────
    leg_x = orig_x
    leg_y = 1.25*inch
    c.saveState()
    c.setFont('Courier-Bold', 7.5)
    c.setFillColor(INK)
    c.drawString(leg_x, leg_y, 'EVIDENCE MARKERS:')
    items = [
        ('A', 'Laptop computer (company-issued; SFPD hold)'),
        ('B', 'Coffee mug on coaster; adjacent notepad w/ pen'),
        ('C', 'Decedent purse (ME hold) — hanging credenza post'),
        ('D', 'Legal notepad w/ handwritten notes (SFPD hold)'),
        ('E', 'Telephone handset — desk surface, right side'),
    ]
    c.setFont('Courier', 7)
    for i, (ltr, desc) in enumerate(items):
        iy = leg_y - 10 - i*11
        # Mini marker
        c.setFillColor(Color(0.92, 0.90, 0.82))
        c.setStrokeColor(RED)
        c.setLineWidth(0.8)
        c.circle(leg_x+6, iy+3, 6, fill=1, stroke=1)
        c.setFillColor(RED)
        c.setFont('Courier-Bold', 6)
        c.drawCentredString(leg_x+6, iy, ltr)
        c.setFillColor(INK)
        c.setFont('Courier', 6.5)
        c.drawString(leg_x+16, iy, desc)
    # Body marker mini legend
    iy2 = leg_y - 10 - len(items)*11
    c.setStrokeColor(RED)
    c.setLineWidth(0.7)
    c.setDash([2,2])
    c.ellipse(leg_x+1, iy2-2, leg_x+13, iy2+10, fill=0, stroke=1)
    c.setDash([])
    c.setLineWidth(0.9)
    c.line(leg_x+3, iy2+8, leg_x+11, iy2+0)
    c.line(leg_x+11, iy2+8, leg_x+3, iy2+0)
    c.setFillColor(INK)
    c.setFont('Courier', 6.5)
    c.drawString(leg_x+16, iy2+2, 'Decedent position at discovery')
    c.restoreState()

    # ── COMPASS CALLOUT NOTE ───────────────────────────────────────────────
    c.saveState()
    c.setFont('Courier', 6.5)
    c.setFillColor(DIM_C)
    notes = [
        'NOTE: Diagram is schematic and approximately to scale based on',
        'investigator field measurements (tape; not survey-grade).',
        'SFPD CSU measurements may differ. Furniture positions are approximate.',
        'Chair position reflects estimated position at time of discovery;',
        'slight rotation from forward-facing noted per DIR Section 3.3.',
        'Building N orientation per building plans provided by management.',
    ]
    for i, note in enumerate(notes):
        c.drawString(orig_x+room_w+0.25*inch, orig_y+room_h - 0.35*inch - i*9, note)
    c.restoreState()

    # ── FOOTER ────────────────────────────────────────────────────────────
    c.saveState()
    c.setFont('Courier', 7)
    c.setFillColor(Color(0.40,0.35,0.30))
    c.drawCentredString(W/2, 0.40*inch,
        "Minnehaha County ME Office  |  Case 2015-ME-0447  |  "
        "Scene Diagram SD-01  |  Page 1 of 1  |  PRELIMINARY")
    c.setStrokeColor(Color(0.45,0.40,0.35,alpha=0.45))
    c.setLineWidth(0.5)
    c.line(0.78*inch, 0.53*inch, W-0.78*inch, 0.53*inch)
    c.restoreState()

    # ── RECEIVED STAMP ────────────────────────────────────────────────────
    c.saveState()
    c.translate(W - 1.60*inch, H - 1.80*inch)
    c.rotate(-9)
    stamp_color = Color(0.10, 0.15, 0.60, alpha=0.55)
    c.setStrokeColor(stamp_color)
    c.setFillColor(Color(1,1,1,alpha=0))
    c.setLineWidth(2.0)
    c.setFont('Helvetica-Bold', 13)
    tw = c.stringWidth("RECEIVED", 'Helvetica-Bold', 13)
    c.rect(-7, -5, tw+14, 23, fill=0, stroke=1)
    c.setLineWidth(0.8)
    c.rect(-9, -7, tw+18, 27, fill=0, stroke=1)
    c.setFillColor(stamp_color)
    c.drawString(0, 0, "RECEIVED")
    c.setFont('Helvetica-Bold', 8)
    c.drawCentredString(tw/2, -13, "SFPD INVESTIGATIONS")
    c.restoreState()

    c.save()
    print(f"  → {path}")


if __name__ == "__main__":
    build()
