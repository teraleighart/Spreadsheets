"""PR-02 — SFPD Detective Supplemental / Case Summary Report (3 pages)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph
from aging import make_onpage, W, H, STAMP_B, HW_BLUE, HW_PENCIL, STAMP_R
from styles import ST, HR, section, body, small, SP, tbl

OUT = os.path.dirname(__file__)


def pr_header():
    return [
        Paragraph('SIOUX FALLS POLICE DEPARTMENT', ST['doc_title']),
        Paragraph('320 West 4th Street  •  Sioux Falls, SD 57104  •  (605) 367-7212', ST['doc_sub']),
        Paragraph('SUPPLEMENTAL INVESTIGATION REPORT — DETECTIVE CASE SUMMARY', ST['sec_head']),
        SP(3),
        HR(),
    ]


def build():
    path = os.path.join(OUT, "PR-02-Detective-Case-Summary.pdf")
    aging = {
        'staple': True,
        1: {
            'rings': [(W * 0.13, H * 0.77, 40, 311, 0.19, 100)],
            'creases': [(0, H * 0.44, W, H * 0.437, 312, 0.68)],
            'foxing': {'count': 26, 'inten': 0.80},
            'stamps': [("SFPD RECORDS — CASE FILE COPY", 0.75 * inch, H * 0.09, 3, STAMP_B, 9, 0.48)],
            'hw': [("visitor ID — PRIORITY — MLS", W - 2.6 * inch, H * 0.615, -1, STAMP_R, 7.5),
                   ("badge anomaly — primary focus", 0.82 * inch, H * 0.53, 1, HW_BLUE, 7.0)],
        },
        2: {
            'rings': [(W * 0.80, H * 0.28, 30, 313, 0.14, 76)],
            'creases': [],
            'foxing': {'count': 18, 'inten': 0.70},
            'stamps': [],
            'hw': [("email = financial fraud?? — JRB", W - 2.8 * inch, H * 0.82, 2, HW_BLUE, 7.5),
                   ("USB not recovered — search desk again", 0.82 * inch, H * 0.625, -1, HW_PENCIL, 7.0),
                   ("Ellsworth motive? — review", W - 2.5 * inch, H * 0.525, 1, STAMP_R, 7.0)],
        },
        3: {
            'rings': [],
            'creases': [(0, H * 0.60, W, H * 0.597, 314, 0.52)],
            'foxing': {'count': 12, 'inten': 0.62},
            'stamps': [("ACTIVE INVESTIGATION — DO NOT RELEASE", 0.75 * inch, H * 0.09, -5, STAMP_R, 8, 0.55)],
            'hw': [("tox WITHHELD — awaiting correlation — RGA", W - 3.6 * inch, H * 0.42, 1, HW_PENCIL, 7.0),
                   ("Whitmore consult — did she ever call?", 0.82 * inch, H * 0.33, -1, HW_BLUE, 7.0)],
        },
    }
    cb = make_onpage(302, "PR-02 Detective Report", 3, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.80 * inch, rightMargin=0.80 * inch,
                            topMargin=0.75 * inch, bottomMargin=0.72 * inch)

    story = pr_header()

    story += [tbl([
        ["Case No.:", "SFPD-2015-48801", "ME Case No.:", "2015-ME-0447"],
        ["Classification:", "Suspicious Death — Homicide Investigation (open)", "Report No.:", "SUPP-001"],
        ["Decedent:", "MARSH, Eleanor Anne  |  DOB: 03/22/1969  |  Female / White", "Age:", "46"],
        ["Assigned Detective:", "Det. Maria L. Santos (Badge #4471)", "Partner:", "Det. James R. Brewer (Badge #3892)"],
        ["Supervisor:", "Lt. C.A. Vasquez, Homicide Unit", "Report Date:", "October 20, 2015"],
        ["Period Covered:", "October 14, 2015 — October 20, 2015 (initial case summary)", "", ""],
    ], col_widths=[1.10 * inch, 2.75 * inch, 1.10 * inch, 1.60 * inch])]

    story += [SP(5), section("SECTION A — CASE OVERVIEW")]
    story += [body(
        "This supplemental report summarizes investigative activity conducted by the Homicide Unit from the date of "
        "discovery of the decedent (October 14, 2015) through October 20, 2015. The decedent, Eleanor Anne Marsh, "
        "Chief Financial Officer of Apex Financial Group, Inc., was found deceased in her office at 4200 S. Western Ave., "
        "Suite 712, Sioux Falls, SD, at approximately 0427 hrs on October 14, 2015. She was discovered by Ramon Fuentes, "
        "an IT contractor, who called 911. Cause and manner of death remain under determination by the Minnehaha County "
        "Medical Examiner's Office; autopsy was conducted October 14, 2015 by Dr. R.G. Adeyemi. Preliminary anatomic "
        "diagnoses are documented in ME Case 2015-ME-0447; final cause and manner of death are deferred pending "
        "toxicology and ancillary study results.")]
    story += [SP(3), body(
        "The Homicide Unit assumed jurisdiction on the morning of October 14, 2015 based on circumstances deemed "
        "suspicious by the initial responding officers and the attending ME investigator. Specifically: (1) the decedent "
        "was a healthy 46-year-old professional with no known acute illness; (2) the entry door to Suite 712 was found "
        "unlocked with no explanation; (3) the electronic access log showed an anomalous use of a contractor's badge "
        "card during the hours preceding discovery; and (4) the decedent's electronic access card showed no exit from "
        "the building on October 13, 2015, consistent with her having remained in the building overnight.")]

    story += [SP(5), section("SECTION B — WITNESS CONTACTS")]
    story += [tbl([
        ["WS No.", "Witness", "Role", "Date / Format", "Status"],
        ["WS-01", "Ramon Fuentes", "IT contractor — discovery", "Oct. 14 — recorded interview", "Transcript complete; alibi for 22:47 hrs UNVERIFIED as of report date"],
        ["WS-02", "Linda Molander", "Office manager, Apex Financial", "Oct. 14 — recorded interview", "Transcript complete; key observations re: visitor and coffee mug"],
        ["WS-03", "Craig Ellsworth", "COO, Apex Financial", "Oct. 15 — written statement (w/ counsel)", "Received; email content not characterized; subpoena issued Oct. 16"],
        ["WS-04", "Diane Kowalski", "Executive assistant to decedent", "Oct. 14 — recorded interview", "Transcript complete; most substantive witness; key items flagged"],
        ["WS-05", "Patrick Herne", "Building security, Vector Security", "Oct. 14 — written statement", "Badge anomaly documented; corroborates access log"],
        ["WS-06", "Victor Solis", "Building manager, Meridian Property", "Oct. 14 — written statement", "Camera outage confirmed; contractor card scope confirmed"],
        ["WS-07", "Dr. Susan Taft, MD", "Treating physician — primary care", "Oct. 15 — phone interview", "Transcript complete; medical records subpoena filed Oct. 16"],
        ["WS-08", "Gregory T. Marsh", "Spouse of decedent", "Oct. 15 — in-person interview", "Transcript in preparation; cooperative; no known relevant information at this time"],
        ["PENDING", "Dr. James Whitmore", "Cardiologist (referral)", "Not yet contacted", "To contact re: whether consultation ever occurred — PENDING"],
        ["PENDING", "'Vren' (surname unknown)", "Unknown male visitor — Oct. 13", "Not identified", "PRIORITY — identity not established; no appointment on calendar; see Section D"],
    ], col_widths=[0.52 * inch, 1.35 * inch, 1.30 * inch, 1.30 * inch, 2.08 * inch])]

    story += [SP(5), section("SECTION C — EVIDENCE SUMMARY")]
    story += [tbl([
        ["Item", "Description", "Collected By", "Current Location / Status"],
        ["EV-A", "Ceramic coffee mug — desk surface, Suite 712", "SFPD CSU", "SFPD Property — submitted for latent print and residue analysis"],
        ["EV-B", "Open leather portfolio / notepad — desk surface", "SFPD CSU", "SFPD Property — handwriting/content analysis pending"],
        ["EV-C", "Decedent's handbag and contents", "SFPD CSU", "SFPD Property — inventory complete; no USB drive recovered"],
        ["EV-D", "Decedent's blouse — stain area", "ME Office", "ME Property — stain nature to be determined; histology pending"],
        ["EV-E", "Decedent's laptop (MacBook Pro)", "SFPD CSU", "SFPD Digital Forensics — imaging in progress; password recovery pending"],
        ["EV-F", "Kowalski personal notepad (Oct. 12–13 entries)", "Det. Santos", "SFPD Property — pages photographed and logged"],
        ["EV-G", "Building electronic access log — Oct. 13–14", "Solis / Det. Brewer", "SFPD Case File — certified copy obtained; original retained by building mgmt."],
        ["EV-H", "Lobby visitor log — Oct. 13–14", "Herne / Det. Brewer", "SFPD Case File — original obtained"],
        ["EV-I", "SFPD CSU scene photographs — 312 frames", "SFPD CSU", "SFPD Digital Evidence Server — Case 2015-48801"],
        ["EV-J", "Email: Marsh to Ellsworth, 23:47 Oct. 13", "Ellsworth (voluntary disclosure)", "SFPD Case File — content RESTRICTED — see Section D"],
        ["EV-K", "Building camera footage — lobby, garage (Oct. 13–14)", "Solis / SFPD", "SFPD Digital Evidence — under review; 7th floor camera non-operational"],
        ["NOT RECOV.", "USB drive (small, black, unlabeled) — described by Kowalski", "—", "Not located at scene, on decedent's person, or in handbag — STATUS UNKNOWN"],
    ], col_widths=[0.62 * inch, 2.15 * inch, 1.05 * inch, 2.73 * inch])]

    story += [SP(5), section("SECTION D — KEY INVESTIGATIVE ISSUES")]
    story += [body("The following issues have been identified as primary investigative priorities as of this report date:")]
    story += [SP(3)]

    issues = [
        ("1. BADGE ACCESS ANOMALY — 22:47 HRS OCTOBER 13, 2015.",
         "Electronic access records confirm that contractor card #CC-2015-0147, assigned to Ramon Fuentes, was used to "
         "access the 7th floor elevator at 22:47 hrs on October 13, 2015. Mr. Fuentes states he was at his residence "
         "at that time and did not use the card. His alibi (girlfriend, K. Varga — interviewed Oct. 15) is partially "
         "corroborating but not definitive; she confirmed he was home by 2200 hrs but states she was asleep by 2230 hrs. "
         "Card was reported in his possession throughout and shows no signs of damage or duplication. "
         "How the card was used at 22:47, and by whom, is the central unresolved question in this investigation. "
         "Request for technical analysis of card has been submitted to Lenel OnGuard system technician."),
        ("2. SUITE 712 DOOR — UNLOCKED UPON DISCOVERY.",
         "The main entry door to Suite 712 was found unlocked and standing open at the time of Fuentes's entry at "
         "approximately 0425 hrs and at officer arrival at 0434 hrs. Contractor card #CC-2015-0147 is confirmed NOT "
         "programmed for Suite 712 entry (confirmed by building manager Solis and Lenel system log). The decedent "
         "would normally have locked her office door upon being last to leave. Who unlocked or left the door unlocked — "
         "and when — has not been established. Suite 712 card access roster has been requested from Apex Financial."),
        ("3. UNKNOWN VISITOR — 'VREN' — OCTOBER 13, APPROX. 14:15 HRS.",
         "An unscheduled male visitor met with the decedent for approximately 40–45 minutes on the afternoon of "
         "October 13. Described as male, mid-40s, gray suit, no tie, foreign accent (Eastern European or German per "
         "witnesses). Did not provide a business card. Last name approximated as 'Vren' or similar by Kowalski. "
         "Decedent appeared shaken following the meeting. Identity of this individual has not been established. "
         "Lobby visitor log does not contain an entry matching this description for that time window — the visitor "
         "either did not sign in or entered via elevator badge without passing the desk. Building camera footage "
         "from the lobby is under review."),
        ("4. ELECTRONIC COMMUNICATION — MARSH TO ELLSWORTH, 23:47 HRS OCTOBER 13.",
         "The decedent sent an electronic mail message to COO Craig Ellsworth at 23:47 hrs on October 13, 2015, "
         "approximately 3.5 to 4 hours before discovery of her body. The message, voluntarily disclosed by Ellsworth, "
         "is approximately 340 words and references — without explicit detail — 'discrepancies that cannot be "
         "explained by accounting error,' 'a conversation we need to have before this goes further,' and 'I cannot "
         "continue to sign off on reports I no longer believe are accurate.' The content of this email is classified "
         "as restricted within this report pending further investigation and legal review. It has been provided to "
         "the Minnehaha County DA's Financial Crimes liaison for initial review. Its implications for motive and "
         "circumstances of death are under active assessment."),
        ("5. MISSING USB DRIVE.",
         "A small black USB drive, described as unlabeled and approximately 2cm in length, was sought by the decedent "
         "repeatedly in the days before her death, per Kowalski. It was not recovered at the scene, in the decedent's "
         "handbag, in her vehicle, or at her residence (initial consent search, Oct. 15 — husband cooperative). "
         "Content of the drive is unknown. Digital forensics is examining the decedent's laptop for any record "
         "of connected devices."),
        ("6. TOXICOLOGY — RESULTS WITHHELD PENDING PATHOLOGIST REVIEW.",
         "Per ME Dr. Adeyemi, toxicology results (ME Tox Lab Accession MCME-TOX-2015-0841) have been completed "
         "but are being withheld from this report pending correlation with autopsy findings. Det. Santos has been "
         "advised informally that results are 'clinically significant' but has not been provided specifics. "
         "Full results are expected to be released to the investigation upon issuance of the ME's final autopsy "
         "report. Cause and manner of death remain deferred."),
    ]

    for title, text in issues:
        story += [Paragraph(f'<b>{title}</b>', ST['body']), SP(2), body(text), SP(4)]

    story += [SP(3), section("SECTION E — PENDING ACTIONS")]
    story += [tbl([
        ["Action Item", "Assigned To", "Target Date", "Status"],
        ["Identify unknown visitor ('Vren') — lobby footage review; international inquiry if needed", "Det. Santos / Det. Brewer", "Oct. 25, 2015", "IN PROGRESS"],
        ["Obtain Apex Financial Suite 712 card access roster", "Det. Brewer", "Oct. 22, 2015", "PENDING — Ellsworth counsel reviewing"],
        ["Lenel card system technical analysis — card #CC-2015-0147 (duplication feasibility)", "Det. Santos / SFPD Tech", "Oct. 28, 2015", "PENDING"],
        ["Fuentes alibi — additional corroboration (cell tower ping, transit records)", "Det. Brewer", "Oct. 25, 2015", "IN PROGRESS"],
        ["Subpoena — Ellsworth personal email and company financial records", "DA Financial Crimes Liaison", "Filed Oct. 16", "PENDING court approval"],
        ["Medical records — Dr. Taft (subpoena ref. 2015-SR-0447-02)", "SFPD Legal", "Filed Oct. 16", "PENDING compliance"],
        ["Contact Dr. James Whitmore — cardiology referral follow-up", "Det. Santos", "Oct. 22, 2015", "NOT YET INITIATED"],
        ["Decedent's laptop digital forensics — password recovery, USB device history, email archive", "SFPD Digital Forensics", "Nov. 1, 2015 (est.)", "IN PROGRESS"],
        ["ME final autopsy report and toxicology release", "ME Dr. Adeyemi", "TBD (brain sections pending fixation)", "AWAITING ME OFFICE"],
        ["Spouse (Gregory Marsh) follow-up interview — financial affairs, insurance", "Det. Santos", "Oct. 28, 2015", "SCHEDULED"],
        ["Apex Financial Q3 financials — obtain for independent review", "DA Financial Crimes", "Pending subpoena", "PENDING"],
    ], col_widths=[2.55 * inch, 1.35 * inch, 0.98 * inch, 1.67 * inch])]

    story += [SP(5), HR(), SP(4)]
    story += [tbl([
        ["Prepared By:", "Det. M.L. Santos (Badge #4471)", "Date:", "October 20, 2015"],
        ["Co-Detective:", "Det. J.R. Brewer (Badge #3892)", "Date:", "October 20, 2015"],
        ["Reviewed By:", "Lt. C.A. Vasquez — Homicide Unit", "Date:", "October 21, 2015"],
        ["Case Status:", "ACTIVE — OPEN HOMICIDE INVESTIGATION", "", ""],
    ], col_widths=[1.10 * inch, 2.90 * inch, 0.65 * inch, 1.90 * inch])]

    story += [SP(4), small("This report contains information gathered in an active criminal investigation. Distribution is restricted "
                           "to authorized SFPD personnel, the Minnehaha County DA's Office, and the ME's Office on a need-to-know basis. "
                           "Unauthorized disclosure may compromise the investigation. All supplemental reports to follow under same case number.")]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
