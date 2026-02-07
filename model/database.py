# models/database.py
import sqlite3

DB_NAME = "compensation.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Claimants (
        claimant_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        monthly_income REAL,
        claimant_type TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Claims (
        claim_id TEXT PRIMARY KEY,
        claimant_id INTEGER,
        claim_date TEXT,
        status TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Policies (
        policy_id INTEGER PRIMARY KEY,
        max_amount REAL,
        income_condition TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Compensations (
        claim_id TEXT,
        amount REAL,
        calculated_date TEXT
    )
    """)

    conn.commit()
    conn.close()
