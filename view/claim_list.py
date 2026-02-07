def show_claim_list(claims):
    print("\n=== รายการคำขอเยียวยาทั้งหมด")
    for c in claims :
        print(f"Claim ID : {c[0]} | Status: {c[3]}")