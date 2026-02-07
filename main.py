from model.database import init_db
from controllers.claim_controller import ClaimController
from auth.auth import login

def main():
    init_db()
    controller = ClaimController()
    role = login()

    if role == "citizen":
        controller.create_claim()
        controller.list_claims()
    elif role == "staff":
        controller.list_claims()
    else:
        print("ผู้ใช้ไม่ถูกต้อง")

if __name__ == "__main__":
    main()