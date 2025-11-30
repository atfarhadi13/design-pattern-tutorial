class CartItem:
    def __init__(self, name: str, unit_price: float, quantity: int = 1):
        self.name = name
        self.unit_price = float(unit_price)
        self.quantity = int(quantity)

    @property
    def total_price(self) -> float:
        return self.unit_price * self.quantity

    def __repr__(self):
        return f"CartItem(name='{self.name}', qty={self.quantity}, unit={self.unit_price}, total={self.total_price})"

class Cart:
    def __init__(self, owner: str | None = None, currency: str = "USD"):
        self.owner = owner
        self.currency = currency
        self.items: list[CartItem] = []   # ← composition

    def add_item(self, item: CartItem):
        self.items.append(item)

    def remove_item(self, name: str):
        self.items = [item for item in self.items if item.name != name]

    def clear(self):
        self.items.clear()

    def total(self) -> float:
        return sum(item.total_price for item in self.items)

    def __repr__(self):
        lines = [f"Cart(owner={self.owner}, currency={self.currency})"]
        for item in self.items:
            lines.append(f"  - {item}")
        lines.append(f"Total: {self.total()} {self.currency}")
        return "\n".join(lines)


if __name__ == "__main__":
    cart = Cart(owner="Amin", currency="USD")

    # Add items (services / products)
    cart.add_item(CartItem(name="House Cleaning - 2h", unit_price=50, quantity=2))
    cart.add_item(CartItem(name="Window Cleaning", unit_price=30, quantity=1))
    cart.add_item(CartItem(name="Carpet Wash", unit_price=40, quantity=3))

    print("Cart after adding items:")
    print(cart)

    cart.remove_item("Window Cleaning")
    print("\nCart after removing 'Window Cleaning':")
    print(cart)

    print("\nFinal total:", cart.total(), cart.currency)
