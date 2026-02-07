from model.general_claim import GeneralClaim
from model.low_claim import LowClaim
from model.high_claim import HighClaim
from model.database import get_connection
from datetime import datetime
import random

class ClaimController:

    def create_claim_web(self, form):
        fname = form["fname"]
        lname = form["lname"]
        income = float(form["income"])

        if income < 6500:
            model = LowClaim(income)
            ctype = "LOW"
        elif income >= 50000:
            model = HighClaim(income)
            ctype = "HIGH"
        else:
            model = GeneralClaim(income)
            ctype = "GENERAL"

        amount = model.calculate_compensation()

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO Claimants (first_name,last_name,monthly_income,claimant_type) VALUES (?,?,?,?)",
            (fname, lname, income, ctype)
        )

        claimant_id = cur.lastrowid
        claim_id = str(random.randint(10000000, 99999999))
        today = datetime.now().strftime("%Y-%m-%d")

        cur.execute("INSERT INTO Claims VALUES (?,?,?,?)",
                    (claim_id, claimant_id, today, "CALCULATED"))

        cur.execute("INSERT INTO Compensations VALUES (?,?,?)",
                    (claim_id, amount, today))

        conn.commit()
        conn.close()

        # return both calculated amount and calculation date for the web UI
        return amount, today

    def list_claims_web(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Claims")
        data = cur.fetchall()
        conn.close()
        return data
