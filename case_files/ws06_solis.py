"""WS-06 — Written Statement: Victor Solis, Building Manager (1 page)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph
from aging import make_onpage, W, H, STAMP_B, HW_BLUE, HW_PENCIL, STAMP_R
from styles import ST, HR, section, body, small, SP, tbl

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
    path = os.path.join(OUT, "WS-06-Solis-Written-Statement.pdf")
    aging = {
        'staple': True,
        1: {
            'rings': [],
            'creases': [(0, H * 0.52, W, H * 0.517, 261, 0.55), (0, H * 0.76, W, H * 0.757, 262, 0.48)],
            'foxing': {'count': 16, 'inten': 0.68},
            'stamps': [("SFPD HOMICIDE — CASE FILE", 0.75 * inch, H * 0.09, -2, STAMP_B, 9, 0.50)],
            'hw': [("camera \"out\" 3 days — convenient — MLS", W - 3.5 * inch, H * 0.595, 1, HW_BLUE, 7.5),
                   ("WO 2015-10-WO-1847 — obtain copy", 0.82 * inch, H * 0.57, -1, HW_PENCIL, 7.0),
                   ("suite 712 card reader — who has access cards?", W - 3.8 * inch, H * 0.46, 1, HW_BLUE, 7.0)],
        },
    }
    cb = make_onpage(206, "WS-06 Solis", 1, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.80 * inch, rightMargin=0.80 * inch,
                            topMargin=0.75 * inch, bottomMargin=0.72 * inch)

    story = ws_header(
        "SWORN WRITTEN WITNESS STATEMENT — BUILDING MANAGEMENT",
        "SFPD Case No. 2015-48801  |  ME Case No. 2015-ME-0447  |  MARSH, Eleanor Anne"
    )

    story += [tbl([
        ["Witness:", "Victor Manuel Solis", "DOB:", "November 19, 1971"],
        ["Address:", "1802 E. 26th St., Sioux Falls, SD 57105", "Phone:", "(605) 332-6614"],
        ["Employer:", "Meridian Property Group, LLC", "Title:", "Building Manager"],
        ["Property:", "4200 S. Western Ave., Sioux Falls, SD 57108", "Tenure:", "Since February 2012"],
        ["Statement Date:", "October 14, 2015", "Received By:", "Det. M.L. Santos (Badge #4471)"],
    ], col_widths=[1.05 * inch, 3.00 * inch, 0.85 * inch, 1.65 * inch], has_hdr=False, alt=False)]

    story += [SP(5), section("STATEMENT")]

    paras = [
        ("I, Victor Manuel Solis, Building Manager for Meridian Property Group, LLC at 4200 S. Western Avenue, Sioux "
         "Falls, SD, provide this sworn statement to the Sioux Falls Police Department in connection with the death "
         "investigation at Suite 712."),

        ("BUILDING ACCESS SYSTEM. The building uses an electronic proximity-card access system (Lenel OnGuard, installed 2013). "
         "The system controls: (1) all exterior building entry points; (2) elevator access to each floor; and (3) "
         "individual suite entry points where tenants have elected to install card readers. Apex Financial Group, "
         "Inc., tenant of Suite 712, elected to install a card reader on the main door of their suite at the time "
         "of their lease commencement in 2012. The Suite 712 card reader is on the Lenel system and requires a "
         "separately programmed card for entry — floor-level access (elevator) does not confer suite access. "
         "Contractor cards issued for floor access do not automatically grant suite access unless specifically "
         "programmed by building management at the tenant's written request."),

        ("CONTRACTOR CARD #CC-2015-0147. This card was issued on October 1, 2015 to Ramon Fuentes, Meridian Tech "
         "Solutions, LLC, for the duration of the Apex Financial server room maintenance project. The card provides "
         "7th floor elevator access and access to the dedicated server room door (SR-07-A). It does NOT provide "
         "access to Suite 712's main door. I have confirmed this with the Lenel system access control records. "
         "The card was not programmed for Suite 712 entry at any point."),

        ("7TH FLOOR HALLWAY CAMERA — STATUS. The 7th floor hallway camera (Camera ID: CAM-07-C, covering the "
         "corridor from the elevator to Suite 712 and the server room) was reported as malfunctioning on "
         "October 11, 2015 by a tenant on that floor. I submitted work order 2015-10-WO-1847 to our contracted "
         "AV maintenance vendor (Integra Systems) on October 12, 2015. As of the morning of October 14, 2015, "
         "the repair had not yet been scheduled. Camera CAM-07-C was therefore non-operational from "
         "approximately October 11, 2015 through at least October 14, 2015. Cameras in the lobby (CAM-01-A, "
         "CAM-01-B), parking garage (CAM-G-01 through CAM-G-04), and other floors were operational and "
         "recording during the relevant period. I am providing copies of all available footage to the Department."),

        ("SUITE 712 CARD ACCESS — TENANT-ISSUED CARDS. Apex Financial Group is responsible for managing "
         "the card access roster for Suite 712. Building management does not maintain records of individual "
         "tenant card assignments for interior suite access. Det. Santos should direct any inquiry about "
         "who holds programmed access to Suite 712's interior door to Apex Financial Group management or "
         "their facilities coordinator."),
    ]

    for p in paras:
        story += [body(p), SP(3)]

    story += [SP(4), HR(), SP(6)]
    story += [tbl([
        ["Declarant Signature:", "______________________________", "Date:", "October 14, 2015"],
        ["Print Name:", "Victor M. Solis", "", ""],
        ["Received By (SFPD):", "Det. M.L. Santos", "Badge:", "#4471"],
    ], col_widths=[1.80 * inch, 2.20 * inch, 0.85 * inch, 1.70 * inch], has_hdr=False, alt=False)]

    story += [SP(4), small("I declare under penalty of perjury under the laws of the State of South Dakota that the foregoing is true "
                           "and correct to the best of my knowledge and belief.")]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
