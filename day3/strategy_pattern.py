"""
Define a family of algorithms (strategies), encapsulate them, and make them interchangeable.
"""

from abc import ABC, abstractmethod

class PriceStrategy(ABC):
    @abstractmethod
    def calculate(self, base_price: float) -> float:
        pass


class NormalPrice(PriceStrategy):
    def calculate(self, base_price):
        return base_price

class HolidayPrice(PriceStrategy):
    def calculate(self, base_price):
        return base_price * 1.2

class EmergencyPrice(PriceStrategy):
    def calculate(self, base_price):
        return base_price * 1.5

class Booking:
    def __init__(self, base_price: float, strategy: PriceStrategy):
        self.base_price = base_price
        self.strategy = strategy

    def total(self):
        return self.strategy.calculate(self.base_price)
    
booking = Booking(100, EmergencyPrice())
print(booking.total())


"""
Why Strategy is powerful?

behavior reusable

low coupling

interchangeable

avoids if/elif/elif/elif chains
"""


"""
his pattern will later help you in:

Dynamic pricing

Flexible payment gateways

Swappable notification systems

Applying different booking logic

AI model selection logic (ensemble models)
"""


"""
Where Strategy is used in Django?

DRF authentication strategies

DRF throttling

Django database backends

Django password hashers
"""