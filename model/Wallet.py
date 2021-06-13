class Wallet:
    def __init__(self, owner, account_balance, SMS_units = {}, SI_units = {}):
        self.owner = owner
        self.account_balance = account_balance
        self.SMS_units = SMS_units
        self.SI_units = SI_units

    def __str__(self):
        return f'Wallet{{account_balance={self.account_balance}, SMS_units={self.SMS_units}, SI_units={self.SI_units}}}'