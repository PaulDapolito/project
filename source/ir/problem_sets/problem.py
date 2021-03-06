__author__ = 'Paul Dapolito'

from source.ir.easytex_element import EasyTeXElement
from source.errors.ir.problem_sets.problem_error import ProblemError


class Problem(EasyTeXElement):
    def __init__(self, label=None, statement=None, solution=None):
        self.label = label
        self.statement = statement
        self.solution = solution

        if self.statement is None:
            raise ProblemError("EasyTeX problems must include a problem statement!")
        elif self.solution is None:
            raise ProblemError("EasyTeX problems must include a solution!")

    def __eq__(self, other):
        return self.label == other.label and self.statement == other.statement and self.solution == other.solution

