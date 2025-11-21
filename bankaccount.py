class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display(self):
        print("\n----- Account Details -----")
        print(f"Account Number: {self.acc_no}")
        print(f"Name: {self.name}")
        print(f"Account Type: {self.acc_type}")
        print(f"Balance: ₹{self.balance}")


# Example usage:
acc1 = BankAccount(12345, "Akshai", "Savings", 1000)

acc1.display()
acc1.deposit(500)
acc1.withdraw(300)
acc1.display()

