import random
from datetime import datetime
from model.database import get_connection
from model.low_claim import LowClaim
from model.high_claim import HighClaim
from model.general_claim import GeneralClaim
from view.claim_form import input_claim_data, show_compensation
from view import claim_list


class ClaimController:
    """Controller for creating and listing claims."""

    def create_claim(self):
        fname, lname, income = input_claim_data()

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
        show_compensation(amount)

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO Claimants (first_name,last_name,monthly_income,claimant_type) VALUES (?,?,?,?)",
            (fname, lname, income, ctype)
        )
        claimant_id = cur.lastrowid

        claim_id = str(random.randint(10000000, 99999999))
        today = datetime.now().strftime("%Y-%m-%d")

        cur.execute(
            "INSERT INTO Claims VALUES (?,?,?,?)",
            (claim_id, claimant_id, today, "CALCULATED")
        )

        cur.execute(
            "INSERT INTO Compensations VALUES (?,?,?)",
            (claim_id, amount, today)
        )

        conn.commit()
        conn.close()

        print("บันทึกคำขอเรียบร้อย\n")

    def list_claims(self):
        """Fetch claims from the DB and show them via the view helper."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Claims")
        claims = cur.fetchall()
        conn.close()

        # call the view function from the claim_list module to avoid name collision
        claim_list.show_claim_list(claims)
