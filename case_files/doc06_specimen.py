"""Document 06 — Specimen / Evidence Retained Sheet (1 page)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate
from aging import make_onpage, W, H, STAMP_B, HW_BLUE
from styles import ST, HR, doc_header, section, body, body_l, small, SP, tbl

OUT = os.path.dirname(__file__)


def build():
    path = os.path.join(OUT, "ME-0447-06-Specimen-Evidence-Retained-Sheet.pdf")
    aging = {
        'staple': True,
        1: {
            'rings': [(W*0.85, H*0.72, 34, 121, 0.19, 41)],
            'creases': [(0, H*0.50, W, H*0.502, 71, 0.72)],
            'foxing': {'count': 40, 'inten': 0.88},
            'stamps': [("SPECIMENS SUBMITTED — SEE TOX FORM", 0.82*inch, H*0.11, 2, STAMP_B, 9, 0.52)],
            'hw': [("all accessions confirmed — DHF 10/14", W-3.1*inch, H*0.145, -1, HW_BLUE, 7.5)],
        },
    }
    cb = make_onpage(106, "Specimen / Evidence Retained Sheet", 1, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.80*inch, rightMargin=0.80*inch,
                            topMargin=0.75*inch, bottomMargin=0.72*inch)
    story = doc_header("SPECIMEN AND EVIDENCE RETAINED SHEET",
                       "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  DOB: 03/22/1969")

    story += [tbl([
        ["Prepared By:", "Dr. Raymond G. Adeyemi, MD (primary) / D.H. Farr (MT-03)", "Date:", "October 14, 2015"],
        ["Purpose of This Sheet:", "Documents all biological and non-biological specimens retained by ME office at autopsy. "
                                   "Does NOT replace laboratory accession records or chain-of-custody submissions. "
                                   "Does NOT include items retained by SFPD.", "", ""],
        ["Autopsy Date:", "October 14, 2015 — 0902 to 1318 hrs", "ME Case #:", "2015-ME-0447"],
    ], col_widths=[1.40*inch, 3.60*inch, 0.65*inch, 1.90*inch], has_hdr=False, alt=False)]

    story += [SP(6), section("BIOLOGICAL SPECIMENS RETAINED OR SUBMITTED")]
    story += [tbl([
        ["Specimen ID", "Type", "Volume / Amount", "Container", "Storage / Disposition", "Analysis", "Lab Accession #"],
        ["SP-01", "Peripheral blood (femoral) — NaF/KOx ×2", "10 mL", "Gray-top Vacutainer ×2", "Submitted — ME Tox Lab", "Comprehensive tox; volatiles; drugs", "PENDING"],
        ["SP-02", "Peripheral blood (femoral) — EDTA", "5 mL", "Purple-top Vacutainer", "Submitted — ME Tox Lab", "Drugs of abuse; therapeutic panel", "PENDING"],
        ["SP-03", "Peripheral blood — reserve (no additive)", "5 mL", "Red-top Vacutainer", "ME Freezer — Case File", "Reserve; use on pathologist order", "N/A"],
        ["SP-04", "Central blood (cardiac — RV) — NaF/KOx ×2", "10 mL", "Gray-top ×2", "Submitted — ME Tox Lab", "Tox (comparison only; PMR artifact expected)", "PENDING"],
        ["SP-05", "Urine (bladder aspirate)", "40 mL", "Sterile collection jar", "Submitted — ME Tox Lab", "Comprehensive tox; drugs; volatiles", "PENDING"],
        ["SP-06", "Vitreous humor — right eye", "2.5 mL", "Gray-top Vacutainer", "Submitted — ME Tox Lab", "Ethanol; electrolytes; drugs", "PENDING"],
        ["SP-07", "Vitreous humor — left eye (reserve)", "2.3 mL", "Gray-top Vacutainer", "ME Freezer — Case File", "Reserve", "N/A"],
        ["SP-08", "Gastric contents — aspirate (total)", "~120 mL", "Wide-mouth specimen jar", "Submitted — ME Tox Lab", "Qualitative/quantitative tox; compound ID", "PENDING"],
        ["SP-09", "Liver — unfixed tissue (tox)", "~50 g", "Wide-mouth specimen jar", "Submitted — ME Tox Lab", "Tissue tox panel", "PENDING"],
        ["SP-10", "Liver — formalin-fixed tissue (histo)", "~30 g", "Formalin jar", "ME Histo Lab", "H&E; PAS; reticulin", "N/A"],
        ["SP-11", "Bile (gallbladder aspirate)", "~15 mL", "Sterile container", "ME Freezer — Case File", "Reserve; tox as directed", "N/A"],
        ["SP-12", "Scalp hair — root-intact (×30 strands)", "30 strands", "Paper coin envelope, sealed", "Submitted — ME Tox Lab", "Segmental hair drug analysis; heavy metals", "PENDING"],
        ["SP-13", "Fingernail clippings — all digits", "All 10", "Paper envelopes (L/R)", "Submitted — SFPD CSU trace lab", "Trace evidence; trace drug", "SFPD assigned"],
        ["SP-14", "Blouse cuff stain — swabs ×2 (wetted)", "2 swabs", "Swab transport tube, sealed", "Submitted — SFPD CSU trace lab", "Unknown substance ID; tox; trace", "SFPD assigned"],
        ["SP-15", "Blouse cuff stain — scraping (reserve)", "Scraping", "Paper envelope, sealed", "ME Freezer — Case File", "Reserve for additional analysis", "N/A"],
        ["SP-16", "Brain — formalin-fixed (whole; pending histo)", "Whole organ", "Formalin container, sealed", "ME Cold Storage — 10% NBF; min. 2 weeks fixation before sectioning", "Neuropathology H&E; special stains", "N/A"],
        ["SP-17", "Cardiac tissue blocks — multiple", "Per histo plan", "Formalin cassettes, labeled", "ME Histo Lab", "H&E; Masson; Movat; as directed", "N/A"],
        ["SP-18", "Lung, kidney, adrenal, thyroid, spleen tissue", "Per histo plan", "Formalin cassettes, labeled", "ME Histo Lab", "H&E; special stains per plan", "N/A"],
        ["SP-19", "Uterus and right ovary — representative sections", "Per histo plan", "Formalin cassettes, labeled", "ME Histo Lab", "H&E; routine gyn sections", "N/A"],
    ], col_widths=[0.48*inch, 1.35*inch, 0.68*inch, 0.95*inch, 1.30*inch, 1.55*inch, 0.74*inch])]

    story += [SP(4), section("NOTES ON SCOPE AND LIMITATIONS")]
    story += [body(
        "This sheet documents specimens retained by the Minnehaha County ME office and specimens submitted by "
        "this office to the ME Toxicology Laboratory or to SFPD Crime Scene Unit for laboratory analysis. It "
        "does not document SFPD-collected evidence items (including the decedent's laptop, notepad, key fob, "
        "access badge, or other items taken from Suite 712 during the crime scene examination), which are "
        "itemized in SFPD Evidence Log SFPD-PROP-48801-A. It does not replace or duplicate the ME Toxicology "
        "Laboratory accession records, which constitute the controlling chain-of-custody document for all "
        "submitted biological specimens. Laboratory accession numbers are pending at the time of this sheet's "
        "preparation and will be entered upon confirmation from the receiving laboratory."),
     body("All specimens marked 'ME Freezer — Case File' are maintained in the ME facility freezer designated "
          "for case evidence, at a temperature of -20°C or below, and may be retrieved for additional analysis "
          "by order of the pathologist, the Chief ME, a court of competent jurisdiction, or authorized legal "
          "representative. The brain (SP-16) is retained in 10% neutral buffered formalin for a minimum of two "
          "weeks to achieve adequate fixation prior to sectioning for neuropathological examination; sectioning "
          "is anticipated no earlier than October 28, 2015. Any request for additional specimens, testing, or "
          "independent examination by parties with standing must be directed to the Chief ME in writing.")]

    story += [SP(4), tbl([
        ["Specimens Packaged By:", "D.H. Farr (MT-03) / Dr. R.G. Adeyemi",  "Signature:", "______________________", "Date:", "10/14/2015"],
        ["Tox Specimens Submitted By:", "D.H. Farr (MT-03)",                "Submission Time:", "1402 hrs CDT", "", ""],
        ["SFPD Items Released To:", "Det. M.J. Orre / SFPD CSU",            "Release Time:", "Approx. 1340 hrs (per Det. Orre)", "", ""],
    ], col_widths=[1.60*inch, 2.10*inch, 0.95*inch, 1.40*inch, 0.45*inch, 0.55*inch], has_hdr=False, alt=False)]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
