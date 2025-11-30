from abc import ABC, abstractmethod


class OrderProcessor(ABC):
    """
    Template Method pattern:
    - process_order() defines the skeleton of the algorithm.
    - Subclasses override specific steps.
    """

    def process_order(self) -> None:
        """Template method: defines the full order workflow."""
        self.validate_order()
        total = self.calculate_total()
        self.process_payment(total)
        self.send_receipt()
        self.save_order()

    # ----- Steps to be customized -----

    @abstractmethod
    def validate_order(self) -> None:
        pass

    @abstractmethod
    def calculate_total(self) -> float:
        pass

    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass

    # ----- Optional hooks with default behavior -----

    def send_receipt(self) -> None:
        print("Sending generic receipt email...")

    def save_order(self) -> None:
        print("Saving order to database...\n")


class OnlineOrderProcessor(OrderProcessor):
    def __init__(self, items: list[float], customer_email: str):
        self.items = items
        self.customer_email = customer_email

    def validate_order(self) -> None:
        print("[Online] Validating cart and customer data...")
        if not self.items:
            raise ValueError("Cart is empty.")
        if "@" not in self.customer_email:
            raise ValueError("Invalid email address.")

    def calculate_total(self) -> float:
        subtotal = sum(self.items)
        tax = subtotal * 0.1  # 10% tax
        total = subtotal + tax
        print(f"[Online] Subtotal: {subtotal:.2f}, Tax: {tax:.2f}, Total: {total:.2f}")
        return total

    def process_payment(self, amount: float) -> None:
        print(f"[Online] Charging credit card for ${amount:.2f}...")

    def send_receipt(self) -> None:
        print(f"[Online] Sending email receipt to {self.customer_email}...")


class InStoreOrderProcessor(OrderProcessor):
    def __init__(self, items: list[float], cashier_name: str):
        self.items = items
        self.cashier_name = cashier_name

    def validate_order(self) -> None:
        print("[In-Store] Validating items at checkout...")
        if not self.items:
            raise ValueError("No items scanned at POS.")
        print(f"[In-Store] Cashier: {self.cashier_name}")

    def calculate_total(self) -> float:
        subtotal = sum(self.items)
        discount = 5.0 if subtotal > 50 else 0.0  # small in-store promo
        total = subtotal - discount
        print(f"[In-Store] Subtotal: {subtotal:.2f}, Discount: {discount:.2f}, Total: {total:.2f}")
        return total

    def process_payment(self, amount: float) -> None:
        print(f"[In-Store] Receiving cash/card payment of ${amount:.2f} at the counter...")

    # Use default send_receipt(), but you could override to print a paper receipt instead
    def send_receipt(self) -> None:
        print("[In-Store] Printing physical receipt...")


if __name__ == "__main__":
    online_items = [20.0, 35.0, 15.0]
    in_store_items = [10.0, 8.0, 5.0, 40.0]

    online_order = OnlineOrderProcessor(online_items, "amin@example.com")
    in_store_order = InStoreOrderProcessor(in_store_items, "Sarah (Cashier)")

    print("=== ONLINE ORDER ===")
    online_order.process_order()

    print("=== IN-STORE ORDER ===")
    in_store_order.process_order()