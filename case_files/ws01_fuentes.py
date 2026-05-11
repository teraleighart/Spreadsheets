"""WS-01 — Interview Transcript: Ramon Fuentes (2 pages)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from aging import make_onpage, W, H, STAMP_B, HW_BLUE, HW_PENCIL, STAMP_R
from styles import ST, HR, section, body, body_l, small, SP, tbl, label_value_tbl

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
        ('LINEBELOW', (0, 0), (-1, 0), 0, (1, 1, 1, 0)),
    ]))
    return t


def ws_header(title, sub):
    from reportlab.platypus import Paragraph as P
    lines = [
        P('SIOUX FALLS POLICE DEPARTMENT', ST['doc_title']),
        P('Criminal Investigations Division — Homicide Unit', ST['doc_sub']),
        P(title, ST['sec_head']),
        SP(2),
        P(sub, ST['small']),
        SP(3),
        HR(),
    ]
    return lines


def build():
    path = os.path.join(OUT, "WS-01-Fuentes-Interview-Transcript.pdf")
    aging = {
        'staple': True,
        1: {
            'rings': [(W * 0.78, H * 0.74, 38, 211, 0.18, 95)],
            'creases': [(0, H * 0.48, W, H * 0.477, 212, 0.65)],
            'foxing': {'count': 28, 'inten': 0.80},
            'stamps': [("SFPD HOMICIDE — CASE FILE", 0.75 * inch, H * 0.09, -4, STAMP_B, 9, 0.50)],
            'hw': [("check badge log — MLS", W - 2.5 * inch, H * 0.53, -1, HW_BLUE, 7.5)],
        },
        2: {
            'rings': [],
            'creases': [(0, H * 0.61, W, H * 0.607, 213, 0.55)],
            'foxing': {'count': 20, 'inten': 0.72},
            'stamps': [],
            'hw': [("door unlocked — key ??", W - 2.6 * inch, H * 0.295, 1, HW_BLUE, 7.5),
                   ("2247 — not him??", 0.82 * inch, H * 0.135, -2, STAMP_R, 7.0)],
        },
    }
    cb = make_onpage(201, "WS-01 Fuentes", 2, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.80 * inch, rightMargin=0.80 * inch,
                            topMargin=0.75 * inch, bottomMargin=0.72 * inch)

    story = ws_header(
        "INTERVIEW TRANSCRIPT — VOLUNTARY WITNESS STATEMENT",
        "SFPD Case No. 2015-48801  |  ME Case No. 2015-ME-0447  |  MARSH, Eleanor Anne"
    )

    story += [tbl([
        ["Witness:", "Ramon Aurelio Fuentes", "DOB:", "04/17/1981"],
        ["Address:", "2218 S. Grange Ave., Apt. 4, Sioux Falls, SD 57105", "Phone:", "(605) 318-7742"],
        ["Employer:", "Meridian Tech Solutions, LLC", "Title:", "IT Systems Technician"],
        ["Interview Date:", "October 14, 2015", "Time:", "0930 — 1047 hrs"],
        ["Location:", "4200 S. Western Ave. — Building Manager Conference Room, 1st Floor", "", ""],
        ["Interviewing Officers:", "Det. Maria L. Santos (Badge #4471); Det. James R. Brewer (Badge #3892)", "", ""],
        ["Transcribed By:", "Ofc. T. Hargrove, SFPD Records Unit", "Reviewed:", "October 16, 2015"],
    ], col_widths=[1.05 * inch, 3.00 * inch, 0.75 * inch, 1.75 * inch], has_hdr=False, alt=False)]

    story += [SP(4), small("This interview was recorded with the consent of the witness. Mr. Fuentes was advised that he was not under arrest, "
                           "was free to leave at any time, and was not required to answer questions. He agreed to speak voluntarily. "
                           "This transcript reflects the audio recording; minor verbal filler (um, uh) has been omitted for readability.")]
    story += [SP(6), section("TRANSCRIPT")]
    story += [SP(3)]

    exchanges = [
        ("DET. SANTOS:", "Mr. Fuentes, thank you for staying with us this morning. I know it's been a long few hours. Can you start by telling us a little about your work and why you were in this building last night?"),
        ("FUENTES:", "Yeah. Sure. I work for Meridian Tech — we're an IT contractor. We've got a service contract with Apex Financial, which is the company on the seventh floor. They've got a server room up there. We've been doing a hardware upgrade over the past couple of weeks — replacing rack units, new UPS systems. Some of that work we have to do off-hours so we don't interrupt normal business operations."),
        ("DET. SANTOS:", "And last night — or rather, early this morning — was that a scheduled maintenance window?"),
        ("FUENTES:", "Yes. Well — I mean, it was on our project schedule. I had it in my calendar. The window was four to seven a.m., so I was supposed to be there by four."),
        ("DET. SANTOS:", "Supposed to be. What time did you actually arrive?"),
        ("FUENTES:", "I got to the lobby — I want to say around 4:15. Maybe a little after. The guard at the desk — the night guard — I signed in, he checked my ID and my contractor card. That's standard. Then I took the elevator up to seven."),
        ("DET. BREWER:", "When you got off the elevator on the seventh floor, what did you see?"),
        ("FUENTES:", "Just the hallway. Normal. The lights in the hall are on a motion sensor — they kind of flicker on when you come out of the elevator. I went toward the server room, which is down toward the north end of the hall, past the main suite — Suite 712."),
        ("DET. SANTOS:", "And as you were walking past Suite 712, what did you notice?"),
        ("FUENTES:", "There was light coming from under the door. The gap at the bottom — light was coming through. I thought that was odd because it was after four in the morning. I figured maybe someone had left a light on, or maybe someone was working really late."),
        ("DET. BREWER:", "Did you stop?"),
        ("FUENTES:", "I kept going at first. I went to the server room, started pulling out my gear. But it bothered me. After a few minutes I went back."),
        ("DET. SANTOS:", "Back to Suite 712?"),
        ("FUENTES:", "Yeah. I knocked. A couple of times. No answer. I tried the handle — and the door just... opened."),
        ("DET. BREWER:", "It was unlocked?"),
        ("FUENTES:", "It was unlocked. Which — I don't know if that's normal for them. I'd never had reason to go in there before. I just know that when I come in after hours normally, everything on that floor is locked up."),
        ("DET. SANTOS:", "What did you see when you opened the door?"),
        ("FUENTES:", "The office. A big executive office. A desk in the middle, a big one. And — there was a woman at the desk. Face-down. Her head was resting on her arms on the desk. Her hair was forward so I couldn't see her face. I thought — I mean, my first thought was she'd fallen asleep at her desk."),
        ("DET. SANTOS:", "What did you do?"),
        ("FUENTES:", "I called out. I said something like — 'Hello? Ma'am?' No response. I walked in a little further. I called again. Nothing. I went around the desk and I put my hand on her shoulder — just to wake her up. And she was — she was cold. And stiff. It wasn't right. I pulled my hand back. I took my phone out and called 911."),
        ("DET. BREWER:", "Did you move anything else? Touch anything else in the office?"),
        ("FUENTES:", "No. I stepped back. I stayed near the door until the dispatcher told me to. They kept me on the phone."),
        ("DET. SANTOS:", "Had you ever seen Ms. Marsh before — Eleanor Marsh, the CFO — had you had any prior contact with her?"),
        ("FUENTES:", "I knew who she was. I'd seen her maybe two or three times when we were doing day work up there. She'd walked past, that kind of thing. But I'd never spoken with her directly."),
        ("DET. SANTOS:", "I want to ask you about something. Our records show that a contractor access card assigned to you — card number CC-2015-0147, which is the card in your possession — that card was used to access the seventh floor at 22:47 last night. 10:47 p.m. Can you explain that?"),
        ("FUENTES:", "What? No. That's — I wasn't here at 10:47. I was at home. My girlfriend was with me."),
        ("DET. BREWER:", "Do you know where your card was last night before you came in at 4:15?"),
        ("FUENTES:", "In my jacket pocket. My work jacket — I had it at home."),
        ("DET. SANTOS:", "Could anyone else have had access to your card?"),
        ("FUENTES:", "No. I mean — not that I know of. I keep it in my jacket. That's where it always is."),
        ("DET. BREWER:", "We're going to want the contact information for your girlfriend so we can confirm your whereabouts last night. Is that all right?"),
        ("FUENTES:", "Yeah. Of course. Whatever you need."),
        ("DET. SANTOS:", "One more thing. When you found the door to Suite 712 unlocked — you said that was unusual. Had you ever had occasion to try that door before?"),
        ("FUENTES:", "No. I just assumed it would be locked because everything else up there is locked after hours. Maybe I'm wrong. But it seemed off."),
        ("DET. SANTOS:", "Okay. Thank you, Mr. Fuentes. We may have additional questions for you. Please don't leave the area without notifying us."),
        ("FUENTES:", "I understand. Am I — is there anything else right now?"),
        ("DET. SANTOS:", "That's all for now. We'll be in touch."),
    ]

    for spk, txt in exchanges:
        story.append(qa(spk, txt))

    story += [SP(8), HR(), SP(4)]
    story += [small("End of transcript. Duration of interview: approximately 1 hour 17 minutes. "
                    "Recording file: SFPD-AUDIO-2015-48801-001. Transcription reviewed and approved by Det. M.L. Santos.")]
    story += [SP(6)]
    story += [tbl([
        ["Witness Signature:", "______________________________", "Date:", "October 14, 2015"],
        ["Det. Santos (Badge #4471):", "______________________________", "Det. Brewer (Badge #3892):", "______________________________"],
    ], col_widths=[1.55 * inch, 2.30 * inch, 1.20 * inch, 1.50 * inch], has_hdr=False, alt=False)]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
