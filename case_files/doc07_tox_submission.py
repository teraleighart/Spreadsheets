"""Document 07 — Toxicology Submission Form (1 page)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate
from aging import make_onpage, W, H, STAMP_B, HW_BLUE
from styles import ST, HR, doc_header, section, body, body_l, small, SP, tbl

OUT = os.path.dirname(__file__)


def build():
    path = os.path.join(OUT, "ME-0447-07-Toxicology-Submission-Form.pdf")
    aging = {
        'staple': True,
        1: {
            'rings': [(W*0.14, H*0.82, 42, 131, 0.21, 51)],
            'creases': [(0, H*0.335, W, H*0.332, 81, 0.75)],
            'foxing': {'count': 38, 'inten': 0.85},
            'stamps': [("SUBMITTED TO TOXICOLOGY LAB", 0.85*inch, H*0.12, 3, STAMP_B, 10, 0.53)],
            'hw': [("submitted 1402 hrs 10/14 — DHF", W-2.9*inch, H*0.155, -1, HW_BLUE, 8)],
        },
    }
    cb = make_onpage(107, "Toxicology Submission Form", 1, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.80*inch, rightMargin=0.80*inch,
                            topMargin=0.75*inch, bottomMargin=0.72*inch)
    story = doc_header("TOXICOLOGY SUBMISSION FORM",
                       "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  DOB: 03/22/1969")

    story += [section("SECTION A — CASE AND SUBMISSION IDENTIFICATION")]
    story += [tbl([
        ["ME Case #:", "2015-ME-0447",                       "Tox Lab Case # (assigned by lab):", "PENDING"],
        ["Decedent Name:", "MARSH, Eleanor Anne",             "DOB:", "March 22, 1969"],
        ["Sex:", "Female",                                    "Age at Death:", "46 years"],
        ["Date of Death (est.):", "October 13, 2015",        "Date of Autopsy:", "October 14, 2015"],
        ["Submitting ME / Path.:", "Dr. Raymond G. Adeyemi, MD — Deputy Chief ME", "Phone:", "(605) 367-4300"],
        ["Submitting Tech. / Staff:", "Dennis H. Farr (MT-03) — Minnehaha County ME Facility",
         "Submission Date/Time:", "October 14, 2015 — 1402 hrs CDT"],
        ["Receiving Lab:", "Minnehaha County ME Toxicology Laboratory — 220 W. Sixth St., Sioux Falls, SD 57104",
         "Priority Level:", "RUSH / Priority-1 Suspicious Case"],
        ["LE Agency:", "Sioux Falls Police Department",       "LE Case #:", "SFPD-2015-48801"],
        ["LE Contact (for results):", "Det. Marcus J. Orre — (605) 367-7211 x3304",
         "ME Contact:", "Dr. Adeyemi / S.L. Kowalczyk (MEI-09)"],
    ], col_widths=[1.50*inch, 2.50*inch, 1.50*inch, 2.05*inch], has_hdr=False, alt=False)]

    story += [SP(5), section("SECTION B — SPECIMENS SUBMITTED")]
    story += [tbl([
        ["Spec. ID", "Specimen Type", "Quantity / Volume", "Container / Preservative", "Condition at Submission"],
        ["SP-01", "Peripheral blood — femoral (NaF/KOx × 2)", "10 mL total", "Gray-top Vacutainer ×2 (NaF/KOx)", "Intact seals; labeled; no hemolysis noted on gross inspection"],
        ["SP-02", "Peripheral blood — femoral (EDTA)", "5 mL", "Purple-top Vacutainer (EDTA)", "Intact; labeled"],
        ["SP-04", "Central blood — cardiac right ventricle (NaF/KOx ×2)", "10 mL total", "Gray-top Vacutainer ×2 (NaF/KOx)", "Intact; labeled; submitted for comparison only — PMR artifact anticipated"],
        ["SP-05", "Urine — bladder aspirate (total volume)", "~40 mL", "Sterile collection jar, sealed", "Intact seal; pale yellow, slightly cloudy; labeled"],
        ["SP-06", "Vitreous humor — right eye", "2.5 mL", "Gray-top Vacutainer (NaF/KOx)", "Intact; clear vitreous; labeled"],
        ["SP-08", "Gastric contents — total aspirate", "~120 mL", "Wide-mouth specimen jar, sealed", "Intact seal; tan-brown semi-liquid; labeled; refrigerated"],
        ["SP-09", "Liver — unfixed tissue (right lobe)", "~50 g", "Wide-mouth specimen jar (no fixative), sealed", "Intact; refrigerated; labeled"],
        ["SP-12", "Scalp hair — root-intact (×30 strands, posterior vertex)", "30 strands", "Paper coin envelope, sealed", "Intact; dry; labeled; roots attached"],
    ], col_widths=[0.50*inch, 1.65*inch, 0.85*inch, 1.60*inch, 2.95*inch])]

    story += [SP(5), section("SECTION C — ANALYSES REQUESTED")]
    story += [tbl([
        ["Analysis Category", "Specimens", "Priority", "Notes / Specific Requests"],
        ["Volatile compounds / Ethanol",
         "SP-01 (blood); SP-06 (vitreous); SP-05 (urine)",
         "RUSH",
         "Full quantitative; report vitreous EtOH separately as primary postmortem alcohol indicator; note PMR concerns on blood specimens"],
        ["Comprehensive drug screen — immunoassay (qualitative)",
         "SP-01 (blood); SP-05 (urine)",
         "RUSH",
         "Broad screen including opiates, benzodiazepines, stimulants, cannabinoids, barbiturates, cocaine/metabolites, antidepressants, antipsychotics, anticonvulsants"],
        ["Confirmation and quantitation — all positives",
         "All positive-screening specimens",
         "RUSH",
         "GC-MS or LC-MS/MS confirmation and quantitation of all immunoassay positives; report in ng/mL with method noted"],
        ["Comprehensive therapeutic drug panel",
         "SP-01 (blood); SP-09 (liver)",
         "RUSH",
         "Cardiac drugs (digoxin, beta-blockers, CCBs, antiarrhythmics); antidepressants; anticoagulants; analgesics; sedative-hypnotics; anticonvulsants; report all detected with quantitation"],
        ["Heavy metals / Trace elements",
         "SP-01 (blood); SP-12 (hair)",
         "Standard",
         "Arsenic, mercury, lead, thallium, cyanide (blood only), and panel as appropriate; hair — segmental analysis if metals detected in blood"],
        ["Carbon monoxide / Carboxyhemoglobin",
         "SP-01 (blood)",
         "RUSH",
         "CO-Hgb saturation (% saturation); correlate with scene (no obvious source but office building — HVAC unknown)"],
        ["Cyanide (blood)",
         "SP-01 (blood — reserve aliquot)",
         "Standard",
         "If CO result is unremarkable; cyanide as general toxic screen component"],
        ["Electrolytes / Vitreous chemistry panel",
         "SP-06 (vitreous)",
         "Standard",
         "Na, K, Cl, glucose, BUN, creatinine; vitreous chemistry for postmortem interval estimation support and metabolic baseline"],
        ["Drugs of abuse — hair",
         "SP-12 (hair — segmental)",
         "Standard",
         "Segmental analysis of scalp hair for chronic drug use history (12-month window if sufficient hair length); opioids, stimulants, benzodiazepines, cocaine, cannabinoids"],
        ["Unknown compound identification — gastric / liver",
         "SP-08 (gastric); SP-09 (liver)",
         "RUSH",
         "Full qualitative scan for unknown compounds; prioritize any compounds not detected in blood screen; report all identifications regardless of concentration"],
    ], col_widths=[1.75*inch, 1.45*inch, 0.60*inch, 3.75*inch])]

    story += [SP(5), section("SECTION D — CASE CONTEXT FOR LABORATORY (NOT FOR PUBLIC DISCLOSURE)")]
    story += [body(
        "The decedent is a 46-year-old white female found deceased in her private office at a multi-story "
        "commercial building in Sioux Falls, South Dakota, after normal business hours. She was discovered "
        "by building janitorial staff and was found seated at her desk in a manner consistent with having "
        "become incapacitated while working. No witnesses to the event of loss of consciousness or collapse "
        "have been identified. No prescription medications were found at the scene and no treating physician "
        "has been identified at the time of this submission. The decedent's medical history is entirely "
        "unknown at this time."),
     body("The autopsy examination revealed no definitive anatomic cause of death on gross examination. "
          "Mild coronary atherosclerosis (estimated 30–40% LAD narrowing) was identified, with no gross "
          "evidence of acute plaque rupture or thrombosis. No acute intracranial pathology, no petechiae "
          "identified grossly, no neck hemorrhage, and no obvious acute trauma were found. A staining on "
          "the left interior cuff of the decedent's blouse was collected separately and submitted to SFPD "
          "CSU for characterization; the nature of this substance is unknown. The possibility of an "
          "exogenous toxic substance playing a role in this death cannot be excluded and is considered "
          "a priority question for the toxicologic examination. The submitting pathologist requests that "
          "the laboratory contact Dr. Adeyemi at (605) 367-4300 immediately upon any positive identification "
          "of a potentially toxic or controlled substance at any concentration level, prior to issuance of "
          "the formal written report.")]

    story += [SP(4), tbl([
        ["Submitted By (signature):", "______________________", "Print Name:", "Dennis H. Farr — MT-03", "Date:", "10/14/2015", "Time:", "1402 hrs"],
        ["Pathologist Authorization:", "______________________", "Print Name:", "Dr. R.G. Adeyemi, MD", "Date:", "10/14/2015", "Time:", "~1345 hrs"],
        ["Received By (Tox Lab):", "______________________", "Print Name:", "________________________", "Date:", "__________", "Time:", "________"],
    ], col_widths=[1.45*inch, 1.20*inch, 0.75*inch, 1.60*inch, 0.45*inch, 0.75*inch, 0.45*inch, 0.55*inch], has_hdr=False, alt=False)]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
