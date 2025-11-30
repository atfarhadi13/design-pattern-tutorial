"""
Method Overriding (super important!)

A child class replaces the behavior of a parent class.
"""

class BaseBooking:
    def calculate_price(self):
        return 100

class PremiumBooking(BaseBooking):
    def calculate_price(self):
        return super().calculate_price() + 50