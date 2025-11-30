from abc import ABC, abstractmethod


class NotificationChannel(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        """Send a notification to the recipient."""
        pass


class EmailChannel(NotificationChannel):
    def __init__(self, from_email: str = "no-reply@muzzomo.com"):
        self.from_email = from_email

    def send(self, recipient: str, message: str) -> None:
        # In real life, integrate with SendGrid / SMTP here
        print("📧 [EMAIL]")
        print(f"From: {self.from_email}")
        print(f"To:   {recipient}")
        print(f"Body: {message}")
        print("-" * 40)


class SMSChannel(NotificationChannel):
    def __init__(self, sender_id: str = "Muzzomo"):
        self.sender_id = sender_id

    def send(self, recipient: str, message: str) -> None:
        # In real life, integrate with Twilio / SMS gateway here
        print("📲 [SMS]")
        print(f"From: {self.sender_id}")
        print(f"To:   {recipient}")
        print(f"Text: {message}")
        print("-" * 40)


# --- Demo usage ---
if __name__ == "__main__":
    email_channel = EmailChannel()
    sms_channel = SMSChannel()

    channels: list[NotificationChannel] = [email_channel, sms_channel]

    for channel in channels:
        channel.send("customer@example.com", "Your booking has been confirmed.")
