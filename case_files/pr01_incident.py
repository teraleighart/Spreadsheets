"""PR-01 — SFPD Initial Incident Report (2 pages)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph
from aging import make_onpage, W, H, STAMP_B, HW_BLUE, HW_PENCIL, STAMP_R
from styles import ST, HR, section, body, small, SP, tbl, label_value_tbl

OUT = os.path.dirname(__file__)


def field_tbl(rows, col_widths=None):
    """Two-column label/value table, no alternating backgrounds, no header."""
    return tbl(rows, col_widths=col_widths, has_hdr=False, alt=False)


def pr_header():
    return [
        Paragraph('SIOUX FALLS POLICE DEPARTMENT', ST['doc_title']),
        Paragraph('320 West 4th Street  •  Sioux Falls, SD 57104  •  (605) 367-7212', ST['doc_sub']),
        Paragraph('INITIAL INCIDENT REPORT', ST['sec_head']),
        SP(3),
        HR(),
    ]


def build():
    path = os.path.join(OUT, "PR-01-Initial-Incident-Report.pdf")
    aging = {
        'staple': True,
        1: {
            'rings': [(W * 0.82, H * 0.55, 34, 301, 0.15, 86)],
            'creases': [(0, H * 0.50, W, H * 0.497, 302, 0.62)],
            'foxing': {'count': 20, 'inten': 0.72},
            'stamps': [("SFPD RECORDS — CASE FILE COPY", 0.75 * inch, H * 0.09, -3, STAMP_B, 9, 0.48)],
            'hw': [("no sign of struggle — MLS", W - 2.8 * inch, H * 0.70, 1, HW_PENCIL, 7.5),
                   ("door unlocked — confirm w/ Fuentes", 0.82 * inch, H * 0.615, -1, HW_BLUE, 7.0)],
        },
        2: {
            'rings': [],
            'creases': [(0, H * 0.38, W, H * 0.377, 303, 0.55)],
            'foxing': {'count': 14, 'inten': 0.65},
            'stamps': [],
            'hw': [("CSU on scene 0519 — log attached", W - 3.0 * inch, H * 0.86, 1, HW_PENCIL, 7.0),
                   ("ME called 0443 — Kowalczyk resp.", 0.82 * inch, H * 0.86, -1, HW_PENCIL, 7.0)],
        },
    }
    cb = make_onpage(301, "PR-01 Incident Report", 2, aging)
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.80 * inch, rightMargin=0.80 * inch,
                            topMargin=0.75 * inch, bottomMargin=0.72 * inch)

    story = pr_header()

    story += [field_tbl([
        ["Case No.:", "SFPD-2015-48801", "Report Type:", "Initial Incident Report"],
        ["ME Case No.:", "2015-ME-0447 (assigned)", "Classification:", "Unattended / Suspicious Death — Under Investigation"],
        ["Date of Incident:", "October 13–14, 2015", "Report Date:", "October 14, 2015"],
        ["Report Prepared By:", "Ofc. D.J. Williams (Badge #2214)", "Partner:", "Ofc. K.R. Chandra (Badge #2891)"],
        ["Supervisor Notified:", "Sgt. B.L. Ortega (Badge #1804)", "Time Notified:", "0441 hrs"],
        ["Homicide Notified:", "Det. M.L. Santos (Badge #4471), paged 0441 hrs", "On-Scene ETA:", "Det. Santos arrived 0528 hrs"],
    ], col_widths=[1.10 * inch, 2.80 * inch, 1.10 * inch, 1.55 * inch])]

    story += [SP(5), section("SECTION A — INCIDENT INFORMATION")]
    story += [field_tbl([
        ["Location:", "4200 S. Western Ave., Suite 712, 7th Floor, Sioux Falls, SD 57108"],
        ["Business Name:", "Apex Financial Group, Inc. (tenant) — Meridian Property Group (building owner)"],
        ["Call Received:", "0427 hrs, October 14, 2015 — 911 dispatch (call placed by Ramon Fuentes, IT contractor, on scene)"],
        ["Units Dispatched:", "Unit 22 (Williams/Chandra) — 0427 hrs"],
        ["Units Arrived:", "0434 hrs — met in lobby by R. Fuentes and building security officer P. Herne"],
        ["Scene Type:", "Interior commercial office — 7th floor executive suite"],
        ["Decedent:", "MARSH, Eleanor Anne — Female, White, DOB 03/22/1969 (age 46) — identified by building access records and employee photo on desk"],
        ["Condition on Arrival:", "Deceased. No signs of life. Decedent found slumped forward at executive desk, face down on arms, facing south. No respiratory effort, no pulse. Skin cool to touch, lividity visible on dependent surfaces. Rigor apparent in jaw and upper extremities."],
        ["EMS Response:", "SFFR Engine 7 and Medic 12 — arrived 0438 hrs. Advanced life support assessment performed. Decedent pronounced deceased at scene at 0441 hrs by Paramedic J. Alvarez (SFFR Medic 12). No resuscitation initiated."],
    ], col_widths=[1.30 * inch, 5.25 * inch])]

    story += [SP(5), section("SECTION B — SCENE DESCRIPTION")]
    story += [body(
        "Upon arrival, Officers Williams and Chandra were escorted by building security officer Herne and the reporting party, Fuentes, "
        "to the 7th floor via elevator. The 7th floor hallway was unoccupied. The door to Suite 712 was found standing open "
        "approximately 90 degrees. No evidence of forced entry was noted at the door frame, lock, or hinges. The electronic "
        "keycard reader mounted to the right of the door was intact and operational per building management.")]
    story += [SP(3), body(
        "The interior of Suite 712 consists of a main executive office (Suite 712-A), an adjacent assistant workstation area "
        "(Suite 712-B), and a small conference alcove (Suite 712-C). All three areas were accessible through the main entry door. "
        "Officers secured the scene perimeter at the main Suite 712 door and the 7th floor elevator lobby.")]
    story += [SP(3), body(
        "The main executive office (712-A) contained the decedent at a large mahogany desk positioned centrally in the room, "
        "facing north. The decedent was seated in a high-back leather executive chair, torso forward with her head resting on her "
        "left forearm on the desk surface. Her right arm was hanging at her side. Her hair was forward, obscuring her face. "
        "A black laptop computer was open on the desk, screensaver active. A ceramic coffee mug (cream exterior, dark interior "
        "staining) was present on the desk surface approximately 18 inches from the decedent's left hand. "
        "An open leather portfolio was present on the desk to the right, containing handwritten notes. "
        "The desk surface was otherwise consistent with active working use — papers, pens, a desk phone (receiver in cradle), "
        "a framed photograph (face down, position noted). No items appeared to have been swept from the desk. "
        "No signs of physical struggle were observed in the office: furniture was upright and in place, no broken items, "
        "no blood or other visible biological material.")]
    story += [SP(3), body(
        "Ambient lighting: overhead fluorescent lights were off. A desk lamp on the northeast corner of the desk was illuminated "
        "and directed downward. The south-facing windows (two, approximately 5 feet wide each) showed the exterior night skyline. "
        "Window latches were confirmed closed and locked by Officer Chandra. Temperature in the room was normal building "
        "ambient (approximately 68–70°F per HVAC reading). No odor of decomposition noted at time of arrival.")]

    story += [SP(5), section("SECTION C — ACTIONS TAKEN")]
    story += [tbl([
        ["Time", "Action", "Officer"],
        ["0434 hrs", "Units arrived lobby; met Fuentes and Herne; proceeded to 7th floor", "Williams / Chandra"],
        ["0436 hrs", "Scene accessed — Suite 712 door open; decedent confirmed unresponsive; scene cleared for safety", "Williams"],
        ["0437 hrs", "Scene secured; Fuentes directed to lobby to await interview; Herne instructed to secure elevator log", "Chandra"],
        ["0438 hrs", "SFFR Engine 7 / Medic 12 arrived on floor; ALS assessment begun", "Williams (liaison)"],
        ["0441 hrs", "Decedent pronounced deceased at scene — Para. J. Alvarez, SFFR Medic 12", "—"],
        ["0441 hrs", "Sgt. Ortega notified; Homicide (Det. Santos) paged", "Williams"],
        ["0443 hrs", "Minnehaha County Medical Examiner's Office notified — on-call line", "Chandra"],
        ["0445 hrs", "SFPD Crime Scene Unit requested", "Williams"],
        ["0452 hrs", "7th floor corridor secured with crime scene tape at elevator lobby", "Chandra"],
        ["0506 hrs", "Building manager Solis notified; responded to building", "Chandra"],
        ["0519 hrs", "SFPD CSU (Ofc. R. Alvarez-Ruiz, CSU-12; Tech. D. Okafor, CSU-07) arrived on scene", "Williams"],
        ["0528 hrs", "Det. M.L. Santos arrived on scene; case transferred to Homicide", "Williams"],
        ["0535 hrs", "Det. J.R. Brewer arrived on scene", "—"],
        ["0612 hrs", "ME Investigator T. Kowalczyk (MEI-09) arrived; jurisdiction accepted", "—"],
        ["0814 hrs", "Decedent transported from scene by DMTS — run DMTS-2015-10-14-007", "—"],
    ], col_widths=[0.72 * inch, 4.78 * inch, 1.05 * inch])]

    story += [SP(5), section("SECTION D — NOTIFICATIONS AND NEXT OF KIN")]
    story += [field_tbl([
        ["Next of Kin:", "MARSH, Gregory T. (spouse) — 4718 Hawthorn Ridge Dr., Sioux Falls, SD 57110"],
        ["NOK Notification:", "Conducted in person by Det. Santos and Victim Services Advocate L. Ferreira at 0752 hrs, October 14, 2015"],
        ["NOK Response:", "Mr. Marsh was cooperative. Requested to remain at residence; agreed. Interview scheduled for October 15, 2015."],
        ["Other Notifications:", "Apex Financial Group — COO Craig Ellsworth notified by telephone at 0805 hrs (Det. Santos); Board chair notification deferred to Ellsworth per company policy"],
    ], col_widths=[1.30 * inch, 5.25 * inch])]

    story += [SP(5), HR(), SP(4)]
    story += [field_tbl([
        ["Prepared By:", "Ofc. D.J. Williams (Badge #2214)", "Date:", "October 14, 2015"],
        ["Reviewed By:", "Sgt. B.L. Ortega (Badge #1804)", "Date:", "October 15, 2015"],
        ["Forwarded To:", "Homicide — Det. M.L. Santos (Badge #4471)", "Case Status:", "Active — Homicide Investigation"],
    ], col_widths=[1.10 * inch, 2.90 * inch, 0.65 * inch, 1.90 * inch])]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
