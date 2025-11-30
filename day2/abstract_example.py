"""
In Python, an abstract class:

cannot be instantiated

defines a common interface

forces subclasses to implement required methods
"""

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass


class StripePayment(PaymentProcessor):
    def pay(self, amount: float):
        print(f"Processing Stripe payment: ${amount}")