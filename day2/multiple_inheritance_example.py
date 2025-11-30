class TimestampMixin:
    def timestamp(self):
        return "2025-05-30"

class LoggableMixin:
    def log(self, msg):
        print("[LOG]:", msg)

class Payment(TimestampMixin, LoggableMixin):
    pass
