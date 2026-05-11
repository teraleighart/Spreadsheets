"""CORR-01 — Letter: SFPD Det. Santos to ME Office, requesting expedited tox (1 page)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from aging import make_onpage, W, H, STAMP_B, HW_BLUE, HW_PENCIL, STAMP_R
from styles import ST, HR, body, small, SP

OUT = os.path.dirname(__file__)

INDENT = dict(leftIndent=0, rightIndent=0)


def ltr(text, style='body'):
    return Paragraph(text, ST['body'])


def ltr_small(text):
    return Paragraph(text, ST['small'])


def build():
    path = os.path.join(OUT, "CORR-01-SFPD-to-ME-Expedited-Tox-Request.pdf")
    aging = {
        'staple': False,
        1: {
            'rings': [],
            'creases': [(0, H * 0.42, W, H * 0.417, 501, 0.62),
                        (0, H * 0.70, W, H * 0.697, 502, 0.55)],
            'foxing': {'count': 14, 'inten': 0.65},
            'stamps': [("RECEIVED — ME OFFICE", W * 0.52, H * 0.89, -7, STAMP_B, 10, 0.52)],
            'hw': [("Oct 19 — responded — RGA", W - 2.4 * inch, H * 0.87, 2, HW_PENCIL, 7.5),
                   ("tox withheld — per protocol — RGA", W - 3.2 * inch, H * 0.325, -1, HW_PENCIL, 7.0)],
        },
    }
    cb = make_onpage(501, "CORR-01", 1, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=1.00 * inch, rightMargin=1.00 * inch,
                            topMargin=0.85 * inch, bottomMargin=0.85 * inch)

    story = [
        Paragraph('SIOUX FALLS POLICE DEPARTMENT', ST['doc_title']),
        Paragraph('Criminal Investigations Division — Homicide Unit', ST['doc_sub']),
        Paragraph('320 West 4th Street  •  Sioux Falls, SD 57104', ST['small']),
        Paragraph('Telephone: (605) 367-7212  •  Fax: (605) 367-8390', ST['small']),
        SP(10),
        HR(),
        SP(10),
        ltr('October 16, 2015'),
        SP(10),
        ltr('<b>Dr. Richard G. Adeyemi, MD</b>'),
        ltr('Forensic Pathologist'),
        ltr('Minnehaha County Medical Examiner\'s Office'),
        ltr('421 N. Western Ave., Suite 200'),
        ltr('Sioux Falls, SD 57104'),
        SP(8),
        ltr('<b>RE: Case No. SFPD-2015-48801 / ME Case No. 2015-ME-0447</b>'),
        ltr('<b>Decedent: MARSH, Eleanor Anne — Request for Expedited Toxicology Results</b>'),
        SP(8),
        ltr('Dear Dr. Adeyemi,'),
        SP(6),
    ]

    paras = [
        ("I am writing on behalf of the Sioux Falls Police Department Homicide Unit in connection with the above-referenced "
         "case, in which your office is conducting the forensic examination of Eleanor Anne Marsh, deceased, discovered "
         "October 14, 2015 at 4200 S. Western Ave., Suite 712, Sioux Falls, SD."),

        ("As you are aware, this matter has been classified by the SFPD as a suspicious death under active homicide "
         "investigation. Our investigation has developed several areas of significant concern, including an unexplained "
         "building access anomaly during the hours preceding discovery, an unidentified individual who met privately "
         "with the decedent on the afternoon of October 13, and electronic communications suggesting potential "
         "financial misconduct that may bear on motive. These circumstances collectively make expedited resolution "
         "of the toxicological analysis a high investigative priority."),

        ("During a brief conversation with your office on October 15, 2015, I was advised by a staff member — I "
         "believe it was your laboratory director — that toxicology results had been completed and were described "
         "as 'clinically significant.' I understand the ME's Office has established protocols regarding the release "
         "of toxicological findings in conjunction with the final autopsy report, and I respect the integrity of "
         "that process. However, I would respectfully request the following:"),

        ("First, that you provide the SFPD with the earliest possible estimate for issuance of the final autopsy "
         "report, or alternatively, an interim release of toxicological findings under a confidentiality agreement, "
         "if your office's protocols permit such accommodation in active homicide investigations."),

        ("Second, and recognizing that it may not be appropriate to characterize findings informally, I would "
         "ask whether you are in a position to advise whether the toxicological findings are consistent with "
         "or inconsistent with natural causes — without disclosing specifics — so that our investigative "
         "prioritization can be appropriately calibrated."),

        ("I am available at your convenience to discuss this request by telephone or in person. I can be reached "
         "at (605) 367-7212, extension 441, or by cellular at (605) 521-0884. I appreciate your office's "
         "cooperation throughout this investigation and look forward to hearing from you."),
    ]

    for p in paras:
        story += [ltr(p), SP(6)]

    story += [
        SP(4),
        ltr('Respectfully submitted,'),
        SP(18),
        ltr('<b>Detective Maria L. Santos</b>'),
        ltr('Badge No. 4471 — Homicide Unit'),
        ltr('Sioux Falls Police Department'),
        SP(6),
        ltr('cc: Det. J.R. Brewer (Badge #3892)'),
        ltr('    Lt. C.A. Vasquez, Homicide Unit Supervisor'),
        ltr('    SFPD Case File 2015-48801'),
        SP(6),
        HR(),
        SP(4),
        ltr_small('SFPD Homicide Unit — Case Correspondence — SFPD-2015-48801-CORR-001 — October 16, 2015'),
    ]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
