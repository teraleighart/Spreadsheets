"""
Shared constants for Ultimate Finance Dashboard.
All tab builders import from here.
"""

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

EXPENSE_CATS = [
    "Housing", "Utilities", "Groceries", "Dining Out", "Transportation",
    "Healthcare", "Insurance", "Personal Care", "Clothing", "Entertainment",
    "Subscriptions", "Education", "Gifts & Donations", "Savings",
    "Debt Payment", "Home Maintenance", "Travel", "Pets", "Miscellaneous",
]

INCOME_CATS = [
    "Primary Salary", "Secondary Income", "Freelance / Contract",
    "Investment Income", "Rental Income", "Social Security",
    "Pension / Retirement", "Other Income",
]

FREQ_OPTIONS  = ["Monthly", "Bi-Weekly", "Weekly", "Quarterly", "Semi-Annual", "Annual"]
STATUS_OPTIONS = ["Paid", "Pending", "Upcoming", "Overdue", "Skipped"]
ACCT_TYPES    = ["Checking", "Savings", "Credit Card", "Cash", "Investment", "HSA", "Other"]

# Fixed row anchors inside every monthly tab — Annual Totals cross-refs depend on these.
MTH_INCOME_TOTAL_ROW  = 13   # row where total actual income lives  (col F)
MTH_EXPENSE_TOTAL_ROW = 37   # row where total actual expenses live  (col F)

# Variable Transactions column positions (1-indexed)
VT_COL_DATE     = 4   # D
VT_COL_DESC     = 5   # E
VT_COL_CATEGORY = 6   # F
VT_COL_AMOUNT   = 7   # G
VT_COL_ACCOUNT  = 8   # H
VT_COL_MONTH    = 9   # I
VT_COL_NOTES    = 10  # J
VT_DATA_START   = 6   # first data row


def sidebar(active=None):
    """Return the sidebar sections dict for any tab."""
    return {
        7:  ("START", None),
        8:  (None, "Instructions"),
        9:  (None, "Setup"),
        11: ("MONEY IN", None),
        12: (None, "Bank Accounts"),
        13: (None, "Paycheck Dashboard"),
        15: ("TRANSACTIONS", None),
        16: (None, "Quick Entry Log"),
        17: (None, "Variable Transactions"),
        18: (None, "Recurring Transactions"),
        19: (None, "Payments"),
        21: ("DASHBOARDS", None),
        22: (None, "All-in-One Dashboard"),
        23: (None, "Annual Totals"),
        24: (None, "Year in Review"),
        25: (None, "Automated Calendar"),
        27: ("MONTHLY", None),
        28: (None, "January"),
        29: (None, "February"),
        30: (None, "March"),
        31: (None, "April"),
        32: (None, "May"),
        33: (None, "June"),
        34: (None, "July"),
        35: (None, "August"),
        36: (None, "September"),
        37: (None, "October"),
        38: (None, "November"),
        39: (None, "December"),
        41: ("PLANNING & GOALS", None),
        42: (None, "50/30/20 Dashboard"),
        43: (None, "Expense Distribution"),
        44: (None, "Subscription Tracker"),
        45: (None, "Sinking Funds"),
        46: (None, "Savings Goals"),
        47: (None, "Debt Calculator"),
        48: (None, "Net Worth"),
        49: (None, "Investment Forecast"),
        50: (None, "Tax Prep Summary"),
        51: (None, "No-Spending Challenge"),
    }
