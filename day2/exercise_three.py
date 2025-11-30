class BaseBooking:
    def __init__(self, base_price: float):
        self.base_price = float(base_price)

    def calculate_price(self) -> float:
        """Base calculation with no extra fees."""
        return self.base_price

    def __repr__(self):
        return f"{self.__class__.__name__}(base={self.base_price}, total={self.calculate_price()})"
    

class HolidayBooking(BaseBooking):
    def calculate_price(self) -> float:
        """
        Holiday booking costs +20%
        """
        base = super().calculate_price()
        return base * 1.20   # +20%


class EmergencyBooking(BaseBooking):
    def calculate_price(self) -> float:
        """
        Emergency booking costs +50%
        """
        base = super().calculate_price()
        return base * 1.50   # +50%


# --- Demo usage ---
if __name__ == "__main__":
    normal = BaseBooking(100)
    holiday = HolidayBooking(100)
    emergency = EmergencyBooking(100)

    print(normal)     # BaseBooking(base=100.0, total=100.0)
    print(holiday)    # HolidayBooking(base=100.0, total=120.0)
    print(emergency)  # EmergencyBooking(base=100.0, total=150.0)
