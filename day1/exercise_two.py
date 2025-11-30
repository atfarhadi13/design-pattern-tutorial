# Encapsulated Payment Class
from datetime import datetime


class Payment:
    def __init__(self, amount: float, currency: str = "USD", method: str = "card", is_paid: bool = False):
        self.__amount = float(amount)   # 🔒 private attribute
        self.currency = currency
        self.method = method
        self.is_paid = is_paid
        self.paid_at: datetime | None = None

    # ✅ Getter for the private amount
    def get_amount(self) -> float:
        return self.__amount

    # ✅ Add a tip safely (no direct external modification)
    def add_tip(self, tip: float):
        if tip <= 0:
            raise ValueError("Tip must be positive.")
        self.__amount += float(tip)

    def mark_paid(self):
        self.is_paid = True
        self.paid_at = datetime.now()

    def __repr__(self):
        status = "PAID" if self.is_paid else "PENDING"
        return f"Payment({self.__amount} {self.currency}, method={self.method}, status={status})"


if __name__ == "__main__":
    payment = Payment(100, currency="USD", method="card")

    print("Base amount:", payment.get_amount())
    payment.add_tip(15)
    print("After tip:", payment.get_amount())

    payment.mark_paid()
    print(payment)
