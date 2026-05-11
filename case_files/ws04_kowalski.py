"""WS-04 — Interview Transcript: Diane Kowalski, Executive Assistant (2 pages)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from aging import make_onpage, W, H, STAMP_B, HW_BLUE, HW_PENCIL, STAMP_R
from styles import ST, HR, section, body_l, small, SP, tbl

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
    path = os.path.join(OUT, "WS-04-Kowalski-Interview-Transcript.pdf")
    aging = {
        'staple': True,
        1: {
            'rings': [(W * 0.80, H * 0.60, 40, 241, 0.21, 100)],
            'creases': [(0, H * 0.44, W, H * 0.437, 242, 0.70)],
            'foxing': {'count': 32, 'inten': 0.85},
            'stamps': [("SFPD HOMICIDE — CASE FILE", 0.75 * inch, H * 0.09, -3, STAMP_B, 9, 0.50)],
            'hw': [("USB DRIVE — locate/log as evidence", W - 3.2 * inch, H * 0.305, 1, STAMP_R, 7.5),
                   ("visitor — no calendar entry — KEY", 0.82 * inch, H * 0.51, -1, HW_BLUE, 7.5)],
        },
        2: {
            'rings': [(W * 0.13, H * 0.50, 32, 243, 0.16, 82)],
            'creases': [],
            'foxing': {'count': 22, 'inten': 0.75},
            'stamps': [],
            'hw': [("\"in over her head\" — exact quote — MLS", W - 3.4 * inch, H * 0.63, 1, HW_BLUE, 7.5),
                   ("cancelled ALL next week — why??", 0.82 * inch, H * 0.52, -1, HW_PENCIL, 7.0)],
        },
    }
    cb = make_onpage(204, "WS-04 Kowalski", 2, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.80 * inch, rightMargin=0.80 * inch,
                            topMargin=0.75 * inch, bottomMargin=0.72 * inch)

    story = ws_header(
        "INTERVIEW TRANSCRIPT — VOLUNTARY WITNESS STATEMENT",
        "SFPD Case No. 2015-48801  |  ME Case No. 2015-ME-0447  |  MARSH, Eleanor Anne"
    )

    story += [tbl([
        ["Witness:", "Diane Marie Kowalski", "DOB:", "August 22, 1977"],
        ["Address:", "3301 S. Duluth Ave., Apt. 11B, Sioux Falls, SD 57105", "Phone:", "(605) 496-2217"],
        ["Employer:", "Apex Financial Group, Inc.", "Title:", "Executive Assistant to CFO"],
        ["Interview Date:", "October 14, 2015", "Time:", "1345 — 1510 hrs"],
        ["Location:", "SFPD Criminal Investigations Division, 320 W. 4th St., Sioux Falls, SD 57104", "", ""],
        ["Interviewing Officers:", "Det. Maria L. Santos (Badge #4471); Det. James R. Brewer (Badge #3892)", "", ""],
        ["Transcribed By:", "Ofc. T. Hargrove, SFPD Records Unit", "Reviewed:", "October 16, 2015"],
    ], col_widths=[1.05 * inch, 3.00 * inch, 0.75 * inch, 1.75 * inch], has_hdr=False, alt=False)]

    story += [SP(4), small("Recorded with witness consent. Ms. Kowalski was advised she was not under arrest and was free to leave. "
                           "She agreed to speak voluntarily. Ms. Kowalski became visibly emotional at several points; breaks were taken as needed.")]
    story += [SP(6), section("TRANSCRIPT")]
    story += [SP(3)]

    exchanges = [
        ("DET. SANTOS:", "Ms. Kowalski, thank you for coming in. I know this is a very difficult day. Can you tell us about your role and how long you've worked with Ms. Marsh?"),
        ("KOWALSKI:", "Four years. I came over with her when she moved to Apex — I'd been her assistant at her previous company for two years before that. So six years total. I — she's the only CFO I've ever supported. I know her well. Knew her."),
        ("DET. SANTOS:", "We appreciate your being here. Can you describe Ms. Marsh's typical work schedule and how that had changed recently?"),
        ("KOWALSKI:", "Normally she was in by 7:45 and left between 5:30 and 6:30. She was disciplined — always. But over the past month, maybe five weeks, she'd been staying much later. Sometimes until nine or ten. I'd leave and she'd still be at her desk. She'd started closing her office door, which she didn't typically do. And she'd been taking calls that she didn't route through me — personal calls, outside the normal process."),
        ("DET. BREWER:", "Did you ask her about it?"),
        ("KOWALSKI:", "Once. About two weeks ago. She said she was working through some things and not to worry. She thanked me for asking. That was — that was Eleanor. Even when she was under pressure she was thoughtful."),
        ("DET. SANTOS:", "Let's talk about yesterday, October 13th. Tell us about the visitor she had in the afternoon."),
        ("KOWALSKI:", "A man came to the suite around two-fifteen. He didn't have an appointment — I keep her calendar and there was nothing listed. He came to my desk directly and said he had a meeting with Ms. Marsh. I asked for his name. He gave a last name — Vren, or Vren something. I didn't catch all of it, and he didn't offer a business card. I told him I'd need to check, and I was about to call into Eleanor's office, but she must have heard something because her door opened and she came out. She saw him and said — and this struck me — she said, 'I'll take it from here, Diane,' and she led him into her office and closed the door."),
        ("DET. BREWER:", "She recognized him?"),
        ("KOWALSKI:", "Yes. Definitely. But she didn't introduce him, which was — Eleanor always introduced people to me. Always."),
        ("DET. SANTOS:", "How long were they in her office?"),
        ("KOWALSKI:", "About forty-five minutes. When he left he walked straight out. He didn't come by my desk. Eleanor came out shortly after and asked me to hold all her calls for the rest of the day. She went back in and closed the door again. That was at — I'd say just after three."),
        ("DET. BREWER:", "How did she seem?"),
        ("KOWALSKI:", "She was pale. She's — she was a composed person. But she looked like someone who'd received bad news. I asked if she needed anything and she said 'Not yet.'"),
        ("DET. SANTOS:", "Not yet."),
        ("KOWALSKI:", "That's what she said. I wrote it down in my personal notepad because it seemed strange."),
        ("DET. SANTOS:", "You mentioned she cancelled appointments. Can you be specific?"),
        ("KOWALSKI:", "On October 12th — the day before — she asked me to cancel and reschedule everything on her calendar for the following week. October 19th through 23rd. That's a full week of meetings, calls, two external engagements. She said she would be — she used the phrase 'unavailable for the foreseeable future.' I assumed she was planning a personal trip or medical leave. But she didn't say."),
        ("DET. BREWER:", "Ms. Kowalski, you mentioned a USB drive."),
        ("KOWALSKI:", "Yes. Over the past week she asked me three or four times if I'd seen a small USB drive — she described it as black, very small, no label. She looked for it herself a couple of times, going through her desk drawers. She was anxious about it. More than I would expect over a data drive."),
        ("DET. SANTOS:", "Do you know what was on it?"),
        ("KOWALSKI:", "No. She never said. But the way she was looking — it mattered to her a great deal."),
        ("DET. SANTOS:", "Did Ms. Marsh ever say anything to you directly that concerned you — about her safety, or what she was dealing with?"),
        ("KOWALSKI:", "On October 12th — the Monday before. After she asked me to clear her calendar. I was getting my things to leave and she stopped me at my desk. She said — and I want to make sure I get this right because I wrote it down — she said, 'Diane, if anything happens, I want you to know that things here are not what they appear to be.' I asked what she meant. She said, 'I'm not sure yet. But I will be soon.' And then she said goodnight."),
        ("DET. BREWER:", "Did you take that as a threat to her safety?"),
        ("KOWALSKI:", "I didn't know what to think. I told myself she was just stressed. I should have taken it more seriously. I should have asked more."),
        ("DET. SANTOS:", "You couldn't have known. Are you aware of any medical conditions Ms. Marsh had?"),
        ("KOWALSKI:", "Her blood pressure — she took medication for it, Lisinopril. I know because the pharmacy occasionally called the main line when she missed a pickup, and she'd have me call them back. She also seemed to have some anxiety — she mentioned once that she'd spoken to a doctor about it. She didn't go into detail."),
        ("DET. SANTOS:", "Is there anything else — anything at all — that you think is relevant?"),
        ("KOWALSKI:", "I don't know if it matters. But two weeks ago — maybe October 1st — I saw a file on her desk when I came in to take dictation. A manila folder, not a company file. She closed it when I came in. I only saw a few words on the tab. It looked like it said 'Q3 — parallel.' I don't know what that means. I never saw that folder again."),
        ("DET. SANTOS:", "Thank you, Ms. Kowalski. We may need to speak with you again."),
    ]

    for spk, txt in exchanges:
        story.append(qa(spk, txt))

    story += [SP(8), HR(), SP(4)]
    story += [small("End of transcript. Duration: approximately 1 hour 25 minutes. "
                    "Recording file: SFPD-AUDIO-2015-48801-003. Reviewed and approved by Det. M.L. Santos. "
                    "Note: Witness provided investigator with handwritten note (personal notepad, Oct. 12 and Oct. 13 entries) — logged as item EV-F.")]
    story += [SP(6)]
    story += [tbl([
        ["Witness Signature:", "______________________________", "Date:", "October 14, 2015"],
        ["Det. Santos (Badge #4471):", "______________________________", "Det. Brewer (Badge #3892):", "______________________________"],
    ], col_widths=[1.55 * inch, 2.30 * inch, 1.20 * inch, 1.50 * inch], has_hdr=False, alt=False)]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
