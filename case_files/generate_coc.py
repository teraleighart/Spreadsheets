#!/usr/bin/env python3
"""Master generator — Chain of Custody documents for Case 2015-48801."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import coc01_evidence

if __name__ == "__main__":
    print("Generating Chain of Custody Log — Case 2015-48801 ...\n")
    coc01_evidence.build()
    print("\nDone.")
