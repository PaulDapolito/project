__author__ = 'Paul Dapolito'


class StatementError(Exception):
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return repr(self.error_message)