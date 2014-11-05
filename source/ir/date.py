__author__ = 'Paul Dapolito'

from ir.easytex_element import EasyTeXElement
from errors.date_error import DateError


class Date(EasyTeXElement):
    def __init__(self, date_string):
        self.date_string = date_string

        if self.date_string == "":
            raise DateError("EasyTeX dates cannot be empty!")

    # TODO: Implement proper LaTeX output
    def latex_output(self):
        pass
