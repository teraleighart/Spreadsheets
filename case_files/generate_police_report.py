#!/usr/bin/env python3
"""Master generator — SFPD police reports for Case 2015-48801 / ME 2015-ME-0447."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import pr01_incident
import pr02_detective

if __name__ == "__main__":
    print("Generating SFPD Police Reports — Case 2015-48801 ...\n")
    pr01_incident.build()
    pr02_detective.build()
    print("\nAll police reports generated.")
