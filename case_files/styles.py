"""Shared styles and table helpers for ME case file PDFs."""
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import Table, TableStyle, HRFlowable, Paragraph, Spacer
from reportlab.lib.units import inch
from aging import (TEXT_CLR, HDR_BG, ROW1_BG, ROW2_BG, GRID_CLR, PAPER_BG)


def mk_styles():
    def ps(name, **kw):
        d = dict(fontName='Courier', fontSize=10, leading=14,
                 textColor=TEXT_CLR, alignment=TA_LEFT, spaceBefore=2, spaceAfter=2)
        d.update(kw); return ParagraphStyle(name, **d)

    return {
        'doc_title': ps('doc_title', fontName='Courier-Bold', fontSize=12, leading=16,
                        alignment=TA_CENTER, spaceAfter=1, spaceBefore=0),
        'doc_sub':   ps('doc_sub',   fontName='Courier', fontSize=9.5, leading=13,
                        alignment=TA_CENTER, spaceAfter=2),
        'sec_head':  ps('sec_head',  fontName='Courier-Bold', fontSize=11, leading=15,
                        spaceBefore=11, spaceAfter=4),
        'sub_head':  ps('sub_head',  fontName='Courier-Bold', fontSize=10, leading=14,
                        spaceBefore=7, spaceAfter=3),
        'body':      ps('body',      fontName='Courier', fontSize=10, leading=14.5,
                        spaceBefore=3, spaceAfter=3, alignment=TA_JUSTIFY),
        'body_l':    ps('body_l',    fontName='Courier', fontSize=10, leading=14.5,
                        spaceBefore=2, spaceAfter=2),
        'small':     ps('small',     fontName='Courier', fontSize=8.5, leading=12),
        'small_b':   ps('small_b',   fontName='Courier-Bold', fontSize=8.5, leading=12),
        'field_l':   ps('field_l',   fontName='Courier-Bold', fontSize=9.5, leading=13),
        'field_v':   ps('field_v',   fontName='Courier',      fontSize=9.5, leading=13),
        'note_it':   ps('note_it',   fontName='Courier', fontSize=9, leading=13,
                        textColor=TEXT_CLR),
        'bold_body': ps('bold_body', fontName='Courier-Bold', fontSize=10, leading=14.5,
                        spaceBefore=3, spaceAfter=3),
    }


ST = mk_styles()


def HR():
    return HRFlowable(width='100%', thickness=0.6, color=GRID_CLR,
                      spaceAfter=4, spaceBefore=4)


def doc_header(full_title, sub="Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  DOB: 03/22/1969"):
    return [
        Paragraph("MINNEHAHA COUNTY OFFICE OF THE MEDICAL EXAMINER", ST['doc_title']),
        Paragraph("220 W. Sixth Street, Suite 140  |  Sioux Falls, SD 57104  |  (605) 367-4300", ST['doc_sub']),
        HR(),
        Paragraph(full_title, ST['doc_title']),
        Paragraph(sub, ST['doc_sub']),
        HR(),
        Spacer(1, 4),
    ]


def section(title):
    return Paragraph(title, ST['sec_head'])


def subsection(title):
    return Paragraph(title, ST['sub_head'])


def body(text):
    return Paragraph(text, ST['body'])


def body_l(text):
    return Paragraph(text, ST['body_l'])


def small(text):
    return Paragraph(text, ST['small'])


def SP(h=6):
    return Spacer(1, h)


def tbl(data, col_widths=None, has_hdr=True, alt=True, extra_style=None):
    """Build a styled Table."""
    ts = [
        ('FONT',          (0,0), (-1,-1), 'Courier',      9.5),
        ('TEXTCOLOR',     (0,0), (-1,-1), TEXT_CLR),
        ('GRID',          (0,0), (-1,-1), 0.5, GRID_CLR),
        ('ALIGN',         (0,0), (-1,-1), 'LEFT'),
        ('VALIGN',        (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING',   (0,0), (-1,-1), 4),
        ('RIGHTPADDING',  (0,0), (-1,-1), 4),
        ('TOPPADDING',    (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]
    if has_hdr:
        ts += [('FONT',       (0,0), (-1,0), 'Courier-Bold', 9.5),
               ('BACKGROUND', (0,0), (-1,0), HDR_BG)]
    if alt:
        start = 1 if has_hdr else 0
        ts += [('ROWBACKGROUNDS', (0, start), (-1,-1), [ROW1_BG, ROW2_BG])]
    if extra_style:
        ts += extra_style
    style = TableStyle(ts)
    t = Table(data, colWidths=col_widths, repeatRows=1 if has_hdr else 0)
    t.setStyle(style)
    return t


def label_value_tbl(rows, col1=2.2*inch, col2=None):
    """Two-column label/value table (no header row)."""
    from reportlab.lib.pagesizes import letter
    W = letter[0]
    margin = 0.8*inch
    avail = W - 2*margin
    if col2 is None:
        col2 = avail - col1
    data = []
    for lbl, val in rows:
        data.append([Paragraph(lbl, ST['field_l']), Paragraph(str(val), ST['field_v'])])
    return tbl(data, col_widths=[col1, col2], has_hdr=False, alt=True)
