class Claim:
    def __init__(self, income):
        self.income = income
    def calculate_compensation(self):
        raise NotImplementedError()