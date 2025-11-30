"""
Concept

Define the steps of an algorithm in a base class, let subclasses override specific steps.
"""

from abc import ABC, abstractmethod

class BookingProcessor(ABC):
    def process(self):
        self.validate()
        self.assign_professional()
        self.notify_user()
        self.save_to_db()

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def assign_professional(self):
        pass

    def notify_user(self):
        print("Sending notification...")

    def save_to_db(self):
        print("Saving booking to DB...")


class NormalBookingProcessor(BookingProcessor):
    def validate(self):
        print("Normal booking validation")

    def assign_professional(self):
        print("Assigning nearest professional")


processor = NormalBookingProcessor()
processor.process()