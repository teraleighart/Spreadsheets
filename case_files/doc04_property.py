"""Document 04 — Personal Effects / Property Inventory (1 page)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from aging import make_onpage, W, H, STAMP_R, STAMP_B, HW_BLUE
from styles import ST, HR, doc_header, section, body, body_l, small, SP, tbl
from reportlab.platypus import SimpleDocTemplate

OUT = os.path.dirname(__file__)


def build():
    path = os.path.join(OUT, "ME-0447-04-Personal-Effects-Property-Inventory.pdf")
    aging = {
        'staple': True,
        1: {
            'rings': [(W*0.14, H*0.55, 40, 91, 0.19, 42)],
            'creases': [(0, H*0.667, W, H*0.664, 51, 0.75)],
            'foxing': {'count': 45, 'inten': 0.92},
            'stamps': [("ME HOLD — DO NOT RELEASE", W*0.5 - 1.9*inch, H*0.13, 5, STAMP_R, 11, 0.55)],
            'hw': [("release pending NOK auth — SLK", W-3.0*inch, H*0.165, -2, HW_BLUE, 8)],
        },
    }
    cb = make_onpage(104, "Personal Effects / Property Inventory", 1, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.80*inch, rightMargin=0.80*inch,
                            topMargin=0.75*inch, bottomMargin=0.72*inch)

    story = doc_header("PERSONAL EFFECTS AND PROPERTY INVENTORY",
                       "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  DOB: 03/22/1969")

    story += [tbl([
        ["Inventory Date:", "October 14, 2015",            "Inventory Time:", "0635 hrs CDT"],
        ["Inventoried By:", "Sandra L. Kowalczyk (MEI-09)", "Witnessed By:", "Dennis H. Farr (MT-03)"],
        ["Location of Inventory:", "ME Facility — Intake Bay C", "Case Number:", "2015-ME-0447"],
        ["Property Status:", "ME HOLD — Pending NOK release authorization (Thomas R. Marsh)", "", ""],
    ], col_widths=[1.55*inch, 2.00*inch, 1.45*inch, 2.55*inch], has_hdr=False, alt=False)]

    story += [SP(4), section("SECTION A — CLOTHING (ON BODY AT TIME OF RECEIPT)")]
    story += [tbl([
        ["Item #", "Description", "Color / Material", "Condition", "Disposition"],
        ["C-01", "Women's blazer, structured — single-breasted, 3-button",
         "Charcoal grey / wool-poly blend", "Intact; no visible damage, tears, or staining beyond normal wear",
         "ME Hold — retained with body pending autopsy; released to NOK after autopsy unless held as evidence"],
        ["C-02", "Women's collared blouse — button-front, long-sleeved",
         "White / silk-look polyester", "Intact; collar open at second button; no visible damage",
         "ME Hold — same as C-01"],
        ["C-03", "Women's dress slacks — straight leg, flat-front",
         "Charcoal grey / wool-poly blend (matching blazer)", "Intact; no visible damage or staining",
         "ME Hold — same as C-01"],
        ["C-04", "Undergarment — brassiere",
         "Nude / nylon-spandex blend", "Intact; no damage",
         "ME Hold — same as C-01"],
        ["C-05", "Undergarment — briefs",
         "Nude / nylon", "Intact; no damage",
         "ME Hold — same as C-01"],
        ["C-06", "Women's low-heeled dress shoes (pair)",
         "Black / leather upper, rubber sole", "Normal wear; no damage; right shoe slightly displaced at toe (noted at scene)",
         "ME Hold — same as C-01"],
    ], col_widths=[0.38*inch, 1.80*inch, 1.25*inch, 1.75*inch, 1.37*inch])]

    story += [SP(4), section("SECTION B — JEWELRY AND ACCESSORIES (ON BODY AT TIME OF RECEIPT)")]
    story += [tbl([
        ["Item #", "Description", "Material / Apparent Composition", "Condition", "Disposition"],
        ["J-01", "Stud earrings (pair) — both present in ears",
         "Yellow metal (gold tone); small round stone, clear, consistent with diamond or CZ",
         "Intact; no damage", "ME Hold"],
        ["J-02", "Wristwatch — left wrist",
         "Round face, silver-tone case, black leather band; dial reads brand name partially obscured by band",
         "Operational; crystal intact; band intact; time display: 11:22 (not verified against actual)",
         "ME Hold"],
        ["J-03", "Ring — right ring finger",
         "Silver-tone metal; oval pale blue stone, consistent with aquamarine or similar",
         "Intact; no damage; stone secure in setting", "ME Hold"],
    ], col_widths=[0.38*inch, 1.80*inch, 1.50*inch, 1.62*inch, 0.75*inch])]

    story += [SP(4), section("SECTION C — PURSE AND PERSONAL ITEMS")]
    story += [body(
        "One (1) structured women's leather handbag, dark burgundy, approximately 13\" × 9\" × 4\", with "
        "dual handles and single interior zipper compartment, was received with the body. The purse was "
        "found at scene looped over the lower corner post of the office credenza adjacent to the decedent's "
        "chair. The purse was not opened or inventoried at the scene; its contents were inventoried at the "
        "ME facility during intake processing. The following items were found inside:")]
    story += [tbl([
        ["Item #", "Description", "Condition / Notes", "Disposition"],
        ["P-01", "South Dakota Driver License — in the name of Eleanor A. Marsh, DOB 03/22/1969, Exp. 2019",
         "Valid; photo consistent with decedent; used as primary ID at intake", "ME Hold — copy made for case file"],
        ["P-02", "Credit / debit card — VISA, name E.A. Marsh",
         "Intact; not expired", "ME Hold"],
        ["P-03", "Credit / debit card — MASTERCARD, name E.A. Marsh",
         "Intact; not expired", "ME Hold"],
        ["P-04", "Credit / debit card — AMEX, name ELEANOR MARSH",
         "Intact; not expired", "ME Hold"],
        ["P-05", "US Currency — loose bills and coins",
         "$43.00 total ($2×$20, 1×$1, coins $0.87; denomination counts recorded separately)",
         "ME Hold; counted in presence of witness"],
        ["P-06", "Business card case — silver metal, hinged",
         "Contains approx. 12–14 business cards in the decedent's name; 3–4 third-party cards",
         "ME Hold"],
        ["P-07", "Mobile phone — smartphone (brand/model not recorded at intake)",
         "Phone locked; screen off; collected by SFPD CSU at scene; NOT received by ME office",
         "SFPD HOLD — not ME property — see SFPD evidence log SFPD-PROP-48801-A"],
        ["P-08", "Lip balm / cosmetic item — small cylindrical",
         "Intact; commercial brand", "ME Hold"],
        ["P-09", "Pen — retractable ballpoint",
         "Intact", "ME Hold"],
        ["P-10", "Folded paper — letter-size, trifolded",
         "Printed document; contents not reviewed by ME office; transferred to SFPD CSU at scene (not received by ME)",
         "SFPD HOLD — see SFPD evidence log"],
        ["P-11", "Fabric pouch — small, zippered; appeared to contain OTC medication tablets",
         "Pouch intact; contents not inventoried by ME at intake; transferred to SFPD CSU at scene",
         "SFPD HOLD — see SFPD evidence log; ME requested copy of contents inventory"],
    ], col_widths=[0.38*inch, 2.25*inch, 2.15*inch, 1.77*inch])]

    story += [SP(4), section("SECTION D — PROPERTY CUSTODY DISTINCTION AND RELEASE STATUS")]
    story += [body(
        "This inventory documents property received by and held in the custody of the Minnehaha County Office "
        "of the Medical Examiner as of October 14, 2015. It does not supersede or represent the totality of "
        "personal property associated with the decedent or the scene. Property retained by SFPD as scene "
        "evidence — including but not limited to the decedent's laptop computer, office notepad, key fob, "
        "building access badge, mobile phone, and items from the decedent's purse identified above as SFPD "
        "holds — is documented under SFPD Evidence Log SFPD-PROP-48801-A and is not the responsibility of "
        "this office to inventory, secure, or release."),
     body("All items listed in Sections A, B, and C as ME Hold are maintained in the ME facility property "
          "storage area under lock and are assigned to Case 2015-ME-0447. These items will not be released "
          "without written next-of-kin release authorization from the authorized next-of-kin (Thomas R. Marsh, "
          "adult son, as identified at intake) or pursuant to court order. Clothing and jewelry may be returned "
          "with the body following autopsy and preparation for release to the funeral home designated by the "
          "next-of-kin, per standard ME office property release protocol (Policy ME-OPS-010, Rev. 2014). "
          "Currency and high-value items will be released separately upon execution of an ME property release "
          "form signed by the authorized next-of-kin and witnessed by ME staff."),
     body("This inventory was completed in the presence of a witness as listed above. Discrepancies between this "
          "inventory and the contents of any bag, pouch, or container received by this office shall be noted "
          "in a supplemental memorandum. No discrepancies were identified at the time of this inventory.")]

    story += [SP(4), tbl([
        ["Role", "Name (Print)", "Signature", "Date", "Time"],
        ["Inventorying Investigator", "Sandra L. Kowalczyk — MEI-09", "______________________", "10/14/2015", "0635"],
        ["Witness — ME Staff", "Dennis H. Farr — MT-03", "______________________", "10/14/2015", "0635"],
        ["Property Custodian Received", "Dennis H. Farr — MT-03", "______________________", "10/14/2015", "0648"],
    ], col_widths=[1.80*inch, 2.10*inch, 1.70*inch, 0.80*inch, 0.55*inch])]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
