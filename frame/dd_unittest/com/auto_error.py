"""自动化测试错误,通过这个错误去处理一些异常"""
class AutoTestException(BaseException):
    """自动化测试错误,通过这个错误去处理一些异常"""

    def __init__(self, reason, *args, **kwargs):
        self.reason = reason
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.reason
