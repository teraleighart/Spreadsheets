"""Document 09 — Ancillary Studies / Histology Index (1 page)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate
from aging import make_onpage, W, H, STAMP_B, HW_BLUE, HW_PENCIL
from styles import ST, HR, doc_header, section, body, body_l, small, SP, tbl

OUT = os.path.dirname(__file__)


def build():
    path = os.path.join(OUT, "ME-0447-09-Ancillary-Studies-Histology-Index.pdf")
    aging = {
        'staple': True,
        1: {
            'rings': [(W*0.83, H*0.82, 36, 161, 0.19, 91)],
            'creases': [(0, H*0.335, W, H*0.332, 101, 0.72), (0, H*0.667, W, H*0.664, 102, 0.68)],
            'foxing': {'count': 44, 'inten': 0.92},
            'stamps': [("CASE FILE — INTERNAL USE ONLY", 0.85*inch, H*0.12, 3, STAMP_B, 9, 0.52)],
            'hw': [("histo slides returned 11/3 — DHF", W-2.9*inch, H*0.235, -1, HW_PENCIL, 7.5),
                   ("await brain sections — RGA", W-2.9*inch, H*0.218, -1, HW_PENCIL, 7.5)],
        },
    }
    cb = make_onpage(109, "Ancillary Studies / Histology Index", 1, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.80*inch, rightMargin=0.80*inch,
                            topMargin=0.75*inch, bottomMargin=0.72*inch)
    story = doc_header("ANCILLARY STUDIES AND HISTOLOGY INDEX",
                       "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  DOB: 03/22/1969")

    story += [tbl([
        ["Index Date:", "October 14, 2015 (initial); updated November 14, 2015",
         "Prepared By:", "D.H. Farr (MT-03) / Dr. R.G. Adeyemi"],
        ["Purpose:", "This index documents ancillary study submissions, histology records, photography archives, "
                     "dictation records, and quality control documentation associated with Case 2015-ME-0447. "
                     "This index is a subset summary of the office's internal archive; some records exist "
                     "exclusively in internal systems (MECS, dictation server, digital photo archive).", "", ""],
    ], col_widths=[0.90*inch, 3.85*inch, 1.00*inch, 1.80*inch], has_hdr=False, alt=False)]

    story += [SP(5), section("SECTION A — HISTOLOGY STUDIES")]
    story += [tbl([
        ["Block ID", "Tissue / Organ", "Sections Taken", "Stains Ordered", "Date Submitted", "Status / Notes"],
        ["HB-01", "Heart — LV free wall, full thickness", "2", "H&E; Masson's trichrome", "10/14/2015", "Slides reviewed 11/03/2015; report pending in final AR"],
        ["HB-02", "Heart — interventricular septum", "1", "H&E; Masson's trichrome", "10/14/2015", "Slides reviewed 11/03/2015"],
        ["HB-03", "Heart — RV free wall", "1", "H&E", "10/14/2015", "Slides reviewed 11/03/2015"],
        ["HB-04", "Coronary arteries — proximal LAD; proximal RCA", "3", "H&E; Movat pentachrome", "10/14/2015", "Slides reviewed 11/03/2015; findings documented in final AR (pending issuance)"],
        ["HB-05", "Conduction system — SA node region; AV node region", "2", "H&E", "10/14/2015", "Slides reviewed 11/03/2015; consult with cardiac path. considered"],
        ["HB-06", "Lung — right lower lobe (dependent)", "2", "H&E; PAS", "10/14/2015", "Slides reviewed 11/03/2015"],
        ["HB-07", "Lung — left lower lobe (dependent)", "2", "H&E", "10/14/2015", "Slides reviewed 11/03/2015"],
        ["HB-08", "Lung — right upper lobe", "1", "H&E", "10/14/2015", "Slides reviewed 11/03/2015"],
        ["HB-09", "Liver — representative sections", "2", "H&E; PAS; reticulin", "10/14/2015", "Slides reviewed 11/03/2015; mild findings noted — details in final AR"],
        ["HB-10", "Left kidney — representative", "1", "H&E; PAS", "10/14/2015", "Slides reviewed 11/03/2015"],
        ["HB-11", "Right kidney — representative", "1", "H&E", "10/14/2015", "Slides reviewed 11/03/2015"],
        ["HB-12", "Brain — frontal cortex (bilateral)", "1", "H&E; LFB", "10/14/2015", "PENDING — awaiting adequate formalin fixation; brain retained; sections anticipated no earlier than 10/28/2015"],
        ["HB-13", "Brain — hippocampus (bilateral)", "2", "H&E", "10/14/2015", "PENDING — same as HB-12"],
        ["HB-14", "Brain — basal ganglia", "1", "H&E", "10/14/2015", "PENDING — same as HB-12"],
        ["HB-15", "Brain — cerebellum", "1", "H&E", "10/14/2015", "PENDING — same as HB-12"],
        ["HB-16", "Brain — brainstem (pons / medulla)", "1", "H&E", "10/14/2015", "PENDING — same as HB-12"],
        ["HB-17", "Thyroid — representative", "1", "H&E", "10/14/2015", "Slides reviewed 11/03/2015"],
        ["HB-18", "Adrenal (bilateral)", "2", "H&E", "10/14/2015", "Slides reviewed 11/03/2015"],
        ["HB-19", "Spleen", "1", "H&E", "10/14/2015", "Slides reviewed 11/03/2015"],
        ["HB-20", "Uterus and right ovary", "2", "H&E", "10/14/2015", "Slides reviewed 11/03/2015; incidental right ovarian cyst confirmed histologically"],
    ], col_widths=[0.52*inch, 1.55*inch, 0.55*inch, 1.20*inch, 0.82*inch, 2.90*inch])]

    story += [SP(4), section("SECTION B — PHOTOGRAPHY AND MEDIA DOCUMENTATION")]
    story += [tbl([
        ["Record Type", "Description", "Media / Location", "Date Created", "Status"],
        ["Autopsy Photography — Pre-Clothing Removal", "Full external; all surfaces; scene-consistent position", "SD Card / ME Photo Archive Case 2015-ME-0447", "10/14/2015", "ARCHIVED — ME digital photo server"],
        ["Autopsy Photography — Clothing Documentation", "Each garment photographed on table pre and post-removal", "SD Card / ME Photo Archive", "10/14/2015", "ARCHIVED"],
        ["Autopsy Photography — External Exam", "All body surfaces; annotated key findings; all 4 surfaces; close-ups of all marks and scars", "SD Card / ME Photo Archive", "10/14/2015", "ARCHIVED"],
        ["Autopsy Photography — Internal Exam", "All major organs in situ and removed; serial coronary cross-sections; brain external; serial brain sections", "SD Card / ME Photo Archive", "10/14/2015", "ARCHIVED"],
        ["Autopsy Photography — Histology Gross", "Gross coronary artery sections; representative organ cross-sections", "SD Card / ME Photo Archive", "10/14/2015", "ARCHIVED"],
        ["Photo Log / Shot List", "Complete annotated shot list with frame-by-frame descriptions", "ME Photo Archive / Case File", "10/14/2015", "IN CASE FILE"],
        ["Scene Photography (SFPD)",
         "Scene photography by SFPD CSU — not ME records; reference SFPD CSU report SFPD-2015-48801",
         "SFPD CSU archive", "10/13–10/14/2015", "NOT ME RECORD — SFPD custody"],
    ], col_widths=[1.65*inch, 2.30*inch, 1.35*inch, 0.80*inch, 1.45*inch])]

    story += [SP(4), section("SECTION C — DICTATION AND TRANSCRIPTION RECORD")]
    story += [tbl([
        ["Record", "Dictated By", "Date / Time Dictated", "Transcription Status", "Approved By / Date"],
        ["Autopsy Report — full narrative, external", "Dr. R.G. Adeyemi", "10/14/2015 — approx. 1330 hrs (same day)", "Transcribed 10/15/2015", "Dr. Adeyemi — approved 10/16/2015"],
        ["Autopsy Report — internal exam continuation", "Dr. R.G. Adeyemi", "10/14/2015 — approx. 1400 hrs", "Transcribed 10/15/2015", "Dr. Adeyemi — approved 10/16/2015"],
        ["Preliminary discussion / opinion section", "Dr. R.G. Adeyemi", "10/14/2015 — approx. 1415 hrs", "Transcribed 10/15/2015", "Dr. Adeyemi — approved 10/16/2015; note: cause/manner deferred"],
        ["Histology review addendum (blocks HB-01 through HB-11, HB-17–19)", "Dr. R.G. Adeyemi", "11/04/2015", "Transcribed 11/05/2015", "Pending Dr. Adeyemi approval — brain sections not yet available"],
        ["Brain neuropathology review (blocks HB-12 through HB-16)", "PENDING", "TBD — brain in fixation", "PENDING", "PENDING — anticipated late November 2015"],
    ], col_widths=[1.90*inch, 1.05*inch, 1.25*inch, 1.10*inch, 2.25*inch])]

    story += [SP(4), section("SECTION D — QUALITY CONTROL AND ADMINISTRATIVE RECORDS")]
    story += [tbl([
        ["QC / Admin Item", "Record Location", "Date", "Status"],
        ["Scale calibration record — autopsy facility (body weight)", "ME Facility Calibration Log — Oct 2015", "09/30/2015 (last cal.)", "In compliance; calibration valid at time of autopsy"],
        ["Scale calibration record — organ scale", "ME Facility Calibration Log — Oct 2015", "09/30/2015 (last cal.)", "In compliance"],
        ["Thermometer calibration — investigator handheld", "MEI-09 Equipment Log", "09/15/2015 (last cal.)", "In compliance; within certification period"],
        ["Body bag / seal inventory record — Seal #MEO-S-2015-3391", "ME Supply / Chain-of-Custody Log", "10/14/2015", "Seal issued to MEI-09 Kowalczyk; applied at scene 0532 hrs; broken by Dr. Adeyemi at autopsy 0902 hrs — documented"],
        ["MECS system case entry — initial (face sheet)", "ME Case Management System (MECS)", "10/14/2015 — 0651 hrs", "Complete; case 2015-ME-0447 active"],
        ["MECS system — autopsy entry", "MECS", "10/16/2015", "Preliminary data entered; pending final update upon report completion"],
        ["ME facility access log — 10/14/2015 (autopsy day)", "ME Facility Security Log", "10/14/2015", "Maintained on site; available on request"],
        ["Peer review / QA (case)", "ME Office QA Program — case selected for peer review", "TBD — upon issuance of final report", "PENDING — peer review scheduled upon final AR issuance"],
    ], col_widths=[2.10*inch, 1.85*inch, 1.10*inch, 2.50*inch])]

    story += [SP(4), body(
        "This Ancillary Studies and Histology Index is a summary document and does not constitute the primary "
        "record for any of the items listed above. The primary records for histology (slide archive and "
        "pathologist's written notes), photography (digital photo server archive), dictation (digital "
        "dictation server), toxicology (laboratory accession files and instrument raw data), and case "
        "management (MECS database) are maintained in their respective systems, which are separate from "
        "the physical case file. This printed index represents a status snapshot as of its date of "
        "preparation and may not reflect subsequent updates to internal electronic systems. Requests for "
        "access to primary records must be directed to the Chief Medical Examiner.")]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
