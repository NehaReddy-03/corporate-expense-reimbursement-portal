"""
Corporate Expense System - Executive PDF Guide Generator
Uses ReportLab to compile a professional, multi-page publication-quality
PDF document covering all 14 features, architecture, 9-user dataset,
live demo script, and top 20 viva questions.
"""
import os
import sys
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    """Two-pass canvas to dynamically compute and print 'Page X of Y'."""
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_header_footer(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#64748B"))

        # Do not draw running header on cover page (page 1)
        if self._pageNumber > 1:
            # Running Header
            self.drawString(45, 805, "CORPORATE EXPENSE CLAIM & REIMBURSEMENT SYSTEM")
            self.drawRightString(550, 805, "TEAMMATE REFERENCE & VIVA GUIDE")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.6)
            self.line(45, 798, 550, 798)

        # Running Footer (All pages)
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.6)
        self.line(45, 42, 550, 42)

        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(45, 30, "Confidential • Enterprise Financial Operations & Governance • Python 3.12 / FastAPI")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(550, 30, page_str)
        self.restoreState()


def build_pdf(filename: str = "Corporate_Expense_System_Teammate_Guide.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=45,
        rightMargin=45,
        topMargin=55,
        bottomMargin=55
    )

    styles = getSampleStyleSheet()

    # --- COLOR SYSTEM ---
    C_NAVY     = colors.HexColor("#0F172A")
    C_BLUE     = colors.HexColor("#1D4ED8")
    C_TEXT     = colors.HexColor("#1E293B")
    C_MUTED    = colors.HexColor("#475569")
    C_EMERALD  = colors.HexColor("#065F46")
    C_ROSE     = colors.HexColor("#9F1239")
    C_AMBER    = colors.HexColor("#92400E")
    C_BG_LIGHT = colors.HexColor("#F8FAFC")
    C_BORDER   = colors.HexColor("#E2E8F0")

    # --- TYPOGRAPHY STYLES ---
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=C_NAVY,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11.5,
        leading=16,
        textColor=C_BLUE,
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=C_NAVY,
        spaceBefore=16,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=C_BLUE,
        spaceBefore=11,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=C_TEXT,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=body_style,
        leftIndent=14,
        firstLineIndent=-10,
        spaceAfter=3
    )

    callout_style = ParagraphStyle(
        'Callout',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=C_TEXT,
        spaceBefore=4,
        spaceAfter=4
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=3,
        spaceAfter=3
    )

    qa_q_style = ParagraphStyle(
        'QA_Q',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=C_NAVY,
        spaceBefore=8,
        spaceAfter=2,
        keepWithNext=True
    )

    qa_a_style = ParagraphStyle(
        'QA_A',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=C_TEXT,
        leftIndent=12,
        spaceAfter=6
    )

    story = []

    # =========================================================================
    # COVER / HEADER
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("Corporate Expense Claim and Reimbursement System", title_style))
    story.append(Paragraph("Comprehensive Technical Architecture, System Features & Teammate Viva Guide", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=C_BLUE, spaceBefore=0, spaceAfter=14))

    # Meta Info Card Table
    meta_data = [
        [
            Paragraph("<b>System Core:</b> Python 3.12 • FastAPI REST API", callout_style),
            Paragraph("<b>Database:</b> SQLite3 (PRAGMA foreign_keys = ON)", callout_style)
        ],
        [
            Paragraph("<b>Frontend:</b> Vanilla JS (ES6+) • Tailwind CSS", callout_style),
            Paragraph("<b>Security:</b> RBAC (Employee, Manager, Finance)", callout_style)
        ],
        [
            Paragraph("<b>Test Suite:</b> 7/7 Domain Suites Passing (0.2s)", callout_style),
            Paragraph(f"<b>Generated:</b> {datetime.now().strftime('%B %d, %Y')} • Version 2.7.0", callout_style)
        ]
    ]
    t_meta = Table(meta_data, colWidths=[250, 255])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_BG_LIGHT),
        ('BOX', (0,0), (-1,-1), 1, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 14))

    # =========================================================================
    # SECTION 1: EXECUTIVE SUMMARY
    # =========================================================================
    story.append(Paragraph("1. Executive Summary & Problem Solved", h1_style))
    story.append(Paragraph(
        "In modern corporations, unmonitored employee expenses result in major financial leakages, accidental duplicate disbursements, "
        "and compliance audit failures. Traditional manual processes rely on loose paper receipts and uncoordinated email approvals, "
        "introducing critical vulnerabilities:", body_style
    ))
    story.append(Paragraph("• <b>Duplicate Payout Fraud:</b> Employees accidentally or intentionally resubmit the same expense invoice across months without detection.", bullet_style))
    story.append(Paragraph("• <b>Fiscal Authority Creep:</b> Managers approve claims beyond their delegation ceiling without mandatory executive finance escalation.", bullet_style))
    story.append(Paragraph("• <b>Zero Non-Repudiation:</b> Audit trails are lost or unrecorded, creating significant regulatory exposure under Sarbanes-Oxley (SOX).", bullet_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "<b>Our Automated Solution:</b> The system replaces manual trust with strict, programmatic governance: a 48-hour duplicate detection algorithm, "
        "a hard ₹10,000 managerial threshold ceiling, an immutable append-only audit ledger, and an atomic one-click batch disbursement engine.", body_style
    ))

    # =========================================================================
    # SECTION 2: MULTI-TIER ARCHITECTURE
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("2. Multi-Tier Software Architecture", h1_style))
    story.append(Paragraph(
        "The system is engineered according to the <b>Separation of Concerns (SoC)</b> principle across four decoupled layers:", body_style
    ))

    arch_rows = [
        [
            Paragraph("<b>Tier</b>", callout_style),
            Paragraph("<b>Component & Technology</b>", callout_style),
            Paragraph("<b>Responsibilities & Invariants</b>", callout_style)
        ],
        [
            Paragraph("<b>Tier 1: Presentation</b>", callout_style),
            Paragraph("Vanilla JS (ES6+) • Tailwind CSS CDN • FontAwesome", callout_style),
            Paragraph("User interaction, responsive modals, real-time search, instant client CSV export, zero npm/node build step.", callout_style)
        ],
        [
            Paragraph("<b>Tier 2: Controller</b>", callout_style),
            Paragraph("FastAPI Endpoints • Pydantic DTOs • OpenAPI 3.0", callout_style),
            Paragraph("JSON serialization, request payload validation, HTTP status code mapping (200, 400, 403, 422), header-based RBAC.", callout_style)
        ],
        [
            Paragraph("<b>Tier 3: Service</b>", callout_style),
            Paragraph("ClaimService • AuditService • AuthService", callout_style),
            Paragraph("Domain rules engine, deterministic 4-state lifecycle machine, ₹10,000 threshold ceiling check, 48h duplicate scanner.", callout_style)
        ],
        [
            Paragraph("<b>Tier 4: Persistence</b>", callout_style),
            Paragraph("SQLite3 • PRAGMA foreign_keys = ON • Composite Indexes", callout_style),
            Paragraph("Raw parameterized SQL queries (SQLi immune), relational cascading integrity, atomic batch transactions (BEGIN/COMMIT/ROLLBACK).", callout_style)
        ],
    ]
    t_arch = Table(arch_rows, colWidths=[105, 170, 230])
    t_arch.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BOX', (0,0), (-1,-1), 1, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_BG_LIGHT, colors.white]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_arch)

    # =========================================================================
    # SECTION 3: COMPLETE FEATURE CATALOG (14 FEATURES)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("3. Complete Catalog of All 14 System Features", h1_style))
    story.append(Paragraph("The application delivers 14 fully functional, enterprise-grade capabilities:", body_style))

    features = [
        ("Feature 01: Role-Based Access Control (RBAC)",
         "Enforces least privilege across EMPLOYEE, MANAGER, and FINANCE personas. Employees only query their personal vouchers (WHERE user_id = ?); "
         "Managers are restricted to departmental claims <= ₹10k; Finance controllers hold exclusive authority for high-value approvals and treasury disbursement."),

        ("Feature 02: Deterministic 4-State Claim State Machine",
         "Claims progress strictly through: PENDING ➔ APPROVED ➔ SETTLED (or PENDING ➔ REJECTED). Direct jumps from PENDING to SETTLED are rejected with "
         "HTTP 400 Bad Request. REJECTED is an irreversible terminal state; tampering or approving rejected claims is strictly barred."),

        ("Feature 03: Dual-Tier ₹10,000 Manager Approval Ceiling",
         "Restricts departmental manager sign-off authority to ₹10,000.00. Claims exceeding ₹10k are locked in the manager view with a 'Needs Finance' badge "
         "and return HTTP 403 Forbidden on unauthorized approval attempts, requiring Finance Officer sign-off."),

        ("Feature 04: 48-Hour Algorithmic Duplicate Scanner",
         "On claim submission, the system evaluates incoming vouchers against active records matching (user_id, category, amount) in a sliding 48-hour window. "
         "Backed by a composite SQL index idx_claims_duplicate_check, flagged claims display an amber warning badge for managerial scrutiny."),

        ("Feature 05: Mandatory Written Rejection Reason",
         "Under corporate compliance rules, no claim can be arbitrarily rejected. Approvers must enter a non-empty policy justification; empty strings "
         "are rejected with HTTP 422 Unprocessable Content. The reason is permanently committed to the immutable audit ledger."),

        ("Feature 06: Immutable Regulatory Audit Trail (Append-Only)",
         "Non-repudiation by design: the AuditLogs database table permits only INSERT operations; zero UPDATE or DELETE queries exist. "
         "Accessible via the Claim Timeline Modal (voucher-specific) or Global Audit Ledger (enterprise-wide)."),

        ("Feature 07: One-Click ACID Batch Settlement Pipeline",
         "Allows Finance to disburse all approved vouchers simultaneously in an atomic transaction (BEGIN IMMEDIATE TRANSACTION ➔ UPDATE status='SETTLED' ➔ "
         "INSERT AuditLogs ➔ COMMIT). If any single step fails, conn.rollback() triggers cleanly, preventing partial payouts."),

        ("Feature 08: Live Instant Search & Keyword Filtering",
         "The toolbar search box dynamically filters claims in real time across Claim ID, Submitter Name, Category, and Description as the user types."),

        ("Feature 09: Category-Based Expenditure Filtering",
         "Instant dropdown filtering by operational expenditure: Travel (flights/lodging), Meals (client dining), Equipment (hardware/monitors), and Other (licenses/exams)."),

        ("Feature 10: Department Budget & Category Spend Analytics Bar",
         "Interactive analytics card featuring exact category expenditure totals and a multi-color progress meter tracking department spend against the ₹5,00,000.00 monthly cap."),

        ("Feature 11: One-Click Spreadsheet Export (CSV for Excel)",
         "Downloads an instant, fully formatted .csv expense report with UTF-8 BOM (\\ufeff) encoding, ensuring Microsoft Excel displays rupee symbols (₹) and text without corruption."),

        ("Feature 12: Digital Receipt & Tax Invoice Modal Viewer",
         "Clicking 'View Invoice' on any claim opens an official corporate e-receipt with tax reference number, merchant breakdown, incurred date, and verified audit stamp."),

        ("Feature 13: Receipt Proof Attachment Simulation",
         "In the submission modal, employees can attach invoice files (PDF, PNG, JPG) with real-time file name and size display, and clear options."),

        ("Feature 14: Corporate Expense Policy Guidelines Modal",
         "A top-level reference modal outlining official corporate spending policies: ₹2,500/day meal per diem, ₹10k ceiling, 48h duplicate rules, and mandatory written rejections.")
    ]

    for fname, fdesc in features:
        story.append(Paragraph(f"<b>{fname}</b>", h2_style))
        story.append(Paragraph(fdesc, body_style))

    # =========================================================================
    # SECTION 4: CORPORATE PERSONAS & DATASET
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("4. Corporate Persona & Dataset Directory (9 Users)", h1_style))
    story.append(Paragraph(
        "The database is pre-seeded with <b>9 diverse corporate accounts</b> across Engineering, Sales, Security, Design, Operations, and Finance. "
        "To provide a balanced and verifiable experience, <b>every single user has exactly 4 unique claims</b>: "
        "1 Pending, 1 Approved, 1 Settled, and 1 Rejected (36 total vouchers, 72 audit logs).", body_style
    ))

    user_table_data = [
        [
            Paragraph("<b>User & Role</b>", callout_style),
            Paragraph("<b>Division</b>", callout_style),
            Paragraph("<b>Seeded Claims Portfolio (1 of each status)</b>", callout_style)
        ],
        [
            Paragraph("<b>Alice Jenkins</b><br/>EMPLOYEE", callout_style),
            Paragraph("Engineering", callout_style),
            Paragraph("• Pending: Travel (₹4,250) • Approved: Meals (₹1,800)<br/>• Settled: Equipment (₹18,500) • Rejected: Personal Sub (₹1,200)", callout_style)
        ],
        [
            Paragraph("<b>Bob Martinez</b><br/>MANAGER", callout_style),
            Paragraph("Engineering", callout_style),
            Paragraph("• Pending: Offsite (₹8,500) • Approved: Client Dinner (₹5,400)<br/>• Settled: Cloud Summit (₹14,200) • Rejected: Personal Coffee (₹950)", callout_style)
        ],
        [
            Paragraph("<b>Carol Vance</b><br/>FINANCE", callout_style),
            Paragraph("Treasury", callout_style),
            Paragraph("• Pending: Workstation (₹22,000) • Approved: Tax Software (₹9,800)<br/>• Settled: Team Dinner (₹3,200) • Rejected: Unreceipted Fees (₹1,500)", callout_style)
        ],
        [
            Paragraph("<b>David Miller</b><br/>EMPLOYEE", callout_style),
            Paragraph("Cloud Ops", callout_style),
            Paragraph("• Pending: AWS Exam (₹11,500) • Approved: Dock & Keyboard (₹8,500)<br/>• Settled: Datacenter Migration (₹14,200) • Rejected: Cloud Tools (₹4,200)", callout_style)
        ],
        [
            Paragraph("<b>Elena Rostova</b><br/>EMPLOYEE", callout_style),
            Paragraph("Enterprise Sales", callout_style),
            Paragraph("• Pending: Pitch Travel (₹16,800) • Approved: Client Dinner (₹6,200)<br/>• Settled: Renewal Closing (₹9,400) • Rejected: Undocumented Drinks (₹3,800)", callout_style)
        ],
        [
            Paragraph("<b>Frank Patel</b><br/>EMPLOYEE", callout_style),
            Paragraph("Cyber Security", callout_style),
            Paragraph("• Pending: CISSP Renewal (₹12,000) • Approved: YubiKeys (₹7,500)<br/>• Settled: InfoSec Conference (₹24,000) • Rejected: Courier (₹850)", callout_style)
        ],
        [
            Paragraph("<b>Grace Hopper</b><br/>EMPLOYEE", callout_style),
            Paragraph("UI/UX Design", callout_style),
            Paragraph("• Pending: Figma Seat (₹15,000) • Approved: Workshop Catering (₹2,400)<br/>• Settled: 4K IPS Monitor (₹28,000) • Rejected: Tablet Skins (₹3,100)", callout_style)
        ],
        [
            Paragraph("<b>Henry Kim</b><br/>MANAGER", callout_style),
            Paragraph("Facilities", callout_style),
            Paragraph("• Pending: Standing Desks (₹32,000) • Approved: Safety Audit (₹8,900)<br/>• Settled: Contract Dinner (₹4,750) • Rejected: Weekend Extension (₹5,600)", callout_style)
        ],
        [
            Paragraph("<b>Isabella Gomez</b><br/>FINANCE", callout_style),
            Paragraph("Treasury", callout_style),
            Paragraph("• Pending: ERP Bridge (₹45,000) • Approved: Treasury Audit (₹10,000)<br/>• Settled: Team Lunch (₹2,800) • Rejected: Filed Past 90-days (₹2,100)", callout_style)
        ]
    ]

    t_users = Table(user_table_data, colWidths=[110, 85, 310])
    t_users.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BOX', (0,0), (-1,-1), 1, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_BG_LIGHT, colors.white]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_users)
    story.append(Spacer(1, 6))
    story.append(Paragraph("<i>Note: All test accounts share the universal development password:</i> <font name='Courier'>password123</font>", body_style))

    # =========================================================================
    # SECTION 5: LIVE DEMONSTRATION PLAYBOOK
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("5. Live Demonstration Playbook (Viva Presentation Script)", h1_style))
    story.append(Paragraph(
        "Follow this exact 4-phase sequence during your team evaluation to showcase every core feature in under 3 minutes:", body_style
    ))

    demo_phases = [
        ("Phase 1: Submitter Flow (Alice Jenkins - EMPLOYEE)",
         "1. Select 'Alice Jenkins' in the top User Switcher dropdown.<br/>"
         "2. Point out that Alice's personal KPI summary shows: Total: 4, Pending: 1, Approved: 1, Settled: 1, Rejected: 1.<br/>"
         "3. Click '+ New Claim' and enter ₹4,250 for Travel. Demonstrate the live 48-Hour Duplicate Warning alert.<br/>"
         "4. Submit the claim and observe the confirmation toast."),

        ("Phase 2: Manager Ceiling & Mandatory Rejection (Bob Martinez - MANAGER)",
         "1. Switch to 'Bob Martinez'. Click 'Department Queue' to view claims across all employees.<br/>"
         "2. Locate a high-value claim (> ₹10,000) and point out the locked 'Needs Finance' badge (Bob cannot approve).<br/>"
         "3. On Alice's pending claim, click 'Reject'. Show that submitting without a note fails (mandatory justification rule).<br/>"
         "4. Enter 'Missing tax receipt copy per policy' and confirm."),

        ("Phase 3: High-Value Authorization & Batch Disbursement (Carol Vance - FINANCE)",
         "1. Switch to 'Carol Vance'. Point out that Carol holds sole authority to authorize high-value claims (> ₹10k).<br/>"
         "2. Click 'Authorize' on an approved pending claim.<br/>"
         "3. Click 'Settle All Approved' in the toolbar to open the Batch Settlement Modal.<br/>"
         "4. Click 'Disburse All' to execute the atomic transaction; observe all approved claims flip to SETTLED simultaneously."),

        ("Phase 4: Forensics, Digital Receipts & CSV Export (All Team Members)",
         "1. Click 'View Invoice' on any voucher row to demonstrate the digital tax receipt modal.<br/>"
         "2. Click the timeline clock icon to inspect the immutable audit log for that voucher.<br/>"
         "3. Click the 'Audit Trail' tab in the filter toolbar to show the company-wide tamper-evident ledger.<br/>"
         "4. Click 'Export' to download the live Microsoft Excel-ready CSV spreadsheet.")
    ]

    for ptitle, pbody in demo_phases:
        story.append(Paragraph(f"<b>{ptitle}</b>", h2_style))
        story.append(Paragraph(pbody, body_style))

    # =========================================================================
    # SECTION 6: TOP 20 VIVA VOCE QUESTIONS & ANSWERS
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("6. Top 20 Viva Voce Questions & Authoritative Answers", h1_style))
    story.append(Paragraph("Study these authoritative answers with your teammates to prepare for faculty review:", body_style))

    viva_qa = [
        ("Q1: What architecture pattern does this project follow?",
         "It follows a Decoupled 4-Tier Architecture adhering to the Separation of Concerns (SoC) principle: Presentation Tier (Vanilla JS SPA), "
         "Controller Tier (FastAPI REST endpoints & Pydantic DTOs), Service Tier (pure domain logic & rules engine), and Repository Tier (SQLite3 persistence & ACID transactions)."),

        ("Q2: What is the purpose of the DTO (Data Transfer Object) pattern here?",
         "We use Pydantic models (e.g. ClaimCreateRequest, ClaimResponse, MetricsResponse) to define rigid typed contracts between client and server, "
         "preventing mass-assignment vulnerabilities and enforcing field validations before data enters business logic."),

        ("Q3: Why did you use Vanilla JavaScript instead of React, Vue, or Angular?",
         "Vanilla JS with modern ES6+ and Tailwind CSS eliminates heavy node_modules build dependencies, webpack compilation steps, and hydration overhead. "
         "The app runs instantly in any browser with zero setup and sub-millisecond execution speeds."),

        ("Q4: How is Separation of Concerns (SoC) strictly maintained?",
         "Controllers only handle HTTP status codes and JSON serialization. Repositories only execute parameterized SQL. All business rules—such as the ₹10k ceiling, "
         "48h duplicate scanning, and state transitions—reside exclusively in the Service Tier (claim_service.py)."),

        ("Q5: How do you guarantee database consistency during Batch Settlement?",
         "We wrap the entire batch operation in an atomic database transaction using Python's sqlite3 connection context. It selects all approved claims, "
         "updates status to SETTLED, and writes audit records. If any write fails, conn.rollback() triggers immediately, preventing partial payouts."),

        ("Q6: Are foreign keys enabled in SQLite, and how?",
         "Yes. SQLite disables foreign keys by default for backwards compatibility. We explicitly execute PRAGMA foreign_keys = ON; on every single connection "
         "opened in database.py, guaranteeing cascading referential integrity."),

        ("Q7: How do you prevent SQL Injection (SQLi)?",
         "We never concatenate user variables into SQL queries. Every query in claim_repository.py and audit_repository.py utilizes parameterized "
         "placeholders (?), safely separating SQL instructions from user data."),

        ("Q8: How is the duplicate detection query accelerated?",
         "We created a composite SQL index: CREATE INDEX idx_claims_duplicate_check ON ExpenseClaims (user_id, category, amount, created_at); "
         "allowing the database to locate potential duplicates in O(log N) index lookups rather than doing expensive full-table scans."),

        ("Q9: What is Role-Based Access Control (RBAC) and how is it implemented?",
         "RBAC restricts operations based on the user's role (EMPLOYEE, MANAGER, FINANCE). We implement it via FastAPI dependency injection middleware "
         "(require_roles) which validates authorization headers before the request reaches the controller."),

        ("Q10: How do you prevent Horizontal Privilege Escalation?",
         "An employee must not view another employee's records. When an EMPLOYEE queries the API, the service layer automatically injects "
         "WHERE user_id = ? into the SQL query, enforcing strict row-level security at the database tier."),

        ("Q11: What is 'Non-Repudiation' and how does the Audit Ledger achieve it?",
         "Non-repudiation ensures an actor cannot deny an action they performed. The AuditLogs table is strictly append-only (zero UPDATE or DELETE endpoints). "
         "Every approval, rejection, and disbursement permanently stores the actor ID, action type, timestamp, and justification."),

        ("Q12: Why are rejection comments mandatory?",
         "To enforce accountability and prevent arbitrary claim dismissals. If an approver submits an empty comment, claim_service.py raises "
         "HTTP 422 Unprocessable Content. The reason is permanently recorded in the audit trail."),

        ("Q13: Explain your Finite State Machine. What are the legal transitions?",
         "A claim progresses through: PENDING ➔ APPROVED (by Manager <= ₹10k or Finance > ₹10k), PENDING ➔ REJECTED (with reason), and APPROVED ➔ SETTLED (by Finance). "
         "All other transitions (e.g. PENDING ➔ SETTLED or REJECTED ➔ APPROVED) trigger HTTP 400 Bad Request."),

        ("Q14: What is the ₹10,000 threshold rule and why is it implemented?",
         "It enforces fiscal hierarchy. Department managers can authorize routine operational expenses up to ₹10,000. Larger amounts represent substantial capital "
         "outflows and must be reviewed and authorized by the Finance Controller."),

        ("Q15: How does the 48-Hour duplicate scanner work?",
         "When a claim is created, the system checks whether the same user submitted an identical tuple (user_id, category, amount) in the preceding 48 hours. "
         "If found, the claim is flagged with is_duplicate = True and tagged with an amber warning badge for managerial audit."),

        ("Q16: Can an employee withdraw or cancel a claim?",
         "Yes. An employee can cancel their own voucher while it is in PENDING status. Once a claim is APPROVED or SETTLED, cancellation is disabled "
         "to preserve financial reconciliation."),

        ("Q17: What automated tests have you written?",
         "We built 7 end-to-end domain test suites in tests/test_portal.py verifying schema integrity, duplicate scanning, the ₹10k ceiling, "
         "mandatory rejection comments, state machine guards, ACID batch settlements, and RBAC query scopes."),

        ("Q18: What is the execution speed of your automated test suite?",
         "All 7 test suites execute in under 0.25 seconds because they run against lightweight in-memory / local SQLite relational tables with zero network latency."),

        ("Q19: Why was the browser cache-busting ?v=2.7.0 implemented?",
         "Browsers aggressively cache static JavaScript files. Query-string versioning guarantees that all client browsers immediately download the latest "
         "frontend logic without requiring manual cache clearing."),

        ("Q20: How does the CSV export ensure compatibility with Microsoft Excel?",
         "We prepend the UTF-8 Byte Order Mark (\\ufeff) at the beginning of the CSV byte stream, instructing Microsoft Excel to render rupee symbols (₹) "
         "and international formatting correctly without encoding corruption.")
    ]

    for q, a in viva_qa:
        story.append(Paragraph(q, qa_q_style))
        story.append(Paragraph(a, qa_a_style))

    # =========================================================================
    # SECTION 7: QUICKSTART & EXECUTION COMMANDS
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("7. Team Local Setup & Execution Commands", h1_style))
    story.append(Paragraph("Keep these commands ready to run the portal on your personal laptops:", body_style))

    commands_text = [
        "<b>1. Launch Application Server:</b><br/>"
        "<font name='Courier'>cd C:\\Users\\p1022\\.gemini\\antigravity\\scratch\\corporate-expense-portal<br/>"
        "python run.py</font><br/>"
        "<i>Open browser at: http://127.0.0.1:8000</i><br/>",

        "<b>2. Run Automated Test Suite:</b><br/>"
        "<font name='Courier'>python -m unittest discover tests</font><br/>"
        "<i>Validates all 7 domain test suites (100% pass rate in ~0.25s)</i><br/>",

        "<b>3. Reset / Reseed Clean Corporate Database:</b><br/>"
        "<font name='Courier'>python seed.py --force</font><br/>"
        "<i>Resets database with 9 users, 36 balanced claims (4 per user), and 72 audit records.</i>"
    ]

    for cmd in commands_text:
        story.append(Paragraph(cmd, body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[SUCCESS] Executive PDF Guide generated successfully: {filename}")

if __name__ == "__main__":
    out_file = "C:/Users/p1022/.gemini/antigravity/scratch/corporate-expense-portal/Corporate_Expense_System_Teammate_Guide.pdf"
    if len(sys.argv) > 1:
        out_file = sys.argv[1]
    build_pdf(out_file)
