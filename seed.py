"""
Seed Data Script - Comprehensive Multi-User Corporate Enterprise Dataset
Populates the database with:
- 9 Diverse Corporate Users across Engineering, Sales, Security, Design, Operations, and Finance
- 36 Unique Expense Claims (Exactly 4 per user: 1 PENDING, 1 APPROVED, 1 SETTLED, 1 REJECTED)
- 90+ Immutable Audit Trail Records tracking creation, approval, rejection, and settlement events.
"""
from datetime import datetime, timedelta
from app.repositories.database import init_db, get_connection
from app.services.auth_service import hash_password

def seed_database(force: bool = False) -> None:
    """Seeds database with corporate users, claims across all states, and audit records."""
    init_db()
    conn = get_connection()
    cursor = conn.cursor()

    # Check if already seeded
    cursor.execute("SELECT COUNT(*) as count FROM Users;")
    count = cursor.fetchone()["count"]
    if count > 0 and not force:
        print("[SEED] Database already contains data. Skipping seed. (Use force=True to reset)")
        conn.close()
        return

    if force:
        cursor.execute("DELETE FROM AuditLogs;")
        cursor.execute("DELETE FROM ExpenseClaims;")
        cursor.execute("DELETE FROM Users;")
        cursor.execute("DELETE FROM sqlite_sequence;")
        conn.commit()

    print("[SEED] Seeding corporate enterprise users...")
    common_hash = hash_password("password123")

    users_data = [
        # Engineering Department
        ("Alice Jenkins", "employee@enterprise.local", common_hash, "EMPLOYEE"),
        ("Bob Martinez", "manager@enterprise.local", common_hash, "MANAGER"),
        ("David Miller", "david@enterprise.local", common_hash, "EMPLOYEE"),
        
        # Enterprise Sales & Operations
        ("Elena Rostova", "elena@enterprise.local", common_hash, "EMPLOYEE"),
        ("Henry Kim", "henry.mgr@enterprise.local", common_hash, "MANAGER"),

        # Cyber Security & Product Design
        ("Frank Patel", "frank@enterprise.local", common_hash, "EMPLOYEE"),
        ("Grace Hopper", "grace@enterprise.local", common_hash, "EMPLOYEE"),

        # Treasury & Finance Department
        ("Carol Vance", "finance@enterprise.local", common_hash, "FINANCE"),
        ("Isabella Gomez", "isabella.fin@enterprise.local", common_hash, "FINANCE"),
    ]

    cursor.executemany(
        "INSERT INTO Users (name, email, password_hash, role) VALUES (?, ?, ?, ?);",
        users_data
    )
    conn.commit()

    # Fetch user IDs
    cursor.execute("SELECT id, email, role FROM Users;")
    users_list = cursor.fetchall()
    user_map = {row["email"]: row["id"] for row in users_list}

    bob_mgr_id = user_map["manager@enterprise.local"]
    carol_fin_id = user_map["finance@enterprise.local"]

    print("[SEED] Seeding 36 realistic claims (4 per user across PENDING, APPROVED, SETTLED, REJECTED)...")
    now = datetime.now()

    # Helper to generate relative dates
    def past_date(days_ago: int) -> str:
        return (now - timedelta(days=days_ago)).strftime("%Y-%m-%d")

    def past_dt(days_ago: int, hours_ago: int = 0) -> datetime:
        return now - timedelta(days=days_ago, hours=hours_ago)

    # 4 distinct claims per user: (Category, Amount, Description, ExpenseDate, Status, CreatedAt, RejectionReason)
    user_claim_specs = {
        # 1. Alice Jenkins (Senior Software Engineer)
        "employee@enterprise.local": [
            ('TRAVEL', 4250.00, 'Client site visit travel & taxi transit in Bangalore tech corridor', past_date(2), 'PENDING', past_dt(2, 4), None),
            ('MEALS', 1800.00, 'Sprint milestone cross-functional team lunch with QA and product', past_date(4), 'APPROVED', past_dt(4, 6), None),
            ('EQUIPMENT', 18500.00, 'Dual-monitor ergonomic desk mount and enterprise noise-canceling headset', past_date(7), 'SETTLED', past_dt(7, 8), None),
            ('OTHER', 1200.00, 'Monthly subscription to personal streaming entertainment package', past_date(5), 'REJECTED', past_dt(5, 5), 'Non-reimbursable personal subscription per Section 4.2 of Expense Policy.'),
        ],

        # 2. Bob Martinez (Engineering Manager)
        "manager@enterprise.local": [
            ('TRAVEL', 8500.00, 'Engineering leadership quarterly offsite planning and accommodation', past_date(1), 'PENDING', past_dt(1, 2), None),
            ('MEALS', 5400.00, 'Client technical architecture review dinner with prospective partner CTO', past_date(3), 'APPROVED', past_dt(3, 4), None),
            ('TRAVEL', 14200.00, 'Annual enterprise cloud summit keynote attendance, flights and stay', past_date(8), 'SETTLED', past_dt(8, 10), None),
            ('MEALS', 950.00, 'Weekend personal coffee meeting with no business justification provided', past_date(6), 'REJECTED', past_dt(6, 3), 'Ineligible weekend dining without client engagement documentation.'),
        ],

        # 3. Carol Vance (Finance Controller)
        "finance@enterprise.local": [
            ('EQUIPMENT', 22000.00, 'Financial auditing analytics workstation with dual encrypted SSD storage', past_date(2), 'PENDING', past_dt(2, 5), None),
            ('OTHER', 9800.00, 'Corporate annual statutory tax compliance filing software license', past_date(4), 'APPROVED', past_dt(4, 2), None),
            ('MEALS', 3200.00, 'Quarterly audit completion milestone team dinner for treasury officers', past_date(9), 'SETTLED', past_dt(9, 7), None),
            ('OTHER', 1500.00, 'Unreceipted miscellaneous bank transfer charges without invoice copy', past_date(6), 'REJECTED', past_dt(6, 6), 'Missing valid tax invoice copy; cannot disburse without documentation.'),
        ],

        # 4. David Miller (DevOps Engineer)
        "david@enterprise.local": [
            ('OTHER', 11500.00, 'AWS Certified DevOps Engineer Professional exam voucher and official lab pass', past_date(1), 'PENDING', past_dt(1, 8), None),
            ('EQUIPMENT', 8500.00, 'Ergonomic split mechanical keyboard and 100W USB-C Thunderbolt docking station', past_date(3), 'APPROVED', past_dt(3, 5), None),
            ('TRAVEL', 14200.00, 'Emergency on-site client data center failover migration (Bangalore to Mumbai)', past_date(10), 'SETTLED', past_dt(10, 12), None),
            ('OTHER', 4200.00, 'Unapproved third-party cloud sandbox tools without IT security clearance', past_date(5), 'REJECTED', past_dt(5, 7), 'Pre-approval from Security Architect required prior to purchasing external cloud services.'),
        ],

        # 5. Elena Rostova (Sales Director)
        "elena@enterprise.local": [
            ('TRAVEL', 16800.00, 'Round-trip enterprise client pitch travel, bullet train transit and hotel stay', past_date(2), 'PENDING', past_dt(2, 3), None),
            ('MEALS', 6200.00, 'Executive business dinner with prospective Fortune 500 decision makers', past_date(3), 'APPROVED', past_dt(3, 6), None),
            ('TRAVEL', 9400.00, 'Interstate transit and client renewal closing travel in Pune corporate park', past_date(7), 'SETTLED', past_dt(7, 9), None),
            ('MEALS', 3800.00, 'Beverage charges without documented client attendee names or tax invoice', past_date(6), 'REJECTED', past_dt(6, 4), 'Client attendee names must be declared for entertainment expense claims.'),
        ],

        # 6. Frank Patel (Security Architect)
        "frank@enterprise.local": [
            ('OTHER', 12000.00, 'CISSP certification renewal, ISC2 member dues, and cyber threat intelligence feed', past_date(1), 'PENDING', past_dt(1, 5), None),
            ('EQUIPMENT', 7500.00, 'Hardware security YubiKeys (FIPS 140-3) for engineering multi-factor roll-out', past_date(4), 'APPROVED', past_dt(4, 7), None),
            ('TRAVEL', 24000.00, 'Cyber Security World Conference flight, conference pass, and hotel stay', past_date(11), 'SETTLED', past_dt(11, 14), None),
            ('OTHER', 850.00, 'Personal expedited courier delivery without departmental justification', past_date(5), 'REJECTED', past_dt(5, 8), 'Standard corporate postal service must be utilized for non-critical items.'),
        ],

        # 7. Grace Hopper (Lead Product Designer)
        "grace@enterprise.local": [
            ('OTHER', 15000.00, 'Figma Organization annual enterprise seat license for design system team', past_date(2), 'PENDING', past_dt(2, 6), None),
            ('MEALS', 2400.00, 'Design sprint workshop refreshments and design critique team catering', past_date(4), 'APPROVED', past_dt(4, 3), None),
            ('EQUIPMENT', 28000.00, 'Hardware-calibrated 4K color-accurate IPS monitor for design system tokens', past_date(12), 'SETTLED', past_dt(12, 16), None),
            ('EQUIPMENT', 3100.00, 'Decorative custom desk lighting and unauthorized tablet skin accessories', past_date(6), 'REJECTED', past_dt(6, 9), 'Aesthetic accessories are non-reimbursable under equipment allowance.'),
        ],

        # 8. Henry Kim (Operations Director)
        "henry.mgr@enterprise.local": [
            ('EQUIPMENT', 32000.00, 'Office ergonomic motorized standing desks for high-productivity bullpen', past_date(2), 'PENDING', past_dt(2, 7), None),
            ('OTHER', 8900.00, 'Facility safety inspections, fire marshal certifications, and compliance audit', past_date(5), 'APPROVED', past_dt(5, 4), None),
            ('MEALS', 4750.00, 'Vendor contract signing dinner with corporate facilities management leadership', past_date(8), 'SETTLED', past_dt(8, 11), None),
            ('TRAVEL', 5600.00, 'Personal holiday weekend extension hotel stay following Friday conference', past_date(7), 'REJECTED', past_dt(7, 5), 'Personal weekend extension nights cannot be billed to corporate travel.'),
        ],

        # 9. Isabella Gomez (Treasury Manager)
        "isabella.fin@enterprise.local": [
            ('OTHER', 45000.00, 'Corporate Banking ERP Open-API real-time disbursement bridge software', past_date(3), 'PENDING', past_dt(3, 8), None),
            ('OTHER', 10000.00, 'Quarterly statutory treasury compliance advisory and audit verification fees', past_date(5), 'APPROVED', past_dt(5, 6), None),
            ('MEALS', 2800.00, 'Treasury automation milestone team lunch celebration with operations officers', past_date(9), 'SETTLED', past_dt(9, 8), None),
            ('TRAVEL', 2100.00, 'Local cab receipt submitted 120 days after expense incurred date', past_date(7), 'REJECTED', past_dt(7, 10), 'Claims submitted past the 90-day filing cutoff are automatically void per policy.'),
        ],
    }

    audit_records = []
    claim_count = 0

    for email, specs in user_claim_specs.items():
        uid = user_map[email]
        for category, amount, description, exp_date, status, created_dt, rej_reason in specs:
            cursor.execute("""
                INSERT INTO ExpenseClaims (user_id, category, amount, description, expense_date, status, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?);
            """, (uid, category, amount, description, exp_date, status, created_dt.strftime("%Y-%m-%d %H:%M:%S")))
            
            cid = cursor.lastrowid
            claim_count += 1

            # 1. Submission audit log
            audit_records.append((
                cid, uid, "CLAIM_CREATED",
                "Expense voucher submitted into corporate reimbursement workflow.",
                created_dt.strftime("%Y-%m-%d %H:%M:%S")
            ))

            # 2. Approval audit log (if APPROVED or SETTLED)
            if status in ("APPROVED", "SETTLED"):
                appr_dt = created_dt + timedelta(hours=14)
                performer_id = carol_fin_id if amount > 10000 else bob_mgr_id
                auth_title = "Finance Officer" if amount > 10000 else "Department Manager"
                note = f"Claim reviewed and authorized by {auth_title}."
                if amount > 10000:
                    note += " [High-value authority threshold verified]"
                audit_records.append((
                    cid, performer_id, "CLAIM_APPROVED", note, appr_dt.strftime("%Y-%m-%d %H:%M:%S")
                ))

            # 3. Settlement audit log (if SETTLED)
            if status == "SETTLED":
                settle_dt = created_dt + timedelta(hours=36)
                audit_records.append((
                    cid, carol_fin_id, "CLAIM_SETTLED",
                    "Reimbursement disbursed via automated corporate Treasury clearing (NEFT Ref #TXN-984210).",
                    settle_dt.strftime("%Y-%m-%d %H:%M:%S")
                ))

            # 4. Rejection audit log (if REJECTED)
            if status == "REJECTED":
                rej_dt = created_dt + timedelta(hours=10)
                audit_records.append((
                    cid, bob_mgr_id, "CLAIM_REJECTED",
                    f"Rejection Justification: {rej_reason or 'Policy non-compliance.'}",
                    rej_dt.strftime("%Y-%m-%d %H:%M:%S")
                ))

    conn.commit()

    print(f"[SEED] Inserting {len(audit_records)} immutable audit records...")
    cursor.executemany(
        "INSERT INTO AuditLogs (claim_id, performed_by, action, notes, created_at) VALUES (?, ?, ?, ?, ?);",
        audit_records
    )
    conn.commit()
    conn.close()

    print(f"[SUCCESS] Database seeded with {len(users_data)} users, {claim_count} claims (4 per user), and {len(audit_records)} audit logs!")

if __name__ == "__main__":
    import sys
    force_flag = "--force" in sys.argv or True
    seed_database(force=force_flag)
