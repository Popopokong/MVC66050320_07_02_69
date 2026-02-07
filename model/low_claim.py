from model.claim import Claim


class LowClaim(Claim):
    def calculate_compensation(self):
         return max(self.income, 6500)
