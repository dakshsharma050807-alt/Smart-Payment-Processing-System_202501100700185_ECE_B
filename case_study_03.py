from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self, user_name):
        self.user_name = user_name
        self.original_amount = 0
        self.final_amount = 0

    @abstractmethod
    def pay(self, amount):
        pass


    def generate_receipt(self):
        print("User:", self.user_name)
        print("Original Amount:", self.original_amount)
        print("Final Amount Paid:", self.final_amount)
        print("---------------------------")


class CreditCardPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        gateway_fee = amount * 0.02
        gst = gateway_fee * 0.18
        self.final_amount = amount + gateway_fee + gst
        self.generate_receipt()


class UPIPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        cashback = 0
        if amount > 1000:
            cashback = 50
        self.final_amount = amount - cashback
        self.generate_receipt()


class PayPalPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        self.final_amount = amount + (amount * 0.03) + 20
        self.generate_receipt()


class WalletPayment(Payment):
    def __init__(self, user_name, balance):
        super().__init__(user_name)
        self.balance = balance

    def pay(self, amount):
        self.original_amount = amount
        if amount > self.balance:
            print("Transaction Failed: Not enough balance for", self.user_name)
        else:
            self.balance = self.balance - amount
            self.final_amount = amount
            self.generate_receipt()


def process_payment(payment_object, amount):
    payment_object.pay(amount)


p1 = CreditCardPayment("Alice")
p2 = UPIPayment("Bob")
p3 = PayPalPayment("Charlie")
p4 = WalletPayment("Diana", 500)

process_payment(p1, 1000)
process_payment(p2, 1200)
process_payment(p3, 1000)
process_payment(p4, 200)
