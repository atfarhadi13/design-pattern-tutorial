"""
Python doesn't have explicit interfaces like Java, BUT:

We can create interface-like behavior using abstract base classes or Protocols (typing module).
"""
from abc import ABC, abstractmethod
from typing import Protocol

class NotificationService(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class Notifier(Protocol):
    def send(self, message: str) -> None:
        ...

class EmailNotifier:
    def send(self, message: str):
        print("Sending EMAIL:", message)

class SMSNotifier:
    def send(self, message: str):
        print("Sending SMS:", message)