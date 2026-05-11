"""CORR-03 — Letter: ME Chief Okonkwo to Minnehaha County DA, formal suspicious death notice (1 page)."""
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
    path = os.path.join(OUT, "CORR-03-ME-to-DA-Suspicious-Death-Notice.pdf")
    aging = {
        'staple': False,
        1: {
            'rings': [],
            'creases': [(0, H * 0.45, W, H * 0.447, 521, 0.58),
                        (0, H * 0.73, W, H * 0.727, 522, 0.50)],
            'foxing': {'count': 10, 'inten': 0.60},
            'stamps': [("RECEIVED — DA OFFICE", W * 0.52, H * 0.89, -6, STAMP_B, 10, 0.52),
                       ("ASSIGNED — FIN. CRIMES UNIT", W * 0.50, H * 0.083, 4, STAMP_B, 8, 0.46)],
            'hw': [("see also EV-J — email subpoena — MLS", W - 3.6 * inch, H * 0.565, 1, HW_BLUE, 7.0),
                   ("Apex Fin. — Q3 review initiated 10/21", 0.82 * inch, H * 0.54, -1, HW_PENCIL, 7.0)],
        },
    }
    cb = make_onpage(521, "CORR-03", 1, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=1.00 * inch, rightMargin=1.00 * inch,
                            topMargin=0.85 * inch, bottomMargin=0.85 * inch)

    story = [
        Paragraph('MINNEHAHA COUNTY MEDICAL EXAMINER\'S OFFICE', ST['doc_title']),
        Paragraph('421 N. Western Ave., Suite 200  •  Sioux Falls, SD 57104', ST['doc_sub']),
        Paragraph('Telephone: (605) 367-4060  •  Fax: (605) 367-4061', ST['small']),
        SP(10),
        HR(),
        SP(10),
        ltr('October 15, 2015'),
        SP(10),
        ltr('<b>The Honorable Sandra K. Burrell</b>'),
        ltr('Minnehaha County State\'s Attorney'),
        ltr('Minnehaha County Courthouse, Suite 310'),
        ltr('415 N. Dakota Ave.'),
        ltr('Sioux Falls, SD 57104'),
        SP(8),
        ltr('<b>RE: Formal Notification — Suspicious / Undetermined Death</b>'),
        ltr('<b>ME Case No. 2015-ME-0447 — MARSH, Eleanor Anne — DOB 03/22/1969</b>'),
        SP(8),
        ltr('Dear State\'s Attorney Burrell,'),
        SP(6),
    ]

    paras = [
        ("Pursuant to South Dakota Codified Law and the established protocols between this office and the "
         "Minnehaha County State's Attorney's Office, I write to formally notify you of a death under "
         "investigation by the Medical Examiner's Office and the Sioux Falls Police Department that we "
         "believe warrants your office's awareness and potential involvement."),

        ("On October 14, 2015, this office assumed jurisdiction over the body of Eleanor Anne Marsh, "
         "female, date of birth March 22, 1969, age 46, discovered deceased in her place of business "
         "at 4200 S. Western Ave., Suite 712, Sioux Falls, SD. Autopsy was performed the same day by "
         "Dr. R.G. Adeyemi, Associate Medical Examiner. Cause and manner of death have been deferred "
         "pending completion of toxicological analysis, neuropathological review, and ancillary histological "
         "studies. A final autopsy report is anticipated in mid to late November 2015."),

        ("The circumstances of Ms. Marsh's death have been deemed suspicious by the SFPD Homicide Unit "
         "(case number SFPD-2015-48801, assigned to Det. M.L. Santos). My office concurs that the "
         "circumstances do not support a straightforward natural death conclusion at this time. "
         "I am not in a position to characterize the toxicological findings further pending completion "
         "of the full case review, but I believe your office should be apprised of this matter now "
         "rather than upon issuance of the final report."),

        ("Additionally, I understand that the SFPD investigation has developed information suggesting "
         "potential financial irregularities at the decedent's place of employment, Apex Financial "
         "Group, Inc. The decedent apparently communicated concerns about financial reporting accuracy "
         "to a senior colleague in the hours before her death. While financial matters are outside "
         "the Medical Examiner's purview, I note this context because it may be relevant to the "
         "question of manner of death and because your office's Financial Crimes Unit may have "
         "independent jurisdiction to investigate regardless of the outcome of the death investigation."),

        ("I am available to brief you or your designee at your convenience and will provide the final "
         "autopsy report and all associated ME records to your office promptly upon completion. "
         "I respectfully request that any inquiries regarding the status of the medical examination "
         "be directed to this office rather than to the SFPD, to ensure that investigative integrity "
         "is maintained."),
    ]

    for p in paras:
        story += [ltr(p), SP(6)]

    story += [
        SP(4),
        ltr('Respectfully,'),
        SP(18),
        ltr('<b>Dr. Patricia A. Okonkwo, MD, JD</b>'),
        ltr('Chief Medical Examiner'),
        ltr('Minnehaha County Medical Examiner\'s Office'),
        SP(6),
        ltr('cc: Dr. R.G. Adeyemi, Associate ME'),
        ltr('    Det. M.L. Santos, SFPD Homicide Unit'),
        ltr('    ME Case File 2015-ME-0447'),
        SP(6),
        HR(),
        SP(4),
        ltr_small('ME Office — Correspondence — ME-0447-CORR-003 — October 15, 2015'),
    ]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
