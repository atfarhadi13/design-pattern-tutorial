from abc import ABC, abstractmethod


class BaseNotification(ABC):
    def __init__(self, recipient: str, message: str):
        self.recipient = recipient
        self.message = message

    @abstractmethod
    def send(self) -> None:
        """Send the notification (to be implemented by subclasses)."""
        pass

    def preview(self) -> str:
        """Common helper used by all notifications."""
        return f"To: {self.recipient} | Message: {self.message}"


class EmailNotification(BaseNotification):
    def __init__(self, recipient: str, message: str, subject: str, from_email: str = "no-reply@muzzomo.com"):
        super().__init__(recipient, message)
        self.subject = subject
        self.from_email = from_email

    def send(self) -> None:
        # In a real app, plug into SendGrid / SMTP here
        print("📧 Sending EMAIL:")
        print(f"From: {self.from_email}")
        print(f"To:   {self.recipient}")
        print(f"Subj: {self.subject}")
        print(f"Body: {self.message}")



class SMSNotification(BaseNotification):
    def __init__(self, recipient: str, message: str, sender_id: str = "Muzzomo"):
        super().__init__(recipient, message)
        self.sender_id = sender_id

    def send(self) -> None:
        # In a real app, plug into Twilio / SMS gateway here
        print("📲 Sending SMS:")
        print(f"From: {self.sender_id}")
        print(f"To:   {self.recipient}")
        print(f"Text: {self.message}")


if __name__ == "__main__":
    notifications: list[BaseNotification] = [
        EmailNotification(
            recipient="customer@example.com",
            message="Your booking has been confirmed.",
            subject="Booking Confirmation",
        ),
        SMSNotification(
            recipient="+15551234567",
            message="Your professional is on the way 🚗",
        ),
    ]

    for n in notifications:
        print("Preview:", n.preview())
        n.send()
        print("-" * 40)
