"""Document 05 — Autopsy Report (7 pages)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, PageBreak
from aging import make_onpage, W, H, STAMP_R, STAMP_B, HW_BLUE, HW_PENCIL
from styles import ST, HR, doc_header, section, subsection, body, body_l, small, SP, tbl

OUT = os.path.dirname(__file__)


def build():
    path = os.path.join(OUT, "ME-0447-05-Autopsy-Report.pdf")

    aging = {
        'staple': True,
        1: {
            'rings': [(W*0.83, H*0.82, 40, 111, 0.20, 34)],
            'creases': [(0, H*0.335, W, H*0.332, 61, 0.78)],
            'foxing': {'count': 38, 'inten': 0.88},
            'stamps': [("AUTOPSY PERFORMED", 0.85*inch, H - 1.75*inch, 0, STAMP_B, 12, 0.55)],
            'hw': [("0900 hrs — Adeyemi / Sandvik", 0.85*inch, H - 2.05*inch, 0, HW_BLUE, 8)],
        },
        2: {
            'rings': [(W*0.12, H*0.18, 48, 122, 0.21, 44)],
            'creases': [(0, H*0.50, W, H*0.498, 62, 0.70)],
            'foxing': {'count': 44, 'inten': 0.85},
            'hw': [("livor fixed — noted", W*0.78, H*0.38, -3, HW_PENCIL, 7.5)],
        },
        3: {
            'rings': [(W*0.85, H*0.55, 35, 133, 0.19, 53)],
            'creases': [(0, H*0.335, W, H*0.337, 63, 0.68)],
            'foxing': {'count': 42, 'inten': 0.90},
        },
        4: {
            'rings': [(W*0.13, H*0.82, 42, 144, 0.22, 64)],
            'creases': [(0, H*0.667, W, H*0.664, 64, 0.80)],
            'foxing': {'count': 40, 'inten': 0.86},
            'hw': [("coronary — request histo blocks", W-2.9*inch, H*0.60, 2, HW_BLUE, 7.5)],
        },
        5: {
            'rings': [(W*0.82, H*0.20, 46, 155, 0.20, 75)],
            'creases': [(0, H*0.50, W, H*0.502, 65, 0.72)],
            'foxing': {'count': 46, 'inten': 0.92},
            'hw': [("histo: brain / liver / kidney / heart", 0.82*inch, H*0.72, 1, HW_BLUE, 8)],
        },
        6: {
            'rings': [(W*0.15, H*0.25, 38, 166, 0.18, 86)],
            'creases': [(0, H*0.335, W, H*0.332, 66, 0.74)],
            'foxing': {'count': 38, 'inten': 0.85},
        },
        7: {
            'rings': [(W*0.82, H*0.72, 44, 177, 0.21, 97)],
            'creases': [(0, H*0.50, W, H*0.498, 67, 0.76)],
            'foxing': {'count': 40, 'inten': 0.88},
            'stamps': [("PRELIMINARY — CAUSE/MANNER DEFERRED", W*0.5-2.3*inch, 1.20*inch, -4, STAMP_R, 10, 0.55)],
            'hw': [("not for release — RGA 10/16", W-2.9*inch, 1.70*inch, 0, HW_BLUE, 7.5)],
        },
    }

    cb = make_onpage(105, "Autopsy Report", 7, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.80*inch, rightMargin=0.80*inch,
                            topMargin=0.75*inch, bottomMargin=0.72*inch)
    story = []

    # ═══════════════════════════════════════════════════════════════════════
    # PAGE 1 — Authority, ID, External Examination Summary
    # ═══════════════════════════════════════════════════════════════════════
    story += doc_header("AUTOPSY REPORT",
                        "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  DOB: 03/22/1969  |  Page 1 of 7")

    story += [tbl([
        ["ME Case #:", "2015-ME-0447",                "Autopsy #:", "AR-2015-0447"],
        ["Decedent Name:", "MARSH, Eleanor Anne",     "DOB:", "March 22, 1969 (Age: 46)"],
        ["Sex:", "Female",                            "Race:", "White / Non-Hispanic (per intake; unverified by pathologist)"],
        ["Height (measured):", "66.0 inches (5 ft 6 in)", "Weight (measured):", "149.4 lbs (67.8 kg)"],
        ["Date of Autopsy:", "October 14, 2015",      "Time Begun:", "0902 hrs CDT"],
        ["Time Concluded:", "1318 hrs CDT",           "Total Elapsed:", "Approximately 4 hours 16 minutes"],
        ["Location:", "Minnehaha County ME Facility — Autopsy Suite A", "Table #:", "A-1"],
        ["Pathologist (Primary):", "Raymond G. Adeyemi, MD, Forensic Pathologist, Deputy Chief ME",
         "Observer / Assisting:", "Dr. Elaine L. Sandvik, MD (Forensic Pathology Fellow)"],
        ["Mortuary Tech.:", "Dennis H. Farr (MT-03) — primary tech.",
         "Photo-Documentation:", "Thomas A. Nkrumah (ME Photography Tech.)"],
        ["LE Present:", "Det. Marcus J. Orre, SFPD (0902–1115 hrs); Sgt. Patricia D. Cull, SFPD (0902–1008 hrs)",
         "", ""],
        ["Body Identified To Pathologist By:", "Exterior body bag tag, ME facility wristband (applied at intake), and case record — Case 2015-ME-0447",
         "ID Confirmed Consistent:", "YES — tag, wristband, and case record all consistent at time of autopsy"],
        ["Seal Status at Autopsy:", "ME Seal #MEO-S-2015-3391 — present and intact; broken by Dr. Adeyemi at 0902 hrs in presence of all listed personnel",
         "", ""],
        ["Autopsy Authority:", "Medical Examiner jurisdiction per SD Codified Law §23-14-1; authorized by Chief ME Dr. P.H. Reinholt, 10/14/2015 0705 hrs",
         "", ""],
    ], col_widths=[1.85*inch, 2.30*inch, 1.40*inch, 2.00*inch], has_hdr=False, alt=False)]

    story += [SP(5), section("EXTERNAL EXAMINATION — SUMMARY")]
    story += [subsection("Body Presentation and Clothing")]
    story += [body(
        "The body of Eleanor Anne Marsh was received at the autopsy suite in a white ME body bag bearing seal "
        "number MEO-S-2015-3391 and an exterior identification tag consistent with the case record. The seal "
        "was examined and found intact prior to opening at 0902 hours by Dr. Adeyemi in the presence of the "
        "attending mortuary technician, forensic pathology fellow, SFPD detectives, and ME photography "
        "technician. The body was that of an adult female, fully clothed in the garments listed in the "
        "personal effects inventory (Case 2015-ME-0447), consistent with those described in the death "
        "investigation report. Clothing was intact and in anatomical position. No rearrangement, tearing, "
        "cutting, or staining inconsistent with normal wear was identified on any item of clothing."),
     body("Clothing was removed in the standard fashion and each item was examined, photographed, and packaged "
          "for retention. No foreign materials, substances, projectiles, defects, or other evidentiary items "
          "were identified on or within the clothing during this examination, with the exception of a faint "
          "brownish staining on the interior left cuff of the blouse, the nature of which is undetermined "
          "pending further study; a sample of this staining was collected and submitted per the specimen "
          "retention sheet for this case.")]

    story += [subsection("General External Description")]
    story += [body(
        "The body is that of an adult white female, consistent with the reported age of 46 years, measuring "
        "66.0 inches (167.6 cm) in height and weighing 149.4 pounds (67.8 kg). Body habitus is lean-normal; "
        "nutritional status is adequate. The skin is pale and cool to the touch, consistent with postmortem "
        "changes and refrigerated storage. Hair is medium brown, naturally pigmented with scattered grey, "
        "shoulder length, in a neat professional style and in a state consistent with a normal workday; no "
        "gross disarray. Irides are hazel-brown. Sclerae are white. Conjunctivae are examined and reveal "
        "no petechial hemorrhage identified on gross examination. Oral cavity: lips are intact, no lacerations "
        "or contusions; dentition is intact and in adequate repair; no foreign material identified in the oral "
        "cavity or oropharynx on gross inspection. Natural dentition; no gross abnormalities."),
     body("Head and scalp: no scalp lacerations, abrasions, or contusions identified. The skull is intact on "
          "palpation and no step-off deformities or crepitus is noted. Facial bones are intact on palpation "
          "without deformity. Ears are without injury. No blood, fluid, or foreign material is identified at "
          "the external auditory canals or nares bilaterally. Neck: the anterior and lateral neck surfaces are "
          "examined without gross abnormality identified; no contusions, abrasions, petechiae, ligature marks, "
          "or patterned injuries are identified on the neck on gross external examination. The larynx and "
          "hyoid bone are assessed by palpation and are grossly intact without tenderness or crepitus; formal "
          "assessment is completed at the time of internal examination.")]

    story += [PageBreak()]

    # ═══════════════════════════════════════════════════════════════════════
    # PAGE 2 — External Continuation, Postmortem Changes
    # ═══════════════════════════════════════════════════════════════════════
    story += doc_header("AUTOPSY REPORT — CONTINUATION",
                        "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  Page 2 of 7")

    story += [section("EXTERNAL EXAMINATION — CONTINUATION")]
    story += [subsection("Upper Extremities")]
    story += [body(
        "The upper extremities are symmetric and well-formed. The hands are examined and reveal no defensive "
        "injuries — no abrasions, lacerations, or patterned impact injuries are identified on the dorsal or "
        "palmar surfaces of either hand. The fingernails are present, intact, and of moderate length, with "
        "applied nail polish, pink-nude color, in good condition consistent with a recent professional manicure. "
        "No subungual debris of evidentiary significance is grossly apparent; nail clippings were obtained from "
        "all ten digits and submitted for trace evidence analysis per the specimen retention sheet. No "
        "venipuncture marks, injection sites, or track marks are identified on the antecubital fossae, "
        "forearms, dorsal hands, or other accessible sites bilaterally on gross examination. A small, "
        "well-healed scar measuring approximately 1.0 × 0.2 cm is identified on the dorsal right forearm "
        "at mid-shaft; the scar is pale, flat, and appears of remote vintage with no acute inflammatory "
        "changes; etiology undetermined."),
     body("The wrists are examined on all surfaces; no ligature or restraint marks, contusions, or abrasions "
          "are identified. Forearms bilaterally: no injuries. Upper arms bilaterally: no injuries. Both "
          "axillae are examined; no abnormalities. The wristwatch (Item J-02 per property inventory) was "
          "present on the left wrist and was removed during clothing examination.")]

    story += [subsection("Trunk — Anterior Surface")]
    story += [body(
        "The anterior trunk is examined following clothing removal. The skin of the anterior chest, abdomen, "
        "and flanks is intact bilaterally with no lacerations, abrasions, contusions, patterned injuries, or "
        "puncture wounds identified on gross examination. The breasts are symmetric without masses, skin "
        "changes, or nipple abnormality. The abdomen is flat without gross distension. The anterior abdominal "
        "wall demonstrates no surgical scars; specifically, no laparotomy scars, laparoscopic port sites, or "
        "appendectomy scars are identified. A well-healed, narrow linear scar is present at the right lower "
        "costal margin, approximately 3.5 cm in length and 0.1 cm in width; this is consistent in appearance "
        "with a remote minor surgical or traumatic scar; no recent inflammatory changes. No other scars, "
        "tattoos, or identifying marks are identified on the anterior trunk.")]

    story += [subsection("Lower Extremities")]
    story += [body(
        "The lower extremities are symmetric and well-formed. No lacerations, abrasions, or contusions are "
        "identified on the anterior or lateral surfaces of either thigh, knee, leg, or foot on gross "
        "examination. No patterned injuries or ligature marks are identified. The ankles and feet are intact. "
        "The toenails are present and intact with applied polish consistent in color with the fingernails. "
        "No venipuncture or injection sites are identified on the lower extremities. The right knee demonstrates "
        "a remote, well-healed surgical scar approximately 4.0 cm in length on the medial aspect; consistent "
        "in appearance with a prior meniscal or ligamentous repair; no acute changes. No varicosities, edema, "
        "or skin changes suggestive of chronic venous disease or pedal edema are identified.")]

    story += [subsection("Back and Posterior Surfaces")]
    story += [body(
        "The decedent is turned to the prone position for examination of the posterior surfaces. The scalp, "
        "posterior neck, back, buttocks, and posterior lower extremities are examined. No lacerations, "
        "abrasions, contusions, or patterned injuries are identified. The skin of the posterior trunk is "
        "intact. No evidence of posterior trauma is identified on gross examination. The spine is palpated "
        "along its length; no deformities, step-off, or crepitus.")]

    story += [subsection("Postmortem Changes — Detailed Assessment")]
    story += [body(
        "Livor mortis is present and is fixed and well-developed. The pattern of livor is predominantly "
        "posterior and right lateral, consistent with a position approximating the seated and right-laterally "
        "inclined body position described in the death investigation report. Livor does not blanch with "
        "finger pressure at any site tested. No paradoxical lividity pattern (inconsistency between current "
        "body position and lividity distribution) is identified. The posterior aspects of the upper arms and "
        "right lateral trunk demonstrate the most prominent lividity. The distribution of livor is broadly "
        "consistent with the position in which the decedent was found, though formal interpretation of "
        "positional consistency requires correlation with scene information; this correlation is noted and "
        "discussed in Section 12 of this report."),
     body("Rigor mortis is present throughout at the time of the autopsy examination. Rigor was well-established "
          "in the jaw, neck, and upper extremities at the time of scene examination per the death investigation "
          "report. At the time of autopsy (0902–1318 hours, October 14, 2015), rigor is present and moderately "
          "firm in all muscle groups assessed. This pattern is broadly consistent with the estimated postmortem "
          "interval of approximately three to nine hours at the time of discovery, with the caveat that rigor "
          "is influenced by multiple factors including ambient temperature, body habitus, and physical activity "
          "at or near the time of death, and cannot alone be used to precisely estimate time of death."),
     body("Body temperature: the body was refrigerated at the ME facility from 0624 hours on October 14, 2015 "
          "until the time of autopsy commencement. Formal body temperature at autopsy is not a reliable "
          "postmortem interval estimator in this context and is not recorded as such. No decomposition changes "
          "are identified; the skin is intact and without bullae, slippage, or putrefactive discoloration. "
          "The eyes are partially open and the sclerae are mildly clouded, consistent with postmortem "
          "desiccation and the estimated postmortem interval.")]

    story += [PageBreak()]

    # ═══════════════════════════════════════════════════════════════════════
    # PAGE 3 — Internal Exam Overview, Organs, Cardiovascular/GI Summary
    # ═══════════════════════════════════════════════════════════════════════
    story += doc_header("AUTOPSY REPORT — CONTINUATION",
                        "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  Page 3 of 7")

    story += [section("INTERNAL EXAMINATION")]
    story += [subsection("Opening and Body Cavity")]
    story += [body(
        "A standard Y-shaped thoracoabdominal incision was made, extending from each shoulder to the sternal "
        "notch and then downward to the pubic symphysis with deflection around the umbilicus. The subcutaneous "
        "tissue of the chest wall is tan-yellow and of normal thickness, without contusions, hemorrhage, or "
        "traumatic separation. The panniculus is approximately 1.5 to 2 cm in thickness, consistent with the "
        "lean-normal body habitus. The anterior chest plate was removed by sectioning the costochondral "
        "junctions bilaterally, revealing the thoracic cavity. No rib fractures, sternum fractures, or anterior "
        "chest wall injuries were identified at this time. No subcutaneous emphysema. The peritoneum was "
        "entered and the abdominal contents were visually surveyed in situ prior to organ removal."),
     body("The thoracic cavity contains no abnormal fluid accumulation bilaterally. No hemothorax, chylothorax, "
          "or significant pleural effusion is present. The lungs fill the thoracic cavity symmetrically. The "
          "pericardial sac is intact and without distension. The abdominal cavity contains no free blood, "
          "abnormal fluid, or gross evidence of perforation, spillage of intestinal contents, or peritonitis. "
          "The abdominal organs are in normal anatomical position; no gross displacement. The retroperitoneum "
          "is examined and is without evidence of hemorrhage or mass. The pelvis is examined; no free pelvic "
          "fluid or pelvic mass identified on gross examination.")]

    story += [subsection("Organ Weights and Summary Table")]
    story += [tbl([
        ["Organ", "Weight (grams)", "Reference Range (approx.)", "Gross Description Summary"],
        ["Heart",         "332 g",   "250–400 g (F)",  "Symmetric chambers; no gross hypertrophy; coronaries patent on gross probing — see p.4"],
        ["Right Lung",    "408 g",   "300–500 g (F)",  "Pink-grey, spongy, no consolidation; anthracotic pigment minimal"],
        ["Left Lung",     "378 g",   "275–450 g (F)",  "Pink-grey, spongy; mild dependent congestion; no consolidation"],
        ["Liver",         "1,384 g", "1,200–1,600 g",  "Brown-red, smooth capsule; no nodularity; mild congestion on cut surface"],
        ["Spleen",        "148 g",   "100–200 g",      "Purple-red, firm, intact capsule; no gross pathology"],
        ["Left Kidney",   "141 g",   "120–170 g",      "Smooth cortex; normal corticomedullary differentiation"],
        ["Right Kidney",  "138 g",   "120–170 g",      "Smooth cortex; normal corticomedullary differentiation"],
        ["Brain",         "1,302 g", "1,200–1,400 g",  "No gross focal lesions; mild diffuse congestion — see p.5"],
        ["Thyroid",       "19 g",    "15–30 g",        "Tan-brown, symmetric lobes; no nodules on cut surface"],
        ["Left Adrenal",  "8 g",     "5–12 g",         "Yellow-tan, normal architecture; no gross lesions"],
        ["Right Adrenal", "7 g",     "5–12 g",         "Yellow-tan, normal architecture; no gross lesions"],
        ["Pancreas",      "82 g",    "70–110 g",       "Lobular; tan-yellow; no gross masses or necrosis"],
        ["Uterus",        "64 g",    "40–80 g (non-pregnant)", "Smooth serosal surface; myometrium without obvious lesion"],
        ["Left Ovary",    "11 g",    "5–15 g",         "Grey-white; no gross masses or cysts; post-follicular changes"],
        ["Right Ovary",   "9 g",     "5–15 g",         "Grey-white; small functional-appearing cyst (approx. 0.8 cm); no gross pathology"],
    ], col_widths=[1.20*inch, 0.88*inch, 1.35*inch, 4.12*inch])]

    story += [SP(4), subsection("Gastrointestinal System")]
    story += [body(
        "The esophagus is intact, without lacerations, Mallory-Weiss tears, or erosions. The gastroesophageal "
        "junction is unremarkable. The stomach contains an estimated 100–150 mL of partially digested material, "
        "tan-brown, semi-liquid in consistency, without gross evidence of blood (old or fresh). No gross foreign "
        "material identified in the gastric contents on visual inspection; gastric contents were aspirated and "
        "submitted in their entirety for toxicological analysis per the specimen retention sheet. The stomach "
        "mucosa is intact without ulceration, erosion, or hemorrhage. The small intestine is examined in "
        "segments; the mucosa is intact throughout its accessible length; no obstructions, perforations, or "
        "masses are identified. The large intestine and colon are examined and without gross pathology. The "
        "rectum and anal canal are intact and without injury. The appendix is present and not grossly inflamed."),
     body("The liver is described in the organ weight summary. On cut surface, the hepatic parenchyma is "
          "brown-red with a mildly accentuated lobular pattern consistent with mild centrilobular congestion; "
          "no discrete nodules, masses, cysts, or areas of hemorrhage or necrosis are identified. The gallbladder "
          "is present and contains approximately 15 mL of dark green bile; the gallbladder wall is thin and "
          "without inflammation; three small, well-formed cholesterol calculi, the largest measuring "
          "approximately 0.6 cm in greatest dimension, are identified within the gallbladder lumen. These "
          "findings are consistent with uncomplicated cholelithiasis without acute cholecystitis and are of "
          "indeterminate significance to the cause of death; tissue sections are submitted for histologic review.")]

    story += [PageBreak()]

    # ═══════════════════════════════════════════════════════════════════════
    # PAGE 4 — Cardiovascular and Respiratory Continuation
    # ═══════════════════════════════════════════════════════════════════════
    story += doc_header("AUTOPSY REPORT — CONTINUATION",
                        "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  Page 4 of 7")

    story += [section("CARDIOVASCULAR SYSTEM — DETAILED EXAMINATION")]
    story += [body(
        "The heart was removed in the standard fashion following examination of the great vessels in situ. "
        "The pericardial sac was intact, smooth, and without adhesions, fibrin deposits, or effusion on "
        "gross examination. The heart weighed 332 grams, within the normal range for an adult female of "
        "this body habitus. The epicardial surface is smooth with a normal distribution of subepicardial "
        "adipose tissue; no contusions, lacerations, or focal lesions are identified on the epicardial "
        "surface. The coronary arteries are examined in their proximal, mid, and distal segments by "
        "transverse sectioning at 3–5 mm intervals following standard perfusion-fixed sections."),
     body("Right coronary artery (RCA): patent throughout its course. The ostium is in normal position. "
          "Mild fibromuscular intimal thickening is present in the proximal segment without hemodynamically "
          "significant stenosis identified on gross examination; estimated cross-sectional luminal diameter "
          "is approximately 90–95% of normal at the most involved segment. No acute plaque rupture, "
          "ulceration, or superimposed thrombosis identified on gross exam; histologic sections submitted. "
          "Left main coronary artery: patent; no significant stenosis. Left anterior descending (LAD): "
          "mild-to-moderate atherosclerotic change in the proximal third; estimated 30–40% luminal narrowing "
          "at the most involved segment; no acute thrombosis or plaque rupture on gross examination; "
          "calcification is minimal. Left circumflex (LCx): patent throughout; mild intimal thickening "
          "without significant stenosis. Note: all coronary assessments are gross only; histologic "
          "examination is required before any conclusion regarding clinically significant coronary disease "
          "can be drawn."),
     body("The cardiac chambers are examined following coronal sectioning. The left ventricle demonstrates "
          "a wall thickness of 1.1 cm, within normal limits for an adult female; no gross hypertrophy, "
          "fibrosis, or scarring is identified on the cut surface. The myocardium is homogeneous, red-brown, "
          "without focal pallor, softening, or areas consistent with gross infarction (acute or remote). "
          "The interventricular septum is intact and of normal thickness. The right ventricle is thin-walled "
          "and without dilation or gross pathology. The cardiac valves are examined: mitral valve leaflets "
          "are thin, translucent, and pliable without thickening, nodularity, vegetations, or prolapse on "
          "gross examination; estimated valve circumference 10 cm. Aortic valve: tricuspid, leaflets thin "
          "and pliable without calcification, fusion, or vegetations. Pulmonic and tricuspid valves: grossly "
          "unremarkable. The aortic root and ascending aorta are examined; the intimal surface shows mild "
          "atherosclerotic change without ulceration, dissection, or aneurysmal dilation.")]

    story += [subsection("Conduction System Note")]
    story += [body(
        "The sinoatrial and atrioventricular nodes are not individually identifiable on gross examination. "
        "Representative sections of the conduction system have been submitted for histologic examination. "
        "The significance of any histologic findings in the conduction system will be addressed in the "
        "supplemental histology report and the final autopsy report upon completion of ancillary studies.")]

    story += [section("RESPIRATORY SYSTEM — DETAILED EXAMINATION")]
    story += [body(
        "The larynx and hyoid bone were examined during the internal examination following removal from the "
        "neck structures. The hyoid bone is intact without fracture of the body or greater or lesser cornu "
        "bilaterally; no hemorrhage into the adjacent soft tissues of the hyoid is identified. The thyroid "
        "cartilage is intact without fracture or hemorrhage. The cricoid cartilage is intact. These findings "
        "are noted in the context of the overall case and are without gross evidence of compressive or "
        "asphyxial mechanism at this level; interpretation requires correlation with all ancillary data."),
     body("The trachea is patent without obstruction, foreign body, or hemorrhage. The mucosa is pink and "
          "intact. The main bronchi are patent bilaterally without foreign bodies or mucus plugging. The "
          "lungs were removed and weighed as documented in the organ weight table. The right lung weighed "
          "408 grams and the left lung 378 grams. The pleural surfaces bilaterally are smooth, glistening, "
          "and without fibrous adhesions, hemorrhage, or effusion. On palpation, both lungs are spongy "
          "and crepitant without focal areas of consolidation, collapse, or mass. On section, the "
          "parenchyma is pink-grey with mild dependent congestion in the lower lobes bilaterally; the "
          "cut surface does not express blood with compression in excess of normal postmortem vascular "
          "pooling. No areas of consolidation, infarct, abscess, or neoplastic lesion are identified on "
          "gross cut section. No pulmonary emboli are identified on examination of the main pulmonary "
          "artery and its lobar branches bilaterally. Minimal anthracotic pigment is present in the "
          "hilar lymph nodes. The pulmonary arteries and veins are patent at accessible levels."),
     body("The bronchopulmonary structures within each lobe are without gross abnormality. Airway mucosa "
          "is intact without hemorrhage or significant congestion. No aspirated material is identified "
          "within the bronchi or peripheral airways on gross examination. Representative sections from "
          "both lungs (upper and lower lobes bilaterally) have been submitted for histologic examination. "
          "Specifically, a question of possible early pulmonary edema in the dependent regions of the "
          "lower lobes is raised, though this finding is nonspecific and common in decedents regardless "
          "of cause of death; histologic correlation is required before any significance can be assigned "
          "to this observation.")]

    story += [PageBreak()]

    # ═══════════════════════════════════════════════════════════════════════
    # PAGE 5 — Neurologic, Endocrine, Renal, Reproductive, Histology Plan
    # ═══════════════════════════════════════════════════════════════════════
    story += doc_header("AUTOPSY REPORT — CONTINUATION",
                        "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  Page 5 of 7")

    story += [section("NEUROLOGIC SYSTEM — DETAILED EXAMINATION")]
    story += [body(
        "The calvarium was opened by circumferential saw cut above the level of the supraorbital ridges and "
        "the mastoid processes posteriorly. The dura mater was intact, smooth, and without epidural or "
        "subdural hemorrhage. The dural sinuses were patent and without thrombosis on gross examination. "
        "The brain was removed in the standard fashion following section of the cranial nerves, cerebral "
        "blood vessels, and spinal cord at the level of the foramen magnum. The brain weighed 1,302 grams, "
        "within normal limits for an adult female of this age. The cerebral hemispheres are symmetric "
        "without focal atrophy, gyral effacement, or obvious focal mass effect. No herniation or "
        "transtentorial displacement is identified."),
     body("The leptomeninges are thin, translucent, and without opacity, hemorrhage, or fibrinous exudate. "
          "No subarachnoid hemorrhage is identified on the surface of the cerebral hemispheres, cerebellum, "
          "or brainstem. The cerebral surface vessels are examined; mild diffuse vascular congestion is "
          "present; no aneurysmal dilation, rupture, or arteriovenous malformation is identified on gross "
          "examination of the circle of Willis or its principal branches. The circle of Willis anatomy is "
          "complete; no focal aneurysm sacs are palpated. The major cerebral arteries — anterior, middle, "
          "and posterior cerebral arteries bilaterally — and the basilar artery demonstrate mild-to-minimal "
          "atherosclerotic change without significant stenosis or occlusion on gross exam."),
     body("The brain was sectioned in the coronal plane at approximately 1.0 cm intervals following brief "
          "external examination. The cortical grey matter is intact without focal lesions, contusions, "
          "hemorrhage, or areas of infarction on gross examination. The white matter is homogeneous and "
          "without focal lesions. The basal ganglia and thalami are symmetric and without gross lesion. "
          "The ventricular system is examined; the lateral ventricles are symmetric and of normal volume "
          "without hydrocephalus or periventricular lesions. The third and fourth ventricles are patent "
          "and without masses or hemorrhage. The cerebellum is symmetric with intact foliar pattern and "
          "without focal lesions. The brainstem is intact; the corticospinal tracts are examined at the "
          "level of the midbrain, pons, and medulla without gross abnormality. No contusional injury is "
          "identified at the brainstem level. Representative sections from the cerebral cortex (frontal, "
          "parietal, temporal lobes bilaterally), hippocampi bilaterally, basal ganglia, cerebellum, and "
          "brainstem have been submitted for histologic examination. Additionally, sections from the "
          "choroid plexus and the dural venous sinuses are submitted.")]

    story += [section("ENDOCRINE SYSTEM")]
    story += [body(
        "The thyroid gland weighed 19 grams and consisted of symmetric lobes joined by an isthmus. The "
        "surface is smooth and without nodularity. On cut section, the thyroid parenchyma is tan-brown, "
        "homogeneous, and without discrete nodules, cysts, calcifications, or hemorrhage. Colloid is "
        "present in the follicles at normal gross appearance. The parathyroid glands are identified in "
        "their standard anatomical positions; all four glands are grossly normal without enlargement. "
        "The adrenal glands were described in the organ weight summary; on cut section, both demonstrate "
        "a normal cortex-to-medulla ratio with a bright yellow cortex and tan medulla without nodularity, "
        "hemorrhage, or focal lesion. The pituitary gland was examined following removal from the sella "
        "turcica; it is grossly unremarkable in size and cut surface appearance. Representative sections "
        "from the thyroid and adrenals are submitted for histologic examination.")]

    story += [section("RENAL AND URINARY TRACT SYSTEM")]
    story += [body(
        "Both kidneys are described in the organ weight summary. On inspection, both kidneys demonstrate "
        "a smooth, intact capsule which strips freely without adherence or subcapsular scarring. The renal "
        "surface is smooth and without focal scarring, petechiae, or cortical lesions. On cut section, the "
        "cortex is normal in width bilaterally, approximately 1.0–1.1 cm, with a sharp and well-defined "
        "corticomedullary junction. The medullary pyramids are tan, well-formed, and without calculi, "
        "cysts, or necrosis. The collecting systems — calyces, renal pelves, and ureters bilaterally — are "
        "patent and without obstruction, stones, or mucosal abnormality on gross examination. The urinary "
        "bladder contains approximately 40 mL of cloudy pale-yellow urine; this was aspirated and submitted "
        "in its entirety for toxicological analysis. The bladder mucosa is intact without hemorrhage or "
        "inflammation. No urethral or bladder lesions are identified.")]

    story += [section("REPRODUCTIVE SYSTEM")]
    story += [body(
        "The uterus and adnexa are examined following removal from the pelvis. The uterus is in the normal "
        "anteverted position. The serosal surface is smooth and glistening. On coronal section, the "
        "endometrium is thin (approximately 0.4 cm), consistent with the secretory phase or post-ovulatory "
        "endometrium given the estimated cycle phase; no endometrial polyps, hyperplasia, or obvious "
        "carcinoma. The myometrium is homogeneous without focal nodularity or leiomyomata identified on "
        "gross examination. The cervix is smooth without lesions, erosion, or stenosis; the cervical os "
        "is patent. The ovaries are as described in the organ weight summary; the left ovary is without "
        "gross pathology; the right ovary demonstrates a small unilocular cyst measuring approximately "
        "0.8 cm in greatest dimension containing clear serous fluid, most consistent with a functional "
        "follicular cyst; this is a common incidental finding. The fallopian tubes bilaterally are patent "
        "on gross examination without salpingitis, torsion, or mass.")]

    story += [section("HISTOLOGY PLAN — TISSUE SECTIONS SUBMITTED")]
    story += [body("The following tissue sections were fixed in 10% neutral buffered formalin and submitted "
                   "to the ME histology laboratory for processing, embedding, sectioning, and hematoxylin "
                   "and eosin staining. Additional special stains or immunohistochemical stains may be "
                   "ordered on a per-block basis following review of the H&E sections by the pathologist."), SP(3)]
    story += [tbl([
        ["Tissue", "Section(s) Taken", "Special Studies Anticipated"],
        ["Heart — LV free wall, full thickness", "2 sections", "H&E; Masson's trichrome (fibrosis)"],
        ["Heart — interventricular septum",       "1 section",  "H&E; Masson's trichrome"],
        ["Heart — RV free wall",                  "1 section",  "H&E"],
        ["Coronary arteries (proximal LAD, RCA)", "3 sections", "H&E; Movat pentachrome (plaque)"],
        ["Conduction system (SA node region, AV node region)", "2 sections", "H&E"],
        ["Lung — right lower lobe (dependent)",   "2 sections", "H&E; PAS (edema confirmation)"],
        ["Lung — left lower lobe (dependent)",    "2 sections", "H&E"],
        ["Lung — right upper lobe",               "1 section",  "H&E"],
        ["Liver",                                 "2 sections", "H&E; PAS; reticulin (architecture)"],
        ["Kidney — left, representative",         "1 section",  "H&E; PAS"],
        ["Kidney — right, representative",        "1 section",  "H&E"],
        ["Brain — frontal cortex",                "1 section",  "H&E; LFB (myelin)"],
        ["Brain — hippocampus (bilateral)",       "2 sections", "H&E"],
        ["Brain — basal ganglia",                 "1 section",  "H&E"],
        ["Cerebellum",                            "1 section",  "H&E"],
        ["Brainstem (pons/medulla)",              "1 section",  "H&E"],
        ["Thyroid",                               "1 section",  "H&E"],
        ["Adrenal (bilateral)",                   "2 sections", "H&E"],
        ["Spleen",                                "1 section",  "H&E"],
        ["Blouse — left cuff stain sample",       "Swab/scraping submitted", "Pending toxicology and trace analysis"],
    ], col_widths=[2.20*inch, 1.10*inch, 4.25*inch])]

    story += [PageBreak()]

    # ═══════════════════════════════════════════════════════════════════════
    # PAGE 6 — Specimen Retention, Documentation Checklist, Lab Correlation
    # ═══════════════════════════════════════════════════════════════════════
    story += doc_header("AUTOPSY REPORT — CONTINUATION",
                        "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  Page 6 of 7")

    story += [section("SPECIMEN RETENTION AND TOXICOLOGY SUBMISSION SUMMARY")]
    story += [body(
        "The following biological specimens were collected during the autopsy examination and submitted "
        "for analysis as specified. Each specimen was labeled with the case number, decedent name, "
        "specimen type, date and time of collection, and the initials of the collecting pathologist. "
        "Chain of custody documentation accompanies each specimen submission. See the separate Specimen "
        "Retention Sheet (Case 2015-ME-0447) and Toxicology Submission Form for full accession detail."), SP(3)]
    story += [tbl([
        ["Specimen", "Volume / Amount", "Container", "Collected From", "Analysis Requested", "Status"],
        ["Peripheral blood (femoral vein)",
         "10 mL (×2 gray-top, ×1 purple-top)",
         "Standard Vacutainer, gray-top (NaF/KOx) and purple-top (EDTA)",
         "Left femoral vein, post-mortem, ligated prior to thoracotomy",
         "Comprehensive tox screen; volatiles; drugs of abuse; therapeutic drugs; heavy metals",
         "SUBMITTED to ME Tox Lab 10/14/2015"],
        ["Peripheral blood (femoral vein) — reserve",
         "5 mL (×1 red-top, no additive)",
         "Red-top Vacutainer",
         "Left femoral vein",
         "Reserve for additional testing as directed by pathologist",
         "RETAINED in ME freezer — Case 2015-ME-0447"],
        ["Central blood (cardiac — right ventricle)",
         "10 mL (×2 gray-top)",
         "Gray-top Vacutainer (NaF/KOx)",
         "Right ventricular chamber",
         "Tox screen (not primary — for comparison with peripheral; subject to postmortem redistribution artifact)",
         "SUBMITTED to ME Tox Lab 10/14/2015"],
        ["Urine (bladder aspirate)",
         "40 mL (approx.)",
         "Sterile urine collection container, sealed",
         "Urinary bladder at autopsy",
         "Comprehensive tox screen; drugs of abuse; therapeutic drugs",
         "SUBMITTED to ME Tox Lab 10/14/2015"],
        ["Vitreous humor — right eye",
         "2.5 mL",
         "Gray-top Vacutainer",
         "Right vitreous chamber (needle aspiration, 27G)",
         "Ethanol; electrolytes (Na, K, Cl, glucose, BUN); drugs; as directed",
         "SUBMITTED to ME Tox Lab 10/14/2015"],
        ["Vitreous humor — left eye (reserve)",
         "2.3 mL",
         "Gray-top Vacutainer",
         "Left vitreous chamber (needle aspiration, 27G)",
         "Reserve for additional testing",
         "RETAINED in ME freezer"],
        ["Gastric contents — aspirate",
         "Approx. 120 mL (total)",
         "Wide-mouth specimen jar, sealed",
         "Stomach aspirate at autopsy",
         "Qualitative and quantitative tox; identification of any toxic compounds or drug matrix",
         "SUBMITTED to ME Tox Lab 10/14/2015"],
        ["Liver — right lobe section",
         "Approx. 50 g",
         "Wide-mouth specimen jar in formalin; separate portion unfixed",
         "Right hepatic lobe, mid-section",
         "Tox (unfixed portion); histo H&E and special stains (fixed portion)",
         "SUBMITTED (tox unfixed) and SUBMITTED (histo formalin)"],
        ["Bile (gallbladder aspirate)",
         "15 mL (approx.)",
         "Sterile container, sealed",
         "Gallbladder at autopsy",
         "Supplemental tox as directed; comparison with serum levels if relevant",
         "RETAINED in ME freezer"],
        ["Scalp hair — 30 strands, with root",
         "Pulled, root intact",
         "Paper coin envelope, sealed",
         "Posterior vertex scalp",
         "Drug hair analysis (segmental); heavy metal screening",
         "SUBMITTED to ME Tox Lab 10/14/2015"],
        ["Fingernail clippings — all 10 digits",
         "Clippings from all digits",
         "Paper coin envelopes (L and R labeled separately), sealed",
         "All fingernail tips, post-removal",
         "Trace evidence analysis; trace drug analysis as directed",
         "SUBMITTED to SFPD CSU trace lab per Det. Orre request; copy to ME file"],
        ["Blouse cuff staining sample",
         "Swab × 2 (wetted); scraping × 1",
         "Swab transport tube, sealed; scraping in paper",
         "Left interior cuff, blouse item C-02",
         "Unknown substance characterization; tox; trace",
         "SUBMITTED to SFPD CSU trace lab per Det. Orre; ME retains scraping reserve"],
    ], col_widths=[1.35*inch, 0.85*inch, 1.00*inch, 0.90*inch, 1.55*inch, 0.90*inch])]

    story += [SP(4), section("AUTOPSY DOCUMENTATION CHECKLIST")]
    story += [tbl([
        ["Item", "Completed", "By", "Notes"],
        ["Photographic documentation — exterior (pre-clothing removal)", "YES", "T.A. Nkrumah", "SD card archived Case 2015-ME-0447"],
        ["Photographic documentation — clothing",                        "YES", "T.A. Nkrumah", "All garments, pre and post-removal"],
        ["Photographic documentation — external exam (all surfaces)",    "YES", "T.A. Nkrumah", ""],
        ["Photographic documentation — internal exam (all major organs)","YES", "T.A. Nkrumah", ""],
        ["Photographic documentation — histology gross sections (notable)", "YES", "T.A. Nkrumah", "Coronary arteries, brain sections"],
        ["Dictation — autopsy narrative (all sections)",                 "YES", "Dr. R.G. Adeyemi", "Dictated to transcription 10/14/2015"],
        ["Transcription — dictation reviewed and approved",             "PENDING", "Dr. R.G. Adeyemi", "Target: 10/16/2015"],
        ["Specimen submission forms signed",                             "YES", "Dr. R.G. Adeyemi", "All forms signed 10/14/2015 post-autopsy"],
        ["Chain of custody documentation — all specimens",              "YES", "Dr. Adeyemi / D.H. Farr", "Maintained in case file"],
        ["Histology blocks — prepared and labeled",                     "YES", "D.H. Farr (MT-03)", "Formalin fixation 10/14/2015; processing 10/15/2015"],
        ["Tox specimens — packaged and submitted",                      "YES", "Dr. Adeyemi / D.H. Farr", "Submitted same day as autopsy"],
        ["Organ retention (brain — fixed, pending histo)",              "YES", "D.H. Farr (MT-03)", "Brain retained in formalin for additional fixation; min. 2 weeks"],
        ["LE — SFPD Det. Orre given verbal preliminary summary",        "YES", "Dr. R.G. Adeyemi", "Oral summary provided on scene departure approx. 1315 hrs; no written prelim released"],
        ["Preliminary report issued (written)",                         "PENDING", "Dr. R.G. Adeyemi", "Target: 10/16–10/17/2015; no written prelim issued as of 10/14"],
        ["Final autopsy report",                                        "PENDING", "Dr. R.G. Adeyemi", "Deferred pending tox (est. 4–8 wks), histo (est. 2–3 wks)"],
    ], col_widths=[3.10*inch, 0.80*inch, 1.30*inch, 2.35*inch])]

    story += [PageBreak()]

    # ═══════════════════════════════════════════════════════════════════════
    # PAGE 7 — Discussion, Preliminary Opinion, Certification
    # ═══════════════════════════════════════════════════════════════════════
    story += doc_header("AUTOPSY REPORT — CONTINUATION",
                        "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  Page 7 of 7")

    story += [section("PRELIMINARY ANATOMIC DIAGNOSES")]
    story += [body(
        "The following represent the anatomic diagnoses supported by the gross autopsy examination. These "
        "diagnoses are preliminary and subject to revision based on histologic, toxicologic, and ancillary "
        "study results. The diagnoses are numbered in approximate order of current perceived significance, "
        "which may change upon receipt of laboratory findings.")]
    story += [tbl([
        ["#", "Diagnosis", "Status / Notes"],
        ["1", "Mild coronary atherosclerosis — most significant in proximal LAD (estimated 30–40% luminal narrowing on gross exam); no gross acute plaque rupture or thrombosis identified",
         "Histologic confirmation pending; clinical significance uncertain without additional cardiac and toxicologic data"],
        ["2", "Mild hepatic congestion with minimal centrilobular accentuation",
         "Histologic sections submitted; may represent passive hepatic congestion of various etiologies; correlation with cardiac and systemic findings required"],
        ["3", "Uncomplicated cholelithiasis (3 small cholesterol calculi, largest 0.6 cm) without evidence of acute cholecystitis",
         "Likely incidental; no clear causal relationship to death on gross examination"],
        ["4", "Mild diffuse cerebral congestion, no focal lesions",
         "Nonspecific; histologic sections submitted; may represent terminal or postmortem change; significance pending"],
        ["5", "Mild dependent pulmonary congestion, bilateral lower lobes",
         "Common postmortem finding; may reflect terminal pulmonary edema or postmortem pooling; histologic confirmation pending"],
        ["6", "Right ovarian follicular cyst (0.8 cm) — incidental",
         "No causal significance identified"],
        ["7", "Remote right knee surgical scar — incidental",
         "No causal significance identified"],
        ["8", "Remote right forearm scar (1.0 cm) — etiology undetermined",
         "No acute significance identified; documented for completeness"],
        ["9", "Staining on left interior cuff of blouse — substance undetermined",
         "Submitted for toxicological and trace analysis; clinical significance unknown"],
    ], col_widths=[0.28*inch, 3.80*inch, 3.47*inch])]

    story += [SP(4), section("PRELIMINARY DISCUSSION")]
    story += [body(
        "Autopsy examination of Eleanor Anne Marsh, a 46-year-old female, was performed at the Minnehaha "
        "County ME facility on October 14, 2015, commencing at 0902 hours and concluding at 1318 hours. "
        "The gross autopsy examination did not reveal a definitive anatomic cause of death. The most "
        "significant gross finding is mild coronary atherosclerosis involving primarily the proximal LAD, "
        "with an estimated 30–40% luminal narrowing on gross examination. Whether this degree of coronary "
        "disease represents a clinically significant substrate for a fatal arrhythmia or other cardiac "
        "event in this decedent cannot be determined on gross examination alone and requires histologic "
        "confirmation and correlation with toxicologic and scene findings."),
     body("No gross evidence of acute trauma sufficient to explain death was identified at autopsy. "
          "The hyoid bone and thyroid and cricoid cartilages were intact. The neck soft tissues were "
          "examined and no hemorrhage into the strap muscles or deep neck structures was identified, "
          "though this finding does not exclude subtle or atypical mechanisms. No petechial hemorrhage "
          "was identified in the conjunctivae, sclerae, or facial skin on gross examination, though "
          "this observation is limited by the postmortem interval and does not exclude findings at the "
          "histologic level. No aspiration of gastric contents into the airways was identified. No "
          "acute intracranial hemorrhage, infarction, or structural lesion was identified at autopsy."),
     body("The mild hepatic congestion and bilateral dependent pulmonary congestion are nonspecific "
          "findings that may be consistent with terminal cardiorespiratory failure of any etiology, "
          "passive venous congestion, or postmortem change. Neither finding is diagnostic of a specific "
          "cause of death in isolation. The staining of the left interior cuff of the blouse is of "
          "unknown nature and has been submitted for analysis; its relevance to the cause of death is "
          "wholly undetermined at this time and no inference should be drawn from its existence."),
     body("The absence of an identified treating physician, known medical history, or medication list at "
          "the time of this autopsy significantly limits the pathologist's ability to correlate gross and "
          "histologic findings with prior clinical status. In particular, the significance of the observed "
          "coronary atherosclerosis, the mild hepatic changes, and any toxicologic findings that may be "
          "identified cannot be fully evaluated without knowledge of the decedent's baseline clinical state, "
          "medication profile, and any relevant prior medical events. The toxicologic examination, including "
          "peripheral blood, central blood, urine, vitreous humor, and gastric contents, is considered "
          "essential to this case and may materially alter the preliminary diagnosis and determination of "
          "cause and manner of death. Histologic examination of the submitted tissue sections is similarly "
          "essential and may reveal microscopic findings not apparent on gross examination."),
     body("At the conclusion of this preliminary report, the cause and manner of death remain deferred "
          "in their entirety pending completion of toxicologic analysis (estimated 4–8 weeks), histologic "
          "examination (estimated 2–3 weeks), and review of investigative information developed by SFPD. "
          "This case will be reviewed by the pathologist upon receipt of all ancillary study results, at "
          "which time a final autopsy report and a determination of cause and manner of death will be "
          "issued if supportable. This preliminary report does not constitute a final determination and "
          "is not suitable for use in legal proceedings without supplementation by the final report.")]

    story += [SP(4), section("PATHOLOGIST PRELIMINARY OPINION")]
    story += [tbl([
        ["Cause of Death:", "DEFERRED — pending toxicology, histology, and investigative information"],
        ["Manner of Death:", "DEFERRED — pending all ancillary studies and investigative results"],
        ["Contributing Conditions:", "NONE ESTABLISHED at this preliminary stage; mild coronary atherosclerosis noted but significance undetermined"],
        ["Case Classification:", "SUSPICIOUS — subject to revision upon receipt of all results"],
        ["Anticipated Final Report:", "Following receipt of tox results (est. 4–8 weeks) and histology (est. 2–3 weeks); final determination of cause and manner of death to follow"],
    ], col_widths=[2.00*inch, 5.55*inch], has_hdr=False, alt=False)]

    story += [SP(6), HR(),
              body("<b>PATHOLOGIST CERTIFICATION — PRELIMINARY:</b> I certify that I performed or directly "
                   "supervised the autopsy examination described in this report on October 14, 2015, and that the "
                   "findings documented herein are accurate to the best of my knowledge based on the gross "
                   "autopsy examination and information available at this time. This report is PRELIMINARY. "
                   "No final cause or manner of death is determined. This report shall not be cited as a final "
                   "determination. A final autopsy report will be issued upon completion of all ancillary studies."), SP(6)]
    story += [tbl([
        ["Pathologist Signature:", "________________________________",  "Date:", "____________", "Time:", "________"],
        ["Print Name / License #:", "Raymond G. Adeyemi, MD  |  SD Med. Lic. #27-4419",
         "Board Cert. (ABFP):", "YES — Forensic Path.", "", ""],
        ["Observer Signature:", "________________________________",    "Print Name:", "Dr. E.L. Sandvik, MD", "", ""],
        ["Reviewed / Approved By:", "________________________________", "Print Name:", "Dr. Paula H. Reinholt, MD — Chief ME", "Date:", "____________"],
    ], col_widths=[1.60*inch, 2.35*inch, 1.00*inch, 1.70*inch, 0.45*inch, 0.50*inch], has_hdr=False, alt=False)]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
