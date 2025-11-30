from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        """Return the discounted total."""
        pass


class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        if percent < 0 or percent > 100:
            raise ValueError("Percent must be between 0 and 100.")
        self.percent = percent

    def apply(self, total: float) -> float:
        discount = total * (self.percent / 100.0)
        return max(total - discount, 0)


class FlatDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        if amount < 0:
            raise ValueError("Discount amount cannot be negative.")
        self.amount = amount

    def apply(self, total: float) -> float:
        return max(total - self.amount, 0)


class Cart:
    def __init__(self, subtotal: float, discount_strategy: DiscountStrategy):
        self.subtotal = float(subtotal)
        self.discount_strategy = discount_strategy

    def final_total(self) -> float:
        return self.discount_strategy.apply(self.subtotal)

    def __repr__(self):
        return (
            f"Cart(subtotal={self.subtotal}, "
            f"final_total={self.final_total()}, "
            f"strategy={self.discount_strategy.__class__.__name__})"
        )
    

if __name__ == "__main__":
    subtotal = 200.0

    carts = [
        Cart(subtotal, NoDiscount()),
        Cart(subtotal, PercentageDiscount(10)),   # 10% off
        Cart(subtotal, FlatDiscount(30)),        # 30 off
    ]

    for c in carts:
        print(c)
