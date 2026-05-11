#!/usr/bin/env python3
"""Master generator — inter-agency correspondence for Case 2015-ME-0447 / SFPD-2015-48801."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import corr01_sfpd_to_me
import corr02_me_to_sfpd
import corr03_me_to_da

if __name__ == "__main__":
    print("Generating Correspondence — Case 2015-ME-0447 / SFPD-2015-48801 ...\n")
    corr01_sfpd_to_me.build()
    corr02_me_to_sfpd.build()
    corr03_me_to_da.build()
    print("\nAll correspondence generated.")
