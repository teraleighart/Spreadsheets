#!/usr/bin/env python3
"""Master generator — runs all 7 witness statements for Case 2015-ME-0447 / SFPD-2015-48801."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import ws01_fuentes
import ws02_molander
import ws03_ellsworth
import ws04_kowalski
import ws05_herne
import ws06_solis
import ws07_taft

if __name__ == "__main__":
    print("Generating Witness Statements — Case 2015-ME-0447 / SFPD-2015-48801 ...\n")
    ws01_fuentes.build()
    ws02_molander.build()
    ws03_ellsworth.build()
    ws04_kowalski.build()
    ws05_herne.build()
    ws06_solis.build()
    ws07_taft.build()
    print("\nAll witness statements generated.")
