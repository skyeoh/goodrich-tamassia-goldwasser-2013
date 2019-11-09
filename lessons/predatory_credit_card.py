# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 2.7 on page 85
from credit_card import CreditCard

class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.

        The initial balance is zero.

        customer the name of the customer (e.g. 'John Bowman')
        bank     the name of the bank (e.g. 'California Savings')
        acnt     the account identifier (e.g. '5391 0375 9387 5309')
        limit    credit limit (measured in dollars)
        apr      annual percentage rate (e.g. 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)    # call super constructor
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """
        success = super().charge(price)                  # call inherited method
        if not success:
            new_balance = super().get_balance() + 5      # assess penalty
            super()._set_balance(new_balance)            # set new balance
        return success                                   # caller expects return value

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        balance = super().get_balance()
        if balance > 0:
            # if positive value, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            super()._set_balance(balance*monthly_factor)

if __name__ == "__main__":
    wallet = []
    wallet.append(PredatoryCreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500, 0.0825))
    wallet.append(PredatoryCreditCard('Michael Stewart', 'California Federal', '3485 0399 3395 1954', 3500, 0.1))
    wallet.append(PredatoryCreditCard('Carl Johanssen', 'California Finance', '5391 0475 1087 5309', 5000, 0.2))
    wallet.append(PredatoryCreditCard('Stanley Mueller', 'California Exchange', '1404 0475 1711 5189', 10000, 0.008))

    count = [0,0,0,0]
    for i in range(1,12):
        price = 1000
        if not wallet[0].charge(price):
            count[0]+=1
        if not wallet[1].charge(price):
            count[1]+=1
        if not wallet[2].charge(price):
            count[2]+=1
        if not wallet[3].charge(price):
            count[3]+=1
    print('No. of times the credit limit is exceeded:', count)
    print()

    for c in range(len(wallet)):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        for i in range(12):
            wallet[c].process_month()
        print('Balance (after APR) =', wallet[c].get_balance())
        print()
