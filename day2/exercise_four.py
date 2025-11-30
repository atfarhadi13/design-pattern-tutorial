from abc import ABC, abstractmethod


class NotificationChannel(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        pass


class EmailChannel(NotificationChannel):
    def __init__(self, from_email: str = "no-reply@muzzomo.com"):
        self.from_email = from_email

    def send(self, recipient: str, message: str) -> None:
        print("📧 [EMAIL]")
        print(f"From: {self.from_email}")
        print(f"To:   {recipient}")
        print(f"Body: {message}")
        print("-" * 40)


class SMSChannel(NotificationChannel):
    def __init__(self, sender_id: str = "Muzzomo"):
        self.sender_id = sender_id

    def send(self, recipient: str, message: str) -> None:
        print("📲 [SMS]")
        print(f"From: {self.sender_id}")
        print(f"To:   {recipient}")
        print(f"Text: {message}")
        print("-" * 40)


def get_notification_channel(channel_type: str) -> NotificationChannel:
    """
    Simple factory function that returns an appropriate NotificationChannel
    instance based on the given type.
    """
    channel_type = channel_type.lower()

    if channel_type == "email":
        return EmailChannel()
    elif channel_type == "sms":
        return SMSChannel()
    else:
        raise ValueError(f"Unknown notification channel type: {channel_type!r}")


# --- Demo usage ---
if __name__ == "__main__":
    # Client code does NOT know which concrete class it gets.
    channel = get_notification_channel("email")
    channel.send("customer@example.com", "Your booking has been confirmed.")

    channel = get_notification_channel("sms")
    channel.send("+15551234567", "Your professional is on the way 🚗")
