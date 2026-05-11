"""CORR-02 — Letter: ME Office Dr. Adeyemi to SFPD Det. Santos, tox withholding response (1 page)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph
from aging import make_onpage, W, H, STAMP_B, HW_BLUE, HW_PENCIL, STAMP_R
from styles import ST, HR, small, SP

OUT = os.path.dirname(__file__)


def ltr(text):
    return Paragraph(text, ST['body'])


def ltr_small(text):
    return Paragraph(text, ST['small'])


def build():
    path = os.path.join(OUT, "CORR-02-ME-to-SFPD-Tox-Response.pdf")
    aging = {
        'staple': False,
        1: {
            'rings': [(W * 0.81, H * 0.48, 30, 511, 0.13, 76)],
            'creases': [(0, H * 0.38, W, H * 0.377, 512, 0.60),
                        (0, H * 0.67, W, H * 0.667, 513, 0.52)],
            'foxing': {'count': 12, 'inten': 0.62},
            'stamps': [("RECEIVED — SFPD HOMICIDE", W * 0.51, H * 0.89, 5, STAMP_B, 10, 0.52)],
            'hw': [("\"clinically significant\" — he won't say more — MLS", W - 4.0 * inch, H * 0.475, -1, HW_BLUE, 7.5),
                   ("brain fixation = Nov?? too slow", 0.82 * inch, H * 0.345, 1, HW_PENCIL, 7.0)],
        },
    }
    cb = make_onpage(511, "CORR-02", 1, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=1.00 * inch, rightMargin=1.00 * inch,
                            topMargin=0.85 * inch, bottomMargin=0.85 * inch)

    story = [
        Paragraph('MINNEHAHA COUNTY MEDICAL EXAMINER\'S OFFICE', ST['doc_title']),
        Paragraph('421 N. Western Ave., Suite 200  •  Sioux Falls, SD 57104', ST['doc_sub']),
        Paragraph('Telephone: (605) 367-4060  •  Fax: (605) 367-4061', ST['small']),
        Paragraph('Dr. Patricia Okonkwo, Chief Medical Examiner  •  Dr. R.G. Adeyemi, Associate ME', ST['small']),
        SP(10),
        HR(),
        SP(10),
        ltr('October 19, 2015'),
        SP(10),
        ltr('<b>Detective Maria L. Santos</b>'),
        ltr('Badge No. 4471 — Homicide Unit'),
        ltr('Sioux Falls Police Department'),
        ltr('320 West 4th Street'),
        ltr('Sioux Falls, SD 57104'),
        SP(8),
        ltr('<b>RE: ME Case No. 2015-ME-0447 / SFPD Case No. 2015-48801</b>'),
        ltr('<b>Decedent: MARSH, Eleanor Anne — Response to October 16 Correspondence</b>'),
        SP(8),
        ltr('Dear Detective Santos,'),
        SP(6),
    ]

    paras = [
        ("Thank you for your letter of October 16, 2015, and for the professional manner in which you and "
         "Detective Brewer have conducted this investigation in coordination with our office. I write to address "
         "your two specific requests and to provide an updated timeline as best I am able."),

        ("Regarding your first request — an estimate for the final autopsy report or an interim release of "
         "toxicological findings — I must respectfully advise that an interim release is not possible under "
         "the protocols of this office, and I want to be direct about my reasons. The toxicological findings "
         "in this case require interpretive context that I cannot responsibly provide in isolation. "
         "The significance of any particular analyte — whether in terms of concentration, timing, or "
         "physiological effect — is inseparable from the totality of the autopsy findings, the decedent's "
         "documented medical history, the postmortem interval, and the circumstances of discovery. "
         "To release numerical results without that interpretive framework risks either alarming or "
         "misdirecting your investigation in ways I am not willing to risk."),

        ("I can tell you that the neuropathological component of this case — specifically the brain sections "
         "referenced in our preliminary report — remains pending adequate formalin fixation. I anticipate "
         "brain sections will be ready for processing no earlier than the final week of October. Histological "
         "review and reporting will follow, with an estimated completion in mid to late November 2015. "
         "The final autopsy report, inclusive of all ancillary studies and the toxicological correlation, "
         "will be issued as a single document upon completion of all components."),

        ("Regarding your second request — whether I can advise informally whether the toxicological findings "
         "are consistent or inconsistent with natural causes — I have considered this carefully. I am not "
         "in a position to make that characterization at this time, and I want to be honest that my "
         "reluctance is substantive rather than procedural. The findings are not straightforward, and any "
         "informal characterization I offered today might require revision when viewed in the full context "
         "of this case. I believe a partial answer would do more harm than good to your investigation. "
         "I ask for your patience and assure you the final report will be thorough."),

        ("I recognize that this timeline creates real difficulty for your investigation and I do not take "
         "that lightly. If it would be useful, I am available to meet with you and Detective Brewer in person "
         "to discuss the general parameters of the case in terms that do not compromise the integrity of "
         "the final report. Please contact my office to schedule such a meeting if you feel it would be "
         "helpful. I remain committed to full cooperation with the Department."),
    ]

    for p in paras:
        story += [ltr(p), SP(6)]

    story += [
        SP(4),
        ltr('Yours sincerely,'),
        SP(18),
        ltr('<b>Dr. Richard G. Adeyemi, MD</b>'),
        ltr('Associate Medical Examiner'),
        ltr('Minnehaha County Medical Examiner\'s Office'),
        SP(6),
        ltr('cc: Dr. P. Okonkwo, Chief Medical Examiner'),
        ltr('    ME Case File 2015-ME-0447'),
        SP(6),
        HR(),
        SP(4),
        ltr_small('ME Office — Correspondence — ME-0447-CORR-002 — October 19, 2015'),
    ]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
