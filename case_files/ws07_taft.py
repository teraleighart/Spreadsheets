"""WS-07 — Phone Interview Transcript: Dr. Susan Taft, MD (2 pages)."""
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
    path = os.path.join(OUT, "WS-07-Taft-Phone-Interview-Transcript.pdf")
    aging = {
        'staple': True,
        1: {
            'rings': [(W * 0.79, H * 0.72, 36, 271, 0.17, 92)],
            'creases': [(0, H * 0.46, W, H * 0.457, 272, 0.63)],
            'foxing': {'count': 24, 'inten': 0.78},
            'stamps': [("SFPD HOMICIDE — CASE FILE", 0.75 * inch, H * 0.09, -3, STAMP_B, 9, 0.50),
                       ("CONFIDENTIAL — MEDICAL", W * 0.52, H * 0.10, 5, STAMP_R, 10, 0.48)],
            'hw': [("subpoena medical records — MLS", W - 3.0 * inch, H * 0.38, 1, HW_BLUE, 7.5)],
        },
        2: {
            'rings': [],
            'creases': [(0, H * 0.65, W, H * 0.647, 273, 0.57)],
            'foxing': {'count': 18, 'inten': 0.70},
            'stamps': [],
            'hw': [("cardiology appt NEVER MADE — why not?", W - 3.6 * inch, H * 0.64, -1, HW_BLUE, 7.5),
                   ("BP 148/92 — elevated, on meds — still high", 0.82 * inch, H * 0.53, 1, HW_PENCIL, 7.0),
                   ("\"other meds\" ??? tox results pending", W - 3.4 * inch, H * 0.465, 1, STAMP_R, 7.0)],
        },
    }
    cb = make_onpage(207, "WS-07 Taft", 2, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.80 * inch, rightMargin=0.80 * inch,
                            topMargin=0.75 * inch, bottomMargin=0.72 * inch)

    story = ws_header(
        "PHONE INTERVIEW TRANSCRIPT — TREATING PHYSICIAN",
        "SFPD Case No. 2015-48801  |  ME Case No. 2015-ME-0447  |  MARSH, Eleanor Anne"
    )

    story += [tbl([
        ["Witness:", "Dr. Susan K. Taft, MD", "DOB:", "February 14, 1968"],
        ["Practice:", "Sioux Falls Medical Associates, 1800 W. 22nd St., Sioux Falls, SD 57105", "Phone:", "(605) 339-4400"],
        ["Specialty:", "Internal Medicine / Primary Care", "License:", "SD-MD-08-4471"],
        ["Interview Date:", "October 15, 2015", "Time:", "1030 — 1115 hrs (by telephone)"],
        ["Interviewing Officer:", "Det. Maria L. Santos (Badge #4471) — SFPD Criminal Investigations Division", "", ""],
        ["Transcribed By:", "Ofc. T. Hargrove, SFPD Records Unit", "Reviewed:", "October 17, 2015"],
        ["Note:", "Dr. Taft was notified of Ms. Marsh's death by Det. Santos at the outset of this call. "
                 "Dr. Taft conferred briefly with in-house counsel before proceeding. Interview was recorded with consent.", "", ""],
    ], col_widths=[1.05 * inch, 3.00 * inch, 0.75 * inch, 1.75 * inch], has_hdr=False, alt=False)]

    story += [SP(4), small("NOTE: Dr. Taft advised Det. Santos that she would answer questions from memory and that a formal medical "
                           "records request under applicable law would be required for complete documentation. She stated she was "
                           "cooperating voluntarily and under the belief that doing so was appropriate under the circumstances "
                           "of an active death investigation.")]
    story += [SP(6), section("TRANSCRIPT")]
    story += [SP(3)]

    exchanges = [
        ("DET. SANTOS:", "Dr. Taft, thank you for speaking with me. I want to confirm — you are Eleanor Marsh's primary care physician?"),
        ("DR. TAFT:", "That's correct. Eleanor has been my patient since 2011. I'm — I'm still processing what you've told me. I saw her just a few weeks ago."),
        ("DET. SANTOS:", "I understand. I'm sorry for the difficult news. Can you tell me what conditions you were treating Ms. Marsh for?"),
        ("DR. TAFT:", "I can tell you what I can recall without the chart in front of me, and I want to be clear that anything I say here is from memory and a formal records request would be needed for documentation. Eleanor had two active diagnoses that I was managing: Stage 1 hypertension — elevated blood pressure — and mild generalized anxiety disorder."),
        ("DET. SANTOS:", "And what medications was she taking?"),
        ("DR. TAFT:", "I prescribed Lisinopril — that's an ACE inhibitor, a standard blood pressure medication — at ten milligrams daily. And Buspirone, ten milligrams daily, for the anxiety. She'd been on the Lisinopril for about two years. The Buspirone was more recent — I started that about eight months ago."),
        ("DET. BREWER:", "Were there any other medications to your knowledge?"),
        ("DR. TAFT:", "Not prescribed by me. Eleanor was forthright about her medications in my experience, but I can only speak to what she reported and what I prescribed. Whether she was taking anything else — over the counter, supplements, or from another provider — I can't say with certainty."),
        ("DET. SANTOS:", "When was her most recent appointment with you?"),
        ("DR. TAFT:", "September 28th. A routine follow-up. She came in for her quarterly check."),
        ("DET. SANTOS:", "How did that visit go?"),
        ("DR. TAFT:", "Her blood pressure was elevated. One-forty-eight over ninety-two. That's above her typical range — she'd been running around one-thirty-five over eighty-five on the Lisinopril, which was acceptable. The September reading concerned me."),
        ("DET. BREWER:", "Did she explain the elevation?"),
        ("DR. TAFT:", "She attributed it to work stress. She also mentioned some new symptoms at that visit: fatigue — she said she was more tired than usual — and some chest tightness with exertion. Walking up stairs, that kind of thing. And she mentioned difficulty sleeping."),
        ("DET. SANTOS:", "What did you do in response to those symptoms?"),
        ("DR. TAFT:", "I made a referral to cardiology. Dr. James Whitmore at Sioux Falls Cardiology Associates. Given her family history and the new symptoms, I wanted a more thorough evaluation. I gave her Dr. Whitmore's number and told her to call within the week."),
        ("DET. BREWER:", "Did she follow through on that?"),
        ("DR. TAFT:", "I don't have any record of a consultation note coming back to my office from Dr. Whitmore, which typically happens if a referral goes through. So to my knowledge, as of our last contact, she had not yet made that appointment. I didn't follow up on it — I should have followed up on it."),
        ("DET. SANTOS:", "Was there any discussion of cardiac history or family history at that visit?"),
        ("DR. TAFT:", "Yes. Eleanor had a significant family history — her father died of a myocardial infarction at 58, and she mentioned an uncle with similar history. That's part of why the referral felt urgent to me. She was 46, she had hypertension, she had the family history, and now these new symptoms. It warranted evaluation."),
        ("DET. SANTOS:", "Was there any discussion of alcohol or substance use?"),
        ("DR. TAFT:", "Routine social history — she reported moderate social alcohol use, no more than a few glasses of wine per week in her characterization. No tobacco, no illicit substance use reported. Nothing that raised a concern."),
        ("DET. BREWER:", "Did she mention anything about her mental state — beyond the anxiety she was already being treated for?"),
        ("DR. TAFT:", "She seemed stressed. More so than usual. She described it as a difficult period at work. I asked if the Buspirone was helping and she said it was taking the edge off but that the situation was 'more complicated than medication could fix.' I noted that as somewhat concerning but she reassured me she wasn't in any danger. I took her at her word."),
        ("DET. SANTOS:", "Is there anything else from that visit — or from your overall care of Ms. Marsh — that you think may be relevant?"),
        ("DR. TAFT:", "One thing. At the September visit, when I asked if she was taking any supplements or vitamins, she said no. But then she paused and said — and this is something I noted at the time as a little odd — she said, 'Nothing that anyone prescribed me.' I asked what she meant. She said never mind, it was nothing. I made a note of it but I didn't press her. I wish I had."),
        ("DET. SANTOS:", "Thank you, Dr. Taft. We'll be in touch regarding the formal records request."),
        ("DR. TAFT:", "Please. Whatever I can do. She was a good person. She deserves answers."),
    ]

    for spk, txt in exchanges:
        story.append(qa(spk, txt))

    story += [SP(8), HR(), SP(4)]
    story += [small("End of transcript. Duration: approximately 45 minutes. "
                    "Recording file: SFPD-AUDIO-2015-48801-005. Note: formal medical records subpoena submitted "
                    "October 16, 2015 (SFPD Legal Ref. 2015-SR-0447-02). Reviewed and approved by Det. M.L. Santos.")]
    story += [SP(6)]
    story += [tbl([
        ["Det. Santos (Badge #4471):", "______________________________", "Date:", "October 15, 2015"],
        ["Det. Brewer (Badge #3892):", "______________________________", "", ""],
    ], col_widths=[1.80 * inch, 2.50 * inch, 0.65 * inch, 1.60 * inch], has_hdr=False, alt=False)]
    story += [SP(3), small("Note: Witness (Dr. Taft) did not sign this transcript as interview was conducted by telephone. "
                           "Transcript was provided to Dr. Taft for review and correction on October 18, 2015. "
                           "No corrections requested.")]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
