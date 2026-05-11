"""WS-03 — Written Statement: Craig Ellsworth, COO (1 page)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph
from aging import make_onpage, W, H, STAMP_B, HW_BLUE, HW_PENCIL, STAMP_R
from styles import ST, HR, section, body, body_l, small, SP, tbl

OUT = os.path.dirname(__file__)


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
    path = os.path.join(OUT, "WS-03-Ellsworth-Written-Statement.pdf")
    aging = {
        'staple': True,
        1: {
            'rings': [],
            'creases': [(0, H * 0.40, W, H * 0.397, 231, 0.58), (0, H * 0.72, W, H * 0.717, 232, 0.52)],
            'foxing': {'count': 18, 'inten': 0.70},
            'stamps': [("SFPD HOMICIDE — CASE FILE", 0.75 * inch, H * 0.09, 2, STAMP_B, 9, 0.50),
                       ("SWORN STATEMENT", W * 0.55, H * 0.88, -8, STAMP_B, 13, 0.45)],
            'hw': [("email content — see subpoena JRB", W - 3.0 * inch, H * 0.345, -1, HW_BLUE, 7.5),
                   ("too composed — MLS", 0.82 * inch, H * 0.31, 1, HW_PENCIL, 7.0)],
        },
    }
    cb = make_onpage(203, "WS-03 Ellsworth", 1, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.80 * inch, rightMargin=0.80 * inch,
                            topMargin=0.75 * inch, bottomMargin=0.72 * inch)

    story = ws_header(
        "SWORN WRITTEN WITNESS STATEMENT",
        "SFPD Case No. 2015-48801  |  ME Case No. 2015-ME-0447  |  MARSH, Eleanor Anne"
    )

    story += [tbl([
        ["Witness:", "Craig Daniel Ellsworth", "DOB:", "September 11, 1964"],
        ["Address:", "5502 E. Tallgrass Pkwy., Sioux Falls, SD 57110", "Phone:", "(605) 334-8821"],
        ["Employer:", "Apex Financial Group, Inc.", "Title:", "Chief Operating Officer"],
        ["Statement Date:", "October 15, 2015", "Submitted Via:", "Personal delivery — attn. Det. M.L. Santos"],
        ["Prepared With:", "Thomas R. Hennessey, Esq. (counsel — present during preparation)", "", ""],
    ], col_widths=[1.05 * inch, 3.00 * inch, 0.85 * inch, 1.65 * inch], has_hdr=False, alt=False)]

    story += [SP(5), section("STATEMENT")]

    paras = [
        ("I, Craig Daniel Ellsworth, Chief Operating Officer of Apex Financial Group, Inc., do hereby voluntarily provide "
         "this written statement to the Sioux Falls Police Department in connection with the death of Eleanor Anne Marsh, "
         "my colleague and the company's Chief Financial Officer."),

        ("I have been employed by Apex Financial Group since March 2010. Ms. Marsh joined the company in January 2011. "
         "For the duration of her tenure, she reported directly to me on financial matters, and she and I maintained "
         "a professional and collegial working relationship. I have no personal information about Ms. Marsh's private "
         "life beyond what is generally known within our organization."),

        ("On the afternoon of October 13, 2015, at approximately 4:30 p.m., I met with Ms. Marsh in her office at "
         "Suite 712, 4200 S. Western Ave. The purpose of the meeting was a scheduled review of fourth-quarter financial "
         "projections and year-end planning matters. The meeting lasted approximately 45 minutes. At its conclusion, "
         "Ms. Marsh appeared professionally engaged and focused, as was entirely typical of her. I said goodnight and "
         "left the building at approximately 5:25 p.m. To my knowledge, that was the last time I saw Ms. Marsh alive."),

        ("Late on the evening of October 13, 2015, at approximately 11:47 p.m., I received an electronic mail message "
         "from Ms. Marsh's company email address. I did not read that message until the morning of October 14, 2015, "
         "at approximately 8:10 a.m., at which time I had already received a telephone call from a detective with the "
         "Sioux Falls Police Department notifying me of Ms. Marsh's death. "
         "The content of that electronic communication has been provided in full to the Sioux Falls Police Department "
         "pursuant to a voluntary disclosure, and I will not characterize or summarize it further in this statement "
         "on the advice of counsel. I wish to be clear that I have cooperated fully with the Department's request for "
         "that record."),

        ("I learned of Ms. Marsh's death on the morning of October 14, 2015, when I received a call from Det. Maria Santos "
         "of the Sioux Falls Police Department at approximately 8:05 a.m. I subsequently notified the company's board "
         "chair and contacted legal counsel. I have directed all Apex Financial personnel to cooperate fully with "
         "the investigation and to make company records available upon proper request."),

        ("I am not aware of any person who may have wished harm upon Ms. Marsh, nor am I aware of any circumstances "
         "that would explain her death. I am prepared to answer additional questions from the Department through "
         "counsel and will make myself available at a mutually agreeable time."),
    ]

    for p in paras:
        story += [body(p), SP(4)]

    story += [SP(4), HR(), SP(6)]
    story += [tbl([
        ["Declarant Signature:", "______________________________", "Date:", "October 15, 2015"],
        ["Print Name:", "Craig D. Ellsworth", "", ""],
        ["Counsel (present during preparation):", "Thomas R. Hennessey, Esq. — Hennessey & Farr LLP", "", ""],
        ["Received By (SFPD):", "______________________________", "Badge:", "____________"],
    ], col_widths=[2.00 * inch, 2.60 * inch, 0.65 * inch, 1.30 * inch], has_hdr=False, alt=False)]

    story += [SP(4), small("I declare under penalty of perjury under the laws of the State of South Dakota that the foregoing is true and correct "
                           "to the best of my knowledge and belief.")]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
