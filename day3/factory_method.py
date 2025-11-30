"""
Instead of calling constructors directly, you create an object through a 
creator class with a method that decides which subclass to instantiate.
"""


from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass


class EmailChannel(NotificationChannel):
    def send(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")


class SMSChannel(NotificationChannel):
    def send(self, recipient, message):
        print(f"Sending SMS to {recipient}: {message}")


class NotificationFactory:
    @staticmethod
    def create(channel_type: str) -> NotificationChannel:
        channel_type = channel_type.lower()
        
        if channel_type == "email":
            return EmailChannel()
        if channel_type == "sms":
            return SMSChannel()

        raise ValueError(f"Unknown channel type: {channel_type}")
