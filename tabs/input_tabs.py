"""
Input tabs: Instructions, Setup, Bank Accounts, Recurring Transactions,
Payments, Variable Transactions, Quick Entry Log.
"""
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

from styling import (
    COLORS, FONT_DISPLAY, FONT_BODY, FONT_MONO,
    setup_sheet, add_gold_rule, add_kpi_card,
    add_status_formatting, add_data_bars,
    add_dropdown, run_quality_gate,
)
from constants import (
    MONTHS, EXPENSE_CATS, INCOME_CATS, FREQ_OPTIONS,
    STATUS_OPTIONS, ACCT_TYPES, sidebar,
    VT_COL_CATEGORY, VT_COL_AMOUNT, VT_COL_MONTH,
)


# ── tiny layout helpers ───────────────────────────────────────

def W(ws, widths):
    for col, w in widths.items():
        ws.column_dimensions[col].width = w

def hdr(ws, row, col, text, end_col=None):
    c = ws.cell(row=row, column=col)
    c.value = f"  {text}"
    c.style = 'section_header'
    if end_col:
        ws.merge_cells(start_row=row, start_column=col, end_row=row, end_column=end_col)

def col_hdr(ws, row, col, labels):
    for i, lbl in enumerate(labels):
        c = ws.cell(row=row, column=col + i)
        c.value = lbl
        c.style = 'column_header'

def drow(ws, row, col, vals, alt=False):
    sn = 'data_alt' if alt else 'data_cell'
    for i, v in enumerate(vals):
        c = ws.cell(row=row, column=col + i)
        c.value = v
        c.style = sn
        if isinstance(v, (int, float)):
            c.alignment = Alignment(horizontal='right', vertical='center')

def trow(ws, row, col, vals):
    for i, v in enumerate(vals):
        c = ws.cell(row=row, column=col + i)
        c.value = v
        c.style = 'total_row'
        if i == 0:
            c.alignment = Alignment(horizontal='left', vertical='center')
        elif isinstance(v, str) and v.startswith('='):
            c.number_format = '"$"#,##0.00'
            c.alignment = Alignment(horizontal='right', vertical='center')
        elif isinstance(v, (int, float)):
            c.number_format = '"$"#,##0.00'
            c.alignment = Alignment(horizontal='right', vertical='center')

def money_fmt(ws, row, col, count=1):
    for i in range(count):
        ws.cell(row=row, column=col + i).number_format = '"$"#,##0.00'

def pct_fmt(ws, row, col):
    ws.cell(row=row, column=col).number_format = '0.0%'


# ═══════════════════════════════════════════════════════════════
# INSTRUCTIONS
# ═══════════════════════════════════════════════════════════════

def build_instructions(wb, ws):
    setup_sheet(ws,
        "Welcome to Your Finance Dashboard",
        subtitle="Your complete money management system — calm, clear, and built for real life.",
        active_tab="Instructions", sections=sidebar("Instructions"))
    W(ws, {'D': 2, 'E': 30, 'F': 54, 'G': 2})

    steps = [
        ("Step 1  —  Set Up Your Basics",
         "Open the Setup tab first. Enter your name, the current year, your currency symbol, "
         "and how often you're paid. This takes two minutes and personalizes the whole workbook."),
        ("Step 2  —  List Your Accounts",
         "Go to Bank Accounts and add every account you use regularly — checking, savings, "
         "and credit cards. Include the current balance so your Net Worth tab starts accurately."),
        ("Step 3  —  Enter Your Recurring Bills",
         "Use Recurring Transactions to log fixed monthly costs: rent or mortgage, utilities, "
         "insurance, loan payments. These are your predictable expenses."),
        ("Step 4  —  Log Spending As It Happens",
         "Open Quick Entry Log whenever you make a purchase. Date, description, amount, category — "
         "done in under 30 seconds. This feeds your monthly budget tabs automatically."),
        ("Step 5  —  Check Your Dashboard Weekly",
         "The All-in-One Dashboard auto-updates from everything you've entered. "
         "Five minutes there each week keeps you completely in control of your finances."),
    ]

    r = 7
    hdr(ws, r, 5, "HOW TO GET STARTED", end_col=10)
    ws.row_dimensions[r].height = 24

    for i, (title, body) in enumerate(steps):
        row = r + 2 + (i * 3)
        ws.row_dimensions[row].height = 22
        ws.row_dimensions[row + 1].height = 32

        bullet = ws.cell(row=row, column=4)
        bullet.value = "▸"
        bullet.font = Font(name=FONT_BODY, size=11, color=COLORS['gold'])
        bullet.fill = PatternFill(start_color=COLORS['bg'], end_color=COLORS['bg'], fill_type='solid')
        bullet.alignment = Alignment(horizontal='center', vertical='center')

        tc = ws.cell(row=row, column=5)
        tc.value = title
        tc.font = Font(name=FONT_BODY, size=10, bold=True, color=COLORS['primary'])
        tc.fill = PatternFill(start_color=COLORS['bg'], end_color=COLORS['bg'], fill_type='solid')
        tc.alignment = Alignment(vertical='center')

        bc = ws.cell(row=row + 1, column=5)
        bc.value = body
        bc.font = Font(name=FONT_BODY, size=10, italic=True, color=COLORS['muted_text'])
        bc.fill = PatternFill(start_color=COLORS['bg'], end_color=COLORS['bg'], fill_type='solid')
        bc.alignment = Alignment(vertical='top', wrap_text=True)
        ws.merge_cells(start_row=row + 1, start_column=5, end_row=row + 1, end_column=10)

    r2 = r + 2 + (len(steps) * 3) + 2
    add_gold_rule(ws, row=r2, start_col=4, end_col=11)
    hdr(ws, r2 + 1, 5, "TAB GUIDE  —  WHAT EVERY TAB DOES", end_col=11)
    ws.row_dimensions[r2 + 1].height = 24

    tab_guide = [
        ("Setup",                  "Personal settings: name, year, currency, pay frequency."),
        ("Bank Accounts",          "Every account you own with institution, type, and balance."),
        ("Recurring Transactions", "Fixed bills that repeat: rent, utilities, insurance, loans."),
        ("Payments",               "One-time or irregular payments with due dates and status."),
        ("Variable Transactions",  "All day-to-day spending — the main source for monthly actuals."),
        ("Quick Entry Log",        "Fastest way to log a transaction. Date, amount, category — done."),
        ("All-in-One Dashboard",   "Your financial command center. KPIs and charts auto-update."),
        ("Annual Totals",          "Year at a glance: total income, spending, and net by month."),
        ("Year in Review",         "Best month, worst month, biggest category, total saved."),
        ("Automated Calendar",     "Monthly bill-due-date grid — see what's due on which day."),
        ("Paycheck Dashboard",     "Track income by pay period and see your YTD total."),
        ("January – December",     "Monthly budget vs. actual by category. Formulas pre-built."),
        ("50/30/20 Dashboard",     "Are your needs, wants, and savings in balance?"),
        ("Expense Distribution",   "Spending breakdown by category — see where money actually goes."),
        ("Subscription Tracker",   "Every subscription with renewal dates and annual cost."),
        ("Sinking Funds",          "Save a little each month toward big planned expenses."),
        ("Savings Goals",          "Named goals with target amounts and projected reach dates."),
        ("Debt Calculator",        "Snowball vs. avalanche — which pays off debt fastest?"),
        ("Net Worth",              "Total assets minus total debts. Updated monthly."),
        ("Investment Forecast",    "Compound growth projection with your numbers."),
        ("Tax Prep Summary",       "Pulls potential deductible categories from your spending log."),
        ("No-Spending Challenge",  "30-day challenge with daily checkboxes and streak counter."),
    ]

    for i, (tab, desc) in enumerate(tab_guide):
        row = r2 + 3 + i
        ws.row_dimensions[row].height = 18
        sn = 'data_cell' if i % 2 == 0 else 'data_alt'
        tc = ws.cell(row=row, column=5)
        tc.value = tab
        tc.style = sn
        tc.font = Font(name=FONT_BODY, size=10, bold=True, color=COLORS['primary'])
        tc.alignment = Alignment(vertical='center')
        dc = ws.cell(row=row, column=6)
        dc.value = desc
        dc.style = sn
        dc.alignment = Alignment(vertical='center')
        ws.merge_cells(start_row=row, start_column=6, end_row=row, end_column=11)


# ═══════════════════════════════════════════════════════════════
# SETUP
# ═══════════════════════════════════════════════════════════════

def build_setup(wb, ws):
    setup_sheet(ws, "Setup",
        subtitle="Fill this in first — your entries here flow through the entire workbook.",
        active_tab="Setup", sections=sidebar("Setup"))
    W(ws, {'D': 2, 'E': 28, 'F': 32, 'G': 28, 'H': 2})

    # ── Personal Info ──────────────────────────────────────────
    r = 6
    hdr(ws, r, 5, "YOUR DETAILS", end_col=8)

    fields = [
        ("Your Name",         "e.g. Sarah Mitchell",         ""),
        ("Year",              "2025",                         ""),
        ("Currency Symbol",   "$",                            "Change to £, €, etc. if needed"),
        ("Pay Frequency",     "Bi-Weekly",                    ""),
        ("Budget Start Month","January",                      ""),
    ]

    for i, (label, default, note) in enumerate(fields):
        row = r + 1 + i
        ws.row_dimensions[row].height = 22

        lc = ws.cell(row=row, column=5)
        lc.value = label
        lc.style = 'data_cell'
        lc.font = Font(name=FONT_BODY, size=10, bold=True, color=COLORS['primary'])
        lc.alignment = Alignment(vertical='center')

        vc = ws.cell(row=row, column=6)
        vc.value = default
        vc.style = 'data_alt'
        vc.alignment = Alignment(vertical='center')

        if note:
            nc = ws.cell(row=row, column=7)
            nc.value = note
            nc.style = 'note_cell'
            nc.alignment = Alignment(vertical='center')

    add_dropdown(ws, 'F9', FREQ_OPTIONS)
    add_dropdown(ws, 'F10', MONTHS)

    # ── Income Sources ─────────────────────────────────────────
    r2 = r + len(fields) + 3
    add_gold_rule(ws, row=r2, start_col=5, end_col=10)
    hdr(ws, r2 + 1, 5, "INCOME SOURCES", end_col=10)
    col_hdr(ws, r2 + 2, 5, ["Income Source", "Type", "Monthly Amount", "Notes"])

    income_sample = [
        ("Primary Salary",      "Salary",    4500, "After tax"),
        ("Freelance Work",      "Contract",   800, "Varies monthly"),
        ("Investment Dividends","Investment", 125, "Quarterly — enter monthly avg"),
    ]
    for i, row_data in enumerate(income_sample):
        row = r2 + 3 + i
        drow(ws, row, 5, row_data, alt=(i % 2 == 1))
        money_fmt(ws, row, 7)
        add_dropdown(ws, f'{get_column_letter(6)}{row}', INCOME_CATS)

    total_r = r2 + 3 + len(income_sample)
    trow(ws, total_r, 5, ["Total Monthly Income",
                           "",
                           f"=SUM(G{r2+3}:G{total_r-1})",
                           ""])

    # ── Expense Categories ─────────────────────────────────────
    r3 = total_r + 3
    add_gold_rule(ws, row=r3, start_col=5, end_col=10)
    hdr(ws, r3 + 1, 5, "EXPENSE CATEGORIES  (edit to match your life)", end_col=10)
    note = ws.cell(row=r3 + 2, column=5)
    note.value = ("These categories appear as dropdowns throughout the workbook. "
                  "Add, remove, or rename them here to match how you actually spend money.")
    note.style = 'note_cell'
    ws.merge_cells(start_row=r3 + 2, start_column=5, end_row=r3 + 2, end_column=10)

    col_hdr(ws, r3 + 3, 5, ["Category", "Include?"])
    for i, cat in enumerate(EXPENSE_CATS):
        row = r3 + 4 + i
        drow(ws, row, 5, [cat, "Yes"], alt=(i % 2 == 1))
        add_dropdown(ws, f'F{row}', ["Yes", "No"])


# ═══════════════════════════════════════════════════════════════
# BANK ACCOUNTS
# ═══════════════════════════════════════════════════════════════

def build_bank_accounts(wb, ws):
    setup_sheet(ws, "Bank Accounts",
        subtitle="A snapshot of every account you own — checking, savings, credit cards, and more.",
        active_tab="Bank Accounts", sections=sidebar("Bank Accounts"))
    W(ws, {'D': 26, 'E': 22, 'F': 16, 'G': 16, 'H': 16, 'I': 30})

    r = 6
    hdr(ws, r, 4, "YOUR ACCOUNTS", end_col=9)
    col_hdr(ws, r + 1, 4, ["Account Name", "Institution", "Type", "Current Balance", "Last Updated", "Notes"])

    sample = [
        ("Primary Checking",  "Chase Bank",    "Checking",    3250.00, "2025-01-01", "Direct deposit account"),
        ("Emergency Savings", "Ally Bank",     "Savings",     8500.00, "2025-01-01", "Goal: 6 months expenses"),
        ("Visa Rewards Card", "Capital One",   "Credit Card", -1250.00,"2025-01-01", "Pay in full each month"),
        ("HSA Account",       "Fidelity",      "HSA",          980.00, "2025-01-01", "Medical expenses only"),
    ]
    for i, row_data in enumerate(sample):
        row = r + 2 + i
        drow(ws, row, 4, row_data, alt=(i % 2 == 1))
        money_fmt(ws, row, 7)
        add_dropdown(ws, f'F{row}', ACCT_TYPES)

    # 10 blank input rows
    for i in range(len(sample), len(sample) + 10):
        row = r + 2 + i
        drow(ws, row, 4, ["", "", "", "", "", ""], alt=(i % 2 == 1))
        add_dropdown(ws, f'F{row}', ACCT_TYPES)

    last_data = r + 2 + len(sample) + 10 - 1
    total_r = last_data + 1
    trow(ws, total_r, 4, ["Total Net Worth (Accounts)",
                           "", "",
                           f"=SUM(G{r+2}:G{last_data})",
                           "", ""])
    money_fmt(ws, total_r, 7)

    add_gold_rule(ws, row=total_r + 2, start_col=4, end_col=9)
    note = ws.cell(row=total_r + 3, column=4)
    note.value = ("Tip: Enter credit card balances as negative numbers — they are debts, not assets. "
                  "The total above reflects your true net position across all accounts.")
    note.style = 'note_cell'
    ws.merge_cells(start_row=total_r + 3, start_column=4, end_row=total_r + 4, end_column=9)


# ═══════════════════════════════════════════════════════════════
# RECURRING TRANSACTIONS
# ═══════════════════════════════════════════════════════════════

def build_recurring_transactions(wb, ws):
    setup_sheet(ws, "Recurring Transactions",
        subtitle="Fixed bills that repeat every month. Enter once and refer back whenever needed.",
        active_tab="Recurring Transactions", sections=sidebar("Recurring Transactions"))
    W(ws, {'D': 28, 'E': 20, 'F': 14, 'G': 14, 'H': 12, 'I': 14, 'J': 22, 'K': 14})

    r = 6
    hdr(ws, r, 4, "RECURRING BILLS & FIXED EXPENSES", end_col=11)
    col_hdr(ws, r + 1, 4,
            ["Description", "Category", "Monthly Amt", "Frequency", "Due Day", "Status", "Account", "Annual Total"])

    sample = [
        ("Rent / Mortgage",   "Housing",       1800,   "Monthly",    1,  "Paid",    "Primary Checking"),
        ("Electricity",       "Utilities",       95,   "Monthly",   15,  "Paid",    "Primary Checking"),
        ("Natural Gas",       "Utilities",       55,   "Monthly",   18,  "Paid",    "Primary Checking"),
        ("Internet",          "Utilities",       65,   "Monthly",   20,  "Paid",    "Primary Checking"),
        ("Car Insurance",     "Insurance",      125,   "Monthly",    5,  "Paid",    "Primary Checking"),
        ("Health Insurance",  "Insurance",      280,   "Monthly",    1,  "Paid",    "Primary Checking"),
        ("Netflix",           "Subscriptions",   15.99,"Monthly",   12,  "Paid",    "Visa Rewards Card"),
        ("Spotify",           "Subscriptions",    9.99,"Monthly",   18,  "Paid",    "Visa Rewards Card"),
        ("Car Payment",       "Debt Payment",   385,   "Monthly",   22,  "Pending", "Primary Checking"),
        ("Gym Membership",    "Personal Care",   45,   "Monthly",    1,  "Paid",    "Visa Rewards Card"),
    ]

    for i, row_data in enumerate(sample):
        row = r + 2 + i
        desc, cat, amt, freq, due, status, acct = row_data
        annual = f"=IF(G{row}=\"Monthly\",F{row}*12,IF(G{row}=\"Bi-Weekly\",F{row}*26,IF(G{row}=\"Weekly\",F{row}*52,IF(G{row}=\"Quarterly\",F{row}*4,IF(G{row}=\"Semi-Annual\",F{row}*2,F{row})))))"
        drow(ws, row, 4, [desc, cat, amt, freq, due, status, acct, annual], alt=(i % 2 == 1))
        money_fmt(ws, row, 6)
        ws.cell(row=row, column=11).number_format = '"$"#,##0.00'
        add_dropdown(ws, f'E{row}', EXPENSE_CATS)
        add_dropdown(ws, f'G{row}', FREQ_OPTIONS)
        add_dropdown(ws, f'I{row}', STATUS_OPTIONS)

    for i in range(len(sample), len(sample) + 15):
        row = r + 2 + i
        annual = f"=IF(G{row}=\"Monthly\",F{row}*12,IF(G{row}=\"Bi-Weekly\",F{row}*26,IF(G{row}=\"Weekly\",F{row}*52,IF(G{row}=\"Quarterly\",F{row}*4,IF(G{row}=\"Semi-Annual\",F{row}*2,F{row})))))"
        drow(ws, row, 4, ["", "", "", "", "", "", "", annual], alt=(i % 2 == 1))
        add_dropdown(ws, f'E{row}', EXPENSE_CATS)
        add_dropdown(ws, f'G{row}', FREQ_OPTIONS)
        add_dropdown(ws, f'I{row}', STATUS_OPTIONS)

    last_data = r + 2 + len(sample) + 15 - 1
    total_r = last_data + 1
    trow(ws, total_r, 4, ["Total Monthly Recurring", "",
                           f"=SUM(F{r+2}:F{last_data})",
                           "", "", "", "",
                           f"=SUM(K{r+2}:K{last_data})"])

    add_status_formatting(ws, f'I{r+2}:I{last_data}')


# ═══════════════════════════════════════════════════════════════
# PAYMENTS
# ═══════════════════════════════════════════════════════════════

def build_payments(wb, ws):
    setup_sheet(ws, "Payments",
        subtitle="One-time and irregular payments — track what's due, what's paid, and what's coming.",
        active_tab="Payments", sections=sidebar("Payments"))
    W(ws, {'D': 14, 'E': 28, 'F': 14, 'G': 20, 'H': 14, 'I': 18, 'J': 30})

    r = 6
    hdr(ws, r, 4, "PAYMENT LOG", end_col=10)
    col_hdr(ws, r + 1, 4,
            ["Due Date", "Payee / Description", "Amount", "Category", "Status", "Payment Method", "Notes"])

    sample = [
        ("2025-01-15", "Dr. Smith — Dental Cleaning", 180,  "Healthcare",    "Paid",     "Visa",   "Annual checkup"),
        ("2025-02-01", "Vehicle Registration",         95,   "Transportation","Upcoming", "Online", "Due Feb 1"),
        ("2025-03-15", "Accountant — Tax Prep",        350,  "Education",     "Upcoming", "Check",  "File by April 15"),
        ("2025-04-01", "Home Warranty Renewal",        450,  "Home Maintenance","Upcoming","Online","Annual premium"),
        ("2025-06-01", "Vet — Annual Exam",            220,  "Pets",          "Upcoming", "Credit", "Both cats"),
    ]

    for i, row_data in enumerate(sample):
        row = r + 2 + i
        drow(ws, row, 4, row_data, alt=(i % 2 == 1))
        money_fmt(ws, row, 6)
        add_dropdown(ws, f'G{row}', EXPENSE_CATS)
        add_dropdown(ws, f'H{row}', STATUS_OPTIONS)

    for i in range(len(sample), len(sample) + 20):
        row = r + 2 + i
        drow(ws, row, 4, ["", "", "", "", "", "", ""], alt=(i % 2 == 1))
        add_dropdown(ws, f'G{row}', EXPENSE_CATS)
        add_dropdown(ws, f'H{row}', STATUS_OPTIONS)

    last_data = r + 2 + len(sample) + 20 - 1
    add_status_formatting(ws, f'H{r+2}:H{last_data}')

    total_r = last_data + 1
    trow(ws, total_r, 4, ["Total Payments Logged", "",
                           f"=SUM(F{r+2}:F{last_data})",
                           "", "", "", ""])


# ═══════════════════════════════════════════════════════════════
# VARIABLE TRANSACTIONS
# ═══════════════════════════════════════════════════════════════

def build_variable_transactions(wb, ws):
    setup_sheet(ws, "Variable Transactions",
        subtitle="Your complete spending log. Every purchase you make goes here. Monthly budget tabs pull from this.",
        active_tab="Variable Transactions", sections=sidebar("Variable Transactions"))
    W(ws, {'D': 14, 'E': 32, 'F': 20, 'G': 14, 'H': 20, 'I': 16, 'J': 28})

    r = 5
    hdr(ws, r, 4, "SPENDING LOG  —  add every purchase here", end_col=10)
    col_hdr(ws, r + 1, 4,
            ["Date", "Description", "Category", "Amount", "Account", "Month", "Notes"])

    sample = [
        ("2025-01-03", "Whole Foods Market",        "Groceries",      87.50, "Primary Checking", "January", "Weekly shop"),
        ("2025-01-05", "Shell Gas Station",         "Transportation", 48.20, "Primary Checking", "January", ""),
        ("2025-01-07", "The Oak Table — Dinner",    "Dining Out",     74.00, "Visa Rewards Card","January", "Anniversary dinner"),
        ("2025-01-09", "Target",                    "Personal Care",  41.35, "Visa Rewards Card","January", ""),
        ("2025-01-12", "Amazon — Kindle books",     "Entertainment",  28.99, "Visa Rewards Card","January", "3 books"),
        ("2025-01-15", "CVS Pharmacy",              "Healthcare",     22.50, "Primary Checking", "January", "Prescriptions"),
        ("2025-01-18", "HomeDepot",                 "Home Maintenance",67.80,"Primary Checking", "January", "Light fixtures"),
        ("2025-01-22", "Trader Joe's",              "Groceries",      64.20, "Primary Checking", "January", ""),
        ("2025-01-25", "Uber",                      "Transportation", 18.40, "Visa Rewards Card","January", "Airport pickup"),
        ("2025-01-28", "Goodwill donation",         "Gifts & Donations",40.00,"Primary Checking","January","Clothing donation"),
    ]

    data_start = r + 2
    for i, row_data in enumerate(sample):
        row = data_start + i
        drow(ws, row, 4, row_data, alt=(i % 2 == 1))
        money_fmt(ws, row, 7)
        add_dropdown(ws, f'F{row}', EXPENSE_CATS)
        add_dropdown(ws, f'I{row}', MONTHS)

    for i in range(len(sample), len(sample) + 200):
        row = data_start + i
        drow(ws, row, 4, ["", "", "", "", "", "", ""], alt=(i % 2 == 1))
        add_dropdown(ws, f'F{row}', EXPENSE_CATS)
        add_dropdown(ws, f'I{row}', MONTHS)

    add_data_bars(ws, f'G{data_start}:G{data_start + len(sample) + 199}', color=COLORS['accent'])

    # Running total banner
    last_data = data_start + len(sample) + 199
    total_r = last_data + 1
    trow(ws, total_r, 4, ["Total Logged", "", "",
                           f"=SUM(G{data_start}:G{last_data})",
                           "", "", ""])
    money_fmt(ws, total_r, 7)


# ═══════════════════════════════════════════════════════════════
# QUICK ENTRY LOG
# ═══════════════════════════════════════════════════════════════

def build_quick_entry_log(wb, ws):
    setup_sheet(ws, "Quick Entry Log",
        subtitle="The fastest way to record a purchase. Stripped down to just what you need.",
        active_tab="Quick Entry Log", sections=sidebar("Quick Entry Log"))
    W(ws, {'D': 14, 'E': 36, 'F': 14, 'G': 22, 'H': 16, 'I': 2})

    r = 5
    note = ws.cell(row=r, column=4)
    note.value = ("  Use this tab for quick daily entry. "
                  "Transfer to Variable Transactions weekly for the full budget picture.")
    note.style = 'note_cell'
    note.alignment = Alignment(vertical='center', wrap_text=True)
    ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=8)
    ws.row_dimensions[r].height = 28

    r2 = r + 2
    hdr(ws, r2, 4, "QUICK ENTRY", end_col=8)
    col_hdr(ws, r2 + 1, 4, ["Date", "Description", "Amount", "Category", "Month"])

    sample = [
        ("2025-01-03", "Coffee + pastry",   6.50,  "Dining Out",    "January"),
        ("2025-01-04", "Gas station",       52.00, "Transportation","January"),
        ("2025-01-05", "Pharmacy",          18.75, "Healthcare",    "January"),
    ]

    data_start = r2 + 2
    for i, row_data in enumerate(sample):
        row = data_start + i
        drow(ws, row, 4, row_data, alt=(i % 2 == 1))
        money_fmt(ws, row, 6)
        add_dropdown(ws, f'G{row}', EXPENSE_CATS)
        add_dropdown(ws, f'H{row}', MONTHS)

    for i in range(len(sample), len(sample) + 100):
        row = data_start + i
        drow(ws, row, 4, ["", "", "", "", ""], alt=(i % 2 == 1))
        add_dropdown(ws, f'G{row}', EXPENSE_CATS)
        add_dropdown(ws, f'H{row}', MONTHS)

    last_data = data_start + len(sample) + 99
    add_data_bars(ws, f'F{data_start}:F{last_data}', color=COLORS['accent'])

    total_r = last_data + 1
    trow(ws, total_r, 4, ["Total Quick Entries", "",
                           f"=SUM(F{data_start}:F{last_data})",
                           "", ""])
    money_fmt(ws, total_r, 6)

    # Weekly total helper
    r3 = total_r + 3
    add_gold_rule(ws, row=r3, start_col=4, end_col=8)
    hdr(ws, r3 + 1, 4, "WEEKLY TOTALS  (by category)", end_col=8)
    col_hdr(ws, r3 + 2, 4, ["Category", "This Week Total"])
    spot_cats = ["Groceries", "Dining Out", "Transportation", "Entertainment", "Personal Care"]
    for i, cat in enumerate(spot_cats):
        row = r3 + 3 + i
        drow(ws, row, 4, [cat,
                           f'=SUMIF(G{data_start}:G{last_data},D{row},F{data_start}:F{last_data})'],
             alt=(i % 2 == 1))
        money_fmt(ws, row, 5)
