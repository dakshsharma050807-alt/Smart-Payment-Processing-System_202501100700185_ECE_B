from abc import ABC, abstractmethod

# 1. [span_2](start_span)Abstract Base Class[span_2](end_span)
class Payment(ABC):
    def __init__(self, user_name):
        self.user_name = user_name
        self.original_amount = 0
        self.final_amount = 0

    @abstractmethod
    def pay(self, amount):
        pass

    # [span_3](start_span)Concrete method to print the receipt[span_3](end_span)
    def generate_receipt(self):
        print("User:", self.user_name)
        print("Original Amount:", self.original_amount)
        print("Final Amount Paid:", self.final_amount)
        print("---------------------------")

# 2. [span_4](start_span)Credit Card: Fee + GST[span_4](end_span)
class CreditCardPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        gateway_fee = amount * 0.02
        gst = gateway_fee * 0.18
        self.final_amount = amount + gateway_fee + gst
        self.generate_receipt()

# 3. [span_5](start_span)UPI: Cashback if amount > 1000[span_5](end_span)
class UPIPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        cashback = 0
        if amount > 1000:
            cashback = 50
        self.final_amount = amount - cashback
        self.generate_receipt()

# 4. [span_6](start_span)PayPal: Fee + Fixed charge[span_6](end_span)
class PayPalPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        self.final_amount = amount + (amount * 0.03) + 20
        self.generate_receipt()

# 5. [span_7](start_span)Wallet: Check balance before paying[span_7](end_span)
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

# 6. [span_8](start_span)Function to demonstrate polymorphism[span_8](end_span)
def process_payment(payment_object, amount):
    payment_object.pay(amount)

# -[span_9](start_span)-- Test the system ---[span_9](end_span)
p1 = CreditCardPayment("Alice")
p2 = UPIPayment("Bob")
p3 = PayPalPayment("Charlie")
p4 = WalletPayment("Diana", 500)

process_payment(p1, 1000)
process_payment(p2, 1200)
process_payment(p3, 1000)
process_payment(p4, 200)