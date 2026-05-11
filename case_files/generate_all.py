#!/usr/bin/env python3
"""Master generator — runs all ME case file documents for Case 2015-ME-0447."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import doc01_intake
import doc02_dir
import doc03_body_receipt
import doc04_property
import doc05_autopsy
import doc06_specimen
import doc07_tox_submission
import doc08_tox_report
import doc09_ancillary

if __name__ == "__main__":
    print("Generating ME Case File 2015-ME-0447 ...\n")
    doc01_intake.build()
    doc02_dir.build()
    doc03_body_receipt.build()
    doc04_property.build()
    doc05_autopsy.build()
    doc06_specimen.build()
    doc07_tox_submission.build()
    doc08_tox_report.build()
    doc09_ancillary.build()
    print("\nAll documents generated.")
