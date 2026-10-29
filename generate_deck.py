"""
Professional Enterprise Capstone Presentation Generator
Constructs a world-class, executive dark-themed 16:9 presentation deck
for the Corporate Expense Claim & Reimbursement Portal.
Designed for 4th-Year Building Enterprise Applications (BEA) academic & viva evaluation.
"""
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_executive_deck(output_path: str = "corporate_expense_portal_presentation.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # --- PALETTE ---
    BG_CANVAS    = RGBColor(10, 14, 23)     # Deep Midnight Canvas #0A0E17
    PANEL_BG     = RGBColor(17, 24, 39)     # Slate 900 Card #111827
    PANEL_BORDER = RGBColor(30, 41, 59)     # Slate 800 Border #1E293B
    TEXT_MAIN    = RGBColor(248, 250, 252)  # Slate 50 White #F8FAFC
    TEXT_MUTED   = RGBColor(148, 163, 184)  # Slate 400 Muted #94A3B8
    TEXT_DIM     = RGBColor(100, 116, 139)  # Slate 500 Dim #64748B

    # Professional Accents
    ACC_EMERALD  = RGBColor(16, 185, 129)   # Emerald #10B981 (Success / Live / Approved)
    ACC_SKY      = RGBColor(14, 165, 233)   # Sky Blue #0EA5E9 (Architecture / Flows)
    ACC_AMBER    = RGBColor(245, 158, 11)   # Amber #F59E0B (Pending / Warning / Rules)
    ACC_ROSE     = RGBColor(244, 63, 94)    # Rose #F43F5E (Rejected / Vulnerability)
    ACC_VIOLET   = RGBColor(139, 92, 246)   # Violet #8B5CF6 (Disbursement / Treasury)

    def set_notes(slide, text: str):
        slide.notes_slide.notes_text_frame.text = text

    def create_base_slide(slide_num: int, kicker: str, title: str, subtitle: str):
        slide = prs.slides.add_slide(blank_layout)
        
        # 1. Dark background canvas
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_CANVAS
        bg.line.fill.background()

        # 2. Top hairline accent bar
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.35), Inches(11.733), Inches(0.025))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = ACC_EMERALD
        top_bar.line.fill.background()

        # 3. Header text block
        h_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.48), Inches(11.733), Inches(1.15))
        tf = h_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_kicker = tf.paragraphs[0]
        p_kicker.text = f"//  {kicker.upper()}"
        p_kicker.font.name = "Calibri"
        p_kicker.font.size = Pt(9.5)
        p_kicker.font.bold = True
        p_kicker.font.color.rgb = ACC_EMERALD

        p_title = tf.add_paragraph()
        p_title.text = title
        p_title.font.name = "Calibri"
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_MAIN
        p_title.space_before = Pt(3)

        if subtitle:
            p_sub = tf.add_paragraph()
            p_sub.text = subtitle
            p_sub.font.name = "Calibri"
            p_sub.font.size = Pt(11)
            p_sub.font.color.rgb = TEXT_MUTED
            p_sub.space_before = Pt(2)

        # 4. Subtle separator line
        div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.72), Inches(11.733), Inches(0.015))
        div.fill.solid()
        div.fill.fore_color.rgb = PANEL_BORDER
        div.line.fill.background()

        # 5. Bottom footer
        ftr_div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.88), Inches(11.733), Inches(0.015))
        ftr_div.fill.solid()
        ftr_div.fill.fore_color.rgb = PANEL_BORDER
        ftr_div.line.fill.background()

        f_box = slide.shapes.add_textbox(Inches(0.8), Inches(6.94), Inches(8.0), Inches(0.3))
        p_f = f_box.text_frame.paragraphs[0]
        p_f.text = "APEX ENTERPRISE SYSTEMS  •  BEA CAPSTONE  •  FASTAPI + SQLITE3 RELATIONAL ARCHITECTURE"
        p_f.font.name = "Calibri"
        p_f.font.size = Pt(8.5)
        p_f.font.bold = True
        p_f.font.color.rgb = TEXT_DIM

        num_box = slide.shapes.add_textbox(Inches(10.5), Inches(6.94), Inches(2.0), Inches(0.3))
        p_n = num_box.text_frame.paragraphs[0]
        p_n.alignment = PP_ALIGN.RIGHT
        p_n.text = f"SLIDE  {slide_num:02d} / 10"
        p_n.font.name = "Calibri"
        p_n.font.size = Pt(9)
        p_n.font.bold = True
        p_n.font.color.rgb = ACC_EMERALD

        return slide

    def add_card(slide, left, top, width, height, border_color=PANEL_BORDER, fill_color=PANEL_BG):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = fill_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)
        return card

    # =========================================================================
    # SLIDE 1: HERO & LIFECYCLE PIPELINE OVERVIEW
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = BG_CANVAS
    bg1.line.fill.background()

    # Left accent vertical bar
    s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.3), Inches(0.08), Inches(2.3)).fill.solid()

    tb1 = s1.shapes.add_textbox(Inches(1.1), Inches(1.2), Inches(11.0), Inches(2.4))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "BUILDING ENTERPRISE APPLICATIONS (BEA)  •  CAPSTONE PROJECT"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACC_EMERALD

    p = tf1.add_paragraph()
    p.text = "Corporate Expense Claim & Reimbursement Portal"
    p.font.name = "Calibri"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    p.space_before = Pt(8)

    p = tf1.add_paragraph()
    p.text = "A Multi-Tier, Role-Governed Financial System with Automated Anti-Fraud & Immutable Ledger"
    p.font.name = "Calibri"
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED
    p.space_before = Pt(6)

    # 4-Stage Horizontal Pipeline Header Label
    tb_pl = s1.shapes.add_textbox(Inches(0.8), Inches(3.9), Inches(11.733), Inches(0.3))
    p_pl = tb_pl.text_frame.paragraphs[0]
    p_pl.text = "CORE REIMBURSEMENT LIFECYCLE (END-TO-END EXECUTION PIPELINE)"
    p_pl.font.name = "Calibri"
    p_pl.font.size = Pt(9.5)
    p_pl.font.bold = True
    p_pl.font.color.rgb = ACC_SKY

    # 4 Structured Pipeline Cards with Arrows
    pipeline_steps = [
        ("01. INITIATION", "Employee Submission", "Category, date, receipts & amount filed via responsive SPA dashboard.", ACC_SKY),
        ("02. COMPLIANCE SCAN", "Automated Anti-Fraud", "48h duplicate invoice scanner & ₹10,000 authority routing check.", ACC_AMBER),
        ("03. AUTHORIZATION", "Role-Based Delegation", "Manager approves claims <= ₹10k; Finance approves high-value vouchers.", ACC_EMERALD),
        ("04. DISBURSEMENT", "One-Click Settlement", "ACID batch disbursement and non-repudiable ledger commit.", ACC_VIOLET)
    ]

    c_w = Inches(2.7)
    c_h = Inches(1.85)
    c_gap = Inches(0.3)
    start_l = Inches(0.8)

    for i, (tag, stitle, desc, acc_col) in enumerate(pipeline_steps):
        left = start_l + i * (c_w + c_gap)
        # Card
        add_card(s1, left, Inches(4.3), c_w, c_h, border_color=acc_col)

        tb_c = s1.shapes.add_textbox(left + Inches(0.15), Inches(4.4), c_w - Inches(0.3), c_h - Inches(0.2))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True

        p1 = tf_c.paragraphs[0]
        p1.text = tag
        p1.font.name = "Calibri"
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.color.rgb = acc_col

        p2 = tf_c.add_paragraph()
        p2.text = stitle
        p2.font.name = "Calibri"
        p2.font.size = Pt(12.5)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN
        p2.space_before = Pt(3)

        p3 = tf_c.add_paragraph()
        p3.text = desc
        p3.font.name = "Calibri"
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = TEXT_MUTED
        p3.space_before = Pt(6)

        # Draw connecting arrow between cards
        if i < 3:
            arr_box = s1.shapes.add_textbox(left + c_w, Inches(4.9), c_gap, Inches(0.5))
            p_arr = arr_box.text_frame.paragraphs[0]
            p_arr.alignment = PP_ALIGN.CENTER
            p_arr.text = "➔"
            p_arr.font.name = "Calibri"
            p_arr.font.size = Pt(16)
            p_arr.font.bold = True
            p_arr.font.color.rgb = TEXT_DIM

    # Footer note
    tb_foot = s1.shapes.add_textbox(Inches(0.8), Inches(6.45), Inches(11.733), Inches(0.3))
    p_ft = tb_foot.text_frame.paragraphs[0]
    p_ft.text = "Technology Stack: Python 3.12  •  FastAPI REST API  •  SQLite3 Relational DB  •  Vanilla JS SPA  •  Academic Year 2026"
    p_ft.font.name = "Calibri"
    p_ft.font.size = Pt(9)
    p_ft.font.color.rgb = TEXT_DIM

    set_notes(s1, (
        "SPEAKER 1 (Team Lead):\n"
        "Good morning Respected Professor and fellow evaluators. Our 4th-year Building Enterprise Applications "
        "capstone project is the Corporate Expense Claim & Reimbursement Portal. "
        "In modern corporations, unmonitored employee expenses cause massive fiscal leakages. "
        "Our system automates the complete 4-stage pipeline shown here: from employee initiation, through algorithmic "
        "anti-fraud scanning, role-based authorization, and atomic treasury disbursement. "
        "Let us examine how our system re-engineers traditional broken workflows."
    ))

    # =========================================================================
    # SLIDE 2: WORKFLOW RE-ENGINEERING (MANUAL VS AUTOMATED PIPELINE)
    # =========================================================================
    s2 = create_base_slide(
        2,
        "Enterprise Problem vs. Solution",
        "Workflow Re-Engineering: Traditional Vulnerabilities vs. Automated Solution",
        "How our automated state pipeline prevents corporate financial leakages and ensures total audit compliance."
    )

    # Left Column: Traditional Broken Workflow (Red/Danger)
    add_card(s2, Inches(0.8), Inches(1.95), Inches(5.7), Inches(4.45), border_color=ACC_ROSE)
    tb_l = s2.shapes.add_textbox(Inches(1.0), Inches(2.05), Inches(5.3), Inches(4.2))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True

    p = tf_l.paragraphs[0]
    p.text = "TRADITIONAL MANUAL PROCESS (HIGH-RISK)"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACC_ROSE

    manual_steps = [
        ("Paper Forms & Scattered Receipts", "Invoices emailed or submitted on paper with zero centralized validation."),
        ("Duplicate Payments Go Undetected", "Employees submit identical claims across months without detection."),
        ("Unauthorized Approvals", "Managers approve expenses beyond authority limits without executive review."),
        ("No Traceable Audit Trail", "Changes are lost in email threads with zero non-repudiation or legal proof.")
    ]
    for i, (title, sub) in enumerate(manual_steps):
        p_t = tf_l.add_paragraph()
        p_t.text = f"✖  Step {i+1}: {title}"
        p_t.font.name = "Calibri"
        p_t.font.size = Pt(10.5)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_MAIN
        p_t.space_before = Pt(8)

        p_s = tf_l.add_paragraph()
        p_s.text = f"    Impact: {sub}"
        p_s.font.name = "Calibri"
        p_s.font.size = Pt(9.5)
        p_s.font.color.rgb = TEXT_MUTED

    # Right Column: Our Automated Governance Engine (Emerald/Success)
    add_card(s2, Inches(6.8), Inches(1.95), Inches(5.7), Inches(4.45), border_color=ACC_EMERALD)
    tb_r = s2.shapes.add_textbox(Inches(7.0), Inches(2.05), Inches(5.3), Inches(4.2))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True

    p = tf_r.paragraphs[0]
    p.text = "OUR AUTOMATED ENTERPRISE PORTAL (100% GOVERNED)"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACC_EMERALD

    portal_steps = [
        ("Centralized Web Portal (SPA)", "Real-time client validation and instantaneous claim tracking."),
        ("48h Duplicate Scanner Algorithm", "Flags identical user + category + amount claims with amber warning badge."),
        ("Dual-Tier ₹10,000 Approval Limit", "Manager approval capped at ₹10,000; larger claims routed strictly to Finance."),
        ("Immutable Ledger & Batch Settle", "Append-only database ledger records every state transition atomically.")
    ]
    for i, (title, sub) in enumerate(portal_steps):
        p_t = tf_r.add_paragraph()
        p_t.text = f"✔  Stage {i+1}: {title}"
        p_t.font.name = "Calibri"
        p_t.font.size = Pt(10.5)
        p_t.font.bold = True
        p_t.font.color.rgb = ACC_EMERALD
        p_t.space_before = Pt(8)

        p_s = tf_r.add_paragraph()
        p_s.text = f"    Benefit: {sub}"
        p_s.font.name = "Calibri"
        p_s.font.size = Pt(9.5)
        p_s.font.color.rgb = TEXT_MUTED

    # Bottom summary banner
    tb_s2_foot = s2.shapes.add_textbox(Inches(0.8), Inches(6.45), Inches(11.733), Inches(0.35))
    p_s2_f = tb_s2_foot.text_frame.paragraphs[0]
    p_s2_f.text = "Key Takeaway: Replaces manual trust with programmatic rules—preventing fraud, enforcing thresholds, and guaranteeing legal auditability."
    p_s2_f.font.name = "Calibri"
    p_s2_f.font.size = Pt(10)
    p_s2_f.font.bold = True
    p_s2_f.font.color.rgb = ACC_SKY

    set_notes(s2, (
        "SPEAKER 1 (Team Lead):\n"
        "Here we contrast the manual legacy process with our automated platform. "
        "In a manual process, receipts are lost, duplicates pass through unchecked, and managers routinely sign off "
        "on expenses exceeding their authority without finance oversight. "
        "Our system re-engineers this by inserting programmatic guards: a 48-hour duplicate detection scanner, "
        "a hard ₹10,000 managerial threshold, and an append-only audit ledger where no record can ever be modified or erased."
    ))

    # =========================================================================
    # SLIDE 3: MULTI-TIER SYSTEM ARCHITECTURE (DECOUPLED SoC)
    # =========================================================================
    s3 = create_base_slide(
        3,
        "Software Engineering",
        "Multi-Tier Architecture & Separation of Concerns (SoC)",
        "Decoupled Presentation, Controller, Service, and Repository layers communicate via strict typed DTO contracts."
    )

    layers = [
        ("TIER 1: PRESENTATION TIER", "Single-Page Application (SPA)", "Vanilla JS (ES6+)  •  Modern Tailwind CSS  •  FontAwesome", "User interaction, dynamic role switcher, responsive claim creation modal, and live timeline rendering.", ACC_SKY),
        ("TIER 2: REST CONTROLLER TIER", "API Gateway & DTO Validation", "FastAPI Endpoints  •  Pydantic Schemas  •  OpenAPI 3.0", "Deserializes JSON, enforces strict data validation (Pydantic), checks auth headers, and maps HTTP codes.", ACC_EMERALD),
        ("TIER 3: BUSINESS SERVICE TIER", "Domain Logic & Rules Engine", "Deterministic State Machine  •  Rules Engine  •  Audit Dispatcher", "Enforces the ₹10k approval threshold, executes the 48h duplicate scanner, and coordinates state transitions.", ACC_AMBER),
        ("TIER 4: REPOSITORY TIER", "Persistence & ACID Transactions", "SQLite3 Relational DB  •  PRAGMA foreign_keys = ON  •  Indices", "Raw parameterized SQL queries (SQLi protected), foreign-key relational integrity, and atomic batch transactions.", ACC_VIOLET)
    ]

    tier_w = Inches(11.733)
    tier_h = Inches(1.0)
    tier_gap = Inches(0.18)
    start_top = Inches(1.9)

    for i, (name, role, tech, desc, acc_col) in enumerate(layers):
        top = start_top + i * (tier_h + tier_gap)
        add_card(s3, Inches(0.8), top, tier_w, tier_h, border_color=acc_col)

        tb_tier = s3.shapes.add_textbox(Inches(1.0), top + Inches(0.1), tier_w - Inches(0.4), tier_h - Inches(0.2))
        tf_t = tb_tier.text_frame
        tf_t.word_wrap = True

        p1 = tf_t.paragraphs[0]
        p1.text = f"{name}  •  {role}"
        p1.font.name = "Calibri"
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = acc_col

        p2 = tf_t.add_paragraph()
        p2.text = f"Tech: {tech}    |    Responsibilities: {desc}"
        p2.font.name = "Calibri"
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = TEXT_MAIN
        p2.space_before = Pt(3)

    # Bottom Architectural Invariants Callout
    tb_s3_inv = s3.shapes.add_textbox(Inches(0.8), Inches(6.45), Inches(11.733), Inches(0.35))
    p_inv = tb_s3_inv.text_frame.paragraphs[0]
    p_inv.text = "Architectural Guarantee: Strict downward dependency flow (Presentation ➔ Controller ➔ Service ➔ Repository). Zero circular dependencies."
    p_inv.font.name = "Calibri"
    p_inv.font.size = Pt(9.5)
    p_inv.font.bold = True
    p_inv.font.color.rgb = ACC_EMERALD

    set_notes(s3, (
        "SPEAKER 2 (Backend & Architecture Lead):\n"
        "Respected Professor, this slide demonstrates our 4-tier software architecture following the Separation of Concerns principle. "
        "The Presentation Tier is an ultra-fast Vanilla JS Single Page Application requiring zero build tools. "
        "It communicates via HTTP REST to our FastAPI Controller Tier, where incoming payloads are validated using Pydantic DTOs. "
        "The Service Tier encapsulates all business rules—no business logic ever leaks into SQL or controllers. "
        "Finally, the Repository Tier manages persistence using SQLite3 with foreign keys strictly enabled. "
        "Any tier can be swapped—for example, switching SQLite to PostgreSQL requires editing only the Repository tier."
    ))

    # =========================================================================
    # SLIDE 4: ROLE-BASED ACCESS CONTROL (RBAC) & PERMISSION MATRIX
    # =========================================================================
    s4 = create_base_slide(
        4,
        "Enterprise Security & Governance",
        "Role-Based Access Control (RBAC) & Security Policy",
        "Enforces least privilege across Employee, Manager, and Finance Officer personas with strict middleware guards."
    )

    roles = [
        ("EMPLOYEE ROLE", "Standard Staff / Submitter", ACC_SKY, [
            "Submit new expense claims with category, date, and description.",
            "View personal claim history (strictly scoped: WHERE user_id = ?).",
            "Track claim lifecycle progression in the Timeline modal.",
            "✖ STRICTLY PROHIBITED from approving, rejecting, or settling claims (HTTP 403 Forbidden)."
        ]),
        ("MANAGER ROLE", "Department Approver", ACC_AMBER, [
            "Inspect all submitted claims across department team members.",
            "AUTHORITY CAP: Approve claims with amounts <= ₹10,000.",
            "Reject non-compliant claims with mandatory justification comment.",
            "✖ BLOCKED from approving claims > ₹10,000 (Requires escalation to Finance)."
        ]),
        ("FINANCE ROLE", "Treasury & Disbursement", ACC_EMERALD, [
            "Sole authorization to approve high-value claims exceeding ₹10,000.",
            "Execute individual and One-Click Batch Settlement across all approved vouchers.",
            "Inspect the immutable Global Enterprise Audit Ledger across all users.",
            "Complete oversight of company-wide cash disbursement metrics."
        ])
    ]

    r_w = Inches(3.7)
    r_h = Inches(4.35)
    r_gap = Inches(0.31)

    for i, (r_name, r_sub, acc_col, items) in enumerate(roles):
        left = Inches(0.8) + i * (r_w + r_gap)
        add_card(s4, left, Inches(1.95), r_w, r_h, border_color=acc_col)

        tb_r = s4.shapes.add_textbox(left + Inches(0.18), Inches(2.05), r_w - Inches(0.36), r_h - Inches(0.2))
        tf_r = tb_r.text_frame
        tf_r.word_wrap = True

        p1 = tf_r.paragraphs[0]
        p1.text = r_name
        p1.font.name = "Calibri"
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = acc_col

        p2 = tf_r.add_paragraph()
        p2.text = r_sub
        p2.font.name = "Calibri"
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = TEXT_MUTED
        p2.space_before = Pt(2)

        for item in items:
            p_item = tf_r.add_paragraph()
            p_item.text = ("• " if not item.startswith("✖") else "") + item
            p_item.font.name = "Calibri"
            p_item.font.size = Pt(9.5)
            p_item.font.bold = item.startswith("✖")
            p_item.font.color.rgb = ACC_ROSE if item.startswith("✖") else TEXT_MAIN
            p_item.space_before = Pt(9)

    tb_s4_foot = s4.shapes.add_textbox(Inches(0.8), Inches(6.45), Inches(11.733), Inches(0.35))
    p_s4_f = tb_s4_foot.text_frame.paragraphs[0]
    p_s4_f.text = "Security Invariant: Permissions are validated server-side in auth_middleware.py. Client UI role-switching is purely for demonstration."
    p_s4_f.font.name = "Calibri"
    p_s4_f.font.size = Pt(9.5)
    p_s4_f.font.bold = True
    p_s4_f.font.color.rgb = ACC_SKY

    set_notes(s4, (
        "SPEAKER 2 (Backend & Architecture Lead):\n"
        "Here is our RBAC matrix. We implement the principle of least privilege. "
        "Employees can only view their own claims—our repository injects 'WHERE user_id = ?' on employee queries to prevent "
        "horizontal privilege escalation. "
        "Managers can view department claims and approve claims up to ₹10,000. If a manager attempts to approve a claim of ₹10,001, "
        "the backend rejects the request with HTTP 403 Forbidden. "
        "Finance officers handle high-value vouchers, batch settlements, and full audit ledger inspection."
    ))

    # =========================================================================
    # SLIDE 5: DETERMINISTIC FINITE CLAIM STATE MACHINE
    # =========================================================================
    s5 = create_base_slide(
        5,
        "Domain State Machine",
        "Deterministic Claim State Machine & Transition Rules",
        "Guarantees that expense claims progress strictly through mathematically validated, irreversible lifecycle states."
    )

    # 4 State Pills across top
    states_def = [
        ("STATE 1: PENDING", "Claim Submitted", "Initial state upon filing by employee. Awaiting compliance and authority review.", ACC_AMBER),
        ("STATE 2: APPROVED", "Authorized Voucher", "Approved by Manager (<= ₹10k) or Finance (> ₹10k). Ready for treasury settlement.", ACC_EMERALD),
        ("STATE 3: SETTLED", "Disbursed & Closed", "Finance executed disbursement transaction. Funds transferred. Terminal closed state.", ACC_VIOLET),
        ("STATE 4: REJECTED", "Denied with Reason", "Denied by Manager or Finance with mandatory comment. Terminal state; non-resubmittable.", ACC_ROSE)
    ]

    s_w = Inches(2.7)
    s_h = Inches(1.5)
    s_gap = Inches(0.3)
    start_l = Inches(0.8)

    for i, (st_name, st_role, st_desc, acc_col) in enumerate(states_def):
        left = start_l + i * (s_w + s_gap)
        add_card(s5, left, Inches(1.95), s_w, s_h, border_color=acc_col)

        tb_s = s5.shapes.add_textbox(left + Inches(0.15), Inches(2.05), s_w - Inches(0.3), s_h - Inches(0.2))
        tf_s = tb_s.text_frame
        tf_s.word_wrap = True

        p1 = tf_s.paragraphs[0]
        p1.text = st_name
        p1.font.name = "Calibri"
        p1.font.size = Pt(10.5)
        p1.font.bold = True
        p1.font.color.rgb = acc_col

        p2 = tf_s.add_paragraph()
        p2.text = st_role
        p2.font.name = "Calibri"
        p2.font.size = Pt(11.5)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN
        p2.space_before = Pt(2)

        p3 = tf_s.add_paragraph()
        p3.text = st_desc
        p3.font.name = "Calibri"
        p3.font.size = Pt(8.5)
        p3.font.color.rgb = TEXT_MUTED
        p3.space_before = Pt(4)

    # Transition Rules Specification Table
    add_card(s5, Inches(0.8), Inches(3.65), Inches(11.733), Inches(2.7), border_color=PANEL_BORDER)
    tb_mat = s5.shapes.add_textbox(Inches(1.0), Inches(3.75), Inches(11.333), Inches(2.5))
    tf_m = tb_mat.text_frame
    tf_m.word_wrap = True

    p = tf_m.paragraphs[0]
    p.text = "VALIDATED TRANSITION MATRIX & EDGE-CASE GUARDS (claim_service.py)"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACC_SKY

    rules = [
        ("PENDING  ➔  APPROVED", "Valid Actor: Manager (if amount <= ₹10,000) OR Finance Officer (any amount). State flips to APPROVED; emits AuditLog."),
        ("PENDING  ➔  REJECTED", "Valid Actor: Manager or Finance Officer. Mandatory rejection reason required; returns HTTP 422 if empty."),
        ("APPROVED  ➔  SETTLED", "Valid Actor: Exclusively Finance Officer. Disburses reimbursement in single or batch mode; commits immutable settlement record."),
        ("ILLEGAL JUMP: PENDING ➔ SETTLED", "Blocked: Returns HTTP 400 Bad Request. System enforces that no unapproved claim can ever bypass management authorization."),
        ("ILLEGAL JUMP: REJECTED ➔ ANY", "Blocked: REJECTED is a terminal state. System returns HTTP 400. Tampering with rejected records is strictly prevented.")
    ]

    for trans, desc in rules:
        p_r = tf_m.add_paragraph()
        p_r.text = f"•  {trans}:  {desc}"
        p_r.font.name = "Calibri"
        p_r.font.size = Pt(9.5)
        p_r.font.color.rgb = TEXT_MAIN
        p_r.space_before = Pt(5)

    tb_s5_foot = s5.shapes.add_textbox(Inches(0.8), Inches(6.45), Inches(11.733), Inches(0.35))
    p_s5_f = tb_s5_foot.text_frame.paragraphs[0]
    p_s5_f.text = "State Pattern Verification: All status updates execute through claim_service.py with precondition assertions, preventing illegal state corruption."
    p_s5_f.font.name = "Calibri"
    p_s5_f.font.size = Pt(9.5)
    p_s5_f.font.bold = True
    p_s5_f.font.color.rgb = ACC_EMERALD

    set_notes(s5, (
        "SPEAKER 2 (Backend & Architecture Lead):\n"
        "This slide details our finite state machine. A claim exists in one of four deterministic states: "
        "PENDING, APPROVED, SETTLED, or REJECTED. "
        "Our state machine enforces critical business invariants: "
        "First, a claim CANNOT jump directly from PENDING to SETTLED without prior approval—attempting this raises HTTP 400. "
        "Second, REJECTED is a terminal state; once rejected, it cannot be revived or approved. "
        "This prevents collusion or backdoor settlements."
    ))

    # =========================================================================
    # SLIDE 6: BUSINESS RULES ENGINE (THRESHOLD & DUPLICATE FRAUD SCANNER)
    # =========================================================================
    s6 = create_base_slide(
        6,
        "Enterprise Business Rules",
        "Business Rules Engine: Dual-Tier Threshold & Anti-Fraud Scanner",
        "Algorithmic governance rules executed prior to state persistence to eliminate human error and fraud."
    )

    # Left: Rule 1 - ₹10,000 Approval Limit
    add_card(s6, Inches(0.8), Inches(1.95), Inches(5.7), Inches(4.45), border_color=ACC_AMBER)
    tb_r1 = s6.shapes.add_textbox(Inches(1.0), Inches(2.05), Inches(5.3), Inches(4.2))
    tf_r1 = tb_r1.text_frame
    tf_r1.word_wrap = True

    p = tf_r1.paragraphs[0]
    p.text = "RULE 1: THE ₹10,000 DUAL-TIER DELEGATION MATRIX"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACC_AMBER

    r1_points = [
        ("Threshold Boundary", "₹10,000.00 exact fiscal ceiling."),
        ("Claims <= ₹10,000", "Department Managers possess autonomous sign-off authority for standard operational expenses."),
        ("Claims > ₹10,000", "Manager approval buttons are disabled; system strictly requires Finance Officer sign-off."),
        ("Enforcement Mechanism", "If a Manager attempts to call POST /api/claims/{id}/approve on a ₹10,001 claim, claim_service.py raises HTTP 403 Forbidden."),
        ("Business Objective", "Eliminates rogue managerial approvals on high-value corporate capital expenditures.")
    ]
    for title, desc in r1_points:
        p_t = tf_r1.add_paragraph()
        p_t.text = f"•  {title}:"
        p_t.font.name = "Calibri"
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_MAIN
        p_t.space_before = Pt(8)

        p_d = tf_r1.add_paragraph()
        p_d.text = f"   {desc}"
        p_d.font.name = "Calibri"
        p_d.font.size = Pt(9.5)
        p_d.font.color.rgb = TEXT_MUTED

    # Right: Rule 2 - 48h Duplicate Scanner
    add_card(s6, Inches(6.8), Inches(1.95), Inches(5.7), Inches(4.45), border_color=ACC_SKY)
    tb_r2 = s6.shapes.add_textbox(Inches(7.0), Inches(2.05), Inches(5.3), Inches(4.2))
    tf_r2 = tb_r2.text_frame
    tf_r2.word_wrap = True

    p = tf_r2.paragraphs[0]
    p.text = "RULE 2: 48-HOUR ALGORITHMIC DUPLICATE SCANNER"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACC_SKY

    r2_points = [
        ("Algorithmic Matching Key", "Tuple comparison: (user_id, category, amount)."),
        ("Sliding Time Window", "datetime.now() - timedelta(hours=48)."),
        ("Index Acceleration", "Backed by composite SQL index: idx_claims_duplicate_check(user_id, category, amount, created_at)."),
        ("Non-Blocking Flagging", "System does not abort creation; it sets is_duplicate = True and renders an Amber Warning Badge on the manager's review queue."),
        ("Rule 3: Rejection Reason", "Mandatory notes check; empty or whitespace notes return HTTP 422 Unprocessable Content.")
    ]
    for title, desc in r2_points:
        p_t = tf_r2.add_paragraph()
        p_t.text = f"•  {title}:"
        p_t.font.name = "Calibri"
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_MAIN
        p_t.space_before = Pt(8)

        p_d = tf_r2.add_paragraph()
        p_d.text = f"   {desc}"
        p_d.font.name = "Calibri"
        p_d.font.size = Pt(9.5)
        p_d.font.color.rgb = TEXT_MUTED

    tb_s6_foot = s6.shapes.add_textbox(Inches(0.8), Inches(6.45), Inches(11.733), Inches(0.35))
    p_s6_f = tb_s6_foot.text_frame.paragraphs[0]
    p_s6_f.text = "Impact: Prevents duplicate invoice reimbursement attacks and enforces corporate financial hierarchy automatically."
    p_s6_f.font.name = "Calibri"
    p_s6_f.font.size = Pt(9.5)
    p_s6_f.font.bold = True
    p_s6_f.font.color.rgb = ACC_AMBER

    set_notes(s6, (
        "SPEAKER 3 (Database & Governance Lead):\n"
        "Here are our automated business rules. "
        "Rule 1 enforces the ₹10,000 threshold. If Alice files a claim for ₹45,000, Bob the manager sees a locked button labeled "
        "'Needs Finance Approval'. Even if Bob crafts a raw POST request, our backend inspects the amount and blocks it. "
        "Rule 2 is our 48-Hour Duplicate Scanner. If an employee accidentally or intentionally files an identical claim within "
        "48 hours, the system queries the composite index, flags the record with is_duplicate = True, and paints an amber alert badge. "
        "Rule 3 enforces mandatory rejection notes so no claim is dismissed without written justification."
    ))

    # =========================================================================
    # SLIDE 7: PERSISTENCE, RELATIONAL SCHEMA & BATCH SETTLEMENT
    # =========================================================================
    s7 = create_base_slide(
        7,
        "Persistence & ACID Transactions",
        "Relational Schema Design & Atomic Batch Settlement Pipeline",
        "Normalised relational data structures with cascading foreign keys and ACID-compliant batch disbursement."
    )

    # Left: 3 Normalized Relational Entities
    add_card(s7, Inches(0.8), Inches(1.95), Inches(5.7), Inches(4.45), border_color=ACC_EMERALD)
    tb_db = s7.shapes.add_textbox(Inches(1.0), Inches(2.05), Inches(5.3), Inches(4.2))
    tf_db = tb_db.text_frame
    tf_db.word_wrap = True

    p = tf_db.paragraphs[0]
    p.text = "RELATIONAL SCHEMA ENTITIES (3RD NORMAL FORM)"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACC_EMERALD

    entities = [
        ("Table: Users (1)", "id (PK), name, email (UNIQUE), password_hash (SHA-256), role ('EMPLOYEE'|'MANAGER'|'FINANCE'), department."),
        ("Table: ExpenseClaims (N)", "id (PK), user_id (FK -> Users.id), category, amount, description, expense_date, status ('PENDING'|'APPROVED'|'SETTLED'|'REJECTED'), is_duplicate (BOOLEAN)."),
        ("Table: AuditLogs (Immutable)", "id (PK), claim_id (FK -> ExpenseClaims.id), performed_by (FK -> Users.id), action, notes, timestamp (ISO-8601)."),
        ("Foreign Key Integrity", "Enforced on every connection via PRAGMA foreign_keys = ON; preventing orphaned records.")
    ]
    for name, schema in entities:
        p_e = tf_db.add_paragraph()
        p_e.text = f"•  {name}:"
        p_e.font.name = "Calibri"
        p_e.font.size = Pt(10)
        p_e.font.bold = True
        p_e.font.color.rgb = TEXT_MAIN
        p_e.space_before = Pt(7)

        p_s = tf_db.add_paragraph()
        p_s.text = f"   {schema}"
        p_s.font.name = "Calibri"
        p_s.font.size = Pt(9)
        p_s.font.color.rgb = TEXT_MUTED

    # Right: Batch Settlement Transaction Pipeline
    add_card(s7, Inches(6.8), Inches(1.95), Inches(5.7), Inches(4.45), border_color=ACC_VIOLET)
    tb_bch = s7.shapes.add_textbox(Inches(7.0), Inches(2.05), Inches(5.3), Inches(4.2))
    tf_bch = tb_bch.text_frame
    tf_bch.word_wrap = True

    p = tf_bch.paragraphs[0]
    p.text = "ONE-CLICK BATCH SETTLEMENT (ACID PIPELINE)"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACC_VIOLET

    bch_steps = [
        ("Step 1: Initiation", "Finance Officer clicks 'Settle All Approved' on the Treasury Dashboard."),
        ("Step 2: Atomic Lock", "Backend opens a single database transaction with conn.isolation_level."),
        ("Step 3: Query & Update", "Fetches all claims WHERE status = 'APPROVED'; executes UPDATE status = 'SETTLED' in one pass."),
        ("Step 4: Audit Emission", "Inserts corresponding AuditLogs records for every settled claim."),
        ("Step 5: Atomic Commit", "Executes conn.commit(). If any single write fails, conn.rollback() triggers immediately.")
    ]
    for st, sd in bch_steps:
        p_st = tf_bch.add_paragraph()
        p_st.text = f"✔  {st}:"
        p_st.font.name = "Calibri"
        p_st.font.size = Pt(10)
        p_st.font.bold = True
        p_st.font.color.rgb = TEXT_MAIN
        p_st.space_before = Pt(7)

        p_sd = tf_bch.add_paragraph()
        p_sd.text = f"   {sd}"
        p_sd.font.name = "Calibri"
        p_sd.font.size = Pt(9)
        p_sd.font.color.rgb = TEXT_MUTED

    tb_s7_foot = s7.shapes.add_textbox(Inches(0.8), Inches(6.45), Inches(11.733), Inches(0.35))
    p_s7_f = tb_s7_foot.text_frame.paragraphs[0]
    p_s7_f.text = "ACID Safety Guarantee: All-or-nothing batch execution prevents partial disbursement states and guarantees financial reconciliation."
    p_s7_f.font.name = "Calibri"
    p_s7_f.font.size = Pt(9.5)
    p_s7_f.font.bold = True
    p_s7_f.font.color.rgb = ACC_EMERALD

    set_notes(s7, (
        "SPEAKER 3 (Database & Governance Lead):\n"
        "This slide covers our relational persistence model and the ACID batch settlement pipeline. "
        "Our SQLite database enforces 3rd Normal Form with three primary entities: Users, ExpenseClaims, and AuditLogs. "
        "We explicitly enable foreign key enforcement on every connection using 'PRAGMA foreign_keys = ON'. "
        "On the right is our One-Click Batch Settlement feature. Instead of forcing the Finance Officer to settle 50 claims one-by-one, "
        "our system executes an atomic transaction: it selects all approved claims, transitions them to SETTLED, writes individual audit records, "
        "and commits. If the server loses power midway, the transaction rolls back cleanly with zero partial disbursements."
    ))

    # =========================================================================
    # SLIDE 8: IMMUTABLE AUDIT TRAIL & REGULATORY COMPLIANCE
    # =========================================================================
    s8 = create_base_slide(
        8,
        "Regulatory Compliance & Forensics",
        "Immutable Audit Trail Architecture & Dual Query Paths",
        "Append-only ledger architecture ensuring complete non-repudiation for Sarbanes-Oxley (SOX) compliance."
    )

    # 3-Stage Ingestion Pipeline
    add_card(s8, Inches(0.8), Inches(1.95), Inches(11.733), Inches(1.85), border_color=ACC_EMERALD)
    tb_aud = s8.shapes.add_textbox(Inches(1.0), Inches(2.05), Inches(11.333), Inches(1.65))
    tf_a = tb_aud.text_frame
    tf_a.word_wrap = True

    p = tf_a.paragraphs[0]
    p.text = "THE IMMUTABLE AUDIT EVENT PIPELINE (NON-REPUDIATION BY DESIGN)"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACC_EMERALD

    aud_flow = [
        ("1. Action Trigger", "Every lifecycle transition (SUBMISSION, APPROVAL, REJECTION, SETTLEMENT) emits an audit event payload."),
        ("2. Service Dispatch", "claim_service.py dispatches the event to audit_service.py with the actor's user_id and timestamp."),
        ("3. Append-Only Persistence", "AuditRepository executes INSERT INTO AuditLogs. ZERO UPDATE or DELETE statements exist in the repository."),
        ("4. Cryptographic Integrity", "Records are immutable; history cannot be rewritten even by database administrators.")
    ]
    for af_t, af_d in aud_flow:
        p_af = tf_a.add_paragraph()
        p_af.text = f"•  {af_t}:  {af_d}"
        p_af.font.name = "Calibri"
        p_af.font.size = Pt(9.5)
        p_af.font.color.rgb = TEXT_MAIN
        p_af.space_before = Pt(4)

    # Bottom Two Columns: Dual Query Paths
    # Left: Claim Timeline Modal
    add_card(s8, Inches(0.8), Inches(4.0), Inches(5.7), Inches(2.35), border_color=ACC_AMBER)
    tb_a1 = s8.shapes.add_textbox(Inches(1.0), Inches(4.1), Inches(5.3), Inches(2.1))
    tf_a1 = tb_a1.text_frame
    tf_a1.word_wrap = True

    p = tf_a1.paragraphs[0]
    p.text = "QUERY PATH A: CLAIM TIMELINE MODAL"
    p.font.name = "Calibri"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = ACC_AMBER

    a1_items = [
        "Scope: Granular, voucher-specific timeline history.",
        "Audience: Accessible to Employees, Managers, and Finance.",
        "Payload: Chronological list of state changes, actors, timestamps, and justification notes.",
        "User Experience: Single click on any claim row renders an interactive vertical timeline modal."
    ]
    for item in a1_items:
        p_item = tf_a1.add_paragraph()
        p_item.text = f"•  {item}"
        p_item.font.name = "Calibri"
        p_item.font.size = Pt(9)
        p_item.font.color.rgb = TEXT_MAIN
        p_item.space_before = Pt(3)

    # Right: Global Enterprise Ledger
    add_card(s8, Inches(6.8), Inches(4.0), Inches(5.7), Inches(2.35), border_color=ACC_SKY)
    tb_a2 = s8.shapes.add_textbox(Inches(7.0), Inches(4.1), Inches(5.3), Inches(2.1))
    tf_a2 = tb_a2.text_frame
    tf_a2.word_wrap = True

    p = tf_a2.paragraphs[0]
    p.text = "QUERY PATH B: GLOBAL AUDIT LEDGER"
    p.font.name = "Calibri"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = ACC_SKY

    a2_items = [
        "Scope: Company-wide tabular ledger across all corporate activities.",
        "Audience: Restricted strictly to Managers and Finance Officers.",
        "Audit Trail: Displays claim ID, employee, action type, approving officer, notes, and timestamp.",
        "Compliance: Guarantees full audit readiness for internal and external forensic investigations."
    ]
    for item in a2_items:
        p_item = tf_a2.add_paragraph()
        p_item.text = f"•  {item}"
        p_item.font.name = "Calibri"
        p_item.font.size = Pt(9)
        p_item.font.color.rgb = TEXT_MAIN
        p_item.space_before = Pt(3)

    tb_s8_foot = s8.shapes.add_textbox(Inches(0.8), Inches(6.45), Inches(11.733), Inches(0.35))
    p_s8_f = tb_s8_foot.text_frame.paragraphs[0]
    p_s8_f.text = "Forensic Assurance: Non-repudiation guarantees that any decision made by any employee or executive is permanently verifiable."
    p_s8_f.font.name = "Calibri"
    p_s8_f.font.size = Pt(9.5)
    p_s8_f.font.bold = True
    p_s8_f.font.color.rgb = ACC_EMERALD

    set_notes(s8, (
        "SPEAKER 3 (Database & Governance Lead):\n"
        "Slide 8 illustrates our regulatory audit architecture. "
        "In enterprise software, the ability to prove who did what and when is legally required under regulations like Sarbanes-Oxley. "
        "Our AuditRepository contains no UPDATE or DELETE statements. It is strictly append-only. "
        "We expose two query paths: employees can inspect the chronological milestone history of their own claim via the Timeline Modal, "
        "while executives and auditors can view the complete tabular Global Audit Ledger across all departments."
    ))

    # =========================================================================
    # SLIDE 9: LIVE DEMONSTRATION PLAYBOOK (2-MINUTE WALKTHROUGH)
    # =========================================================================
    s9 = create_base_slide(
        9,
        "System Verification & Walkthrough",
        "Live System Demonstration Playbook: 4-Phase Persona Walkthrough",
        "Demonstrating end-to-end functionality across Employee, Manager, and Finance roles on the running server."
    )

    demo_stages = [
        ("PHASE 1: EMPLOYEE", "Alice Jenkins (Engineering)", ACC_SKY, [
            "Select 'Alice Jenkins' in Header Role Switcher.",
            "Click '+ Submit New Claim'.",
            "Fill ₹4,250 for Travel; submit claim.",
            "Observe live 48h duplicate warning badge."
        ]),
        ("PHASE 2: MANAGER", "Bob Martinez (Engineering)", ACC_AMBER, [
            "Switch role to 'Bob Martinez'.",
            "Inspect Department Approval Queue.",
            "Observe ₹45,000 claim locked ('Needs Finance').",
            "Click 'Reject' on a claim; submit mandatory justification."
        ]),
        ("PHASE 3: FINANCE", "Carol Vance (Treasury)", ACC_EMERALD, [
            "Switch role to 'Carol Vance'.",
            "Authorize high-value claim (> ₹10k).",
            "Click 'Settle All Approved (₹52,000)' button.",
            "Observe atomic batch status update to SETTLED."
        ]),
        ("PHASE 4: AUDIT & API", "Audit & OpenAPI Docs", ACC_VIOLET, [
            "Open Claim Timeline Modal on Alice's voucher.",
            "Switch to Global Audit Ledger view.",
            "Navigate to http://127.0.0.1:8000/docs.",
            "Execute live Swagger API call in OpenAPI UI."
        ])
    ]

    dm_w = Inches(2.7)
    dm_h = Inches(4.35)
    dm_gap = Inches(0.3)

    for i, (p_phase, p_user, acc_col, steps) in enumerate(demo_stages):
        left = start_l + i * (dm_w + dm_gap)
        add_card(s9, left, Inches(1.95), dm_w, dm_h, border_color=acc_col)

        tb_dm = s9.shapes.add_textbox(left + Inches(0.15), Inches(2.05), dm_w - Inches(0.3), dm_h - Inches(0.2))
        tf_dm = tb_dm.text_frame
        tf_dm.word_wrap = True

        p1 = tf_dm.paragraphs[0]
        p1.text = p_phase
        p1.font.name = "Calibri"
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = acc_col

        p2 = tf_dm.add_paragraph()
        p2.text = p_user
        p2.font.name = "Calibri"
        p2.font.size = Pt(9.5)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN
        p2.space_before = Pt(2)

        for step in steps:
            p_s = tf_dm.add_paragraph()
            p_s.text = f"➔  {step}"
            p_s.font.name = "Calibri"
            p_s.font.size = Pt(9.5)
            p_s.font.color.rgb = TEXT_MUTED
            p_s.space_before = Pt(8)

    tb_s9_foot = s9.shapes.add_textbox(Inches(0.8), Inches(6.45), Inches(11.733), Inches(0.35))
    p_s9_f = tb_s9_foot.text_frame.paragraphs[0]
    p_s9_f.text = "Live Execution Endpoint: http://127.0.0.1:8000  •  Interactive Swagger Documentation: http://127.0.0.1:8000/docs"
    p_s9_f.font.name = "Calibri"
    p_s9_f.font.size = Pt(9.5)
    p_s9_f.font.bold = True
    p_s9_f.font.color.rgb = ACC_EMERALD

    set_notes(s9, (
        "DEMO LEAD (Any Teammate / Entire Team):\n"
        "Professor, we will now transition to our 2-minute live software demonstration. "
        "We will execute four rapid scenarios: "
        "First, as Alice Jenkins, we submit a claim to demonstrate real-time duplicate checking. "
        "Second, as Bob Martinez, we show how the system locks Bob out from approving claims over ₹10,000. "
        "Third, as Carol Vance in Finance, we approve the high-value expense and execute the One-Click Batch Settlement. "
        "Finally, we open the immutable audit timeline and inspect the live Swagger OpenAPI documentation."
    ))

    # =========================================================================
    # SLIDE 10: AUTOMATED TEST SUITE & CAPSTONE CONCLUSION
    # =========================================================================
    s10 = create_base_slide(
        10,
        "Quality Assurance & Conclusion",
        "Automated Test Suite (7/7 Passing) & Architectural Conclusion",
        "Continuous integration verification and summary of key enterprise software engineering competencies."
    )

    # Top: Test Suite Grid (7 Passing Tests)
    tests = [
        ("Test 01", "Database Schema & Seeder", "PASSED", ACC_SKY),
        ("Test 02", "48h Duplicate Scanner", "PASSED", ACC_AMBER),
        ("Test 03", "₹10k Approval Limit", "PASSED", ACC_AMBER),
        ("Test 04", "Mandatory Rejection Note", "PASSED", ACC_ROSE),
        ("Test 05", "Claim State Machine", "PASSED", ACC_EMERALD),
        ("Test 06", "ACID Batch Settlement", "PASSED", ACC_VIOLET),
        ("Test 07", "Audit Trail Query Scopes", "PASSED", ACC_EMERALD)
    ]

    t_w = Inches(1.58)
    t_h = Inches(1.2)
    t_gap = Inches(0.11)

    for i, (t_id, t_name, t_stat, acc_col) in enumerate(tests):
        left = start_l + i * (t_w + t_gap)
        add_card(s10, left, Inches(1.95), t_w, t_h, border_color=acc_col)

        tb_t = s10.shapes.add_textbox(left + Inches(0.08), Inches(2.05), t_w - Inches(0.16), t_h - Inches(0.2))
        tf_t = tb_t.text_frame
        tf_t.word_wrap = True

        p1 = tf_t.paragraphs[0]
        p1.text = t_id
        p1.font.name = "Calibri"
        p1.font.size = Pt(9.5)
        p1.font.bold = True
        p1.font.color.rgb = acc_col

        p2 = tf_t.add_paragraph()
        p2.text = t_name
        p2.font.name = "Calibri"
        p2.font.size = Pt(8.5)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN
        p2.space_before = Pt(2)

        p3 = tf_t.add_paragraph()
        p3.text = f"✔ {t_stat}"
        p3.font.name = "Calibri"
        p3.font.size = Pt(9)
        p3.font.bold = True
        p3.font.color.rgb = ACC_EMERALD
        p3.space_before = Pt(3)

    # Center: 7/7 Passing Banner
    add_card(s10, Inches(0.8), Inches(3.3), Inches(11.733), Inches(0.55), border_color=ACC_EMERALD)
    tb_b = s10.shapes.add_textbox(Inches(1.0), Inches(3.35), Inches(11.333), Inches(0.45))
    p_b = tb_b.text_frame.paragraphs[0]
    p_b.alignment = PP_ALIGN.CENTER
    p_b.text = "✔ ALL 7 AUTOMATED DOMAIN TEST SUITES PASSING (0.19s EXECUTION TIME • 100% SUCCESS RATE)"
    p_b.font.name = "Calibri"
    p_b.font.size = Pt(11)
    p_b.font.bold = True
    p_b.font.color.rgb = ACC_EMERALD

    # Bottom: 4 Architectural Takeaways
    add_card(s10, Inches(0.8), Inches(4.0), Inches(11.733), Inches(2.35), border_color=PANEL_BORDER)
    tb_con = s10.shapes.add_textbox(Inches(1.0), Inches(4.1), Inches(11.333), Inches(2.1))
    tf_c = tb_con.text_frame
    tf_c.word_wrap = True

    p = tf_c.paragraphs[0]
    p.text = "CORE CAPSTONE ARCHITECTURAL TAKEAWAYS:"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACC_SKY

    takeaways = [
        ("Decoupled Separation of Concerns", "Presentation, Controller, Service, and Repository layers communicate exclusively via typed DTO contracts, eliminating domain leakage."),
        ("Zero-Build Lightweight Portability", "Zero npm or webpack build tooling needed; self-contained FastAPI server and SQLite3 database runs seamlessly on any environment."),
        ("Algorithmic Fiscal Governance", "Dual-tier approval limits (₹10k) and 48-hour duplicate detection eliminate corporate fraud and human oversight errors programmatically."),
        ("Non-Repudiation by Design", "Strict append-only audit trail guarantees complete transparency, legal defensibility, and compliance with enterprise financial governance standards.")
    ]

    for title, desc in takeaways:
        p_t = tf_c.add_paragraph()
        p_t.text = f"•  {title}:  {desc}"
        p_t.font.name = "Calibri"
        p_t.font.size = Pt(9.5)
        p_t.font.color.rgb = TEXT_MAIN
        p_t.space_before = Pt(3)

    tb_s10_foot = s10.shapes.add_textbox(Inches(0.8), Inches(6.45), Inches(11.733), Inches(0.35))
    p_s10_f = tb_s10_foot.text_frame.paragraphs[0]
    p_s10_f.text = "Thank you, Respected Professor and Evaluators. The team is now open for Viva Voce questions."
    p_s10_f.font.name = "Calibri"
    p_s10_f.font.size = Pt(10)
    p_s10_f.font.bold = True
    p_s10_f.font.color.rgb = ACC_EMERALD

    set_notes(s10, (
        "SPEAKER 1 (Team Lead):\n"
        "In conclusion, our Corporate Expense Claim & Reimbursement Portal demonstrates complete mastery of "
        "Building Enterprise Applications concepts. "
        "Our automated test suite runs 7 comprehensive domain tests in under 0.2 seconds with a 100% pass rate. "
        "We have achieved decoupled multi-tier architecture, zero-dependency portability, algorithmic fiscal governance, "
        "and non-repudiable auditability. "
        "We thank you for your time and guidance, and we welcome any questions from the Professor."
    ))

    prs.save(output_path)
    print(f"[SUCCESS] Generated world-class executive deck: {output_path}")

if __name__ == "__main__":
    out_file = "C:/Users/p1022/.gemini/antigravity/scratch/corporate-expense-portal/corporate_expense_portal_presentation.pptx"
    if len(sys.argv) > 1:
        out_file = sys.argv[1]
    build_executive_deck(out_file)
