"""ANSWER KEY — Sealed solution document (3 pages: cover + 2 solution pages)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import Color
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, PageBreak
from reportlab.pdfgen.canvas import Canvas
from aging import make_onpage, W, H, STAMP_B, HW_BLUE, HW_PENCIL, STAMP_R, aged_bg, rubber_stamp, hw_note
from styles import ST, HR, section, body, small, SP, tbl

OUT = os.path.dirname(__file__)

RED   = STAMP_R
BLUE  = STAMP_B
BLACK = Color(0.06, 0.06, 0.06)


def cover_page(c, doc):
    """Render the sealed cover page entirely via canvas."""
    aged_bg(c, seed=999)

    # Heavy border
    c.setStrokeColor(Color(0.35, 0.10, 0.10, alpha=0.85))
    c.setLineWidth(4)
    c.rect(0.40 * inch, 0.40 * inch, W - 0.80 * inch, H - 0.80 * inch, fill=0, stroke=1)
    c.setLineWidth(1.5)
    c.rect(0.52 * inch, 0.52 * inch, W - 1.04 * inch, H - 1.04 * inch, fill=0, stroke=1)

    # Case header
    c.setFillColor(BLACK)
    c.setFont('Courier-Bold', 11)
    c.drawCentredString(W / 2, H - 1.30 * inch, 'CASE NO. 2015-ME-0447 / SFPD-2015-48801')
    c.setFont('Courier', 9)
    c.drawCentredString(W / 2, H - 1.52 * inch, 'MARSH, Eleanor Anne  |  DOB: 03/22/1969')

    # Main seal text
    c.setFont('Courier-Bold', 28)
    c.setFillColor(Color(0.60, 0.08, 0.06, alpha=0.88))
    c.drawCentredString(W / 2, H * 0.62, 'SEALED')

    c.setFont('Courier-Bold', 13)
    c.drawCentredString(W / 2, H * 0.55, 'SOLUTION DOCUMENT')

    c.setFont('Courier', 9)
    c.setFillColor(BLACK)
    for i, line in enumerate([
        'This envelope contains the complete case solution.',
        'Open only after your investigation is complete.',
        'Reading this document before completing your investigation',
        'will irreversibly alter your experience of the case.',
    ]):
        c.drawCentredString(W / 2, H * 0.48 - i * 14, line)

    # Stamps
    rubber_stamp(c, 'DO NOT OPEN — CASE ACTIVE', W * 0.30, H * 0.35, -8, RED, 11, 0.70)
    rubber_stamp(c, 'DO NOT OPEN — CASE ACTIVE', W * 0.65, H * 0.32, 6,  RED, 11, 0.65)
    rubber_stamp(c, 'SOLUTION — AUTHORIZED EYES ONLY', W * 0.48, H * 0.22, -3, BLUE, 9, 0.62)

    # Handwritten
    hw_note(c, 'when you are ready — open here', W * 0.27, H * 0.135, -2, HW_PENCIL, 8.5)

    # Footer
    c.setFont('Courier', 7)
    c.setFillColor(Color(0.30, 0.25, 0.18, alpha=0.70))
    c.drawCentredString(W / 2, 0.55 * inch,
                        'Minnehaha County ME / SFPD Homicide Unit — Case File 2015-ME-0447 — Solution Document')


def build():
    path = os.path.join(OUT, "ANSWER-KEY-Sealed-Solution-Document.pdf")

    # Page 1 aging (cover — lots of stamps, no table content)
    aging_p2 = {
        'rings': [(W * 0.14, H * 0.70, 38, 991, 0.18, 95)],
        'creases': [(0, H * 0.44, W, H * 0.437, 992, 0.68)],
        'foxing': {'count': 30, 'inten': 0.85},
        'stamps': [("MINNEHAHA COUNTY ME — FINAL", 0.75 * inch, H * 0.09, -3, BLUE, 9, 0.52)],
        'hw': [("tox confirmed — digoxin — RGA — 11/22/2015", W - 3.8 * inch, H * 0.87, 1, HW_PENCIL, 7.5),
               ("HOMICIDE — arrest warrant issued 12/04", 0.82 * inch, H * 0.87, -1, STAMP_R, 7.5)],
    }
    aging_p3 = {
        'rings': [(W * 0.81, H * 0.35, 32, 993, 0.15, 82)],
        'creases': [],
        'foxing': {'count': 20, 'inten': 0.75},
        'stamps': [("CASE CLOSED — HOMICIDE", W * 0.52, H * 0.09, 4, RED, 11, 0.58)],
        'hw': [("Ellsworth arraigned 12/08 — held w/o bail — MLS", W - 4.0 * inch, H * 0.86, 1, HW_PENCIL, 7.0)],
    }

    full_aging = {
        'staple': True,
        2: aging_p2,
        3: aging_p3,
    }

    # onPage callback: page 1 = cover_page, pages 2+ = aged_cb
    aged_cb = make_onpage(998, "Answer Key", 3, full_aging)

    def on_page(c, doc):
        if doc.page == 1:
            cover_page(c, doc)
        else:
            aged_cb(c, doc)

    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.80 * inch, rightMargin=0.80 * inch,
                            topMargin=0.75 * inch, bottomMargin=0.72 * inch)

    # Pages 2–3 content
    story = [
        PageBreak(),

        Paragraph('MINNEHAHA COUNTY MEDICAL EXAMINER\'S OFFICE', ST['doc_title']),
        Paragraph('Sioux Falls Police Department — Homicide Unit', ST['doc_sub']),
        Paragraph('FINAL CASE RESOLUTION SUMMARY', ST['sec_head']),
        SP(2),
        Paragraph('Case No. 2015-ME-0447 / SFPD-2015-48801  |  MARSH, Eleanor Anne  |  FOR SOLUTION REFERENCE ONLY', ST['small']),
        SP(3),
        HR(),
    ]

    story += [tbl([
        ["ME Final Report Issued:", "November 22, 2015", "Case Status:", "CLOSED — HOMICIDE"],
        ["Cause of Death:", "Acute digoxin toxicity", "Manner of Death:", "HOMICIDE"],
        ["Pathologist:", "Dr. R.G. Adeyemi, MD — Minnehaha County ME", "Signed:", "November 22, 2015"],
        ["Arrest:", "Craig Daniel Ellsworth — December 4, 2015", "Charges:", "First-Degree Murder; Securities Fraud; Embezzlement"],
        ["Arraigned:", "December 8, 2015 — Minnehaha County Circuit Court", "Bond:", "Denied — held without bail"],
    ], col_widths=[1.25 * inch, 2.45 * inch, 1.15 * inch, 1.70 * inch])]

    story += [SP(5), section("WHAT HAPPENED — FULL CASE NARRATIVE")]
    story += [body(
        "Eleanor Marsh had been CFO of Apex Financial Group for four years when, in August 2015, she identified "
        "anomalies in the Q3 client account reconciliations that could not be explained by accounting error. "
        "Over six weeks she quietly reconstructed a parallel set of transactions — a shadow ledger — that "
        "revealed COO Craig Ellsworth had been systematically diverting client investment funds through a "
        "network of shell accounts for approximately eighteen months, embezzling in excess of $4.1 million. "
        "The evidence she assembled — account records, wire transfer confirmations, and internal emails "
        "that Ellsworth apparently believed were deleted — was stored on a small black USB drive she kept "
        "in her desk drawer. She labeled the paper folder on her desk 'Q3 — parallel.' She told no one "
        "except her attorney.")]
    story += [SP(3), body(
        "On October 13, 2015, Eleanor met with Heinrich Vrenner, Esq., a financial crimes and "
        "whistleblower attorney she had retained in secret two weeks earlier. Vrenner advised her that "
        "her findings constituted a serious securities violation, that she had potential personal legal "
        "exposure if she delayed reporting, and that she should go to regulators within 48 hours. "
        "After Vrenner left, Eleanor returned to her desk. She was frightened but resolved. At 11:47 p.m. "
        "she emailed Ellsworth — not to threaten him, but because she still believed he might do the "
        "right thing. The email told him she had found the parallel accounts, that she could not continue "
        "to sign off on reports she knew to be false, and that she intended to contact the SEC and the "
        "South Dakota Division of Banking the following morning unless he contacted her first.")]
    story += [SP(3), body(
        "Ellsworth read the email that night. He did not call. Instead, he drove to the office.")]
    story += [SP(3), body(
        "Ellsworth had his own Suite 712 access card. He entered the building through the lobby — "
        "Patrick Herne was briefly away from his desk — using a duplicate contractor card he had arranged "
        "as a potential red herring (a copy of Ramon Fuentes's card, made from the card's RFID data "
        "during a moment when Fuentes had left it unattended during a bathroom break the previous week). "
        "That duplicate generated the 22:47 badge entry attributed to 'Fuentes.' Ellsworth then used "
        "his own Suite 712 card to enter the office. Eleanor was at her desk. He was calm. He may have "
        "told her he wanted to talk. He used the opportunity to go to the breakroom — the regular coffee "
        "pot was still warm — and add a prepared solution of digoxin to her mug while she was not watching. "
        "He then took the USB drive from her desk. He stayed long enough to confirm she had drunk the "
        "coffee, then left. He was gone before midnight. The 7th floor hallway camera, which he had "
        "arranged to be disabled three days earlier through a proxy tenant complaint, recorded nothing.")]
    story += [SP(3), body(
        "Digoxin is a cardiac glycoside used therapeutically in heart failure and arrhythmia management. "
        "In toxic doses — particularly in a patient already taking Lisinopril, which potentiates its "
        "effect by lowering potassium — it causes progressive bradyarrhythmia and ventricular fibrillation. "
        "Death can occur within two to four hours and, in a 46-year-old woman with documented mild "
        "coronary artery disease and hypertension, the presentation is nearly indistinguishable from "
        "sudden cardiac death. Ellsworth knew about Eleanor's heart. He knew about Dr. Taft's referral "
        "to cardiology. He had listened to enough of her conversations with Diane Kowalski over four years.")]
    story += [SP(3), body(
        "What Ellsworth did not know: that Eleanor had suspected she might be in danger. The laptop "
        "forensic examination recovered a private browser session from October 11, 2015 in which "
        "she had searched the terms 'digoxin interactions lisinopril,' 'symptoms digoxin toxicity,' "
        "and 'how to detect poisoning before it happens.' She did not know how she might be targeted "
        "or when. She told Diane that 'things here are not what they appear to be.' She cancelled "
        "the following week's calendar because she intended to be in a very different place by then — "
        "either a federal reporting office, or somewhere safe. She ran out of time by hours.")]

    story += [SP(5), section("EVIDENCE THAT CONFIRMS THE SOLUTION")]
    story += [tbl([
        ["Clue / Evidence Item", "What It Proves"],
        ["Tox results (MCME-TOX-2015-0841) — digoxin detected at 3.8 ng/mL serum; not prescribed by any known physician",
         "Cause of death. Toxic level. Ellsworth sourced digoxin through a compounding pharmacy contact under a false identity — traced via financial records subpoena."],
        ["EV-A — coffee mug: regular (caffeinated) coffee residue; Marsh never drank regular after 6pm",
         "The mug was Ellsworth's vehicle. He poured from the regular pot because he didn't know her routine. Or he used it precisely because it was not her usual drink — she would not have chosen it herself."],
        ["Badge entry 22:47 — card #CC-2015-0147 (Fuentes) — while Fuentes was home",
         "Ellsworth created a duplicate card as a red herring to implicate or confuse. RFID cloning device found in Ellsworth's home office during search warrant execution."],
        ["Suite 712 door unlocked at discovery",
         "Ellsworth used his own COO access card to enter and exit. He did not re-lock the door on exit — an oversight, or he assumed Ellie would eventually lock up herself."],
        ["7th floor camera offline Oct 11–14 (WO 2015-10-WO-1847)",
         "The tenant 'complaint' on Oct 11 was placed by a burner phone registered to a shell LLC that Ellsworth controlled. Confirmed via phone records and DA financial investigation."],
        ["Missing USB drive — not recovered at scene, on person, or at residence",
         "Ellsworth took it. Found during search of his vehicle on Dec 4, 2015, concealed under the spare tire well. Drive contained the complete parallel account evidence."],
        ["EV-J — email Marsh to Ellsworth, 23:47 Oct 13 — 'discrepancies...reports I can no longer sign off on'",
         "Establishes motive. Ellsworth knew she was going to the SEC in the morning. He had hours to act."],
        ["Laptop forensics — browser search 'digoxin interactions lisinopril' — Oct 11, 2015",
         "Eleanor suspected she was being targeted. She did not know who or when. She died before she could act on her suspicion."],
        ["Kowalski: 'things here are not what they appear to be' — Oct 12",
         "Eleanor was telling the person she trusted most that something was very wrong. She stopped short of naming Ellsworth because she wasn't certain Kowalski would be safe knowing."],
        ["Dr. Taft: Ellie said 'nothing that anyone prescribed me' re: medications — Sept 28",
         "Eleanor may have been experiencing early low-dose digoxin symptoms (fatigue, chest tightness) and suspected she was being microdosed. She hinted at this to her doctor but did not elaborate — possibly because she wasn't sure yet."],
    ], col_widths=[2.80 * inch, 3.75 * inch])]

    story += [SP(5), section("THE PEOPLE — WHERE THEY ENDED UP")]
    story += [tbl([
        ["Person", "Outcome"],
        ["Craig Ellsworth", "Arrested Dec. 4, 2015. Charged: First-Degree Murder, Securities Fraud (7 counts), Embezzlement. Convicted on all counts, April 2017. Sentenced to life without parole plus 40 years concurrent."],
        ["Ramon Fuentes", "Cleared of all suspicion. The badge anomaly traced entirely to Ellsworth's RFID clone. Fuentes cooperated fully and was never charged."],
        ["Heinrich Vrenner, Esq.", "Voluntarily came forward after Eleanor's death became public. His testimony about the Oct 13 meeting established Eleanor's state of mind and intent to report — key to establishing the murder motive at trial."],
        ["Diane Kowalski", "Key prosecution witness. The personal notepad entries were entered into evidence. She testified for three days. Established victim's knowledge, fear, and intent."],
        ["Dr. Susan Taft", "Provided expert medical testimony re: digoxin-Lisinopril interaction. Later publicly noted that Eleanor's Sept 28 symptoms — chest tightness, fatigue — were consistent with early chronic digoxin toxicity."],
        ["Gregory Marsh (spouse)", "Cooperated fully. Received a civil settlement from Apex Financial Group's insurers on behalf of Eleanor's estate. He and their two children relocated to Minneapolis in 2016."],
        ["Apex Financial Group", "Receivership, November 2015. Client funds ($4.1M) substantially recovered via Ellsworth's personal and business assets. Firm dissolved February 2016."],
    ], col_widths=[1.50 * inch, 5.05 * inch])]

    story += [SP(5), HR(), SP(4)]
    story += [small("This solution document is for reference only and does not constitute part of the official ME or police case file. "
                    "Case 2015-ME-0447 / SFPD-2015-48801 is a work of fiction created for entertainment purposes. "
                    "All persons, organizations, events, and case details depicted are entirely fictitious.")]

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
