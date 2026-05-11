"""
ME Case 2015-ME-0447 — Crime Scene and Evidence Photo Generator
Produces aged polaroid-format PNGs: crime scene (CS) and evidence (EV) series.
All imagery is procedurally drawn — no stock photos used.
"""

import os, math, random
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont

OUT    = os.path.join(os.path.dirname(__file__), "photos")
os.makedirs(OUT, exist_ok=True)

PW, PH  = 660, 820          # full polaroid dims (px)
IW, IH  = 600, 600          # inner photo dims
PAD_L   = 30
PAD_T   = 30
PAD_B   = 190               # wide bottom caption area

MONO    = "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf"
MONO_B  = "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf"
SANS    = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B  = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SERIF   = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"


def fnt(path, size):
    try:    return ImageFont.truetype(path, size)
    except: return ImageFont.load_default()


# ── LOW-LEVEL EFFECTS ─────────────────────────────────────────────────────

def add_grain(img, intensity=18, seed=42):
    rng = random.Random(seed)
    g   = img.convert('RGBA')
    px  = g.load()
    w, h = g.size
    for y in range(h):
        for x in range(w):
            r,gg,b,a = px[x,y]
            n = rng.randint(-intensity, intensity)
            px[x,y] = (max(0,min(255,r+n)), max(0,min(255,gg+n)),
                       max(0,min(255,b+n)), a)
    return g.convert('RGB')


def add_vignette(img, strength=0.55):
    w, h = img.size
    mask = Image.new('L', (w, h), 255)
    md   = ImageDraw.Draw(mask)
    cx, cy = w//2, h//2
    for i in range(min(cx,cy), 0, -1):
        v = int(255 * (i / min(cx,cy)) ** 1.4)
        md.ellipse([(cx-i, cy-i), (cx+i, cy+i)], fill=min(255,v+int((1-strength)*255)))
    mask = mask.filter(ImageFilter.GaussianBlur(radius=min(w,h)//5))
    dark = Image.new('RGB', (w, h), (0,0,0))
    img  = Image.composite(img, dark, mask)
    return img


def add_flash(img, cx=None, cy=None, radius=None, alpha=90):
    """Hot-spot flash effect centered at (cx,cy)."""
    w, h = img.size
    if cx is None: cx = w//2
    if cy is None: cy = h//2
    if radius is None: radius = int(min(w,h)*0.55)
    overlay = Image.new('RGBA', (w, h), (0,0,0,0))
    od      = ImageDraw.Draw(overlay)
    for r in range(radius, 0, -4):
        a = int(alpha * (1 - r/radius) ** 1.8)
        od.ellipse([(cx-r, cy-r), (cx+r, cy+r)], fill=(255,255,240,a))
    return Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')


def radial_glow(draw, cx, cy, r_outer, r_inner, color_inner, color_outer, steps=30):
    """Draw a radial glow effect (desk lamp / light source)."""
    ci = color_inner
    co = color_outer
    for i in range(steps, 0, -1):
        frac = i / steps
        r    = int(r_inner + (r_outer - r_inner) * (1 - frac))
        c    = tuple(int(ci[j] + (co[j]-ci[j]) * (1-frac)) for j in range(3))
        a    = int(ci[3] + (co[3]-ci[3]) * (1-frac)) if len(ci) == 4 else 255
        col  = c + (a,) if len(ci) == 4 else c
        draw.ellipse([(cx-r, cy-r), (cx+r, cy+r)], fill=col)


def draw_desk_texture(draw, x1, y1, x2, y2, rng, base=(58, 44, 32)):
    """Fill a rectangle with dark wood grain texture."""
    draw.rectangle([(x1,y1),(x2,y2)], fill=base)
    for _ in range(40):
        gx1 = rng.randint(x1, x2-1)
        gy1 = rng.randint(y1, y2-1)
        gl  = rng.randint(20, (x2-x1)//2)
        draw.line([(gx1, gy1), (gx1+gl, gy1+rng.randint(-2,2))],
                  fill=(max(0,base[0]-rng.randint(5,15)),
                        max(0,base[1]-rng.randint(3,10)),
                        max(0,base[2]-rng.randint(2,8))),
                  width=1)


def floor_texture(draw, poly, rng, base=(45, 42, 38)):
    """Fill polygon with subtle floor texture."""
    draw.polygon(poly, fill=base)


def window_glow(draw, x1, y1, x2, y2, rng):
    """Draw a window with city-light glow effect."""
    draw.rectangle([(x1,y1),(x2,y2)], fill=(38,48,68))
    # Blinds / horizontal lines
    bh = (y2-y1)//14
    for i in range(14):
        ly = y1 + i*bh
        alpha_val = rng.randint(28,45)
        draw.line([(x1,ly),(x2,ly)], fill=(25,32,48), width=2)
    # Distant light blobs
    for _ in range(5):
        lx = rng.randint(x1+10, x2-10)
        ly = rng.randint(y1+10, y2-10)
        lr = rng.randint(3,9)
        lc = rng.choice([(220,195,120),(200,210,225),(230,200,150)])
        draw.ellipse([(lx-lr,ly-lr),(lx+lr,ly+lr)], fill=lc)
    # Frame
    draw.rectangle([(x1,y1),(x2,y2)], outline=(55,52,44), width=3)
    # Center divider
    draw.line([(x1+(x2-x1)//2, y1),(x1+(x2-x1)//2, y2)], fill=(55,52,44), width=2)
    draw.line([(x1, y1+(y2-y1)//2),(x2, y1+(y2-y1)//2)], fill=(55,52,44), width=2)


# ── RULER / SCALE BAR ────────────────────────────────────────────────────

def draw_scale_ruler(draw, x, y, length=120, label="10 CM"):
    """Draw a yellow-black scale ruler for evidence photos."""
    seg = length // 10
    for i in range(10):
        fill = (240,200,20) if i % 2 == 0 else (20,20,20)
        draw.rectangle([(x+i*seg, y), (x+(i+1)*seg, y+14)], fill=fill)
    draw.rectangle([(x,y),(x+length,y+14)], outline=(180,160,0), width=1)
    f = fnt(MONO, 11)
    draw.text((x+length+5, y+1), label, fill=(220,210,170), font=f)


def draw_evidence_card(draw, x, y, text, rng):
    """Draw a small white evidence identification card."""
    tw = 120; th = 34
    draw.rectangle([(x,y),(x+tw,y+th)], fill=(240,235,215), outline=(180,160,100), width=1)
    f1 = fnt(MONO_B, 10)
    f2 = fnt(MONO, 9)
    draw.text((x+4, y+3), "SFPD CSU / ME", fill=(40,40,40), font=f1)
    draw.text((x+4, y+17), text[:20], fill=(40,40,40), font=f2)


# ── SCENE PHOTOS ──────────────────────────────────────────────────────────

def scene_room_overview(rng):
    """CS-01: Looking south into Suite 712 from entry doorway."""
    img  = Image.new('RGBA', (IW, IH), (18, 16, 22, 255))
    draw = ImageDraw.Draw(img)
    w, h = IW, IH
    vx, vy = w//2, int(h*0.40)

    # Left wall
    draw.polygon([(0,0),(int(w*0.20),0),(vx,vy),(0,h)], fill=(30,27,36,255))
    # Right wall
    draw.polygon([(w,0),(int(w*0.80),0),(vx,vy),(w,h)], fill=(26,24,32,255))
    # Ceiling
    draw.polygon([(int(w*0.20),0),(int(w*0.80),0),(vx,vy)], fill=(20,18,26,255))
    # Floor
    floor_poly = [(0,h),(w,h),(int(w*0.75),vy),(int(w*0.25),vy)]
    floor_texture(draw, floor_poly, rng, base=(42,39,35))
    # Back wall
    draw.polygon([(int(w*0.20),0),(int(w*0.80),0),(int(w*0.75),vy),(int(w*0.25),vy)],
                 fill=(34,31,40,255))

    # Desk lamp glow on ceiling/back wall (before desk)
    radial_glow(draw, int(w*0.28), int(vy+40), 110, 18,
                (195,165,80,90),(18,16,22,0))

    # Windows on back wall (two windows)
    win_y1,win_y2 = int(vy+5), int(vy+h*0.25)
    window_glow(draw, int(w*0.27), win_y1, int(w*0.50), win_y2, rng)
    window_glow(draw, int(w*0.52), win_y1, int(w*0.74), win_y2, rng)

    # Conference table (right side, receding)
    conf_poly = [(int(w*0.62),int(h*0.65)),(int(w*0.95),int(h*0.60)),
                 (int(w*0.90),vy+60),(int(w*0.62),vy+55)]
    draw.polygon(conf_poly, fill=(52,40,30,255))

    # Main desk surface (center, foreground)
    dk_x1,dk_y1 = int(w*0.15), int(h*0.56)
    dk_x2,dk_y2 = int(w*0.68), int(h*0.72)
    top_poly = [(dk_x1,dk_y1),(dk_x2,dk_y1),
                (dk_x2-15,int(vy+60)),(dk_x1+15,int(vy+60))]
    draw.polygon(top_poly, fill=(58,44,32,255))
    draw.rectangle([(dk_x1,dk_y1),(dk_x2,dk_y2)], fill=(44,33,24,255))  # front face

    # Laptop on desk (closed, dark)
    lap = [(int(w*0.22),int(vy+65)),(int(w*0.46),int(vy+65)),
           (int(w*0.45),int(vy+85)),(int(w*0.22),int(vy+85))]
    draw.polygon(lap, fill=(24,24,30,255))

    # Coffee mug
    mug_cx,mug_cy = int(w*0.20), int(vy+72)
    draw.ellipse([(mug_cx-12,mug_cy-12),(mug_cx+12,mug_cy+12)], fill=(58,48,38,255))
    draw.ellipse([(mug_cx-9,mug_cy-9),(mug_cx+9,mug_cy+9)], fill=(42,32,24,255))

    # Desk lamp (left side of desk)
    lamp_x,lamp_y = int(w*0.17), int(vy+30)
    draw.ellipse([(lamp_x-5,lamp_y-18),(lamp_x+5,lamp_y-8)], fill=(200,190,150,255))
    draw.line([(lamp_x,lamp_y-8),(lamp_x-4,lamp_y+22)], fill=(140,130,100,255), width=3)
    radial_glow(draw, lamp_x, lamp_y-12, 80, 10,
                (210,180,80,120),(18,16,22,0))

    # Chair back (visible above desk)
    chair_x = int(w*0.40)
    ch_top  = int(vy+28)
    draw.rounded_rectangle([(chair_x-35,ch_top),(chair_x+35,ch_top+55)],
                           radius=10, fill=(38,36,44,255))

    # Decedent — slumped silhouette suggestion in chair
    # Head (inclined right)
    hx = int(w*0.44); hy = ch_top + 20
    draw.ellipse([(hx-16,hy-20),(hx+16,hy+18)], fill=(62,55,50,255))
    # Hair
    draw.ellipse([(hx-16,hy-20),(hx+16,hy-5)], fill=(35,28,22,255))
    # Shoulder/torso slumped right
    draw.polygon([(chair_x-28,ch_top+55),(chair_x+28,ch_top+55),
                  (hx+18,hy),(hx-18,hy)], fill=(52,46,58,255))

    # Flash hotspot
    img = add_flash(img, cx=int(w*0.5), cy=int(h*0.52), radius=240, alpha=60)
    img = add_grain(img, intensity=22, seed=rng.randint(0,9999))
    img = add_vignette(img, strength=0.65)
    return img.convert('RGB')


def scene_desk_surface(rng):
    """CS-02: Desk surface — looking down at slight angle."""
    img  = Image.new('RGBA', (IW, IH), (52, 40, 28, 255))
    draw = ImageDraw.Draw(img)
    w, h = IW, IH

    # Desk surface fills most of frame (dark wood)
    draw_desk_texture(draw, 0, 0, w, h, rng, base=(55,42,30))

    # Coaster (round, cork-colored)
    cx,cy = int(w*0.22), int(h*0.40)
    draw.ellipse([(cx-28,cy-28),(cx+28,cy+28)], fill=(88,68,42,255))
    draw.ellipse([(cx-24,cy-24),(cx+24,cy+24)], fill=(100,78,50,255))
    # Mug
    draw.ellipse([(cx-20,cy-20),(cx+20,cy+20)], fill=(215,210,200,255))
    draw.ellipse([(cx-15,cy-15),(cx+15,cy+15)], fill=(55,42,32,255))
    # Coffee surface (slightly less dark)
    draw.ellipse([(cx-12,cy-12),(cx+12,cy+12)], fill=(52,36,18,255))

    # Laptop (closed, silver-grey)
    lap_x1,lap_y1 = int(w*0.30), int(h*0.12)
    lap_x2,lap_y2 = int(w*0.90), int(h*0.62)
    draw.rectangle([(lap_x1,lap_y1),(lap_x2,lap_y2)], fill=(36,36,40,255))
    draw.rectangle([(lap_x1+4,lap_y1+4),(lap_x2-4,lap_y2-4)], fill=(28,28,32,255))
    # Apple-like logo dim
    draw.ellipse([(lap_x1+(lap_x2-lap_x1)//2-10,lap_y1+(lap_y2-lap_y1)//2-12),
                  (lap_x1+(lap_x2-lap_x1)//2+10,lap_y1+(lap_y2-lap_y1)//2+12)],
                 fill=(38,38,42,255))

    # Notepad (legal yellow, lower left)
    np_x1,np_y1 = int(w*0.00), int(h*0.55)
    np_x2,np_y2 = int(w*0.28), int(h*0.98)
    draw.rectangle([(np_x1,np_y1),(np_x2,np_y2)], fill=(210,192,120,255))
    draw.rectangle([(np_x1,np_y1),(np_x2,np_y1+22)], fill=(190,170,100,255))
    # Lines on notepad
    f = fnt(MONO, 8)
    for i,line in enumerate(["quarterly rec.", "— variance -2.1M", "3rd Q finalize", "   cross-ref HW", "call back T.W.", "filing ext. ??", "board pkg 10/20"]):
        draw.text((np_x1+6, np_y1+26+i*14), line, fill=(80,60,20,255), font=f)
    # Horizontal rule lines
    for li in range(0,int(h*0.43),14):
        draw.line([(np_x1+2,np_y1+22+li),(np_x2-2,np_y1+22+li)], fill=(180,160,90,255), width=1)
    # Red margin line
    draw.line([(np_x1+30,np_y1),(np_x1+30,np_y2)], fill=(200,80,80,200), width=1)

    # Pen (diagonal, uncapped)
    pen_x1,pen_y1 = int(w*0.03), int(h*0.82)
    pen_x2,pen_y2 = int(w*0.26), int(h*0.94)
    draw.line([(pen_x1,pen_y1),(pen_x2,pen_y2)], fill=(30,30,38,255), width=5)
    draw.line([(pen_x1,pen_y1),(pen_x1+8,pen_y1+14)], fill=(200,195,180,255), width=2)

    # Phone handset (right side)
    ph_x,ph_y = int(w*0.82), int(h*0.80)
    draw.rounded_rectangle([(ph_x-18,ph_y-45),(ph_x+18,ph_y+30)],
                           radius=8, fill=(42,42,48,255))

    # Desk lamp light pool (upper left, warm glow)
    radial_glow(draw, 0, 0, 200, 0,
                (200,165,60,80),(52,40,28,0))

    img = add_flash(img, cx=int(w*0.55), cy=int(h*0.38), radius=280, alpha=55)
    img = add_grain(img, intensity=20, seed=rng.randint(0,9999))
    img = add_vignette(img, strength=0.50)
    return img.convert('RGB')


def scene_decedent_chair(rng):
    """CS-03: Decedent position — chair from NE angle."""
    img  = Image.new('RGBA', (IW, IH), (20, 18, 24, 255))
    draw = ImageDraw.Draw(img)
    w, h = IW, IH

    # Floor
    floor_texture(draw, [(0,int(h*0.62)),(w,int(h*0.62)),(w,h),(0,h)], rng, base=(38,35,32))
    # Wall behind
    draw.rectangle([(0,0),(w,int(h*0.62))], fill=(28,25,34,255))
    # Credenza (behind chair, dark wood)
    draw.rectangle([(int(w*0.52),int(h*0.28)),(w,int(h*0.60))], fill=(48,36,26,255))
    draw.rectangle([(int(w*0.52),int(h*0.28)),(w,int(h*0.31))], fill=(38,28,18,255))
    # Binders on credenza
    binder_colors = [(80,40,40),(40,60,80),(40,80,50),(70,70,35)]
    for i,bc in enumerate(binder_colors):
        bx = int(w*0.54) + i*28
        draw.rectangle([(bx,int(h*0.31)),(bx+24,int(h*0.56))], fill=bc)
        draw.rectangle([(bx,int(h*0.31)),(bx+24,int(h*0.32))], fill=(bc[0]+20,bc[1]+20,bc[2]+20))

    # Desk edge (lower frame)
    draw.rectangle([(0,int(h*0.70)),(int(w*0.55),int(h*0.76))], fill=(55,42,30,255))
    draw.rectangle([(0,int(h*0.68)),(int(w*0.55),int(h*0.70))], fill=(68,52,38,255))

    # Chair (executive chair, seen from NE)
    ch_cx = int(w*0.38)
    # Chair seat
    draw.ellipse([(ch_cx-80,int(h*0.58)),(ch_cx+80,int(h*0.68))], fill=(35,33,42,255))
    # Chair back (tall, padded)
    draw.rounded_rectangle([(ch_cx-62,int(h*0.15)),(ch_cx+62,int(h*0.60))],
                           radius=15, fill=(40,38,48,255))
    # Chair cushion sheen
    draw.ellipse([(ch_cx-48,int(h*0.18)),(ch_cx+48,int(h*0.35))], fill=(48,46,58,255))
    # Arm rests
    draw.rounded_rectangle([(ch_cx-80,int(h*0.44)),(ch_cx-55,int(h*0.58))],
                           radius=6, fill=(32,30,40,255))
    draw.rounded_rectangle([(ch_cx+55,int(h*0.44)),(ch_cx+80,int(h*0.58))],
                           radius=6, fill=(32,30,40,255))

    # Decedent — seated, slumped forward and right
    # Torso / blazer (dark charcoal)
    torso_cx = ch_cx + 18   # shifted right (slumped)
    torso_cy = int(h*0.44)
    draw.ellipse([(torso_cx-45,torso_cy-70),(torso_cx+45,torso_cy+50)],
                 fill=(52,50,58,255))  # blazer body
    # Blouse visible at collar area
    draw.ellipse([(torso_cx-14,torso_cy-72),(torso_cx+14,torso_cy-50)],
                 fill=(210,205,198,255))
    # Right arm on desk (forearm)
    draw.rounded_rectangle([(torso_cx+28,torso_cy-20),(torso_cx+80,torso_cy+8)],
                           radius=8, fill=(52,48,56,255))
    # Hand
    draw.ellipse([(torso_cx+74,torso_cy-18),(torso_cx+96,torso_cy+2)],
                 fill=(175,148,128,255))

    # Head — inclined right, onto right shoulder
    hx = torso_cx + 32; hy = torso_cy - 90
    # Hair
    draw.ellipse([(hx-26,hy-32),(hx+26,hy+18)], fill=(42,32,24,255))
    # Face (partially visible, turned right)
    draw.ellipse([(hx-18,hy-22),(hx+18,hy+16)], fill=(175,148,128,255))
    # Eyes slightly open (not graphic — just suggest)
    draw.line([(hx-8,hy-4),(hx+2,hy-4)], fill=(55,42,35,255), width=2)

    # Left arm in lap
    draw.rounded_rectangle([(torso_cx-65,torso_cy+30),(torso_cx-12,torso_cy+50)],
                           radius=8, fill=(52,48,56,255))

    # Flash from upper right (crime scene camera angle)
    img = add_flash(img, cx=int(w*0.68), cy=int(h*0.22), radius=320, alpha=65)
    img = add_grain(img, intensity=24, seed=rng.randint(0,9999))
    img = add_vignette(img, strength=0.60)
    return img.convert('RGB')


def scene_entry_doorway(rng):
    """CS-04: Suite 712 entry — looking from hallway into antechamber."""
    img  = Image.new('RGBA', (IW, IH), (15, 14, 18, 255))
    draw = ImageDraw.Draw(img)
    w, h = IW, IH

    # Hallway wall (frame photo)
    draw.rectangle([(0,0),(w,h)], fill=(22,20,28,255))
    # Hallway floor stripe
    draw.rectangle([(0,int(h*0.72)),(w,h)], fill=(30,28,32,255))
    # Hallway ceiling
    draw.rectangle([(0,0),(w,int(h*0.08))], fill=(18,16,22,255))

    # Door frame (white/cream)
    fr_x1,fr_y1 = int(w*0.20), int(h*0.06)
    fr_x2,fr_y2 = int(w*0.82), int(h*0.88)
    draw.rectangle([(fr_x1-8,fr_y1-4),(fr_x2+8,fr_y2+4)], fill=(68,65,60,255))  # frame
    draw.rectangle([(fr_x1,fr_y1),(fr_x2,fr_y2)], fill=(20,18,24,255))  # opening

    # Antechamber visible beyond (slightly lighter)
    draw.rectangle([(fr_x1,fr_y1),(fr_x2,fr_y2)], fill=(28,25,34,255))

    # Inner office doorway (inner door) ajar / open
    in_x1,in_y1 = int(w*0.36), int(h*0.14)
    in_x2,in_y2 = int(w*0.72), int(h*0.84)
    draw.rectangle([(in_x1,in_y1),(in_x2,in_y2)], fill=(35,30,42,255))

    # Light from inner office (desk lamp glow bleeding through)
    radial_glow(draw, int(w*0.54), int(h*0.50), 200, 20,
                (200,165,60,80),(28,25,34,0))

    # Door (open, visible edge / shadow)
    door_edge_x = int(w*0.70)
    draw.polygon([(door_edge_x,fr_y1),(door_edge_x+12,fr_y1),
                  (in_x2+8,in_y1),(in_x2,in_y1)], fill=(60,55,48,255))  # door thickness
    draw.polygon([(door_edge_x,fr_y2),(door_edge_x+12,fr_y2),
                  (in_x2+8,in_y2),(in_x2,in_y2)], fill=(50,45,38,255))

    # Antechamber chair (secondary workstation, partially visible)
    draw.rectangle([(fr_x1+8,int(h*0.55)),(fr_x1+60,int(h*0.80))], fill=(32,30,38,255))

    # Filing cabinet (left side of antechamber)
    draw.rectangle([(fr_x1+5,int(h*0.20)),(fr_x1+45,int(h*0.70))], fill=(55,52,48,255))
    for dh in [0.30,0.45,0.60]:
        draw.line([(fr_x1+5,int(h*dh)),(fr_x1+45,int(h*dh))], fill=(42,40,36,255), width=2)
        draw.ellipse([(fr_x1+20,int(h*dh)-4),(fr_x1+30,int(h*dh)+4)], fill=(120,110,90,255))

    # SFPD CRIME SCENE tape suggestion (yellow stripe across bottom)
    tape_y = int(h*0.88)
    draw.rectangle([(0,tape_y),(w,tape_y+18)], fill=(215,195,20,210))
    draw.rectangle([(0,tape_y+4),(w,tape_y+14)], fill=(20,20,20,180))
    f = fnt(SANS_B, 9)
    for tx in range(0, w, 110):
        draw.text((tx+4, tape_y+4), "CRIME SCENE DO NOT CROSS", fill=(215,195,20,255), font=f)

    img = add_flash(img, cx=int(w*0.52), cy=int(h*0.50), radius=260, alpha=55)
    img = add_grain(img, intensity=26, seed=rng.randint(0,9999))
    img = add_vignette(img, strength=0.70)
    return img.convert('RGB')


def scene_desk_lamp(rng):
    """CS-05: Desk lamp and immediate work area detail."""
    img  = Image.new('RGBA', (IW, IH), (22, 18, 14, 255))
    draw = ImageDraw.Draw(img)
    w, h = IW, IH
    draw_desk_texture(draw, 0, int(h*0.28), w, h, rng, base=(52,40,28))

    # Desk lamp base, arm, head
    base_x, base_y = int(w*0.22), int(h*0.80)
    draw.ellipse([(base_x-22,base_y-8),(base_x+22,base_y+8)], fill=(120,115,100,255))
    draw.line([(base_x,base_y-8),(base_x-8,int(h*0.34))], fill=(130,125,108,255), width=5)
    draw.line([(base_x-8,int(h*0.34)),(base_x+40,int(h*0.22))], fill=(130,125,108,255), width=5)
    # Lamp head
    draw.polygon([(base_x+20,int(h*0.18)),(base_x+60,int(h*0.18)),
                  (base_x+72,int(h*0.28)),(base_x+8,int(h*0.28))],
                 fill=(175,165,120,255))
    # Bulb glow
    radial_glow(draw, base_x+40, int(h*0.22), 240, 12,
                (240,210,90,180),(22,18,14,0))

    # Illuminated notepad
    np_x,np_y = int(w*0.28), int(h*0.36)
    draw.rectangle([(np_x,np_y),(np_x+260,np_y+200)], fill=(205,188,115,255))
    draw.rectangle([(np_x,np_y),(np_x+260,np_y+20)], fill=(188,170,100,255))
    f = fnt(MONO, 9)
    lines = ["quarterly rec.", "— variance -2.1M", "3rd Q finalize",
             "   cross-ref HW", "call back T.W.",
             "filing ext. ??", "board pkg 10/20"]
    for i,line in enumerate(lines):
        draw.text((np_x+35, np_y+26+i*14), line, fill=(75,55,18,255), font=f)
    for li in range(0, 182, 14):
        draw.line([(np_x+4,np_y+22+li),(np_x+256,np_y+22+li)], fill=(175,155,85,255), width=1)
    draw.line([(np_x+30,np_y),(np_x+30,np_y+200)], fill=(195,75,75,180), width=1)

    # Pen resting on notepad
    pen_ang = -0.15
    pen_cx = np_x + 130; pen_cy = np_y + 140
    for t in range(-70, 71):
        px = int(pen_cx + t * math.cos(pen_ang))
        py = int(pen_cy + t * math.sin(pen_ang))
        draw.ellipse([(px-3,py-3),(px+3,py+3)], fill=(30,28,36,255))

    # Partial mug (edge of lamp light area)
    mug_x,mug_y = int(w*0.06), int(h*0.50)
    draw.ellipse([(mug_x,mug_y),(mug_x+50,mug_y+60)], fill=(220,215,205,255))
    draw.ellipse([(mug_x+5,mug_y+5),(mug_x+45,mug_y+55)], fill=(45,32,20,255))

    img = add_flash(img, cx=int(w*0.50), cy=int(h*0.45), radius=240, alpha=45)
    img = add_grain(img, intensity=20, seed=rng.randint(0,9999))
    img = add_vignette(img, strength=0.58)
    return img.convert('RGB')


# ── EVIDENCE PHOTOS ───────────────────────────────────────────────────────

def ev_coffee_mug(rng):
    """EV-A: Coffee mug on desk — Item C-7."""
    img  = Image.new('RGBA', (IW, IH), (58, 44, 30, 255))
    draw = ImageDraw.Draw(img)
    w,h  = IW, IH
    draw_desk_texture(draw, 0, 0, w, h, rng, base=(58,44,30))

    # Coaster
    cx,cy = w//2, int(h*0.48)
    draw.ellipse([(cx-52,cy-52),(cx+52,cy+52)], fill=(90,70,44,255))
    draw.ellipse([(cx-46,cy-46),(cx+46,cy+46)], fill=(105,82,55,255))

    # Mug body
    draw.ellipse([(cx-38,cy+20),(cx+38,cy+80)], fill=(215,210,202,255))  # bottom
    draw.rectangle([(cx-38,cy-38),(cx+38,cy+50)], fill=(215,210,202,255))  # body
    draw.ellipse([(cx-38,cy-42),(cx+38,cy-28)], fill=(205,200,192,255))  # rim
    # Coffee surface (top)
    draw.ellipse([(cx-30,cy-42),(cx+30,cy-28)], fill=(40,25,12,255))
    # Handle
    draw.arc([(cx+32,cy-10),(cx+62,cy+28)], start=315, end=135, fill=(200,196,188,255), width=7)

    # Partial coffee ring on desk (adjacent)
    draw.arc([(cx+45,cy+10),(cx+75,cy+40)], start=0, end=360,
             fill=(75,54,30,200), width=3)

    # Evidence markers
    draw_scale_ruler(draw, cx-55, int(h*0.82), 120, "10 CM")
    draw_evidence_card(draw, cx+60, int(h*0.14), "EV-A / C-7", rng)

    # Item number placard
    draw.rectangle([(cx-18,cy-90),(cx+18,cy-68)], fill=(240,235,215,255))
    draw.text((cx-13,cy-88), "EV-A", fill=(40,40,40,255), font=fnt(MONO_B,14))

    img = add_flash(img, cx=cx, cy=cy-20, radius=280, alpha=60)
    img = add_grain(img, intensity=18, seed=rng.randint(0,9999))
    img = add_vignette(img, strength=0.48)
    return img.convert('RGB')


def ev_notepad(rng):
    """EV-B: Legal notepad with pen — desk surface."""
    img  = Image.new('RGBA', (IW, IH), (56, 42, 28, 255))
    draw = ImageDraw.Draw(img)
    w,h  = IW, IH
    draw_desk_texture(draw, 0, 0, w, h, rng, base=(56,42,28))

    nx1,ny1 = int(w*0.15), int(h*0.08)
    nx2,ny2 = int(w*0.85), int(h*0.82)
    draw.rectangle([(nx1,ny1),(nx2,ny2)], fill=(212,195,118,255))
    # Top binding strip
    draw.rectangle([(nx1,ny1),(nx2,ny1+28)], fill=(185,165,95,255))
    # Lines
    f  = fnt(MONO, 10)
    fi = fnt(MONO, 9)
    for li in range(0,int(h*0.72),16):
        draw.line([(nx1+4,ny1+30+li),(nx2-4,ny1+30+li)], fill=(178,158,82,255), width=1)
    # Red margin
    draw.line([(nx1+38,ny1),(nx1+38,ny2)], fill=(200,75,75,180), width=1)
    # Handwritten notes (deliberate, slightly messy)
    notes = [
        "quarterly rec. — Hartwell acct",
        "  variance: -$2.1M (!!)",
        "3rd Q closeout — finalize",
        "   cross-reference w/ HW files",
        "call back Tom W. re: allocation",
        "board package due 10/20",
        "   confirm sig pages — R.W.",
        "filing extension — check status",
        "wire confirm: pending 10/14",
        "",
        "   see attached — p. 3 ??",
    ]
    for i,note in enumerate(notes):
        col = (65,45,12,255) if i != 1 else (160,30,30,255)
        draw.text((nx1+44, ny1+32+i*16), note, fill=col, font=f)

    # Pen resting diagonally across notepad
    for t in range(-200,201):
        angle = -0.22
        px = int(w*0.50 + t*math.cos(angle))
        py = int(h*0.78 + t*math.sin(angle))
        r  = 4 if abs(t)>180 else 3
        col = (28,26,34,255) if abs(t) > 185 else (38,36,44,255)
        draw.ellipse([(px-r,py-r),(px+r,py+r)], fill=col)
    # Pen clip
    for t in range(150, 195):
        angle = -0.22
        px = int(w*0.50 + t*math.cos(angle))
        py = int(h*0.78 + t*math.sin(angle))
        draw.ellipse([(px-2,py-5),(px+2,py-1)], fill=(180,170,130,255))

    draw_scale_ruler(draw, nx1+20, ny2+10, 160, "10 CM")
    draw_evidence_card(draw, nx2-140, ny1-42, "EV-B / desk", rng)

    img = add_flash(img, cx=w//2, cy=h//2, radius=300, alpha=55)
    img = add_grain(img, intensity=18, seed=rng.randint(0,9999))
    img = add_vignette(img, strength=0.50)
    return img.convert('RGB')


def ev_purse(rng):
    """EV-C: Decedent's purse on credenza post."""
    img  = Image.new('RGBA', (IW, IH), (30,27,35,255))
    draw = ImageDraw.Draw(img)
    w,h  = IW, IH

    # Credenza surface (dark wood edge, horizontal)
    draw.rectangle([(0,int(h*0.55)),(w,int(h*0.62))], fill=(52,40,28,255))
    draw.rectangle([(0,int(h*0.62)),(w,h)], fill=(44,34,22,255))
    # Wall behind
    draw.rectangle([(0,0),(w,int(h*0.55))], fill=(28,25,34,255))

    # Credenza corner post (vertical)
    post_x = int(w*0.35)
    draw.rectangle([(post_x-10,int(h*0.50)),(post_x+10,h)], fill=(40,30,20,255))

    # Purse hanging from post (handles over post)
    p_cx = post_x
    p_ty = int(h*0.26)
    p_by = int(h*0.62)
    p_w  = 130
    # Handle (strap loop over post)
    draw.arc([(p_cx-28,int(h*0.22)),(p_cx+28,int(h*0.38))],
             start=180,end=0,fill=(90,38,38,255),width=8)
    # Purse body (structured rectangular)
    draw.rounded_rectangle([(p_cx-p_w//2,p_ty),(p_cx+p_w//2,p_by)],
                           radius=8, fill=(88,34,44,255))
    # Clasp
    draw.rectangle([(p_cx-18,p_ty+2),(p_cx+18,p_ty+12)], fill=(160,140,90,255))
    draw.ellipse([(p_cx-6,p_ty+4),(p_cx+6,p_ty+10)], fill=(140,120,75,255))
    # Leather texture lines
    for lx in range(p_cx-p_w//2+15, p_cx+p_w//2-10, 22):
        draw.line([(lx,p_ty+18),(lx,p_by-10)], fill=(78,28,36,255), width=1)
    # Bottom stitching
    for sx in range(p_cx-p_w//2+8, p_cx+p_w//2-8, 6):
        draw.ellipse([(sx,p_by-10),(sx+3,p_by-7)], fill=(70,26,32,255))

    draw_scale_ruler(draw, int(w*0.05), int(h*0.72), 120, "10 CM")
    draw_evidence_card(draw, int(w*0.60), int(h*0.18), "EV-C / P-00", rng)

    img = add_flash(img, cx=p_cx, cy=(p_ty+p_by)//2, radius=270, alpha=65)
    img = add_grain(img, intensity=22, seed=rng.randint(0,9999))
    img = add_vignette(img, strength=0.62)
    return img.convert('RGB')


def ev_blouse_stain(rng):
    """EV-D: Blouse left interior cuff — stain detail (close-up)."""
    img  = Image.new('RGBA', (IW, IH), (208, 204, 196, 255))
    draw = ImageDraw.Draw(img)
    w,h  = IW, IH

    # White fabric fills frame — cloth texture
    for _ in range(800):
        fx = rng.randint(0,w); fy = rng.randint(0,h)
        fl = rng.randint(3,18)
        fang = rng.uniform(0, math.pi)
        ex = int(fx + fl*math.cos(fang))
        ey = int(fy + fl*math.sin(fang))
        draw.line([(fx,fy),(ex,ey)], fill=(195,191,183,255), width=1)

    # Cuff fold / edge
    draw.rounded_rectangle([(int(w*0.08),int(h*0.12)),(int(w*0.92),int(h*0.88))],
                           radius=20, fill=(210,206,198,255))
    draw.rounded_rectangle([(int(w*0.10),int(h*0.14)),(int(w*0.90),int(h*0.86))],
                           radius=18, fill=(215,211,203,255))
    # Cuff seam
    draw.line([(int(w*0.10),int(h*0.50)),(int(w*0.90),int(h*0.50))],
              fill=(195,191,183,255), width=2)
    # Button hole
    draw.rounded_rectangle([(int(w*0.78),int(h*0.42)),(int(w*0.84),int(h*0.58))],
                           radius=4, fill=(200,196,188,255), outline=(180,175,168,255), width=1)

    # THE STAIN — brownish, irregular, medium-sized
    # Multiple overlapping ellipses for organic stain shape
    stain_cx, stain_cy = int(w*0.42), int(h*0.44)
    stain_shapes = [
        (stain_cx,     stain_cy,     40, 32, (130, 90, 52, 140)),
        (stain_cx+12,  stain_cy-8,   25, 20, (115, 78, 42, 120)),
        (stain_cx-18,  stain_cy+12,  30, 22, (140, 96, 55, 110)),
        (stain_cx+5,   stain_cy+18,  18, 14, (108, 70, 38, 100)),
        (stain_cx-8,   stain_cy-14,  20, 16, (125, 84, 46, 105)),
        (stain_cx+28,  stain_cy+8,   14, 10, (120, 80, 44, 90)),
        (stain_cx-30,  stain_cy+5,   12, 8,  (132, 88, 50, 95)),
    ]
    stain_layer = Image.new('RGBA', (w,h), (0,0,0,0))
    sd = ImageDraw.Draw(stain_layer)
    for sx,sy,rr,rv,col in stain_shapes:
        sd.ellipse([(sx-rr,sy-rv),(sx+rr,sy+rv)], fill=col)
    stain_layer = stain_layer.filter(ImageFilter.GaussianBlur(radius=4))
    img = Image.alpha_composite(img.convert('RGBA'), stain_layer)

    # Drip / spread marks
    img = img.convert('RGBA')
    dd  = ImageDraw.Draw(img)
    for _ in range(8):
        dx = stain_cx + rng.randint(-35,45)
        dy = stain_cy + rng.randint(-25,35)
        dr = rng.randint(3,9)
        dd.ellipse([(dx-dr,dy-dr),(dx+dr,dy+dr)],
                   fill=(115,75,40,rng.randint(50,100)))

    # Evidence items
    draw_scale_ruler(dd, int(w*0.10), int(h*0.82), 140, "5 CM")
    draw_evidence_card(dd, int(w*0.55), int(h*0.80), "EV-D / SP-14", rng)
    # Arrow pointing to stain
    arr_x,arr_y = stain_cx+60, stain_cy-50
    dd.line([(arr_x,arr_y),(stain_cx+15,stain_cy-12)], fill=(220,30,30,200), width=2)
    dd.polygon([(stain_cx+15,stain_cy-12),
                (stain_cx+22,stain_cy-22),(stain_cx+6,stain_cy-22)],
               fill=(220,30,30,200))
    dd.text((arr_x+4,arr_y-16), "STAIN", fill=(200,25,25,255), font=fnt(MONO_B,11))

    img = add_flash(img, cx=w//2, cy=h//2, radius=290, alpha=40)
    img = add_grain(img, intensity=14, seed=rng.randint(0,9999))
    img = add_vignette(img, strength=0.38)
    return img.convert('RGB')


# ── POLAROID WRAPPER ─────────────────────────────────────────────────────

def make_polaroid(photo_img, caption, photo_id, case="2015-ME-0447",
                  date="10/14/2015", photog="T.A.N.", rng=None):
    if rng is None: rng = random.Random()
    p = Image.new('RGB', (PW, PH), (248, 242, 224))   # aged cream
    draw = ImageDraw.Draw(p)

    # Aged border — subtle banding
    for y in range(PH):
        a = int(4 * abs(math.sin(y/80.0 + rng.uniform(0,1))))
        bv = max(0, rng.randint(-a, a))
        draw.line([(0,y),(PW-1,y)], fill=(248-bv, 242-bv, 224-bv))

    # Photo area shadow
    draw.rectangle([(PAD_L+3, PAD_T+3), (PAD_L+IW+3, PAD_T+IH+3)],
                   fill=(180,170,150))
    # Paste photo
    p.paste(photo_img.resize((IW, IH)), (PAD_L, PAD_T))

    # Border scratches / scuffs (subtle)
    for _ in range(12):
        sx = rng.randint(0,PW); sy = rng.randint(0,PH)
        sl = rng.randint(8,40)
        draw.line([(sx,sy),(sx+sl,sy+rng.randint(-3,3))],
                  fill=(225,218,200), width=1)

    # Grain on border
    for _ in range(400):
        gx = rng.randint(0,PW); gy = rng.randint(0,PH)
        gv = rng.randint(215,250)
        draw.point((gx,gy), fill=(gv,gv,int(gv*0.92)))

    # Bottom caption area: hand-written pen style
    cap_y = PAD_T + IH + 22
    f_hw  = fnt(SERIF, 16)                # closest to pen feel
    f_sm  = fnt(MONO, 10)
    f_tiny= fnt(MONO, 9)

    # Caption (main handwritten line)
    draw.text((PAD_L + 8, cap_y), caption, fill=(42, 55, 120), font=f_hw)

    # Secondary info line (photo number, date, photographer)
    info = f"{photo_id}  |  {date}  |  Photog: {photog}"
    draw.text((PAD_L + 8, cap_y + 32), info, fill=(80, 80, 80), font=f_sm)

    # Case number (small, bottom right, printed look)
    cn_text = f"Case {case}  |  Minnehaha County ME"
    draw.text((PAD_L + 8, cap_y + 50), cn_text, fill=(100, 95, 85), font=f_tiny)

    # Photo number stamp (top-left corner of border)
    draw.text((8, 6), photo_id, fill=(90, 85, 72), font=fnt(MONO_B, 11))

    # Apply slight rotation
    angle = rng.uniform(-2.8, 2.8)
    pad   = 30
    canvas = Image.new('RGB', (PW + 2*pad, PH + 2*pad), (230, 225, 210))
    canvas.paste(p, (pad, pad))
    rotated = canvas.rotate(angle, resample=Image.BICUBIC, expand=False)
    return rotated.crop((pad//2, pad//2, PW+pad+pad//2, PH+pad+pad//2))


# ── MAIN ─────────────────────────────────────────────────────────────────

PHOTOS = [
    ("CS-01", scene_room_overview,   "Suite 712 overview — from entry, looking S",      "10/14/2015", "T.A.N."),
    ("CS-02", scene_desk_surface,    "Desk surface — laptop, mug, notepad",             "10/14/2015", "T.A.N."),
    ("CS-03", scene_decedent_chair,  "Decedent position — desk chair, NE angle",        "10/14/2015", "T.A.N."),
    ("CS-04", scene_entry_doorway,   "Suite 712 entry — hallway to antechamber",        "10/14/2015", "T.A.N."),
    ("CS-05", scene_desk_lamp,       "Desk lamp / work area — immediate detail",        "10/14/2015", "T.A.N."),
    ("EV-A",  ev_coffee_mug,         "Coffee mug on coaster — Item C-7",               "10/14/2015", "T.A.N."),
    ("EV-B",  ev_notepad,            "Legal notepad w/ pen — desk surface",            "10/14/2015", "T.A.N."),
    ("EV-C",  ev_purse,              "Decedent purse — credenza lower post",            "10/14/2015", "T.A.N."),
    ("EV-D",  ev_blouse_stain,       "Blouse left interior cuff — stain (SP-14)",      "10/14/2015", "T.A.N."),
]


def main():
    base_rng = random.Random(2015)
    print("Generating crime scene and evidence photos ...\n")
    for photo_id, scene_fn, caption, date, photog in PHOTOS:
        rng = random.Random(base_rng.randint(0, 999999))
        photo = scene_fn(rng)
        polaroid = make_polaroid(photo, caption, photo_id,
                                 date=date, photog=photog, rng=rng)
        fname = os.path.join(OUT, f"ME-0447-{photo_id}.png")
        polaroid.save(fname, "PNG", dpi=(300, 300))
        print(f"  → {fname}")
    print("\nDone.")


if __name__ == "__main__":
    main()
