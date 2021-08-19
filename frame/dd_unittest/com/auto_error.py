class AutoTestException(BaseException):
    def __init__(self, reason, *args, **kwargs):
        self.reason = reason
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.reason
