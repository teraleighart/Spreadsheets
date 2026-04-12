"""
Dashboard tabs:
  All-in-One Dashboard, Annual Totals, Year in Review,
  Automated Calendar, Paycheck Dashboard.
"""
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import BarChart, LineChart, DoughnutChart, Reference
from openpyxl.utils import get_column_letter

from styling import (
    COLORS, FONT_DISPLAY, FONT_BODY, FONT_MONO,
    setup_sheet, add_gold_rule, add_kpi_card, style_chart,
    add_dropdown,
)
from constants import (
    MONTHS, EXPENSE_CATS, INCOME_CATS, sidebar,
    MTH_INCOME_TOTAL_ROW, MTH_EXPENSE_TOTAL_ROW,
)


def _W(ws, widths):
    for col, w in widths.items():
        ws.column_dimensions[col].width = w


def _sec(ws, row, col, text, end_col=None):
    c = ws.cell(row=row, column=col)
    c.value = f"  {text}"
    c.style = 'section_header'
    if end_col:
        ws.merge_cells(start_row=row, start_column=col, end_row=row, end_column=end_col)


def _col_hdr(ws, row, col, labels):
    for i, lbl in enumerate(labels):
        c = ws.cell(row=row, column=col + i)
        c.value = lbl
        c.style = 'column_header'


def _drow(ws, row, col, vals, alt=False, fmt=None):
    sn = 'data_alt' if alt else 'data_cell'
    for i, v in enumerate(vals):
        c = ws.cell(row=row, column=col + i)
        c.value = v
        c.style = sn
        if isinstance(v, (int, float)) or (isinstance(v, str) and v.startswith('=')):
            c.alignment = Alignment(horizontal='right', vertical='center')
        if fmt and i < len(fmt) and fmt[i]:
            c.number_format = fmt[i]


def _trow(ws, row, col, vals):
    for i, v in enumerate(vals):
        c = ws.cell(row=row, column=col + i)
        c.value = v
        c.style = 'total_row'
        if i == 0:
            c.alignment = Alignment(horizontal='left', vertical='center')
        elif isinstance(v, str) and v.startswith('='):
            c.number_format = '"$"#,##0.00'
            c.alignment = Alignment(horizontal='right', vertical='center')


# ═══════════════════════════════════════════════════════════════
# ALL-IN-ONE DASHBOARD
# ═══════════════════════════════════════════════════════════════

def build_all_in_one_dashboard(wb, ws):
    setup_sheet(ws, "All-in-One Dashboard",
        subtitle="Your complete financial picture — auto-updated from everything you've entered.",
        active_tab="All-in-One Dashboard", sections=sidebar("All-in-One Dashboard"))

    _W(ws, {'D': 14, 'E': 14, 'F': 14, 'G': 14, 'H': 14, 'I': 14,
            'J': 2, 'K': 14, 'L': 14, 'M': 14, 'N': 14, 'O': 14, 'P': 14})

    # ── KPI CARDS (row 7–9) ───────────────────────────────────
    # Annual Totals will be in rows 8–19 of the Annual Totals sheet
    # Income col E, Expenses col F, Net col G
    ytd_income   = "=SUM('Annual Totals'!E8:E19)"
    ytd_expenses = "=SUM('Annual Totals'!F8:F19)"
    ytd_net      = "=SUM('Annual Totals'!G8:G19)"
    ytd_rate     = f"=IF(SUM('Annual Totals'!E8:E19)>0,SUM('Annual Totals'!G8:G19)/SUM('Annual Totals'!E8:E19),0)"

    add_kpi_card(ws, 7, 4,  "Total Income YTD",   ytd_income,   fmt='"$"#,##0',
                 accent_color=COLORS['primary'])
    add_kpi_card(ws, 7, 8,  "Total Expenses YTD", ytd_expenses, fmt='"$"#,##0',
                 accent_color=COLORS['accent'])
    add_kpi_card(ws, 7, 12, "Net Savings YTD",    ytd_net,      fmt='"$"#,##0',
                 accent_color=COLORS['success'])
    add_kpi_card(ws, 7, 16, "Savings Rate",        ytd_rate,     fmt='0.0%',
                 accent_color=COLORS['gold'])

    # ── HIDDEN CHART DATA (rows 80–93) ────────────────────────
    # Annual Totals sheet rows 8–19 (Jan–Dec), cols E=Income, F=Expenses, G=Net
    # Mirror that data here for chart series references
    _col_hdr(ws, 80, 4, ["Month", "Income", "Expenses", "Net Savings"])
    for i, month in enumerate(MONTHS):
        row = 81 + i
        ws.cell(row=row, column=4).value = month
        ws.cell(row=row, column=5).value = f"='Annual Totals'!E{8 + i}"
        ws.cell(row=row, column=6).value = f"='Annual Totals'!F{8 + i}"
        ws.cell(row=row, column=7).value = f"='Annual Totals'!G{8 + i}"

    # Category spend data (rows 95–113) — top categories from Variable Transactions
    _col_hdr(ws, 95, 4, ["Category", "YTD Actual"])
    for i, cat in enumerate(EXPENSE_CATS):
        row = 96 + i
        ws.cell(row=row, column=4).value = cat
        ws.cell(row=row, column=5).value = (
            f"=SUMIF('Variable Transactions'!$F:$F,D{row},'Variable Transactions'!$G:$G)"
        )

    # ── CHART 1: Income vs Expenses Bar ───────────────────────
    bar = BarChart()
    bar.type = "col"
    bar.grouping = "clustered"
    cats = Reference(ws, min_col=4, min_row=81, max_row=92)
    income_data = Reference(ws, min_col=5, min_row=80, max_row=92)
    expense_data = Reference(ws, min_col=6, min_row=80, max_row=92)
    bar.add_data(income_data, titles_from_data=True)
    bar.add_data(expense_data, titles_from_data=True)
    bar.set_categories(cats)
    style_chart(bar, "Monthly Income vs. Expenses", chart_type='bar', width=18, height=10)
    ws.add_chart(bar, "D12")

    # ── CHART 2: Net Savings Line ─────────────────────────────
    line = LineChart()
    net_data = Reference(ws, min_col=7, min_row=80, max_row=92)
    line.add_data(net_data, titles_from_data=True)
    line.set_categories(cats)
    style_chart(line, "Monthly Net Savings Trend", chart_type='line', width=18, height=10)
    ws.add_chart(line, "L12")

    # ── CHART 3: Expense Category Donut ───────────────────────
    donut = DoughnutChart()
    cat_labels = Reference(ws, min_col=4, min_row=96, max_row=114)
    cat_data   = Reference(ws, min_col=5, min_row=95, max_row=114)
    donut.add_data(cat_data, titles_from_data=True)
    donut.set_categories(cat_labels)
    style_chart(donut, "Spending by Category", chart_type='donut', width=14, height=10)
    ws.add_chart(donut, "D29")

    # ── CHART 4: Income vs Expenses Line (trend) ──────────────
    trend = LineChart()
    inc2 = Reference(ws, min_col=5, min_row=80, max_row=92)
    exp2 = Reference(ws, min_col=6, min_row=80, max_row=92)
    trend.add_data(inc2, titles_from_data=True)
    trend.add_data(exp2, titles_from_data=True)
    trend.set_categories(cats)
    style_chart(trend, "Income vs. Expenses Trend", chart_type='line', width=14, height=10)
    ws.add_chart(trend, "L29")

    # ── QUICK STATS TABLE (row 44) ────────────────────────────
    add_gold_rule(ws, row=44, start_col=4, end_col=13)
    _sec(ws, 45, 4, "QUICK STATS", end_col=13)
    _col_hdr(ws, 46, 4, ["Metric", "Value"])

    quick_stats = [
        ("Highest spending month",
         "=INDEX('Annual Totals'!D8:D19,MATCH(MAX('Annual Totals'!F8:F19),'Annual Totals'!F8:F19,0))"),
        ("Lowest spending month",
         "=INDEX('Annual Totals'!D8:D19,MATCH(MIN(IF('Annual Totals'!F8:F19>0,'Annual Totals'!F8:F19)),IF('Annual Totals'!F8:F19>0,'Annual Totals'!F8:F19),0))"),
        ("Largest expense category",
         "=INDEX('Variable Transactions'!F:F,MATCH(MAX(COUNTIF('Variable Transactions'!F:F,'Variable Transactions'!F:F)),'Variable Transactions'!F:F,0))"),
        ("Months where you saved money",
         "=COUNTIF('Annual Totals'!G8:G19,\">0\")"),
        ("Average monthly savings",
         "=IFERROR(AVERAGEIF('Annual Totals'!G8:G19,\">0\",'Annual Totals'!G8:G19),0)"),
    ]

    for i, (label, formula) in enumerate(quick_stats):
        row = 47 + i
        alt = (i % 2 == 1)
        lc = ws.cell(row=row, column=4)
        lc.value = label
        lc.style = 'data_alt' if alt else 'data_cell'
        lc.alignment = Alignment(vertical='center')
        vc = ws.cell(row=row, column=5)
        vc.value = formula
        vc.style = 'data_alt' if alt else 'data_cell'
        vc.alignment = Alignment(horizontal='right', vertical='center')
        if i == 4:
            vc.number_format = '"$"#,##0.00'


# ═══════════════════════════════════════════════════════════════
# ANNUAL TOTALS
# ═══════════════════════════════════════════════════════════════

def build_annual_totals(wb, ws):
    setup_sheet(ws, "Annual Totals",
        subtitle="Your complete year at a glance — income, expenses, and net savings by month.",
        active_tab="Annual Totals", sections=sidebar("Annual Totals"))
    _W(ws, {'D': 18, 'E': 16, 'F': 16, 'G': 16, 'H': 14, 'I': 14})

    r = 6
    _sec(ws, r, 4, "YEAR AT A GLANCE", end_col=9)
    _col_hdr(ws, r + 1, 4,
             ["Month", "Total Income", "Total Expenses", "Net Savings", "Savings Rate", "Status"])

    for i, month in enumerate(MONTHS):
        row = r + 2 + i   # rows 8–19

        # Cross-sheet refs to each monthly tab's total rows
        income_f   = f"='{month}'!F{MTH_INCOME_TOTAL_ROW}"
        expenses_f = f"='{month}'!F{MTH_EXPENSE_TOTAL_ROW}"
        net_f      = f"=E{row}-F{row}"
        rate_f     = f"=IF(E{row}>0,G{row}/E{row},0)"
        status_f   = f"=IF(G{row}>0,\"Surplus\",IF(G{row}=0,\"Breakeven\",\"Deficit\"))"

        alt = (i % 2 == 1)
        _drow(ws, row, 4, [month, income_f, expenses_f, net_f, rate_f, status_f],
              alt=alt,
              fmt=[None, '"$"#,##0.00', '"$"#,##0.00', '"$"#,##0.00', '0.0%', None])

    total_r = r + 2 + 12   # row 20
    _trow(ws, total_r, 4, [
        "ANNUAL TOTALS",
        f"=SUM(E{r+2}:E{r+13})",
        f"=SUM(F{r+2}:F{r+13})",
        f"=SUM(G{r+2}:G{r+13})",
        f"=IF(E{total_r}>0,G{total_r}/E{total_r},0)",
        "",
    ])
    ws.cell(row=total_r, column=8).number_format = '0.0%'

    # Status colour coding
    from openpyxl.styles.differential import DifferentialStyle
    from openpyxl.formatting.rule import Rule
    surplus_s = DifferentialStyle(
        fill=PatternFill(start_color=COLORS['success'], end_color=COLORS['success'], fill_type='solid'))
    deficit_s = DifferentialStyle(
        fill=PatternFill(start_color=COLORS['danger'], end_color=COLORS['danger'], fill_type='solid'))
    first = f'I{r+2}'
    cell_rng = f'I{r+2}:I{r+13}'
    ws.conditional_formatting.add(cell_rng, Rule(
        type='containsText', operator='containsText', text='Surplus',
        dxf=surplus_s, formula=[f'NOT(ISERROR(SEARCH("Surplus",{first})))']))
    ws.conditional_formatting.add(cell_rng, Rule(
        type='containsText', operator='containsText', text='Deficit',
        dxf=deficit_s, formula=[f'NOT(ISERROR(SEARCH("Deficit",{first})))']))

    # Sparkline-like data bars on Net Savings (col G)
    from styling import add_data_bars
    add_data_bars(ws, f'G{r+2}:G{r+13}', color=COLORS['primary'])


# ═══════════════════════════════════════════════════════════════
# YEAR IN REVIEW
# ═══════════════════════════════════════════════════════════════

def build_year_in_review(wb, ws):
    setup_sheet(ws, "Year in Review",
        subtitle="Your financial highlights for the year — the numbers worth celebrating (and learning from).",
        active_tab="Year in Review", sections=sidebar("Year in Review"))
    _W(ws, {'D': 32, 'E': 22, 'F': 22, 'G': 2})

    # Annual Totals income/expense/net in E8:G19
    AT_E = "'Annual Totals'!E8:E19"
    AT_F = "'Annual Totals'!F8:F19"
    AT_G = "'Annual Totals'!G8:G19"
    AT_D = "'Annual Totals'!D8:D19"

    highlights = [
        # (label, formula, format)
        ("Best saving month",
         f"=IFERROR(INDEX({AT_D},MATCH(MAX({AT_G}),{AT_G},0)),\"—\")", None),
        ("Most money saved (single month)",
         f"=IFERROR(MAX({AT_G}),0)", '"$"#,##0.00'),
        ("Highest spending month",
         f"=IFERROR(INDEX({AT_D},MATCH(MAX({AT_F}),{AT_F},0)),\"—\")", None),
        ("Most you spent in a month",
         f"=IFERROR(MAX({AT_F}),0)", '"$"#,##0.00'),
        ("Total income this year",
         f"=SUM({AT_E})", '"$"#,##0.00'),
        ("Total expenses this year",
         f"=SUM({AT_F})", '"$"#,##0.00'),
        ("Total net savings this year",
         f"=SUM({AT_G})", '"$"#,##0.00'),
        ("Average monthly savings rate",
         f"=IFERROR(AVERAGEIF({AT_G},\">0\",{AT_G})/AVERAGEIF({AT_E},\">0\",{AT_E}),0)", '0.0%'),
        ("Months you ran a surplus",
         f"=COUNTIF({AT_G},\">0\")", '0'),
        ("Months you ran a deficit",
         f"=COUNTIF({AT_G},\"<0\")", '0'),
        ("Biggest spending category (YTD)",
         "=IFERROR(INDEX('Variable Transactions'!F:F,MATCH(LARGE(COUNTIF('Variable Transactions'!F:F,'Variable Transactions'!F:F),1),COUNTIF('Variable Transactions'!F:F,'Variable Transactions'!F:F),0)),\"—\")",
         None),
        ("Total transactions logged",
         "=COUNTA('Variable Transactions'!D6:D5000)-1", '0'),
    ]

    r = 6
    _sec(ws, r, 4, "YOUR YEAR IN REVIEW", end_col=6)
    _col_hdr(ws, r + 1, 4, ["What We're Looking At", "Your Number"])

    for i, (label, formula, fmt) in enumerate(highlights):
        row = r + 2 + i
        ws.row_dimensions[row].height = 22
        alt = (i % 2 == 1)

        lc = ws.cell(row=row, column=4)
        lc.value = label
        lc.style = 'data_alt' if alt else 'data_cell'
        lc.alignment = Alignment(vertical='center')

        vc = ws.cell(row=row, column=5)
        vc.value = formula
        vc.style = 'data_alt' if alt else 'data_cell'
        vc.alignment = Alignment(horizontal='right', vertical='center')
        if fmt:
            vc.number_format = fmt

    # Motivational note
    r2 = r + 2 + len(highlights) + 2
    add_gold_rule(ws, row=r2, start_col=4, end_col=6)
    note = ws.cell(row=r2 + 1, column=4)
    note.value = ("Every number here is calculated automatically from what you've entered in your monthly tabs "
                  "and Variable Transactions log. The more consistently you track, the more accurate this picture becomes.")
    note.style = 'note_cell'
    ws.merge_cells(start_row=r2 + 1, start_column=4, end_row=r2 + 3, end_column=6)
    ws.row_dimensions[r2 + 1].height = 40


# ═══════════════════════════════════════════════════════════════
# AUTOMATED CALENDAR
# ═══════════════════════════════════════════════════════════════

def build_automated_calendar(wb, ws):
    setup_sheet(ws, "Automated Calendar",
        subtitle="Bill due dates mapped by day of the month — see what's coming before it sneaks up on you.",
        active_tab="Automated Calendar", sections=sidebar("Automated Calendar"))
    _W(ws, {'D': 10, 'E': 22, 'F': 22, 'G': 22, 'H': 22, 'I': 22, 'J': 22, 'K': 22})

    r = 6
    _sec(ws, r, 4, "MONTHLY BILL CALENDAR  —  due dates from Recurring Transactions", end_col=11)

    # Day-of-month grid: rows = weeks, cols = days
    day_headers = ["Day", "Bill / Payee", "Amount", "Category", "Account", "Status", "Frequency", "Notes"]
    _col_hdr(ws, r + 1, 4, day_headers)

    # Pull from Recurring Transactions (rows 8–32 of that sheet, col H = Due Day)
    # We list days 1–31 and VLOOKUP/INDEX-MATCH to find recurring items due on that day
    for day in range(1, 32):
        row = r + 1 + day
        ws.row_dimensions[row].height = 18
        alt = (day % 2 == 1)

        # Description: INDEX-MATCH from Recurring Transactions where Due Day = this day
        desc_f = (f"=IFERROR(INDEX('Recurring Transactions'!D:D,"
                  f"MATCH({day},'Recurring Transactions'!H:H,0)),\"\")")
        amt_f  = (f"=IFERROR(INDEX('Recurring Transactions'!F:F,"
                  f"MATCH({day},'Recurring Transactions'!H:H,0)),\"\")")
        cat_f  = (f"=IFERROR(INDEX('Recurring Transactions'!E:E,"
                  f"MATCH({day},'Recurring Transactions'!H:H,0)),\"\")")
        acct_f = (f"=IFERROR(INDEX('Recurring Transactions'!J:J,"
                  f"MATCH({day},'Recurring Transactions'!H:H,0)),\"\")")
        stat_f = (f"=IFERROR(INDEX('Recurring Transactions'!I:I,"
                  f"MATCH({day},'Recurring Transactions'!H:H,0)),\"\")")
        freq_f = (f"=IFERROR(INDEX('Recurring Transactions'!G:G,"
                  f"MATCH({day},'Recurring Transactions'!H:H,0)),\"\")")

        _drow(ws, row, 4,
              [day, desc_f, amt_f, cat_f, acct_f, stat_f, freq_f, ""],
              alt=alt,
              fmt=[None, None, '"$"#,##0.00', None, None, None, None, None])


# ═══════════════════════════════════════════════════════════════
# PAYCHECK DASHBOARD
# ═══════════════════════════════════════════════════════════════

def build_paycheck_dashboard(wb, ws):
    setup_sheet(ws, "Paycheck Dashboard",
        subtitle="Track every paycheck and see your year-to-date income grow in real time.",
        active_tab="Paycheck Dashboard", sections=sidebar("Paycheck Dashboard"))
    _W(ws, {'D': 16, 'E': 20, 'F': 14, 'G': 16, 'H': 14, 'I': 14, 'J': 28})

    r = 6
    _sec(ws, r, 4, "PAYCHECK LOG", end_col=10)
    _col_hdr(ws, r + 1, 4,
             ["Pay Date", "Income Source", "Gross Amount", "Net (Take-Home)", "Month", "Period", "Notes"])

    sample = [
        ("2025-01-03",  "Primary Salary",   4807.69, 3680.00, "January",  "Pay Period 1", "Bi-weekly"),
        ("2025-01-17",  "Primary Salary",   4807.69, 3680.00, "January",  "Pay Period 2", "Bi-weekly"),
        ("2025-01-20",  "Freelance Work",    950.00,  950.00, "January",  "Invoice #201", "Client project"),
        ("2025-02-07",  "Primary Salary",   4807.69, 3680.00, "February", "Pay Period 3", "Bi-weekly"),
        ("2025-02-21",  "Primary Salary",   4807.69, 3680.00, "February", "Pay Period 4", "Bi-weekly"),
    ]

    data_start = r + 2
    for i, row_data in enumerate(sample):
        row = data_start + i
        _drow(ws, row, 4, row_data, alt=(i % 2 == 1),
              fmt=[None, None, '"$"#,##0.00', '"$"#,##0.00', None, None, None])
        add_dropdown(ws, f'H{row}', MONTHS)

    for i in range(len(sample), len(sample) + 50):
        row = data_start + i
        _drow(ws, row, 4, ["", "", "", "", "", "", ""], alt=(i % 2 == 1))
        add_dropdown(ws, f'H{row}', MONTHS)

    last_data = data_start + len(sample) + 49
    total_r = last_data + 1
    _trow(ws, total_r, 4, ["TOTAL YTD", "",
                            f"=SUM(F{data_start}:F{last_data})",
                            f"=SUM(G{data_start}:G{last_data})",
                            "", "", ""])

    # Monthly income summary
    r2 = total_r + 3
    add_gold_rule(ws, row=r2, start_col=4, end_col=10)
    _sec(ws, r2 + 1, 4, "INCOME BY MONTH", end_col=10)
    _col_hdr(ws, r2 + 2, 4, ["Month", "Gross Total", "Net Total", "# Paychecks"])

    for i, month in enumerate(MONTHS):
        row = r2 + 3 + i
        gross_f = (f"=SUMIF(H{data_start}:H{last_data},\"{month}\","
                   f"F{data_start}:F{last_data})")
        net_f   = (f"=SUMIF(H{data_start}:H{last_data},\"{month}\","
                   f"G{data_start}:G{last_data})")
        count_f = f"=COUNTIF(H{data_start}:H{last_data},\"{month}\")"
        _drow(ws, row, 4, [month, gross_f, net_f, count_f],
              alt=(i % 2 == 1),
              fmt=[None, '"$"#,##0.00', '"$"#,##0.00', '0'])
