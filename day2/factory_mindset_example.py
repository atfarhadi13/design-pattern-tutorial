from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass


class StripePayment(PaymentProcessor):
    def pay(self, amount: float):
        print(f"Processing Stripe payment: ${amount}")


class PayPalPayment(PaymentProcessor):
    def pay(self, amount: float):
        print(f"Processing PayPal payment: ${amount}")


def get_payment_processor(method: str) -> PaymentProcessor:
    if method == "stripe":
        return StripePayment()
    elif method == "paypal":
        return PayPalPayment()
    raise ValueError("Unknown payment method")

