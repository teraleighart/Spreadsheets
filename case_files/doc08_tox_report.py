"""Document 08 — Toxicology Report (2 pages)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, PageBreak
from aging import make_onpage, W, H, STAMP_R, STAMP_B, HW_BLUE, HW_PENCIL
from styles import ST, HR, doc_header, section, subsection, body, body_l, small, SP, tbl

OUT = os.path.dirname(__file__)


def build():
    path = os.path.join(OUT, "ME-0447-08-Toxicology-Report.pdf")
    aging = {
        'staple': True,
        1: {
            'rings': [(W*0.82, H*0.78, 38, 141, 0.19, 61)],
            'creases': [(0, H*0.667, W, H*0.664, 91, 0.70)],
            'foxing': {'count': 36, 'inten': 0.82},
            'stamps': [("TOXICOLOGY REPORT — OFFICIAL", 0.85*inch, H - 1.70*inch, 0, STAMP_B, 11, 0.52)],
            'hw': [("see interp. page 2 — RGA", W-2.5*inch, H*0.31, -2, HW_BLUE, 8)],
        },
        2: {
            'rings': [(W*0.14, H*0.20, 44, 152, 0.20, 72)],
            'creases': [(0, H*0.335, W, H*0.332, 92, 0.75)],
            'foxing': {'count': 42, 'inten': 0.88},
            'stamps': [("PRELIMINARY — NOT FINAL", W*0.5-1.4*inch, 1.22*inch, -6, STAMP_R, 11, 0.55)],
            'hw': [("correlation required before conclusions", 0.82*inch, H*0.52, 2, HW_PENCIL, 8),
                   ("RGA — 11/18/2015", 0.82*inch, H*0.508, 2, HW_PENCIL, 7.5)],
        },
    }
    cb = make_onpage(108, "Toxicology Report", 2, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.80*inch, rightMargin=0.80*inch,
                            topMargin=0.75*inch, bottomMargin=0.72*inch)
    story = []

    # ═══════════════════════════════════════════════════════════════════════
    # PAGE 1 — Lab identification, specimens, results table
    # ═══════════════════════════════════════════════════════════════════════
    story += doc_header("TOXICOLOGY LABORATORY REPORT",
                        "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  DOB: 03/22/1969  |  Page 1 of 2")

    story += [tbl([
        ["ME Case #:", "2015-ME-0447",                     "Tox Lab Case #:", "MCME-TOX-2015-0841"],
        ["Decedent:", "MARSH, Eleanor Anne",               "DOB:", "March 22, 1969  |  Age: 46"],
        ["Date Specimens Received:", "October 14, 2015 — 1402 hrs",
         "Date Report Issued:", "November 14, 2015"],
        ["Report Status:", "PRELIMINARY — Pending Pathologist Review and Signout",
         "Report Version:", "1.0 (Initial)"],
        ["Lab Director:", "Dr. Constance M. Heikkila, PhD, D-ABFT",
         "Analyst Assigned:", "Marcus T. Vogelmann, MS, D-ABFT (Tox Spec. III)"],
        ["Submitting Pathologist:", "Dr. Raymond G. Adeyemi, MD — Deputy Chief ME",
         "Rush Status:", "RUSH — Priority-1 Suspicious"],
        ["Lab Address:", "220 W. Sixth Street, Suite 140, Sioux Falls, SD 57104",
         "Lab Phone:", "(605) 367-4310"],
    ], col_widths=[1.50*inch, 2.55*inch, 1.40*inch, 2.10*inch], has_hdr=False, alt=False)]

    story += [SP(5), section("SPECIMENS RECEIVED AND CONDITION")]
    story += [tbl([
        ["Spec. ID", "Type", "Volume Received", "Condition at Receipt", "Analysis Performed"],
        ["SP-01", "Peripheral blood — femoral (NaF/KOx ×2)", "9.8 mL (loss during transport normal)", "Seals intact; labels intact; no leakage; mild hemolysis noted (postmortem artifact)",
         "Ethanol; comprehensive screen; confirmation/quant. of positives; CO-Hgb; cyanide; heavy metals"],
        ["SP-02", "Peripheral blood — femoral (EDTA)", "4.9 mL", "Intact; labeled; normal appearance",
         "Drugs of abuse immunoassay; therapeutic panel; confirmations"],
        ["SP-04", "Central blood — cardiac RV (NaF/KOx ×2)", "9.5 mL", "Intact; labeled; mild hemolysis (postmortem)",
         "Ethanol; comprehensive screen; comparison purposes — results qualified per Section C note"],
        ["SP-05", "Urine — bladder aspirate", "38 mL", "Intact seal; pale yellow-amber, slightly cloudy; labeled",
         "Ethanol; drugs of abuse immunoassay; therapeutic panel; confirmations"],
        ["SP-06", "Vitreous humor — right eye", "2.4 mL (minor loss at centrifugation)", "Intact; clear; labeled",
         "Ethanol; electrolytes (Na/K/Cl/glucose/BUN); drugs"],
        ["SP-08", "Gastric contents", "~112 mL (evaporative loss)", "Intact seal; tan-brown semi-liquid; labeled; refrigerated",
         "Qualitative scan; compound ID; ethanol; drugs"],
        ["SP-09", "Liver — unfixed tissue", "48 g", "Intact; refrigerated; normal appearance on receipt; labeled",
         "Tissue ethanol; tissue drug concentrations for confirmed positives"],
        ["SP-12", "Scalp hair — root-intact", "30 strands (approx. 7 cm average length)", "Intact; labeled; dry",
         "Segmental hair analysis (12-month window; 1 cm per segment); drugs; heavy metals"],
    ], col_widths=[0.50*inch, 1.55*inch, 0.85*inch, 1.65*inch, 3.00*inch])]

    story += [SP(5), section("ANALYTICAL RESULTS — SUMMARY TABLE")]
    story += [body(
        "Results below represent all compounds detected above applicable reporting thresholds. Compounds "
        "screened but not detected at reportable concentrations are listed in the negative panel summary "
        "following the results table. Units are mg/L unless otherwise noted. Abbreviations: "
        "Peri-B = peripheral blood (femoral); Cent-B = central blood (cardiac); U = urine; V = vitreous; "
        "GC = gastric contents; Liv = liver tissue (mg/kg); H = hair (ng/mg per cm segment); "
        "ND = not detected; NP = not performed on this specimen; Qual. = qualitative only; &lt;LOQ = detected below limit of quantitation.")]
    story += [SP(3), tbl([
        ["Compound / Class", "Peri-B\n(mg/L)", "Cent-B\n(mg/L)", "Urine\n(mg/L)", "Vitreous\n(mg/L)", "Gastric\n(mg/L)", "Liver\n(mg/kg)", "Notes"],
        ["Ethanol", "See note", "See note", "See note", "See note", "See note", "NP",
         "WITHHELD PENDING FINAL PATHOLOGIST REVIEW — report values will be disclosed in final signed report; consult Dr. Adeyemi"],
        ["Carbon monoxide (CO-Hgb %sat)", "See note", "NP", "NP", "NP", "NP", "NP",
         "WITHHELD — see pathologist consultation note"],
        ["Cyanide (blood)", "ND", "NP", "NP", "NP", "NP", "NP",
         "Not detected at reportable threshold; method: modified Conway microdiffusion"],
        ["Compounds — Class I (acid screen)", "See note", "See note", "See note", "NP", "See note", "See note",
         "WITHHELD — one or more compounds detected; identities and concentrations reserved pending pathologist sign-out and final report"],
        ["Compounds — Class II (basic screen)", "See note", "See note", "See note", "NP", "See note", "See note",
         "WITHHELD — see above"],
        ["Compounds — Class III (neutral screen)", "ND/NP", "ND/NP", "ND/NP", "NP", "ND/NP", "ND/NP",
         "No reportable compounds detected in neutral screen — standard immunoassay and GC/MS"],
        ["Heavy metals panel (As, Hg, Pb, Tl)", "See note", "NP", "NP", "NP", "NP", "NP",
         "WITHHELD — results reserved pending pathologist sign-out"],
        ["Hair — drugs (segmental, per cm)", "NP", "NP", "NP", "NP", "NP", "NP",
         "WITHHELD — hair analysis results reserved pending sign-out; consult Dr. Adeyemi before distribution"],
        ["Vitreous — electrolytes / chemistry", "NP", "NP", "NP", "See note", "NP", "NP",
         "WITHHELD — values documented; significance interpretation reserved for pathologist in final report"],
    ], col_widths=[1.75*inch, 0.52*inch, 0.52*inch, 0.52*inch, 0.52*inch, 0.52*inch, 0.52*inch, 2.58*inch])]

    story += [SP(4), small(
        "NOTE TO RECEIVING PATHOLOGIST: Per your verbal instruction to the laboratory on October 14, 2015, "
        "and the written note on the Toxicology Submission Form (Case 2015-ME-0447), the Minnehaha County "
        "ME Toxicology Laboratory has complied with your directive to withhold specific compound identifications "
        "and concentrations from this preliminary report pending direct consultation. Dr. Adeyemi has been "
        "notified by telephone (November 3, 2015) of preliminary laboratory findings. The complete results "
        "table, including all identified compounds and concentrations, will be incorporated into the Final "
        "Toxicology Report upon Dr. Adeyemi's written authorization for release. Distribution of this "
        "preliminary report is restricted to the pathologist of record and the Chief ME. No results are "
        "to be released to law enforcement, next-of-kin, or any other party pending the final signed report.")]

    story += [PageBreak()]

    # ═══════════════════════════════════════════════════════════════════════
    # PAGE 2 — Interpretive Statement, Limitations, Sign-off
    # ═══════════════════════════════════════════════════════════════════════
    story += doc_header("TOXICOLOGY REPORT — CONTINUATION",
                        "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  Page 2 of 2")

    story += [section("NEGATIVE PANEL — COMPOUNDS SCREENED AND NOT DETECTED")]
    story += [body(
        "The following compound classes and specific agents were screened using validated immunoassay and/or "
        "chromatographic methods and were not detected at or above applicable reporting thresholds in the "
        "indicated specimen types. 'Not detected' does not mean 'absent'; it indicates that the compound was "
        "not present at or above the established cutoff concentration for the method used.")]
    story += [tbl([
        ["Compound Class / Specific Agents", "Specimens Tested", "Method", "Result"],
        ["Cyanide", "Peripheral blood", "Modified Conway microdiffusion", "NOT DETECTED"],
        ["Organic phosphorus compounds (organophosphate pesticides)", "Blood; gastric contents; liver", "GC-MS", "NOT DETECTED"],
        ["Carbamate compounds", "Blood; urine", "GC-MS", "NOT DETECTED"],
        ["Strychnine", "Blood; urine; gastric", "GC-MS", "NOT DETECTED"],
        ["Ricin / protein toxin marker", "Blood", "ELISA (screening)", "NOT DETECTED"],
        ["Iron (toxic range)", "Blood", "ICP-MS", "NOT DETECTED (within normal reference range)"],
        ["Antifreeze components (ethylene glycol metabolites — glycolic acid)", "Blood; urine", "GC-MS / enzymatic", "NOT DETECTED"],
        ["Salicylates", "Blood; urine", "Colorimetric / GC-MS", "NOT DETECTED"],
        ["Acetaminophen", "Blood; urine", "Colorimetric / LC-MS", "NOT DETECTED at toxic threshold"],
        ["Class III neutral compounds (volatile solvents, non-acid/base toxicants)", "Blood; urine; gastric", "GC-MS headspace", "NOT DETECTED"],
        ["Digoxin / digitalis glycosides", "Blood", "ELISA immunoassay; LC-MS confirmation", "NOT DETECTED — below assay LOD"],
        ["Insulin / hypoglycemic agents — immunoassay", "Blood", "ELISA (screening)", "NOT DETECTED — note: postmortem insulin quantitation unreliable; blood glucose withheld pending interpretation"],
    ], col_widths=[2.55*inch, 1.40*inch, 1.35*inch, 2.25*inch])]

    story += [SP(5), section("INTERPRETIVE STATEMENT AND LIMITATIONS")]
    story += [body(
        "This section provides interpretive guidance from the toxicology laboratory for the use of the "
        "certifying pathologist. The interpretive statement does not constitute a determination of cause "
        "or manner of death; that determination rests exclusively with the pathologist and the medical "
        "examiner office. The following limitations apply to all results and interpretations in this report "
        "and must be communicated to any recipient of toxicology results.")]

    story += [subsection("Postmortem Redistribution (PMR)")]
    story += [body(
        "All drug and alcohol concentrations determined from postmortem blood specimens — including both "
        "peripheral (femoral) and central (cardiac) blood — are subject to the phenomenon of postmortem "
        "redistribution (PMR). PMR refers to the redistribution of drugs and other substances within the "
        "body after death, driven by passive diffusion, putrefactive processes, and changes in tissue "
        "binding, pH, and protein integrity. PMR can result in measured drug concentrations in postmortem "
        "blood that are substantially higher or lower than the antemortem (in-life) blood concentration "
        "at or near the time of death. The degree of PMR is variable across drug classes, route of "
        "administration, dosing history, time since last dose, and postmortem interval. Drugs with large "
        "volumes of distribution, high tissue binding, or cardiac or pulmonary depot concentrations are "
        "generally more susceptible to PMR, and central blood concentrations are typically more affected "
        "than peripheral blood. Peripheral femoral blood is the preferred specimen for postmortem "
        "quantitation but is not immune to PMR. All quantitative blood results in this case must be "
        "interpreted with this limitation prominently in mind, and antemortem drug concentrations "
        "cannot be reliably back-calculated from postmortem measurements alone.")]

    story += [subsection("Vitreous Humor as Alternative Specimen")]
    story += [body(
        "Vitreous humor from the right eye was submitted and analyzed in this case. Vitreous is generally "
        "less susceptible to postmortem redistribution than blood, due to its physical isolation from "
        "the central circulation and the relative avascular nature of the vitreous compartment. Vitreous "
        "ethanol concentration is considered more reflective of the true antemortem blood alcohol "
        "concentration than postmortem blood and is the preferred specimen for alcohol quantitation when "
        "available. Vitreous drug concentrations, however, are not uniformly predictive of blood "
        "concentrations for all drug classes; correlation between vitreous and blood drug levels varies "
        "by compound and should be interpreted cautiously. Electrolyte and metabolite values from vitreous "
        "are documented and may assist in estimating antemortem metabolic status and postmortem interval, "
        "but reference ranges for vitreous chemistry are subject to postmortem change and should be "
        "interpreted with appropriate caution.")]

    story += [subsection("Tolerance, Polypharmacy, and Unknown Baseline")]
    story += [body(
        "A critical limitation in this case is the complete absence of the decedent's antemortem medical "
        "history, medication list, and baseline drug or substance use information at the time of this "
        "report's preparation. The clinical significance of any detected drug concentration depends in "
        "substantial part on whether the decedent was a chronic user of the identified substance (which "
        "can elevate tolerance, altering the pharmacologically effective or lethal concentration), whether "
        "the substance was prescribed at a specific therapeutic dose (which provides a clinical baseline "
        "for comparison), and whether multiple substances were co-administered (which may produce "
        "pharmacodynamic interactions not predictable from individual concentrations alone). Without "
        "this information, the toxicology laboratory cannot determine whether any detected concentration "
        "represents a therapeutic level, a supratherapeutic level, a potentially toxic level, or a "
        "concentration consistent with postmortem redistribution of a prescribed therapeutic dose. "
        "This determination requires integration of toxicology results with all available clinical, "
        "investigative, and autopsy information by the certifying pathologist. The laboratory recommends "
        "that every effort be made to obtain the decedent's medication history, pharmacy records, and "
        "medical records before the final toxicology report is issued.")]

    story += [subsection("Hair Analysis — Limitations")]
    story += [body(
        "Segmental hair analysis provides information about drug exposure over an extended historical "
        "window rather than at the time of death. Results from hair analysis are not quantitatively "
        "comparable to blood or urine drug concentrations and cannot be used to determine a blood "
        "concentration at any particular time. Hair drug concentrations are influenced by melanin "
        "content, cosmetic treatment, environmental contamination, and hair growth rate variability. "
        "A negative hair result does not definitively exclude prior drug exposure; a positive hair "
        "result confirms exposure during the analyzed growth period but does not establish timing "
        "or frequency with precision. Hair analysis results in this case are to be used as supplemental "
        "historical context only, not as primary toxicologic evidence.")]

    story += [SP(4), section("DISTRIBUTION AND SIGN-OFF")]
    story += [tbl([
        ["Report Distribution:", "Dr. R.G. Adeyemi, MD (pathologist of record — primary); Dr. P.H. Reinholt, MD (Chief ME — copy); Case File 2015-ME-0447. "
                                 "NOT FOR RELEASE to law enforcement, next-of-kin, or any other party without written authorization by the certifying pathologist and/or Chief ME."],
    ], col_widths=[1.40*inch, 6.15*inch], has_hdr=False, alt=False)]
    story += [SP(4), tbl([
        ["Toxicologist Signature:", "______________________", "Print Name:", "Marcus T. Vogelmann, MS, D-ABFT",   "Date:", "11/14/2015"],
        ["Lab Director Signature:", "______________________", "Print Name:", "Dr. Constance M. Heikkila, PhD, D-ABFT", "Date:", "11/14/2015"],
        ["Pathologist Received:", "______________________", "Print Name:", "Dr. Raymond G. Adeyemi, MD",        "Date:", "__________"],
        ["Pathologist Reviewed:", "______________________", "Notes:", "Final release pending pathologist signout. Final report to supersede this preliminary report upon issuance.", "", ""],
    ], col_widths=[1.40*inch, 1.25*inch, 0.80*inch, 2.35*inch, 0.45*inch, 1.30*inch], has_hdr=False, alt=False)]

    story += [SP(6), small(
        "This report is the property of the Minnehaha County Office of the Medical Examiner and the "
        "Minnehaha County ME Toxicology Laboratory. It is intended solely for use by authorized personnel "
        "of those offices in connection with Case 2015-ME-0447. Unauthorized reproduction, distribution, "
        "or use is prohibited. This is a PRELIMINARY report; results are subject to revision. A final "
        "signed toxicology report will be issued following pathologist review and authorization. "
        "Lab Case #: MCME-TOX-2015-0841  |  Analytical file archived per laboratory standard operating procedure.")]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
