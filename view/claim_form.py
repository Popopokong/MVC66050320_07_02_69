def input_claim_data():
    print("\n กรอกข้อมูลคำขอเยียวยา ")
    fname = input("ชื่อ")
    lname = input("นามสกุล: ")
    income = float(input("รายได้ต่อเดือน บาท: "))
    
    return fname , lname, income
def show_compensation(amount):
    print(f"\n ท่านมีสิทธิได้รับเงินเยียวยาจำนวน {amount:,.2f} บาท ")
    