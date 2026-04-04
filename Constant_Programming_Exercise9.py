class BankAccount:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    # Deposit money
    def deposit(self, value):
        self.amount += value

    # Withdraw money
    def withdraw(self, value):
        if value > self.amount:
            print("Not enough balance!")
        else:
            self.amount -= value

    # Adjust interest rate
    def set_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    # Get balance
    def get_balance(self):
        return self.amount

    # Calculate interest
    def calculate_interest(self, days):
        return self.amount * self.interest_rate * days / 365

    # Display account info
    def __str__(self):
        return f"{self.name} | Balance: ${self.amount} | Interest Rate: {self.interest_rate}"


def test_bank():
    account = BankAccount("Kegeler", "9876543", 2000, 0.05)

    print("Initial account")
    print(account)

    account.deposit(118000000)
    print("\nAfter deposit:")
    print(account)

    account.withdraw(300000)
    print("\nAfter withdraw:")
    print(account)

    account.withdraw(200000000)

    account.set_interest_rate(0.1)
    print("\nAfter changing interest rate:")
    print(account)

    print("\nCurrent balance:", account.get_balance())

    days = 30
    interest = account.calculate_interest(days)
    print(f"\nInterest for {days} days: ${interest:.2f}")


if __name__ == "__main__":
    test_bank()
