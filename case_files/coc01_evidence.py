"""COC-01 — Evidence Chain of Custody Log (2 pages)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph
from aging import make_onpage, W, H, STAMP_B, HW_BLUE, HW_PENCIL, STAMP_R
from styles import ST, HR, section, body, small, SP, tbl

OUT = os.path.dirname(__file__)


def coc_header():
    return [
        Paragraph('SIOUX FALLS POLICE DEPARTMENT — EVIDENCE DIVISION', ST['doc_title']),
        Paragraph('Property and Evidence Control Unit  •  320 W. 4th St., Sioux Falls, SD 57104', ST['doc_sub']),
        Paragraph('CHAIN OF CUSTODY — MASTER EVIDENCE LOG', ST['sec_head']),
        SP(3),
        HR(),
    ]


def build():
    path = os.path.join(OUT, "COC-01-Evidence-Chain-of-Custody.pdf")
    aging = {
        'staple': True,
        1: {
            'rings': [(W * 0.80, H * 0.81, 33, 401, 0.15, 84)],
            'creases': [(0, H * 0.53, W, H * 0.527, 402, 0.60)],
            'foxing': {'count': 18, 'inten': 0.70},
            'stamps': [("SFPD EVIDENCE DIVISION", 0.75 * inch, H * 0.09, -3, STAMP_B, 10, 0.50)],
            'hw': [("USB not recov. — scene re-examined 10/16 — neg.", W - 3.8 * inch, H * 0.475, 1, HW_PENCIL, 7.0)],
        },
        2: {
            'rings': [],
            'creases': [(0, H * 0.40, W, H * 0.397, 403, 0.55)],
            'foxing': {'count': 14, 'inten': 0.65},
            'stamps': [("ACTIVE — DO NOT RELEASE WITHOUT AUTH.", 0.75 * inch, H * 0.09, 2, STAMP_R, 8, 0.52)],
            'hw': [("laptop — no USB hist. pre-Oct 8 — DFU", W - 3.5 * inch, H * 0.73, -1, HW_PENCIL, 7.0),
                   ("EV-J restricted — DA eyes only", 0.82 * inch, H * 0.565, 1, HW_BLUE, 7.5)],
        },
    }
    cb = make_onpage(401, "COC-01 Evidence Log", 2, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.80 * inch, rightMargin=0.80 * inch,
                            topMargin=0.75 * inch, bottomMargin=0.72 * inch)

    story = coc_header()

    story += [tbl([
        ["Case No.:", "SFPD-2015-48801", "ME Case No.:", "2015-ME-0447"],
        ["Decedent:", "MARSH, Eleanor Anne — DOB 03/22/1969", "Classification:", "Suspicious Death / Homicide Investigation"],
        ["Primary Detective:", "Det. M.L. Santos (Badge #4471)", "Partner:", "Det. J.R. Brewer (Badge #3892)"],
        ["Evidence Officer:", "Ofc. R. Alvarez-Ruiz, CSU-12", "Property Room:", "SFPD Evidence Division — Bay 7, Shelf C"],
        ["Log Opened:", "October 14, 2015 — 0519 hrs (on-scene)", "Last Updated:", "October 20, 2015"],
    ], col_widths=[1.10 * inch, 2.80 * inch, 1.10 * inch, 1.55 * inch])]

    story += [SP(5), section("SECTION A — EVIDENCE INVENTORY (SFPD-COLLECTED)")]
    story += [small("Items collected at scene (Suite 712, 4200 S. Western Ave.) by SFPD CSU on October 14, 2015 unless noted otherwise. "
                    "ME-collected biological specimens tracked separately under ME Case 2015-ME-0447 — see Section C.")]
    story += [SP(3), tbl([
        ["Item ID", "Description", "Collected By", "Date / Time", "Collection Location", "Package / Seal"],
        ["EV-A", "Ceramic coffee mug — cream exterior, dark interior residue staining; possible lip/print transfer on rim", "CSU-12 Alvarez-Ruiz", "Oct. 14 / 0534 hrs", "Decedent desk surface — Suite 712-A", "Paper bag #1 — SFPD seal #E-2015-48801-001"],
        ["EV-B", "Open leather portfolio containing handwritten notes — 14 pages with entries; blue ballpoint pen clipped to cover", "CSU-12 Alvarez-Ruiz", "Oct. 14 / 0538 hrs", "Decedent desk surface — Suite 712-A", "Paper bag #2 — seal #E-2015-48801-002"],
        ["EV-C", "Decedent's black leather structured handbag and full contents (itemized in PR-01 supplement) — wallet, personal effects", "CSU-12 Alvarez-Ruiz", "Oct. 14 / 0544 hrs", "Decedent chair — hanging from right armrest", "Paper bag #3 — seal #E-2015-48801-003"],
        ["EV-D", "Decedent's white button-down blouse — stain approx. 3cm diam., upper right chest, brownish-red, dried; collected by ME at autopsy", "ME Office — Dr. Adeyemi / MT-03 Farr", "Oct. 14 / approx. 1115 hrs", "ME Facility — autopsy suite, post-removal", "ME Property Bag — ME seal #ME-0447-C-04; transferred SFPD Oct. 17"],
        ["EV-E", "Apple MacBook Pro laptop — 13-inch, space gray, serial no. C02PX8BYFVH5 — screensaver active at recovery; power-on", "CSU-07 Okafor", "Oct. 14 / 0551 hrs", "Decedent desk surface — Suite 712-A", "Anti-static bag — seal #E-2015-48801-004"],
        ["EV-F", "Witness notepad — personal — Diane Kowalski; relevant entries Oct. 12 and Oct. 13 flagged; provided voluntarily", "Det. Santos", "Oct. 14 / 1510 hrs", "SFPD CID interview room — Kowalski surrender", "Paper envelope — seal #E-2015-48801-005"],
        ["EV-G", "Building electronic access log — certified copy — Oct. 11–14, 2015; all floors; source: Lenel OnGuard system printout", "Det. Brewer / V. Solis", "Oct. 14 / 0910 hrs", "Building manager office — 1st floor", "Paper bag #4 — seal #E-2015-48801-006"],
        ["EV-H", "Lobby visitor log — original — Oct. 13–14, 2015; source: building security desk", "Det. Brewer / P. Herne", "Oct. 14 / 0855 hrs", "Building lobby security desk", "Paper bag #5 — seal #E-2015-48801-007"],
        ["EV-I", "SFPD CSU scene photograph set — 312 digital frames on SD card; card backed up to SFPD digital evidence server", "CSU-12 Alvarez-Ruiz / CSU-07 Okafor", "Oct. 14 / 0519–0748 hrs", "Suite 712 — all areas", "SD card in evidence envelope — seal #E-2015-48801-008"],
        ["EV-J", "Email: Marsh to Ellsworth — Oct. 13, 2015, 23:47 hrs — electronic record; voluntarily disclosed; printed copy + original EML file on CD", "Det. Santos", "Oct. 15 / 1130 hrs", "SFPD CID — from Ellsworth counsel", "Sealed envelope — RESTRICTED — seal #E-2015-48801-009 — DA access only"],
        ["EV-K", "Building surveillance video — lobby (CAM-01-A, CAM-01-B), parking garage (CAM-G-01 through CAM-G-04) — Oct. 13 1800 hrs through Oct. 14 0900 hrs — USB drive provided by Solis", "Det. Brewer / V. Solis", "Oct. 14 / 1045 hrs", "Building manager office — 1st floor", "Evidence USB in envelope — seal #E-2015-48801-010"],
        ["NOT RECOV.", "USB drive (small, black, no label, approx. 2cm) — described by witness Kowalski as sought by decedent — not located at scene, on person, at residence, or in vehicle — OUTSTANDING", "—", "N/A", "N/A — not recovered despite searches Oct. 14 and Oct. 16", "—"],
    ], col_widths=[0.52 * inch, 2.18 * inch, 1.00 * inch, 0.78 * inch, 1.18 * inch, 1.89 * inch])]

    story += [SP(5), section("SECTION B — TRANSFER AND MOVEMENT LOG")]
    story += [tbl([
        ["Date / Time", "Item(s)", "Released By", "Received By", "Purpose / Destination", "Seal Verified"],
        ["Oct. 14 / 0900 hrs", "EV-A, EV-B, EV-C, EV-E, EV-G, EV-H, EV-I, EV-K", "CSU-12 Alvarez-Ruiz", "Ofc. M. Tran — SFPD Property Room", "Transfer: scene to SFPD Evidence Division, Bay 7, Shelf C", "Yes — all seals intact"],
        ["Oct. 14 / 1045 hrs", "EV-F (Kowalski notepad)", "Det. Santos", "Ofc. M. Tran — SFPD Property Room", "Voluntary surrender — logged intake", "Yes"],
        ["Oct. 15 / 0830 hrs", "EV-A", "Ofc. M. Tran", "SFPD Forensic Lab — Latent Print Unit", "Latent print analysis + residue swab for lab analysis", "Yes — reseal #FL-2015-48801-A1"],
        ["Oct. 15 / 0830 hrs", "EV-B", "Ofc. M. Tran", "SFPD Forensic Lab — Document Analysis", "Handwriting analysis; content review / transcription", "Yes — reseal #FL-2015-48801-B1"],
        ["Oct. 16 / 0900 hrs", "EV-E", "Ofc. M. Tran", "SFPD Digital Forensics Unit — Tech. B. Yeun", "Forensic imaging; password bypass; USB device history; email archive extraction", "Yes — reseal #DFU-2015-48801-E1"],
        ["Oct. 17 / 1400 hrs", "EV-D", "ME Office — MT-03 Farr", "Ofc. M. Tran — SFPD Property Room (transfer from ME)", "ME analysis complete on clothing item; transferred to SFPD custody; pending additional testing", "Yes — ME seal intact on arrival; resealed #E-2015-48801-D2"],
        ["Oct. 20 / 1100 hrs", "EV-K", "Ofc. M. Tran", "Det. Brewer — SFPD CID", "Video review — lobby and garage footage, Oct. 13–14", "Yes — temporary checkout; return required"],
    ], col_widths=[0.82 * inch, 0.90 * inch, 1.08 * inch, 1.25 * inch, 1.85 * inch, 0.65 * inch])]

    story += [SP(5), section("SECTION C — ME OFFICE SPECIMENS (CROSS-REFERENCE ONLY)")]
    story += [body(
        "Biological specimens and toxicological samples collected at autopsy are maintained under the custody of the "
        "Minnehaha County Medical Examiner's Office under ME Case No. 2015-ME-0447. A total of 19 specimens "
        "(SP-01 through SP-19) were collected and are documented in ME form ME-0447-06-Specimen-Evidence-Retained-Sheet. "
        "Toxicological specimens were submitted to ME Toxicology Laboratory under accession MCME-TOX-2015-0841. "
        "Results of toxicological analysis have been completed and are held by the ME's Office pending pathologist "
        "review and correlation. Release of ME specimens to SFPD custody, if required, will be documented under "
        "separate chain of custody addendum upon ME authorization. SFPD claims no current custody of any ME specimens.")]

    story += [SP(5), HR(), SP(4)]
    story += [tbl([
        ["Log Maintained By:", "Ofc. M. Tran — SFPD Evidence Division", "Badge:", "#3341"],
        ["Reviewed By:", "Det. M.L. Santos (Badge #4471)", "Date:", "October 20, 2015"],
        ["Supervisor:", "Sgt. L. Whitfield — Evidence Division", "Date:", "October 20, 2015"],
    ], col_widths=[1.40 * inch, 2.70 * inch, 0.65 * inch, 1.80 * inch])]
    story += [SP(4), small(
        "All items remain in active case status. No items may be released, returned, or destroyed without written "
        "authorization from the assigned detective and Evidence Division supervisor. Any discrepancy in seal integrity "
        "must be reported immediately to the Evidence Division supervisor and the assigned detective. "
        "This log is subject to disclosure in any subsequent legal proceedings.")]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
