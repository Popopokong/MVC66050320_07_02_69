from model.claim import Claim
class GeneralClaim(Claim):
    def calculate_compensation(self):
        return min(self.income, 20000)