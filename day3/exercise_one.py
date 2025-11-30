from abc import ABC, abstractmethod


# 1) Abstract product
class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount: float) -> None:
        """Process a payment of the given amount."""
        pass


# 2) Concrete products
class StripePayment(PaymentProcessor):
    def process(self, amount: float) -> None:
        # here you would call Stripe SDK / API
        print(f"💳 [Stripe] Processing payment: ${amount:.2f}")


class PaypalPayment(PaymentProcessor):
    def process(self, amount: float) -> None:
        # here you would call PayPal SDK / API
        print(f"💰 [PayPal] Processing payment: ${amount:.2f}")


# 3) Factory (creator)
class PaymentFactory:
    @staticmethod
    def create(processor_type: str) -> PaymentProcessor:
        processor_type = processor_type.lower()

        if processor_type == "stripe":
            return StripePayment()
        elif processor_type == "paypal":
            return PaypalPayment()
        else:
            raise ValueError(f"Unknown payment processor type: {processor_type!r}")


# --- Demo usage ---
if __name__ == "__main__":
    factory = PaymentFactory()

    stripe_processor = factory.create("stripe")
    stripe_processor.process(120.0)

    paypal_processor = factory.create("paypal")
    paypal_processor.process(89.99)
