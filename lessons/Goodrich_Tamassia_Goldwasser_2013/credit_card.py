# Goodrich, Tamassia, Goldwasser (2013) Code Fragments 2.1, 2.2, 2.3 on pages 70-71, 73
class CreditCard:
    """A consumer credit class."""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.

        The initial balance is zero.

        customer the name of the customer (e.g. 'John Bowman')
        bank     the name of the bank (e.g. 'California Savings')
        acnt     the account identifier (e.g. '5391 0375 9387 5309')
        limit    credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """Charge given price to card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:     # if charge would exceed limit
            return False                            # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount

    def _set_balance(self, new_balance):
        """Set new balance."""
        self._balance = new_balance

if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('Michael Stewart', 'California Federal', '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('Carl Johanssen', 'California Finance', '5391 0475 1087 5309', 5000))
    wallet.append(CreditCard('Stanley Mueller', 'California Exchange', '1404 0475 1711 5189', 10000))

    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
        wallet[3].charge(4*val)

    for c in range(len(wallet)):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
        wallet[c]._set_balance((c+1)*123)
        print('Set new balance =', wallet[c].get_balance())
        print()
