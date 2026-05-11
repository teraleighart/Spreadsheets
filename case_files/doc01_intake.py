"""Document 01 — ME Case Intake Face Sheet (1 page)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from aging import make_onpage, W, H, STAMP_R, STAMP_B, HW_BLUE
from styles import ST, HR, doc_header, section, subsection, body, body_l, small, SP, tbl, label_value_tbl

OUT = os.path.join(os.path.dirname(__file__))


def build():
    path = os.path.join(OUT, "ME-0447-01-Intake-Face-Sheet.pdf")

    aging = {
        'staple': True,
        1: {
            'rings': [
                (W - 1.35*inch, H - 1.10*inch, 38, 7, 0.21, 34),   # upper-right ring
            ],
            'creases': [
                (0, H*0.335, W, H*0.335 + 6, 21, 0.85),             # horizontal tri-fold crease
                (0, H*0.668, W, H*0.668 - 5, 22, 0.90),
            ],
            'foxing': {'count': 45, 'inten': 0.90},
            'stamps': [
                ("RECEIVED", W - 2.1*inch, H - 1.8*inch, -12, STAMP_R, 15, 0.58),
                ("ME JURISDICTION ACCEPTED", 1.05*inch, 1.20*inch, 4, STAMP_B, 9, 0.55),
            ],
            'hw': [
                ("SLK 10/14/15  0648", W - 2.2*inch, 1.42*inch, 0, HW_BLUE, 8),
                ("Priority-1 — Adeyemi", 1.05*inch, H - 0.80*inch, 2, HW_BLUE, 7.5),
            ],
            'smudges': [
                (3.1*inch, H - 2.8*inch, 55, 18, 3, 0.06),
            ],
        },
    }

    cb = make_onpage(101, "Intake Face Sheet", 1, aging)
    doc = SimpleDocTemplate(
        path, pagesize=letter,
        leftMargin=0.80*inch, rightMargin=0.80*inch,
        topMargin=0.75*inch,  bottomMargin=0.72*inch,
    )

    story = doc_header("DEATH INVESTIGATION CASE — INTAKE FACE SHEET",
                        "Case No. 2015-ME-0447  |  Date Opened: October 14, 2015  |  Priority: P-1 SUSPICIOUS")

    # ── SECTION A — Administrative Identifiers ──────────────────────────────
    story += [section("SECTION A — ADMINISTRATIVE IDENTIFIERS")]
    story += [tbl([
        ["ME Case Number:", "2015-ME-0447",              "Year / Sequential:", "2015 / 0447"],
        ["Date Case Opened:", "October 14, 2015",        "Time Case Opened:", "0312 hrs CDT"],
        ["Case Type:", "Unattended / Suspicious — Workplace", "Jurisdiction:", "Minnehaha County, SD"],
        ["Assigned Investigator:", "Sandra L. Kowalczyk, MSFS (MEI-09)", "Roster #:", "MEI-09"],
        ["Assigned Pathologist:", "Dr. Raymond G. Adeyemi, MD", "Autopsy Priority:", "Priority-1 (Suspicious)"],
        ["Law Enforcement Agency:", "Sioux Falls Police Dept. (SFPD)", "LE OCA #:", "SFPD-2015-48801"],
        ["LE Case Agent:", "Det. Marcus J. Orre, SFPD Investigations", "Agent Phone:", "(605) 367-7211 x3304"],
        ["EMS / Fire Agency:", "Sioux Falls Fire Rescue (SFFR) Sta. 1", "EMS Run #:", "SFFR-2015-19442"],
    ], col_widths=[1.55*inch, 1.85*inch, 1.55*inch, 1.55*inch], has_hdr=False)]

    # ── SECTION B — Decedent Identification ─────────────────────────────────
    story += [SP(4), section("SECTION B — DECEDENT IDENTIFICATION")]
    story += [tbl([
        ["Name (Last, First, Middle):", "Marsh, Eleanor Anne",       "Alias / Known As:", '"Ellie" (per colleagues at scene)'],
        ["Date of Birth:", "March 22, 1969",                         "Age at Death (est.):", "46 years"],
        ["Sex:", "Female",                                            "Race / Ethnicity:", "White / Non-Hispanic (per LE; unverified at intake)"],
        ["Height (estimated at scene):", "5 ft 6 in (approx.)",      "Weight (estimated at scene):", "Approx. 145–155 lbs (investigator estimate)"],
        ["SSN (last 4 only):", "XXX-XX-6214",                        "SSN Source:", "HR records, H&M Financial — per company counsel 0430 hrs"],
        ["Occupation:", "Chief Financial Officer (CFO)",              "Employer:", "Hartwell & Marsh Financial Partners, LLC"],
        ["Employer Address:", "4200 S. Western Ave., Ste. 700, Sioux Falls SD 57105",
                                                                      "Employer Phone:", "(605) 334-7200"],
        ["Residence Address:", "2814 Ridgecrest Drive, Sioux Falls, SD 57103",
                                                                      "Residence Confirmed By:", "SD DL on person; corroborated by LE"],
        ["Marital Status (at intake):", "Divorced (reported by coworkers; unconfirmed)",
                                                                      "Next of Kin (at intake):", "Thomas R. Marsh (adult son) — notified via SFPD approx. 0445"],
        ["ID Method — Primary:", "Visual ID by coworkers; SD Driver License recovered from purse on scene",
                                                                      "ID Method — Secondary:", "Fingerprints rolled postmortem; submitted SFPD AFIS 10/14/2015"],
        ["ID Formally Confirmed:", "PENDING — subject to fingerprint or secondary confirmation", "", ""],
    ], col_widths=[1.80*inch, 2.20*inch, 1.40*inch, 2.10*inch], has_hdr=False)]

    # ── SECTION C — Location of Death / Discovery ────────────────────────────
    story += [SP(4), section("SECTION C — LOCATION OF DEATH / DISCOVERY")]
    story += [tbl([
        ["Location Found:", "Private office, Suite 712, 7th Floor (SW corner), 4200 S. Western Ave., Sioux Falls, SD 57105",
         "Location Type:", "Commercial office bldg. — multi-tenant, privately owned"],
        ["Location of Death (if diff.):", "Presumed same as found; no evidence of pre-discovery transport — PENDING scene investigation",
         "County:", "Minnehaha"],
        ["Date Body Found:", "October 13, 2015 (approx. 2248 hrs CDT)",
         "Date/Time Pronounced:", "October 13, 2015 at 2303 hrs CDT — on scene, Suite 712"],
        ["Pronounced By:", "SFFR Paramedic Supervisor Thomas Kiedrowski, NRP (Cert. #SD-PM-4412)",
         "Resuscitation Attempted:", "NO — deceased on EMS arrival; no resuscitation indicated"],
        ["ME Jurisdiction Auth. By:", "S.L. Kowalczyk (MEI-09) following consult w/ Dr. Adeyemi at 0250 hrs",
         "Basis for ME Jurisdiction:", "Unattended; suspicious circumstances; no known treating physician; no apparent natural cause"],
        ["Death Certificate Auth.:", "Medical Examiner — per SD Codified Law §23-14-1 et seq.; accepted 0248 hrs 10/14/2015",
         "DC Status:", "NOT YET FILED — Cause & Manner DEFERRED pending autopsy and ancillary studies"],
    ], col_widths=[1.70*inch, 2.30*inch, 1.30*inch, 2.20*inch], has_hdr=False)]

    # ── SECTION D — Notification ─────────────────────────────────────────────
    story += [SP(4), section("SECTION D — INITIAL NOTIFICATION")]
    story += [tbl([
        ["Notified By:", "SFPD Patrol Dispatcher — Christine M. Dell (via ME after-hours dispatch line)",
         "Notification Date/Time:", "October 14, 2015 at 0248 hrs CDT"],
        ["Investigator On-Call:", "S.L. Kowalczyk, MSFS (MEI-09)",
         "Pathologist Notified:", "Dr. R.G. Adeyemi, MD — 0250 hrs (authorized scene response & case acceptance)"],
        ["Investigator Departed ME Office:", "0304 hrs",
         "Investigator Arrived at Scene:", "0321 hrs"],
        ["Chief ME Notified:", "Dr. Paula H. Reinholt, MD (Chief ME) — 0705 hrs via Dr. Adeyemi",
         "Chief ME Authorization:", "P-1 autopsy authorized; ME case acceptance confirmed"],
    ], col_widths=[1.80*inch, 2.40*inch, 1.40*inch, 1.90*inch], has_hdr=False)]

    # ── SECTION E — Body Receipt ─────────────────────────────────────────────
    story += [SP(4), section("SECTION E — BODY RECEIPT SUMMARY")]
    story += [tbl([
        ["Body Released from Scene By:", "Det. M.J. Orre (SFPD — scene authority)",
         "Release Time (approx.):", "October 14, 2015 — 0538 hrs CDT"],
        ["Transport Provider:", "Dakota Mortuary Transport Services (DMTS)",
         "DMTS Run #:", "DMTS-2015-10-14-007"],
        ["Transport Personnel:", "Curtis D. Halverson / Janel M. Tripp (DMTS)",
         "ME Seal Applied:", "YES — Seal #MEO-S-2015-3391 (applied on scene by MEI-09)"],
        ["Body Arrived ME Facility:", "October 14, 2015 — 0622 hrs CDT",
         "Received At Facility By:", "Mortuary Tech. Dennis H. Farr (MT-03)"],
        ["Seal Intact at Receipt:", "YES — verified by Farr and Kowalczyk jointly",
         "Discrepancies at Receipt:", "None noted at intake"],
        ["Storage Location:", "Cooler Bay C, Shelf 2 — tagged Case 2015-ME-0447",
         "Autopsy Scheduled:", "October 14, 2015 — 0900 hrs, Suite A"],
    ], col_widths=[1.80*inch, 2.30*inch, 1.40*inch, 2.00*inch], has_hdr=False)]

    # ── SECTION F — Property Summary ─────────────────────────────────────────
    story += [SP(4), section("SECTION F — PERSONAL EFFECTS / PROPERTY SUMMARY")]
    story += [tbl([
        ["Clothing Items (on body):", "6 items — blazer, blouse, slacks, undergarments ×2, shoes (1 pair)",
         "Jewelry / Accessories:", "4 items — earrings ×2, wristwatch, ring (see full inventory)"],
        ["Purse / Bag:", "1 leather structured handbag received; contents inventoried separately (11 items); ME hold pending NOK release auth.",
         "Currency / Cards:", "$43.00 cash; 3 credit/debit cards; SD DL; business card case — ME hold"],
        ["Items Retained by SFPD:", "Laptop, desk notepad, key fob, building access badge — NOT received by ME; refer SFPD evidence log",
         "Property Receipts:", "ME Receipt to SFPD: Form ME-PR-2015-0447\nSFPD Receipt to ME: SFPD-PROP-48801-A"],
    ], col_widths=[1.80*inch, 2.30*inch, 1.40*inch, 2.00*inch], has_hdr=False)]

    # ── SECTION G — Office Use Only ──────────────────────────────────────────
    story += [SP(4), section("SECTION G — OFFICE USE ONLY")]
    story += [tbl([
        ["Item", "Status", "Initials", "Date/Time", "Notes"],
        ["Face Sheet Completed",       "COMPLETE",             "SLK",     "10/14/2015 0648", "Entered by MEI-09"],
        ["Case Entered into MECS",     "COMPLETE",             "SLK",     "10/14/2015 0651", "ME case management system"],
        ["LE Liaison Confirmed",       "COMPLETE",             "SLK",     "10/14/2015",      "Det. Orre — primary LE contact"],
        ["NOK Notification (ME role)", "PENDING — LE primary", "—",       "—",               "SFPD conducting NOK notification; ME to follow up re: release auth."],
        ["Body Seal Verification",     "COMPLETE",             "DHF/SLK", "10/14/2015 0622", "Both parties confirmed seal intact"],
        ["Autopsy Authorized",         "COMPLETE",             "RGA/PHR", "10/14/2015 0705", "Authorized by Chief ME Reinholt"],
        ["Tox Submission",             "PENDING",              "—",       "—",               "Post-autopsy; same day as autopsy"],
        ["Histology Submission",       "PENDING",              "—",       "—",               "Awaiting block preparation"],
        ["Preliminary Report Issued",  "PENDING",              "—",       "—",               "Target: 5 business days post-autopsy"],
        ["Final Report / DC Filed",    "PENDING",              "—",       "—",               "DEFERRED — pending tox and histology"],
        ["County Attorney Notified",   "COMPLETE",             "SLK",     "10/14/2015 0712", "On-call rep acknowledged; no immediate action required"],
        ["DCI Notification",           "SFPD DETERMINATION",  "—",       "—",               "Det. Orre assessing independently; not ME function at this stage"],
        ["Case File Closed",           "OPEN",                 "—",       "—",               "Active investigation"],
    ], col_widths=[2.10*inch, 1.40*inch, 0.65*inch, 1.20*inch, 2.15*inch])]

    # ── Certification block ───────────────────────────────────────────────────
    story += [SP(8), HR(),
              body_l("INTAKE INVESTIGATOR CERTIFICATION: I certify that the information recorded on this face sheet is "
                     "accurate to the best of my knowledge based on information available at the time of intake, and that "
                     "the body was received and documented in accordance with Minnehaha County ME Office policies and "
                     "procedures (Policy ME-OPS-004, Rev. 2014)."),
              SP(4)]
    story += [tbl([
        ["Investigator Signature:", "________________________________",  "Date:", "10/14/2015", "Time:", "0648 hrs"],
        ["Print Name / Badge:",     "Sandra L. Kowalczyk, MSFS — MEI-09", "Reviewed By (Path.):", "Dr. R.G. Adeyemi", "Date:", "__________"],
    ], col_widths=[1.40*inch, 1.90*inch, 0.55*inch, 1.35*inch, 0.45*inch, 0.85*inch], has_hdr=False, alt=False)]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
