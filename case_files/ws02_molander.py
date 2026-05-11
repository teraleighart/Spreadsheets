"""WS-02 — Interview Transcript: Linda Molander (2 pages)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from aging import make_onpage, W, H, STAMP_B, HW_BLUE, HW_PENCIL, STAMP_R
from styles import ST, HR, section, body, body_l, small, SP, tbl

OUT = os.path.dirname(__file__)


def qa(spk, txt):
    t = Table([[Paragraph(f'<b>{spk}</b>', ST['small_b']),
                Paragraph(txt, ST['body_l'])],
               [Paragraph('', ST['small_b']), Paragraph('', ST['body_l'])]],
              colWidths=[1.40 * inch, 5.10 * inch])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    return t


def ws_header(title, sub):
    return [
        Paragraph('SIOUX FALLS POLICE DEPARTMENT', ST['doc_title']),
        Paragraph('Criminal Investigations Division — Homicide Unit', ST['doc_sub']),
        Paragraph(title, ST['sec_head']),
        SP(2),
        Paragraph(sub, ST['small']),
        SP(3),
        HR(),
    ]


def build():
    path = os.path.join(OUT, "WS-02-Molander-Interview-Transcript.pdf")
    aging = {
        'staple': True,
        1: {
            'rings': [(W * 0.15, H * 0.68, 34, 221, 0.17, 88)],
            'creases': [(0, H * 0.55, W, H * 0.547, 222, 0.62)],
            'foxing': {'count': 25, 'inten': 0.78},
            'stamps': [("SFPD HOMICIDE — CASE FILE", 0.75 * inch, H * 0.09, 3, STAMP_B, 9, 0.50)],
            'hw': [("who was the visitor?? — JRB", W - 2.8 * inch, H * 0.42, 1, HW_BLUE, 7.5)],
        },
        2: {
            'rings': [(W * 0.82, H * 0.22, 30, 223, 0.14, 78)],
            'creases': [],
            'foxing': {'count': 18, 'inten': 0.70},
            'stamps': [],
            'hw': [("decaf only — RX conflict?", 0.82 * inch, H * 0.58, -1, HW_BLUE, 7.5),
                   ("car still in garage — overnight", W - 3.1 * inch, H * 0.44, 1, HW_PENCIL, 7.0)],
        },
    }
    cb = make_onpage(202, "WS-02 Molander", 2, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.80 * inch, rightMargin=0.80 * inch,
                            topMargin=0.75 * inch, bottomMargin=0.72 * inch)

    story = ws_header(
        "INTERVIEW TRANSCRIPT — VOLUNTARY WITNESS STATEMENT",
        "SFPD Case No. 2015-48801  |  ME Case No. 2015-ME-0447  |  MARSH, Eleanor Anne"
    )

    story += [tbl([
        ["Witness:", "Linda Claire Molander", "DOB:", "06/03/1963"],
        ["Address:", "814 W. Bittersweet Ln., Sioux Falls, SD 57108", "Phone:", "(605) 271-9034"],
        ["Employer:", "Apex Financial Group, Inc.", "Title:", "Office Manager"],
        ["Interview Date:", "October 14, 2015", "Time:", "1115 — 1224 hrs"],
        ["Location:", "SFPD Criminal Investigations Division, 320 W. 4th St., Sioux Falls, SD 57104", "", ""],
        ["Interviewing Officers:", "Det. Maria L. Santos (Badge #4471); Det. James R. Brewer (Badge #3892)", "", ""],
        ["Transcribed By:", "Ofc. T. Hargrove, SFPD Records Unit", "Reviewed:", "October 16, 2015"],
    ], col_widths=[1.05 * inch, 3.00 * inch, 0.75 * inch, 1.75 * inch], has_hdr=False, alt=False)]

    story += [SP(4), small("This interview was recorded with the consent of the witness. Ms. Molander was advised she was not under arrest "
                           "and was free to leave at any time. She agreed to speak voluntarily.")]
    story += [SP(6), section("TRANSCRIPT")]
    story += [SP(3)]

    exchanges = [
        ("DET. SANTOS:", "Ms. Molander, thank you for coming in. Can you tell us how long you've worked at Apex Financial and what your role involves?"),
        ("MOLANDER:", "Six years in February. I'm the office manager, so I handle operations — scheduling, vendors, building liaison, supplies, HR coordination. I work closely with all the senior staff, including Eleanor."),
        ("DET. SANTOS:", "Including Ms. Marsh."),
        ("MOLANDER:", "Yes. She and I worked together closely. I wouldn't say we were personal friends — we didn't socialize outside the office — but I respected her enormously. She was very capable."),
        ("DET. SANTOS:", "Can you walk us through this morning — what happened when you arrived?"),
        ("MOLANDER:", "I got to the building at — I checked my phone later — it was 7:31. I park in the garage on the west side, take the elevator up. As I was crossing the lobby toward the elevator bank, the man — the IT contractor, Mr. Fuentes — he came out of one of the stairwells. He looked — he looked shaken. He came straight toward me and said there was something wrong, that I shouldn't go upstairs, that he'd found someone."),
        ("DET. BREWER:", "What did you think at that point?"),
        ("MOLANDER:", "I thought maybe someone had broken in. Or a medical emergency of some kind. He said he'd already called 911. I took out my phone and I called Mr. Ellsworth — Craig Ellsworth, our COO — to let him know something was happening."),
        ("DET. SANTOS:", "Let's talk about Ms. Marsh. Had you noticed anything different about her behavior recently — in the days or weeks leading up to this?"),
        ("MOLANDER:", "Yes. The past — I'd say three, maybe four weeks, she'd been different. Quieter. She was staying very late. I knew because the cleaning crew — they'd mention it to me, or I'd see her car still in the garage when I left at six or seven. She'd always worked hard, but this was different."),
        ("DET. BREWER:", "Different how?"),
        ("MOLANDER:", "She seemed distracted. In our brief interactions she was — short. Not rude, Eleanor was never rude — but brief. Like she was carrying something. And she declined the staff birthday lunch we had two weeks ago. She never misses that kind of thing."),
        ("DET. SANTOS:", "Yesterday — October 13th — did you see Ms. Marsh?"),
        ("MOLANDER:", "Yes. She came in at her normal time, around eight, eight-fifteen. We spoke briefly in the morning — nothing significant, just operational things. And then in the afternoon, maybe around two o'clock or a little after, she had a visitor."),
        ("DET. BREWER:", "Tell us about that."),
        ("MOLANDER:", "A man I didn't recognize. He came to the reception area — we share a receptionist with two other suites on the floor, a woman named Gloria — and asked for Ms. Marsh. Gloria brought him over to me because it wasn't my desk specifically, but I happened to be near reception. He said he had an appointment. I wasn't aware of one. Diane — Ms. Kowalski, Eleanor's assistant — would know more. She was at her desk just outside Eleanor's office."),
        ("DET. SANTOS:", "Can you describe this man?"),
        ("MOLANDER:", "He was — I'd say mid-forties. Professional looking. Dark gray suit, no tie. He had an accent — I couldn't place it exactly. Eastern European maybe, or German. He was polite but not especially warm."),
        ("DET. BREWER:", "How long was he there?"),
        ("MOLANDER:", "I wasn't watching, but he went in to see Eleanor, and I was aware that I didn't see him leave for some time. I'd estimate thirty to fifty minutes. I didn't think much of it at the time — Eleanor had outside meetings occasionally."),
        ("DET. SANTOS:", "Do you know if Ms. Marsh sent an email to Craig Ellsworth late last night?"),
        ("MOLANDER:", "I only know that because Craig mentioned it. When I reached him this morning, he said he'd gotten an email from her around midnight. He seemed — not upset, but careful about it."),
        ("DET. SANTOS:", "Careful how?"),
        ("MOLANDER:", "He just said he'd received it and that he'd deal with the police. He didn't tell me what was in it."),
        ("DET. BREWER:", "Was Ms. Marsh's car in the garage when you arrived this morning?"),
        ("MOLANDER:", "Yes. A silver BMW — hers. That struck me when I got to the lobby and Fuentes stopped me. Her car being there overnight is unusual. She lives in the Hawthorn neighborhood — it's twenty minutes. She would have driven home."),
        ("DET. SANTOS:", "Did you ever have any reason to be concerned about Ms. Marsh's health?"),
        ("MOLANDER:", "She mentioned — not to me specifically, but I overheard her say once that she was watching her blood pressure. And she was very particular about her coffee. She told me once that she only drank decaf after her afternoon break because of her blood pressure medication. She was strict about that."),
        ("DET. BREWER:", "Why does that matter to you now?"),
        ("MOLANDER:", "Because Diane told me this morning — when we were both waiting, before you brought us in separately — that the coffee mug on Eleanor's desk was from the breakroom pot. The regular pot. The one that's always on after five. And Eleanor would never have poured from that pot. Not intentionally."),
        ("DET. SANTOS:", "Ms. Molander, is there anything else you think we should know?"),
        ("MOLANDER:", "I just — I want to say that Eleanor Marsh was a careful, controlled person. Whatever happened, it wasn't carelessness on her part. I'm sure of that."),
        ("DET. SANTOS:", "Thank you. We may follow up with you. Please don't discuss the details of this interview with other Apex employees for the time being."),
    ]

    for spk, txt in exchanges:
        story.append(qa(spk, txt))

    story += [SP(8), HR(), SP(4)]
    story += [small("End of transcript. Duration: approximately 1 hour 9 minutes. "
                    "Recording file: SFPD-AUDIO-2015-48801-002. Reviewed and approved by Det. M.L. Santos.")]
    story += [SP(6)]
    story += [tbl([
        ["Witness Signature:", "______________________________", "Date:", "October 14, 2015"],
        ["Det. Santos (Badge #4471):", "______________________________", "Det. Brewer (Badge #3892):", "______________________________"],
    ], col_widths=[1.55 * inch, 2.30 * inch, 1.20 * inch, 1.50 * inch], has_hdr=False, alt=False)]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
