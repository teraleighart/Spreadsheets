"""Document 02 — Death Investigation Report (5 pages)."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Spacer, PageBreak
from aging import make_onpage, W, H, STAMP_R, STAMP_B, HW_BLUE, HW_PENCIL
from styles import ST, HR, doc_header, section, subsection, body, body_l, small, SP, tbl

OUT = os.path.dirname(__file__)


def build():
    path = os.path.join(OUT, "ME-0447-02-Death-Investigation-Report.pdf")

    aging = {
        'staple': True,
        1: {
            'rings': [(W*0.84, H*0.88, 32, 11, 0.20, 32)],
            'creases': [(0, H*0.335, W, H*0.330, 31, 0.80), (0, H*0.667, W, H*0.671, 32, 0.75)],
            'foxing': {'count': 42, 'inten': 0.90},
            'stamps': [("RECEIVED", W-1.9*inch, H-1.7*inch, -9, STAMP_R, 14, 0.55)],
            'hw': [("F/U — access log??", 4.2*inch, H*0.58, 3, HW_BLUE, 8),
                   ("confirmed Orre", 4.2*inch, H*0.575, 3, HW_BLUE, 7)],
        },
        2: {
            'rings': [(W*0.12, H*0.22, 44, 22, 0.19, 44), (W*0.88, H*0.60, 28, 53, 0.17, 28)],
            'creases': [(0, H*0.50, W, H*0.503, 33, 0.70)],
            'foxing': {'count': 38, 'inten': 0.85},
            'hw': [("no CCTV south corridor — key gap", 0.82*inch, H*0.42, 1, HW_BLUE, 7.5)],
        },
        3: {
            'rings': [(W*0.80, H*0.15, 50, 13, 0.23, 55)],
            'creases': [(0, H*0.335, W, H*0.337, 34, 0.65)],
            'foxing': {'count': 50, 'inten': 0.95},
            'hw': [("check pharmacy records", W-2.3*inch, H*0.71, -2, HW_PENCIL, 8)],
            'smudges': [(2.5*inch, H*0.38, 70, 22, 15, 0.065)],
        },
        4: {
            'rings': [(W*0.15, H*0.78, 36, 44, 0.18, 66)],
            'creases': [(0, H*0.667, W, H*0.664, 35, 0.80)],
            'foxing': {'count': 44, 'inten': 0.88},
            'hw': [("timeline gap — critical", 0.82*inch, H*0.52, 4, HW_BLUE, 8),
                   ("3–9 hr window", 0.82*inch, H*0.508, 4, HW_BLUE, 7.5)],
        },
        5: {
            'rings': [(W*0.82, H*0.82, 42, 55, 0.21, 77)],
            'creases': [(0, H*0.335, W, H*0.332, 36, 0.72)],
            'foxing': {'count': 40, 'inten': 0.82},
            'stamps': [("PRELIMINARY — NOT FINAL", W*0.5 - 1.5*inch, 1.15*inch, -5, STAMP_R, 11, 0.52)],
            'hw': [("no manner cert. — RGA 10/16", W-2.8*inch, 1.70*inch, 0, HW_BLUE, 7.5)],
        },
    }

    cb = make_onpage(102, "Death Investigation Report", 5, aging)
    doc = SimpleDocTemplate(
        path, pagesize=letter,
        leftMargin=0.80*inch, rightMargin=0.80*inch,
        topMargin=0.75*inch,  bottomMargin=0.72*inch,
    )

    story = []

    # ══════════════════════════════════════════════════════════════════════
    # PAGE 1 — Notification and Circumstances of Discovery
    # ══════════════════════════════════════════════════════════════════════
    story += doc_header(
        "DEATH INVESTIGATION REPORT — INVESTIGATOR NARRATIVE",
        "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  DOB: 03/22/1969  |  Page 1 of 5")

    story += [tbl([
        ["ME Case #:", "2015-ME-0447",           "Date/Time Opened:", "10/14/2015 — 0312 hrs CDT"],
        ["Decedent:", "MARSH, Eleanor Anne",      "Date of Death (est.):", "10/13/2015 (exact TBD)"],
        ["Investigator:", "S.L. Kowalczyk (MEI-09)", "Report Prepared:", "10/14/2015"],
        ["Pathologist:", "Dr. R.G. Adeyemi, MD", "Status:", "PRELIMINARY — Cause/Manner DEFERRED"],
    ], col_widths=[1.30*inch, 2.20*inch, 1.55*inch, 2.45*inch], has_hdr=False, alt=False)]

    story += [SP(6), section("1. NOTIFICATION AND INITIAL INTAKE"), subsection("1.1 — Notification Details")]
    story += [body(
        "On October 14, 2015, at approximately 0248 hours Central Daylight Time, this investigator was contacted via "
        "the Minnehaha County Medical Examiner Office after-hours dispatch line by SFPD Patrol Dispatch Operator "
        "Christine M. Dell. Operator Dell relayed that SFPD patrol units and Sioux Falls Fire Rescue had responded "
        "to 4200 South Western Avenue, Suite 712, on the seventh floor of the Hartwell and Marsh Financial Partners "
        "building, regarding a reported unresponsive person. She advised that the individual had been pronounced dead "
        "on scene by EMS at approximately 2303 hours on October 13, 2015, and that the attending patrol officers "
        "considered the circumstances unclear and potentially suspicious in nature. Operator Dell reported that SFPD "
        "Detective Marcus J. Orre had been paged and was en route to assume scene authority as of the time of the "
        "notification call to this office."),
     body("Operator Dell provided the following information at initial notification: the decedent was described as a "
          "white female, approximately 40 to 50 years of age, found seated at or near her office desk by building "
          "maintenance personnel during a routine after-hours cleaning assignment. She was described as fully clothed "
          "and in no immediately obvious state of physical distress or gross external trauma per the initial EMS field "
          "report as relayed. No witnesses to the event of collapse or loss of consciousness had been identified at "
          "that time. No known medical emergency contacts or treating physicians had been identified by the initial "
          "patrol responders, and no emergency medical alert devices or current prescription medications were observed "
          "on scene at the time of EMS arrival, per Operator Dell's relay of the SFFR field report summary."),
     body("This investigator contacted on-call pathologist Dr. Raymond G. Adeyemi by telephone at 0250 hours and "
          "relayed the notification information in full. Dr. Adeyemi authorized this investigator to respond to the "
          "scene and provisionally accepted ME jurisdiction pending scene assessment. Dr. Adeyemi noted that the "
          "described circumstances — specifically an unattended death of a middle-aged individual in a workplace "
          "setting, occurring outside of normal business hours, without any identified treating physician and without "
          "any apparent immediate natural cause — were consistent with South Dakota Codified Law §23-14-1 criteria "
          "for medical examiner jurisdiction and directed that the case be opened accordingly. A case number was "
          "assigned (2015-ME-0447) and the case was entered into the ME office case management system at 0251 hours.")]

    story += [subsection("1.2 — Investigator Response and Scene Arrival")]
    story += [body(
        "This investigator departed the ME office at 0304 hours and arrived at the scene address, 4200 South Western "
        "Avenue, Sioux Falls, South Dakota, at approximately 0321 hours. The exterior of the building was secured by "
        "two SFPD patrol vehicles, units 214 and 237, positioned at the main lobby entrance and the south parking "
        "structure access road respectively. Building security personnel, subsequently identified as Kevin T. Molander, "
        "employed by Summit Property Security Services as the overnight shift supervisor for the building, met this "
        "investigator at the front lobby entrance and escorted this investigator to the seventh floor via the service "
        "elevator at the direction of Detective Orre, who had communicated instructions to building security by radio "
        "prior to this investigator's arrival."),
     body("Upon arrival on the seventh floor, this investigator was met by Detective Marcus J. Orre at the elevator "
          "lobby at approximately 0325 hours. Detective Orre confirmed that the scene had been secured since "
          "approximately 0010 hours on October 14 and that no individuals other than SFPD patrol personnel, building "
          "security staff, and the SFFR first responders had been permitted access to Suite 712 or the immediately "
          "surrounding hallway following the initial discovery. Detective Orre provided an overview of available "
          "information as known at that time, summarized in Section 3 of this report. Detective Orre also advised "
          "that SFPD's Crime Scene Unit had been notified and was expected on scene within the hour; CSU personnel "
          "arrived at approximately 0412 hours and conducted concurrent scene documentation, which is not further "
          "described herein as it falls within SFPD jurisdiction and documentation responsibility.")]

    story += [subsection("1.3 — Additional Notifications Made by This Office")]
    story += [body(
        "Following the initial scene assessment, this investigator contacted Dr. Adeyemi by telephone at approximately "
        "0430 hours to provide an updated account of scene conditions and decedent presentation. Based on the reported "
        "findings, Dr. Adeyemi directed this investigator to proceed with full scene documentation, obtain all "
        "available history from LE sources and any available next-of-kin or employer contacts, and to arrange "
        "transport of the body to the ME facility following release by LE scene authority. Dr. Adeyemi advised that "
        "a Priority-1 autopsy would be scheduled for 0900 hours the same morning, pending no change in circumstances."),
     body("At approximately 0705 hours on October 14, 2015, Dr. Adeyemi contacted Chief Medical Examiner Dr. Paula H. "
          "Reinholt and provided notification of the case. Dr. Reinholt authorized the Priority-1 autopsy and confirmed "
          "ME case acceptance. This investigator also contacted the Minnehaha County Attorney's Office death "
          "notification line at 0712 hours as required by office protocol for all cases assigned a suspicious "
          "designation; an on-call representative of that office acknowledged receipt and indicated no immediate action "
          "on their part was required at that stage. South Dakota Division of Criminal Investigation (DCI) was not "
          "contacted by this office at intake, as the determination of whether to involve DCI rests with SFPD; "
          "this investigator noted for the record that Detective Orre indicated he would be assessing that "
          "question independently and would keep this office informed.")]

    story += [PageBreak()]

    # ══════════════════════════════════════════════════════════════════════
    # PAGE 2 — Scene Description
    # ══════════════════════════════════════════════════════════════════════
    story += doc_header(
        "DEATH INVESTIGATION REPORT — CONTINUATION",
        "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  Page 2 of 5")

    story += [section("2. CIRCUMSTANCES OF DISCOVERY"), subsection("2.1 — Initial Discovery Account")]
    story += [body(
        "Based on information relayed to this investigator by Detective Orre at the scene, and supplemented by a "
        "brief and limited discussion with the individual who discovered the body, the following represents the ME "
        "office's current understanding of how the decedent was found. This account is considered preliminary and "
        "subject to revision pending formal recorded witness interviews by SFPD Investigations."),
     body("At approximately 2248 hours on October 13, 2015, a building custodial employee subsequently identified "
          "as Roberto J. Fuentes, employed by Paramount Commercial Cleaning Services (PCCS), was conducting routine "
          "after-hours janitorial services on the seventh floor of 4200 South Western Avenue. Mr. Fuentes was "
          "reportedly working along the south hallway of the floor when he used his issued access passkey to enter "
          "Suite 712 for the purpose of emptying wastebaskets and vacuuming. The suite, a private corner office "
          "occupied by the decedent, was described by Mr. Fuentes as having its interior office lights on — "
          "specifically both the overhead fluorescent panel lights and the desk lamp — which Mr. Fuentes indicated "
          "he interpreted at first as an indication that someone was working late, a circumstance he described as "
          "not uncommon on this floor during certain periods. Mr. Fuentes reportedly called out a verbal greeting "
          "upon entering the suite antechamber and received no response."),
     body("Mr. Fuentes reportedly proceeded to the inner office doorway and observed the decedent seated in her "
          "office chair, which was positioned facing the desk. He described her as appearing slumped slightly forward "
          "and to the right, with her right forearm and the outer aspect of her right hand resting on the desk "
          "surface and her head inclined toward her right shoulder. He described her eyes as partially open and her "
          "skin color as pale. He stated that she did not respond to his repeated verbal greetings or to his "
          "approach, at which point he touched her left shoulder and stated she felt cold and did not move. "
          "Mr. Fuentes exited the suite and immediately contacted building security via the interior phone system "
          "located in the hallway. This investigator notes that the foregoing account was relayed secondhand "
          "through Detective Orre and is not the product of a direct formal interview by this office; the account "
          "is documented here for completeness and is explicitly preliminary."),
     body("Building security supervisor Kevin T. Molander responded to the seventh floor within approximately four "
          "minutes and entered Suite 712 to assess the situation. Molander confirmed the decedent's unresponsive "
          "state, observed no immediate signs of physical distress or obvious injury, and contacted SFPD dispatch "
          "and SFFR simultaneously at approximately 2256 hours. Molander stated he did not relocate the decedent, "
          "administer any intervention, or remove any items from the office prior to the arrival of emergency "
          "services. SFFR Unit 1 arrived on scene at approximately 2301 hours. EMS personnel confirmed "
          "unresponsiveness and the absence of pulse, respiratory effort, and pupillary response. Based on their "
          "assessment of body temperature and preliminary gross postmortem changes — the degree of which was not "
          "formally specified in their run report as reviewed by this investigator — SFFR Paramedic Supervisor "
          "Thomas Kiedrowski, NRP, determined that resuscitation efforts were not indicated and pronounced the "
          "decedent deceased at 2303 hours, October 13, 2015. No resuscitation was attempted. SFPD patrol units "
          "(Officer L.D. Harmon, Badge #1142, and Officer B.T. Schraeder, Badge #2078) arrived at approximately "
          "2304 hours and secured the floor pending the arrival of a detective.")]

    story += [section("3. SCENE DESCRIPTION"), subsection("3.1 — Building and Floor Layout")]
    story += [body(
        "The scene of death is located at 4200 South Western Avenue, Sioux Falls, South Dakota, a seven-story "
        "commercial office building of modern steel-frame and glass construction, identified by exterior signage "
        "and building records as the Hartwell and Marsh Financial Partners corporate headquarters. The building is "
        "set back approximately forty feet from South Western Avenue with a secured enclosed lobby and a parking "
        "structure situated to the south. The seventh floor is the uppermost occupied floor and is occupied entirely "
        "by Hartwell and Marsh Financial Partners. Access to the seventh floor is controlled via electronic key-card "
        "readers at each stairwell door and at both elevator banks; a log of after-hours access events was "
        "requested by Detective Orre from building management and was not made available to this investigator at "
        "the time of the scene examination."),
     body("The seventh floor layout, as observed and described to this investigator by building security supervisor "
          "Molander, consists of a central elevator lobby leading to an open reception and administrative work "
          "area, with a perimeter ring of private offices along the north, east, south, and west walls. Suite 712 "
          "is located in the southwest corner of the floor. The hallway immediately outside Suite 712 is a "
          "secondary corridor running east-west along the south side of the building. This corridor is not "
          "monitored by interior CCTV. Building management confirmed that a camera is positioned at the south "
          "stairwell door, approximately thirty feet east of Suite 712, and another at the south end of the main "
          "elevator lobby, approximately sixty feet to the north. The status and retrieval of recorded footage "
          "from these cameras was outside the scope of this investigator's role at the scene and is a matter "
          "for SFPD Investigations.")]

    story += [subsection("3.2 — Suite 712: Antechamber and Inner Office")]
    story += [body(
        "Suite 712 consists of two rooms: a small rectangular antechamber, approximately twelve by eight feet, "
        "which serves as an assistant or reception area and contains a secondary workstation, two guest chairs, "
        "and a lateral filing cabinet; and an inner private office accessed through a connecting interior doorway "
        "fitted with a solid wood door, hinged to swing inward. At the time of this investigator's arrival, the "
        "door to the inner office was in the open position, consistent with what SFPD patrol reported."),
     body("The inner office measures approximately eighteen by fifteen feet. The room is furnished with a large "
          "executive desk positioned centrally, oriented so that the occupant would face north toward the entry "
          "doorway when seated. Behind the desk to the west, a credenza holds a printer, a desktop computer "
          "docking station, and a series of labeled binders. Along the east wall, a rectangular conference table "
          "with six chairs is positioned. The south wall contains floor-to-ceiling windows overlooking the south "
          "parking structure. At the time of this investigator's arrival, interior blinds were open, ceiling "
          "fluorescent lighting and desk lamp were both illuminated, and the wall thermostat read 71°F."),
     body("The desk surface contained, as observed without disturbance: a closed laptop computer (company-issued "
          "per coworkers; retained by SFPD CSU), a legal-sized notepad with handwritten notes (retained SFPD CSU), "
          "a ceramic coffee mug on a coaster approximately twelve inches to the left of the laptop containing a "
          "liquid substance consistent with coffee (collected by SFPD CSU for laboratory analysis; not submitted to "
          "ME office), an uncapped ballpoint pen resting on the notepad, and a telephone handset on the right side "
          "of the desk surface. No food packaging, prescription medication bottles, over-the-counter medications, "
          "or visible chemical substances were identified on the desk surface, in the visible portions of the "
          "credenza, or in any immediately accessible location in the office. The waste receptacle beneath the "
          "right side of the desk was empty, consistent with having been recently serviced per Mr. Fuentes.")]

    story += [PageBreak()]

    # ══════════════════════════════════════════════════════════════════════
    # PAGE 3 — Witness Table, Medical History, Limitations
    # ══════════════════════════════════════════════════════════════════════
    story += doc_header(
        "DEATH INVESTIGATION REPORT — CONTINUATION",
        "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  Page 3 of 5")

    story += [section("4. INFORMATION SOURCES AND WITNESS / CONTACT SUMMARY")]
    story += [body(
        "The following table summarizes individuals from whom information was obtained or attempted at scene or during "
        "initial intake on October 14, 2015. This table does not constitute a witness list for prosecutorial "
        "purposes, which remains the exclusive responsibility of SFPD. Information here reflects only what was "
        "relayed to the ME investigator in the context of death investigation intake and is qualified accordingly. "
        "Formal recorded statements were conducted separately by SFPD and are not reproduced here.")]
    story += [SP(4), tbl([
        ["Name / Role", "Affiliation", "Contact Method", "Information Provided to ME Investigator"],
        ["Det. Marcus J. Orre\n(SFPD Investigations)",
         "Sioux Falls Police Dept.",
         "In person, on scene",
         "Overview of scene conditions; decedent ID by employees; timeline of discovery; directed ME investigator access; advised re: SFPD evidence holds."],
        ["Para. Sup. T. Kiedrowski, NRP\n(SFFR Station 1)",
         "Sioux Falls Fire Rescue",
         "In person, on scene (brief)",
         "Confirmed pronouncement time 2303 hrs 10/13/2015; described gross postmortem changes observed by EMS (lividity, estimated skin temp.); confirmed no resuscitation; provided run # SFFR-2015-19442."],
        ["Roberto J. Fuentes\n(Custodial)",
         "Paramount Commercial Cleaning Services",
         "Via Det. Orre relay, on scene",
         "Described discovery; reported lights on; no response to verbal greeting; tactile contact w/ decedent's left shoulder; perceived skin temp. as cold. Direct ME interview deferred to SFPD formal process."],
        ["Kevin T. Molander\n(Security Supervisor)",
         "Summit Property Security Services",
         "In person, on scene",
         "Confirmed after-hours access control; provided floor layout orientation; described response to Fuentes; confirmed no known 7th-floor personnel between approx. 1900 hrs and discovery. CCTV retrieval is LE function."],
        ["Karla J. Brennan\n(Building Mgmt. Rep.)",
         "Pinnacle Property Mgmt. Group",
         "Phone — 0510 hrs 10/14/2015",
         "Confirmed HVAC schedule and 7th-floor temp. range (70–72°F after-hours). Electronic entry log not available at time of contact; directed Det. Orre's request to property ownership."],
        ["Gregory R. Whitfield\n(Managing Partner, H&M)",
         "Hartwell & Marsh Financial Partners, LLC",
         "Phone via Det. Orre intro — 0445 hrs",
         "Confirmed decedent's identity and CFO role (approx. 9 yrs). Stated decedent in 'good health as far as he knew.' No knowledge of chronic conditions or treating physician. Provided SSN (last 4) and NOK info. Expressed surprise at circumstances."],
        ["Thomas R. Marsh\n(Adult Son / NOK)",
         "Decedent's family",
         "Via Det. Orre relay — post-0610 hrs",
         "Unaware of any diagnosed medical conditions; denied knowledge of prescriptions; stated decedent had not complained of illness recently. Personal physician unknown to him; stated decedent 'didn't like doctors.' ME to follow up re: release authorization and history."],
        ["Company Legal Counsel\n(name not provided to ME)",
         "Hartwell & Marsh Financial Partners, LLC",
         "Phone, via Det. Orre — indirect",
         "Provided SSN (last 4) for identification purposes. No other substantive information to ME at this stage."],
    ], col_widths=[1.35*inch, 1.30*inch, 0.90*inch, 4.00*inch])]

    story += [SP(6), section("5. MEDICAL AND SOCIAL HISTORY — INTAKE STATUS"), subsection("5.1 — Medical History")]
    story += [body(
        "At the time of case intake and scene response, no formal medical history was available to this investigator. "
        "No treating physician was identified by any source contacted during the initial intake process. Both the "
        "decedent's adult son, Thomas R. Marsh, and managing partner Gregory R. Whitfield independently stated they "
        "had no knowledge of the decedent's being under active physician care, though neither was in a position to "
        "confirm or deny the existence of a primary care or specialist relationship with certainty. No medical alert "
        "bracelet or identification was observed on the decedent's person or in her purse contents. No prescription "
        "medication bottles were identified at the scene, in the decedent's personal effects, or in any location on "
        "the seventh floor accessible to this investigator or described by SFPD as identified during the scene "
        "search. The decedent's personal physician, if any, has not been identified as of the close of this "
        "investigator's scene and intake activities."),
     body("No emergency medical services history was available at intake. SFPD was requested to inquire whether the "
          "decedent had any prior SFFR transport history; that inquiry was pending as of the preparation of this "
          "report. No hospital discharge records, outpatient clinic visit records, or pharmacy records were obtained "
          "at intake; acquisition of such records, to the extent they are available and accessible, is a pending "
          "investigative action for both this office and SFPD, subject to applicable legal process.")]

    story += [subsection("5.2 — Psychiatric, Behavioral, and Substance History")]
    story += [body(
        "No information was available at intake regarding psychiatric history, prior mental health treatment, known "
        "behavioral health conditions, or substance use history. Gregory Whitfield and Thomas Marsh were each, "
        "independently, asked whether the decedent had expressed any ideation of self-harm or any unusual personal "
        "distress in the period preceding her death; both stated no without apparent hesitation. Whitfield added "
        "that the decedent had appeared at work in normal functional capacity through, to his knowledge, the end "
        "of the prior business day, October 13, 2015, though he stated he had not spoken with her personally "
        "that afternoon. A partial empty bottle consistent with a commercially available wine varietal was noted "
        "by SFPD CSU personnel in the inner-office waste receptacle of an adjacent suite (Suite 708); no alcoholic "
        "beverage containers were identified in Suite 712 or associated with the decedent. This information is "
        "recorded for completeness and does not establish any connection to the decedent.")]

    story += [PageBreak()]

    # ══════════════════════════════════════════════════════════════════════
    # PAGE 4 — Limitations, External Observations at Scene, Chronology
    # ══════════════════════════════════════════════════════════════════════
    story += doc_header(
        "DEATH INVESTIGATION REPORT — CONTINUATION",
        "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  Page 4 of 5")

    story += [section("6. KNOWN LIMITATIONS OF INTAKE INFORMATION")]
    story += [body(
        "The following limitations are identified as of the date of this investigator's report and are noted for "
        "the record to ensure appropriate caution in interpreting all preliminary findings:"),
     body("<b>(a) No identified treating physician.</b> The absence of a known primary care physician or specialist "
          "at intake significantly limits this investigator's ability to obtain a clinical history, recent laboratory "
          "values, active medication list, or any documented conditions relevant to the cause of death. This "
          "limitation is considered material and will require active follow-up by both this office and SFPD."),
     body("<b>(b) No eyewitness to collapse or loss of consciousness.</b> The decedent was discovered postmortem. "
          "No individual has come forward who observed the decedent's condition deteriorate, collapse, or become "
          "unresponsive. The last known observation of the decedent in an ambulatory or conscious state has not "
          "been confirmed at the time of this report, representing a critical chronological gap."),
     body("<b>(c) No medication list.</b> Neither the scene nor any source contacted at intake yielded a current or "
          "historical medication list for the decedent. The absence of observed medications at the scene is notable "
          "but does not rule out the possibility that the decedent maintained medications at her residence or "
          "elsewhere, or that any medications present at the scene may have been removed prior to or after "
          "discovery by an unknown party."),
     body("<b>(d) Building access record not yet reviewed.</b> The electronic key-card access log for the seventh "
          "floor was not available to this investigator or SFPD at the time of the scene examination. This leaves "
          "the exact time of the decedent's last documented entry onto the floor, and the presence or absence of "
          "other individuals on the floor after normal business hours, presently unconfirmed."),
     body("<b>(e) CCTV footage not reviewed.</b> Interior CCTV coverage of the building's lobby, elevator banks, "
          "and some hallways was not reviewed by this investigator; review and retrieval are an SFPD Investigations "
          "function. Gaps in CCTV coverage, specifically along the south corridor where Suite 712 is located, "
          "are a material limitation to establishing movement on that floor after business hours."),
     body("<b>(f) Wide postmortem interval estimate.</b> Given available environmental temperature data, the absence "
          "of a witnessed time of collapse, and the degree of postmortem changes grossly observed at scene, a "
          "preliminary estimate of the postmortem interval at the time of this investigator's scene arrival "
          "(approximately 0325–0500 hrs, October 14, 2015) is conservatively in the range of three to nine hours. "
          "This range is broad and subject to significant revision based on autopsy findings and ancillary data. "
          "Any estimation of time of death beyond this range is not supported by currently available information.")]

    story += [section("7. EXTERNAL OBSERVATION AT SCENE — SUMMARY")]
    story += [body(
        "The following is a summary of this investigator's external observations of the decedent at the scene "
        "prior to transport. These observations are preliminary in nature, made under field conditions, and are "
        "not a substitute for the formal autopsy examination. All measurements and weights referenced are "
        "approximations pending formal measurement at autopsy."),
     body("The decedent was found seated in an ergonomic executive desk chair on the inner side of the desk, in "
          "a position consistent with normal working posture. The chair had rotated slightly to the right "
          "(east) from a direct forward-facing orientation, approximately fifteen to twenty degrees. The decedent's "
          "torso was slumped forward and to the right, right forearm and outer hand resting on the desk surface, "
          "left arm in the lap. Head inclined rightward and slightly forward, right cheek resting lightly on the "
          "right shoulder. Feet rested on the floor beneath the desk. No evidence of significant postmortem or "
          "perimortem extremity repositioning was apparent, though this is a limited field assessment."),
     body("The decedent was wearing a white collared blouse, dark-charcoal dress slacks, a blazer, and "
          "low-heeled dress shoes. Clothing was in place and did not appear rearranged, disordered, or torn. "
          "The collar button was open at the second button from the top. No acute trauma, external hemorrhage, "
          "ligature marks, petechial hemorrhage (to the extent visible), or gross deformity was identified on "
          "external examination at the scene. These observations are explicitly limited by body position, clothing "
          "coverage, and ambient lighting conditions, and shall not be interpreted as ruling out findings that "
          "will be assessed at formal autopsy."),
     body("Postmortem changes observed at the scene: Lividity was present and appeared fixed along the posterior "
          "and right lateral surfaces of the decedent as accessible to examination without disrobing; the pattern "
          "was generally consistent with the observed seated position but this correlation requires autopsy "
          "confirmation. Rigor mortis was present and appeared well-established in the upper extremities, jaw, and "
          "neck; lesser development was noted in the lower extremities based on passive manipulation. Skin "
          "temperature was assessed with a handheld infrared thermometer at 77.4°F at the right forearm at "
          "approximately 0345 hours; ambient room temperature was 70.8°F at the same time. No decomposition "
          "changes were identified on gross external examination at the scene. Taken together, these postmortem "
          "changes are consistent with an estimated postmortem interval in the range described in Section 6(f) "
          "above, subject to formal analysis at autopsy.")]

    story += [SP(4), section("8. PRELIMINARY CHRONOLOGY")]
    story += [body("The following chronology reflects information available as of the preparation of this report and "
                   "is explicitly preliminary, incomplete, and subject to revision."), SP(3)]
    story += [tbl([
        ["Date/Time (CDT)", "Event", "Source / Notes"],
        ["10/13/2015 — Business hours (est. to 1800)",
         "Decedent reported at work in normal capacity; last confirmed in-person contact with colleagues unspecified (not yet determined by this office)",
         "G.R. Whitfield (employer) — informal; SFPD to develop formally"],
        ["10/13/2015 — After 1800 (est.)",
         "Decedent remains on 7th floor after normal business hours; basis and duration unknown; access log and CCTV review pending",
         "Building security — Molander; SFPD inquiry pending"],
        ["10/13/2015 — 2248 hrs (approx.)",
         "Decedent discovered unresponsive by R.J. Fuentes (custodial) during routine cleaning; Suite 712 lights on; decedent seated at desk",
         "R.J. Fuentes via Det. Orre relay"],
        ["10/13/2015 — 2252 hrs (approx.)",
         "Building security supervisor Molander arrives on 7th floor; confirms decedent unresponsive; contacts SFPD and SFFR",
         "K.T. Molander — on scene"],
        ["10/13/2015 — 2301 hrs",
         "SFFR Unit 1 arrives on scene; EMS confirms unresponsiveness, no pulse, no respirations",
         "SFFR Run Report #SFFR-2015-19442"],
        ["10/13/2015 — 2303 hrs",
         "Decedent pronounced deceased on scene by Paramedic Supervisor T. Kiedrowski, NRP. No resuscitation attempted.",
         "SFFR; ME records"],
        ["10/13/2015 — 2304 hrs",
         "SFPD patrol units 214 and 237 (Officers Harmon and Schraeder) arrive; secure scene",
         "SFPD dispatch records"],
        ["10/14/2015 — 0248 hrs",
         "ME office notified by SFPD dispatch (Operator Dell); case opened (2015-ME-0447)",
         "ME dispatch log"],
        ["10/14/2015 — 0250 hrs",
         "ME investigator contacts Dr. Adeyemi; ME jurisdiction authorized; P-1 autopsy tentatively ordered",
         "ME records"],
        ["10/14/2015 — 0321 hrs",
         "ME Investigator Kowalczyk arrives at scene; met by Det. Orre",
         "Investigator log"],
        ["10/14/2015 — 0412 hrs",
         "SFPD Crime Scene Unit arrives; concurrent scene documentation",
         "SFPD CSU log (not ME document)"],
        ["10/14/2015 — 0430 hrs",
         "ME investigator contacts Dr. Adeyemi with scene update; transport and autopsy confirmed",
         "ME records"],
        ["10/14/2015 — 0538 hrs",
         "Body released from scene by Det. Orre; transferred to Dakota Mortuary Transport (Halverson, Tripp); ME Seal #MEO-S-2015-3391 applied",
         "ME records; DMTS run sheet"],
        ["10/14/2015 — 0622 hrs",
         "Body received at ME facility by Mortuary Tech. Farr; seal verified intact; stored Cooler Bay C, Shelf 2",
         "ME facility receipt log"],
        ["10/14/2015 — 0705 hrs",
         "Dr. Adeyemi notifies Chief ME Dr. Reinholt; P-1 autopsy authorized",
         "ME records"],
        ["10/14/2015 — 0900 hrs",
         "Autopsy performed, Suite A, by Dr. Adeyemi (primary) with Dr. Sandvik (observer) — see Autopsy Report",
         "ME Autopsy Report 2015-ME-0447"],
    ], col_widths=[1.40*inch, 3.60*inch, 2.55*inch])]

    story += [PageBreak()]

    # ══════════════════════════════════════════════════════════════════════
    # PAGE 5 — Investigator Opinion, Certification
    # ══════════════════════════════════════════════════════════════════════
    story += doc_header(
        "DEATH INVESTIGATION REPORT — CONTINUATION",
        "Case No. 2015-ME-0447  |  MARSH, Eleanor Anne  |  Page 5 of 5")

    story += [section("9. INVESTIGATOR OPINION AND PRELIMINARY ASSESSMENT")]
    story += [body(
        "The following represents this investigator's preliminary assessment based solely on information available "
        "at the time of scene examination and intake, prior to completion of the autopsy and ancillary studies. "
        "This section does not constitute a final determination of cause or manner of death. All conclusions "
        "contained herein are provisional, may be revised or retracted in whole or in part based on subsequent "
        "findings, and should not be cited or relied upon as a final medical or legal determination."),
     body("The decedent, Eleanor Anne Marsh, a 46-year-old female with no identified medical history at the time "
          "of intake, was found deceased in her private office at 4200 South Western Avenue, Suite 712, Sioux "
          "Falls, SD, after normal business hours on October 13, 2015. The circumstances of her death as known at "
          "intake include the following notable features: (1) the death was unwitnessed, with no individual "
          "identified who observed the decedent's condition deteriorate or who last saw the decedent in a "
          "confirmed living state at a specific documented time; (2) no obvious acute external trauma was "
          "identified on gross scene examination, though this examination was limited; (3) no prescription "
          "medications or acute toxicological exposures were identified at the scene, though this absence is "
          "not dispositive; (4) postmortem changes at the scene were grossly consistent with a multi-hour "
          "interval, with fixedness of lividity and well-established rigor; and (5) the setting and circumstances "
          "do not immediately suggest a clear natural, accidental, or intentional etiology on the basis of scene "
          "information alone."),
     body("This investigator does not, based on scene examination and intake information, identify a single "
          "leading hypothesis for manner of death. The absence of obvious trauma, the discovery in a private "
          "locked-access office after business hours, the absence of identified witnesses, and the absence of "
          "any known medical history collectively support the determination that a thorough autopsy examination "
          "with full toxicological screening and appropriate ancillary studies is necessary before any "
          "preliminary opinion regarding cause or manner of death can be responsibly offered. The designation "
          "of 'suspicious' circumstances at intake is based on process criteria — specifically the unattended "
          "nature of the death, the absence of a known treating physician, and the features described above — "
          "and does not constitute a finding or allegation that the death was caused by the action or omission "
          "of any third party."),
     body("Pending results of the autopsy (performed October 14, 2015, see separate Autopsy Report for Case "
          "2015-ME-0447), toxicology (specimens submitted October 14, 2015, see Toxicology Submission Form), "
          "histological examination, and any further information developed by SFPD Investigations, this "
          "investigator's opinion regarding cause and manner of death is deferred in its entirety. No preliminary "
          "death certificate will be issued pending these results. The case remains open and active.")]

    story += [SP(6), section("10. PENDING ACTIONS — ME OFFICE")]
    story += [tbl([
        ["Action Item", "Responsible Party", "Target / Status"],
        ["Obtain formal autopsy report and incorporate into case file",
         "Dr. R.G. Adeyemi / ME Records",
         "Preliminary: within 5 business days; Final: TBD pending tox/histo"],
        ["Toxicology specimen submission and tracking",
         "ME Lab Liaison",
         "Submitted 10/14/2015 (see Tox Submission Form); results est. 4–8 wks"],
        ["Histology slides preparation and review",
         "ME Histology Tech / Dr. Adeyemi",
         "Pending; tissue blocks submitted at autopsy"],
        ["Identify decedent's treating physician(s) if any",
         "SFPD (primary) / ME Investigator (support)",
         "Pending; no physician identified at intake"],
        ["Obtain pharmacy and medical records (via legal process as needed)",
         "SFPD Investigations",
         "Pending SFPD subpoena or records request; ME to coordinate if needed"],
        ["Review decedent's residential address for medications / medical items",
         "SFPD Investigations (residential search scope TBD)",
         "Pending SFPD determination and any warrant"],
        ["Obtain and review building electronic key-card access log, 7th floor",
         "SFPD Investigations",
         "Pending — log held by building ownership; SFPD inquiry noted on scene"],
        ["CCTV footage review — lobby, elevator, south stairwell door",
         "SFPD Investigations",
         "Pending — SFPD to retrieve; coverage gaps on south corridor noted"],
        ["Next-of-kin release authorization for personal effects held by ME",
         "ME Investigator / NOK (T.R. Marsh)",
         "Pending — contact initiated via SFPD; release auth. form not yet received"],
        ["Final death certificate issuance",
         "Dr. Adeyemi / Chief ME Reinholt",
         "DEFERRED — pending tox, histo, and final cause/manner determination"],
    ], col_widths=[2.60*inch, 1.90*inch, 3.05*inch])]

    story += [SP(8), HR(),
              body("<b>INVESTIGATOR CERTIFICATION:</b> I certify that the foregoing Death Investigation Report is "
                   "an accurate account of my observations, the information obtained at the scene and during initial "
                   "intake, and my preliminary assessment, to the best of my knowledge as of the date of preparation. "
                   "This report is PRELIMINARY. No final determination of cause or manner of death is made herein. "
                   "All opinions are subject to revision upon receipt of autopsy, toxicology, histology, and "
                   "investigative findings."), SP(4)]
    story += [tbl([
        ["Investigator Signature:", "________________________________", "Date:", "10/14/2015", "Time:", "1022 hrs"],
        ["Print Name / Badge #:",   "Sandra L. Kowalczyk, MSFS — Investigator II — MEI-09",
         "Reviewer (Pathologist):", "Dr. Raymond G. Adeyemi, MD", "Date:", "____________"],
        ["Reviewer Signature:",     "________________________________", "Case Status:", "OPEN / PRELIMINARY", "", ""],
    ], col_widths=[1.40*inch, 2.10*inch, 0.85*inch, 1.50*inch, 0.45*inch, 1.25*inch], has_hdr=False, alt=False)]

    doc.build(story, onFirstPage=cb, onLaterPages=cb)
    print(f"  → {path}")


if __name__ == "__main__":
    build()
