from model.claim import Claim


class HighClaim(Claim):
    def calculate_compensation(self):
        amount = self.income / 5
        return min(amount, 20000)