"""Document 03 — Body Receipt / Transport Record (1 page)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from aging import make_onpage, W, H, STAMP_B, HW_BLUE
from styles import ST, HR, doc_header, section, subsection, body, body_l, small, SP, tbl
from reportlab.platypus import SimpleDocTemplate

OUT = os.path.dirname(__file__)


def build():
    path = os.path.join(OUT, "ME-0447-03-Body-Receipt-Transport-Record.pdf")
    aging = {
        'staple': True,
        1: {
            'rings': [(W*0.82, H*0.78, 36, 81, 0.20, 33)],
            'creases': [(0, H*0.50, W, H*0.498, 41, 0.80)],
            'foxing': {'count': 42, 'inten': 0.90},
            'stamps': [("CHAIN OF CUSTODY INTACT", 0.90*inch, H*0.18, 3, STAMP_B, 10, 0.52)],
            'hw': [("DHF / SLK — verified seal 0622", W-2.9*inch, H*0.29, -1, HW_BLUE, 7.5)],
        },
    }
    cb = make_onpage(103, "Body Receipt / Transport Record", 1, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.80*inch, rightMargin=0.80*inch,
                            topMargin=0.75*inch, bottomMargin=0.72*inch)

    story = doc_header("BODY RECEIPT AND TRANSPORT RECORD",
                       "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  DOB: 03/22/1969")

    story += [section("SECTION A — SCENE RELEASE AND INITIAL TRANSFER")]
    story += [tbl([
        ["Scene Address:", "4200 S. Western Ave., Suite 712, Sioux Falls, SD 57105",
         "Scene County:", "Minnehaha"],
        ["LE Scene Authority:", "Det. Marcus J. Orre — SFPD Investigations",
         "LE Badge / ID:", "#3304"],
        ["Date / Time Released from Scene:", "October 14, 2015 — 0538 hrs CDT",
         "Released To:", "Dakota Mortuary Transport Services (DMTS)"],
        ["ME Investigator Present at Release:", "Sandra L. Kowalczyk, MSFS (MEI-09)",
         "Body Bag Type:", "Standard ME body pouch — white, zippered, single compartment"],
        ["Body Bag Sealed by ME:", "YES",
         "ME Seal Number:", "MEO-S-2015-3391"],
        ["Seal Applied By:", "S.L. Kowalczyk, MEI-09",
         "Time Seal Applied:", "0532 hrs CDT, October 14, 2015"],
        ["Outer Tag Applied:", "YES — Case 2015-ME-0447, Marsh E.A., DOB 03/22/1969",
         "Tag Applied By:", "S.L. Kowalczyk, MEI-09"],
        ["Condition of Body at Release:", "No gross external trauma; postmortem changes present (see DIR Section 7); clothing in place; no apparent disturbance", "", ""],
    ], col_widths=[2.00*inch, 2.55*inch, 1.40*inch, 1.55*inch], has_hdr=False)]

    story += [SP(4), section("SECTION B — TRANSPORT DETAILS")]
    story += [tbl([
        ["Transport Provider:", "Dakota Mortuary Transport Services (DMTS)",
         "DMTS Run #:", "DMTS-2015-10-14-007"],
        ["Transport Vehicle:", "DMTS Unit 4 (white transit van, plate SD-DMTS-04)",
         "Vehicle Condition:", "Standard operating; no anomalies noted"],
        ["Transport Personnel — Primary:", "Curtis D. Halverson (DMTS Driver / Tech.), Cert. #SD-MT-0892",
         "Personnel — Secondary:", "Janel M. Tripp (DMTS Tech.), Cert. #SD-MT-1140"],
        ["Time Departed Scene:", "0542 hrs CDT, October 14, 2015",
         "Time Arrived ME Facility:", "0622 hrs CDT, October 14, 2015"],
        ["Route Used:", "South Western Ave. to E. 41st St. to Minnesota Ave. to W. 6th St. — direct route",
         "Est. Distance:", "Approx. 4.2 miles"],
        ["Any Stops During Transport:", "NO — direct transport; no stops made between scene and ME facility",
         "", ""],
        ["Body Repositioned During Transport:", "NO — body bag remained sealed and positioned on transport gurney throughout",
         "", ""],
    ], col_widths=[2.00*inch, 2.55*inch, 1.40*inch, 1.55*inch], has_hdr=False)]

    story += [SP(4), section("SECTION C — RECEIPT AT ME FACILITY")]
    story += [tbl([
        ["Facility Address:", "220 W. Sixth Street, Sioux Falls, SD 57104 — Bay C Intake",
         "Date / Time of Receipt:", "October 14, 2015 — 0622 hrs CDT"],
        ["Received By:", "Dennis H. Farr, Mortuary Technician (MT-03)",
         "ME Staff Present:", "S.L. Kowalczyk, MSFS (MEI-09)"],
        ["ME Seal # (as received):", "MEO-S-2015-3391",
         "Seal Condition at Receipt:", "INTACT — no tampering, cutting, or breach observed"],
        ["Seal Verified By:", "D.H. Farr (MT-03) and S.L. Kowalczyk (MEI-09) — jointly",
         "Verification Time:", "0624 hrs CDT"],
        ["Discrepancies / Anomalies:", "NONE — body bag, seal, and outer tag all intact and consistent with on-scene documentation",
         "", ""],
        ["Body Weight (measured at intake):", "149.4 lbs",
         "Body Weight Measured By:", "D.H. Farr (MT-03) using calibrated facility scale (Cal. Date 09/30/2015)"],
        ["Storage Location Assigned:", "Cooler Bay C, Shelf 2",
         "Storage Temp. at Assignment:", "36°F (monitored; within protocol range 34–40°F)"],
        ["Case Label Affixed to Storage:", "YES — Case 2015-ME-0447 / Marsh E.A. / 10/14/2015",
         "Autopsy Scheduled:", "October 14, 2015 — 0900 hrs, Autopsy Suite A"],
    ], col_widths=[2.00*inch, 2.55*inch, 1.40*inch, 1.55*inch], has_hdr=False)]

    story += [SP(4), section("SECTION D — TRANSPORT NARRATIVE")]
    story += [body(
        "This section provides a narrative account of the chain of custody from scene departure to ME facility "
        "receipt, prepared by ME Investigator Kowalczyk based on direct observation and documentation. The body "
        "of Eleanor Anne Marsh was placed in a standard ME body pouch at the scene of death, Suite 712, "
        "4200 South Western Avenue, Sioux Falls, South Dakota, under the direct observation of this investigator. "
        "The pouch was sealed with ME seal number MEO-S-2015-3391 and a printed exterior identification tag was "
        "affixed bearing the case number, decedent name, and date of birth. Transfer of the body to DMTS "
        "personnel (Halverson and Tripp) was accomplished at 0542 hours CDT on October 14, 2015, following the "
        "formal release of the body by SFPD Detective Orre at 0538 hours. This investigator observed the loading "
        "of the body bag onto the DMTS transport gurney and into the DMTS transport vehicle."),
     body("Transport was direct from the scene address to the Minnehaha County ME facility, a distance of "
          "approximately 4.2 miles via a standard surface route with no stops, deviations, or incidents reported "
          "by DMTS personnel. This investigator followed the DMTS vehicle to the ME facility and was present for "
          "receipt. Upon arrival at 0622 hours, the body bag was unloaded from the transport vehicle and brought "
          "to Bay C intake. Seal number MEO-S-2015-3391 was examined by both Mortuary Technician Farr and this "
          "investigator and found to be intact, with no visible breach, cutting, or tampering. The exterior "
          "identification tag was also present and legible. The body was weighed on the facility's calibrated "
          "platform scale (last calibration September 30, 2015, within protocol) and a weight of 149.4 pounds "
          "was recorded. The body was then transferred to Cooler Bay C, Shelf 2, at the appropriate refrigeration "
          "temperature of 36°F, pending autopsy scheduled for 0900 hours the same morning."),
     body("At no point during the transport and receipt process was the body bag opened, the seal broken, the "
          "outer identification tag removed or altered, or the decedent's body accessed by any party. The chain "
          "of custody is considered intact and uninterrupted from scene release to ME facility storage. Any "
          "subsequent access to the body for the purpose of autopsy examination was conducted under ME office "
          "protocols by authorized personnel.")]

    story += [SP(4), section("SECTION E — SIGNATURES AND CERTIFICATION")]
    story += [tbl([
        ["Role", "Name (Print)", "Signature", "Date", "Time"],
        ["SFPD Scene Release", "Det. Marcus J. Orre — #3304", "______________________", "10/14/2015", "0538"],
        ["DMTS Transport (Primary)", "Curtis D. Halverson — #SD-MT-0892", "______________________", "10/14/2015", "0542"],
        ["DMTS Transport (Secondary)", "Janel M. Tripp — #SD-MT-1140", "______________________", "10/14/2015", "0542"],
        ["ME Investigator (Scene / Transport)", "Sandra L. Kowalczyk — MEI-09", "______________________", "10/14/2015", "0624"],
        ["ME Mortuary Tech. (Receipt)", "Dennis H. Farr — MT-03", "______________________", "10/14/2015", "0624"],
    ], col_widths=[1.70*inch, 2.10*inch, 1.70*inch, 0.80*inch, 0.55*inch])]

    story += [SP(6), small(
        "This Body Receipt and Transport Record becomes part of the permanent case file for Case 2015-ME-0447 and "
        "documents the chain of custody of the decedent from scene release to ME facility intake. Any "
        "discrepancies noted after receipt must be documented in a separate supplemental memorandum and "
        "submitted to the case pathologist and Chief ME within 24 hours of discovery per ME Office Policy "
        "ME-OPS-007 (Chain of Custody), Rev. 2013. No discrepancies were noted at intake.")]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
