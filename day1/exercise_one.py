from datetime import datetime


class User:
    def __init__(self, user_id: int, full_name: str, email: str):
        self.user_id = user_id
        self.full_name = full_name
        self.email = email

    def __repr__(self):
        return f"User(id={self.user_id}, name='{self.full_name}')"


class Professional:
    def __init__(self, prof_id: int, full_name: str, service_category: str):
        self.prof_id = prof_id
        self.full_name = full_name
        self.service_category = service_category

    def __repr__(self):
        return f"Professional(id={self.prof_id}, name='{self.full_name}', category='{self.service_category}')"


class Payment:
    def __init__(self, amount: float, currency: str = "USD", method: str = "card", is_paid: bool = False):
        self.amount = amount
        self.currency = currency
        self.method = method
        self.is_paid = is_paid
        self.paid_at: datetime | None = None

    def mark_paid(self):
        self.is_paid = True
        self.paid_at = datetime.now()

    def __repr__(self):
        status = "PAID" if self.is_paid else "PENDING"
        return f"Payment({self.amount} {self.currency}, method={self.method}, status={status})"


class Booking:
    def __init__(
        self,
        booking_id: int,
        title: str,
        customer: User,
        professional: Professional,
        scheduled_for: datetime,
        payment: Payment,
    ):
        self.booking_id = booking_id
        self.title = title
        self.customer = customer            # composition
        self.professional = professional    # composition
        self.scheduled_for = scheduled_for
        self.payment = payment              # composition
        self.status = "pending"

    def mark_completed(self):
        self.status = "completed"

    def cancel(self, reason: str | None = None):
        self.status = "cancelled"
        self.cancel_reason = reason

    def __repr__(self):
        return (
            f"Booking(id={self.booking_id}, title='{self.title}', "
            f"customer={self.customer.full_name}, "
            f"professional={self.professional.full_name}, "
            f"status={self.status}, payment={self.payment})"
        )


# --- Demo usage (you can run this) ---
if __name__ == "__main__":
    # Create a customer
    customer = User(user_id=1, full_name="Amin Nasiri", email="amin@example.com")

    # Create a professional
    pro = Professional(prof_id=10, full_name="John Electrician", service_category="Electrical")

    # Create a payment
    payment = Payment(amount=120.0, currency="USD", method="card")

    # Create a booking that COMPOSES the above objects
    booking = Booking(
        booking_id=1001,
        title="Fix living room lights",
        customer=customer,
        professional=pro,
        scheduled_for=datetime(2025, 12, 1, 14, 0),
        payment=payment,
    )

    print("Before payment:")
    print(booking)

    # Mark payment as paid
    payment.mark_paid()

    print("\nAfter payment:")
    print(booking)
