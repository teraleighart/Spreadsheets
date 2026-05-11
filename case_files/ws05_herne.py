"""WS-05 — Written Statement: Patrick Herne, Security Guard (1 page)."""
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
    path = os.path.join(OUT, "WS-05-Herne-Written-Statement.pdf")
    aging = {
        'staple': True,
        1: {
            'rings': [(W * 0.14, H * 0.35, 32, 251, 0.16, 82)],
            'creases': [(0, H * 0.59, W, H * 0.587, 252, 0.60)],
            'foxing': {'count': 22, 'inten': 0.76},
            'stamps': [("SFPD HOMICIDE — CASE FILE", 0.75 * inch, H * 0.09, 4, STAMP_B, 9, 0.50)],
            'hw': [("2247 = Fuentes card / not Fuentes ??", W - 3.4 * inch, H * 0.495, -2, STAMP_R, 7.5),
                   ("lobby gap — 22 min unobserved — JRB", 0.82 * inch, H * 0.455, 1, HW_BLUE, 7.0),
                   ("CCTV floor 7 offline — see Solis", W - 3.0 * inch, H * 0.37, 1, HW_PENCIL, 7.0)],
        },
    }
    cb = make_onpage(205, "WS-05 Herne", 1, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.80 * inch, rightMargin=0.80 * inch,
                            topMargin=0.75 * inch, bottomMargin=0.72 * inch)

    story = ws_header(
        "SWORN WRITTEN WITNESS STATEMENT — SECURITY PERSONNEL",
        "SFPD Case No. 2015-48801  |  ME Case No. 2015-ME-0447  |  MARSH, Eleanor Anne"
    )

    story += [tbl([
        ["Witness:", "Patrick James Herne", "DOB:", "March 7, 1986"],
        ["Address:", "519 N. Marion Rd., Sioux Falls, SD 57106", "Phone:", "(605) 214-5503"],
        ["Employer:", "Vector Security Solutions, Inc. (contracted to Meridian Property Group)", "Title:", "Security Officer"],
        ["Post:", "4200 S. Western Ave. — Lobby / Building Security", "Shift:", "1800–0600 (night)"],
        ["Statement Date:", "October 14, 2015", "Received By:", "Det. J.R. Brewer (Badge #3892)"],
    ], col_widths=[1.05 * inch, 3.00 * inch, 0.85 * inch, 1.65 * inch], has_hdr=False, alt=False)]

    story += [SP(5), section("STATEMENT")]

    paras = [
        ("I, Patrick James Herne, Security Officer employed by Vector Security Solutions, Inc., stationed at 4200 S. Western "
         "Avenue, Sioux Falls, SD, do hereby provide this sworn statement in connection with the death investigation "
         "at Suite 712 of this building."),

        ("I was on duty for the evening/overnight shift on October 13–14, 2015, from 1800 hours to 0600 hours. My post "
         "is the building lobby security desk. My responsibilities include monitoring the lobby, verifying contractor "
         "and after-hours access, maintaining the manual visitor log, and making periodic floor checks as time allows."),

        ("The following is a summary of relevant access events that I can confirm from the electronic badge access log "
         "printout provided to me by building management (Mr. Victor Solis) and from my personal recollection and "
         "manual visitor log entries:"),
    ]

    for p in paras:
        story += [body(p), SP(3)]

    story += [tbl([
        ["Time", "Card / Access Event", "Notes"],
        ["0814 hrs — Oct. 13", "Badge-in: Card #TE-712-001 (Eleanor Marsh, Suite 712 tenant card) — 7th floor elevator access", "Normal business-hours arrival; not noted as unusual"],
        ["No record — Oct. 13", "Badge-out: No record of Ms. Marsh's card being used to exit the building or the 7th floor on October 13, 2015", "Her card was not used to exit. Building also has a manual fire-stair exit (no card required from inside)."],
        ["2247 hrs — Oct. 13", "Badge-in: Card #CC-2015-0147 (Contractor card — assigned to Ramon Fuentes, Meridian Tech Solutions) — 7th floor elevator access", "ANOMALY: Mr. Fuentes had not yet signed in at my desk at this time. I was not at the lobby desk at approximately 2230–2252 hrs (see below). I did not personally observe anyone enter the elevator at 2247."],
        ["0417 hrs — Oct. 14", "Badge-in: Card #CC-2015-0147 (Ramon Fuentes) — 7th floor elevator access", "Mr. Fuentes arrived at my desk at approximately 0415–0416 hrs. He produced his contractor ID (Meridian Tech Solutions photo ID), signed the manual visitor log, and I confirmed his identity before he proceeded to the elevator. This is the standard contractor after-hours procedure."],
        ["0427 hrs — Oct. 14", "911 call placed — confirmed by dispatch notification to building phone", "Mr. Fuentes called me from upstairs via building phone shortly after 0427 to notify me that police were coming."],
    ], col_widths=[1.35 * inch, 3.60 * inch, 1.60 * inch])]

    story += [SP(4), body(
        "Regarding my absence from the lobby desk at approximately 2230–2252 hrs on October 13, 2015: I used "
        "the restroom during that interval. The men's restroom is approximately 40 feet from the lobby desk, "
        "down the south corridor. During this time, the lobby entrance is not physically monitored. The electronic "
        "badge system continues to function and log entries during any gap in my desk coverage. I was not aware "
        "of the 2247 access event until Mr. Solis provided me the access log printout this morning at the request "
        "of the police.")]

    story += [SP(4), body(
        "I have provided the manual visitor log for the evening of October 13–14, 2015 to Det. Brewer. "
        "The log reflects no entry for anyone accessing the 7th floor between 1800 hrs October 13 and "
        "Mr. Fuentes's arrival at 0415 hrs October 14, other than those entries noted above as electronic-badge-only "
        "(i.e., not passing my desk). I cannot explain why card #CC-2015-0147 was used at 2247 hrs if "
        "Mr. Fuentes was not present in the building at that time.")]

    story += [SP(4), HR(), SP(6)]
    story += [tbl([
        ["Declarant Signature:", "______________________________", "Date:", "October 14, 2015"],
        ["Print Name:", "Patrick J. Herne", "Badge / ID:", "VEC-SD-2015-0047"],
        ["Received By (SFPD):", "Det. J.R. Brewer", "Badge:", "#3892"],
    ], col_widths=[1.80 * inch, 2.20 * inch, 0.85 * inch, 1.70 * inch], has_hdr=False, alt=False)]

    story += [SP(4), small("I declare under penalty of perjury under the laws of the State of South Dakota that the foregoing is true "
                           "and correct to the best of my knowledge and belief.")]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
