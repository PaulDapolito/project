__author__ = 'Paul Dapolito'

from pyparsing import *

from errors.parser.parse_document_error import ParseDocumentError
from errors.parser.parse_text_error import ParseTextError


from ir.shared.author import Author
from ir.shared.collaborator import Collaborator
from ir.memorandums.date import Date
from ir.shared.title import Title
from ir.memorandums.subtitle import Subtitle
from ir.problem_sets.school import School
from ir.problem_sets.course import Course
from ir.problem_sets.due_date import DueDate
from ir.problem_sets.label import Label
from ir.problem_sets.statement import Statement
from ir.problem_sets.solution import Solution
from ir.problem_sets.problem import Problem
from ir.memorandums.content import Content
from ir.memorandums.section import Section
from ir.problem_sets.problem_set import ProblemSet
from ir.memorandums.memorandum import Memorandum

# Terminals
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = caps.lower()
alphas = caps + lowers
digits = "0123456789"
symbols = "[]{}()<>\'\"=|.,;\/:-$?!*_+#^`"

space = " "
newline = "\n"
tab = space + space + space + space
whitespace = space + newline + tab

terminals = alphas + digits + symbols + whitespace
text = ZeroOrMore(Word(terminals)).leaveWhitespace()

# Grammar
## Author
author_expr = Suppress(Literal("author:") + White(space)) + restOfLine
author = author_expr.setResultsName("author")

## Collaborators [Optional]
collaborator = Word(alphas)
collaborators_group = Group(delimitedList(collaborator))
collaborators_ignored = Suppress(Literal("collaborators:") + White(space))
collaborators_expr = collaborators_ignored + collaborators_group
optional_collaborators = Optional(collaborators_expr.setResultsName("collaborators"), default=list())

## Date [Optional]
date_expr = Suppress(Literal("date:") + White(space)) + restOfLine + Suppress(LineEnd())
optional_date = Optional(date_expr.setResultsName("date"), default=list())

## Title
title_expr = Suppress(Literal("title:") + White(space)) + restOfLine + Suppress(LineEnd())
title = title_expr.setResultsName("title")

## Title [Optional]
optional_title = Optional(title.setResultsName("title"), default=list())

## Subtitle [Optional]
subtitle_expr = Suppress(Literal("subtitle:") + White(space)) + restOfLine
optional_subtitle = Optional(subtitle_expr.setResultsName("subtitle"), default=list())

## School [Optional]
school_expr = Suppress(Literal("school:") + White(space)) + restOfLine
optional_school = Optional(school_expr.setResultsName("school"), default=list())

## Course [Optional]
course_expr = Suppress(Literal("course:") + White(space)) + restOfLine
optional_course = Optional(course_expr.setResultsName("course"), default=list())

## Due Date [Optional]
due_date_expr = Suppress(Literal("due_date:") + White(space)) + restOfLine
optional_due_date = Optional(due_date_expr.setResultsName("due_date"), default=list())

## Label [Optional]
label_expr = Suppress(Literal("label:") + White(space)) + restOfLine + Suppress(LineEnd())
optional_label = Optional(label_expr.setResultsName("label"), default=list())

## Statement
statement_ignored = Suppress(Literal("statement:") + White(newline))
statement_lines = Group(OneOrMore(Regex(ur'\s\s\s\s\s\s\s\s\s\s\s\s(.+)').leaveWhitespace() + Suppress(White(newline))))
statement_expr = statement_ignored + statement_lines
statement = statement_expr.setResultsName("statement")

## Solution
solution_ignored = Suppress(Literal("solution:") + White(newline))
solution_lines = Group(OneOrMore(Regex(ur'\s\s\s\s\s\s\s\s\s\s\s\s(.+)').leaveWhitespace() + Suppress(White(newline))))
solution_expr = solution_ignored + solution_lines
solution = solution_expr.setResultsName("solution")

## Problem
problem_ignored = Suppress(Literal("problem:") + LineEnd())
problem = problem_ignored + Group(optional_label + statement + solution)
problems_expr = Group(OneOrMore(problem))
problems = problems_expr.setResultsName("problems")

## Content
content_lines = Group(OneOrMore(Regex(ur'\s\s\s\s\s\s\s\s\s\s\s\s(.+)').leaveWhitespace() + Suppress(White(newline))))
content_expr = Suppress(Literal("content:") + White(newline)) + content_lines
content = content_expr.setResultsName("content")

## Section
section = Group(Suppress(Literal("section:") + LineEnd()) + title + content)
sections_expr = Group(OneOrMore(section))
sections = sections_expr.setResultsName("sections")

## Problem Set
problem_set_identifier = Literal("problem_set")
problem_set_ignored = Suppress(Literal(":") + LineEnd())
problem_set_headers = author & optional_collaborators & optional_due_date & optional_title & optional_course & optional_school
problem_set = problem_set_identifier + problem_set_ignored + problem_set_headers + problems

## Memorandum
memorandum_identifier = Literal("memorandum")
memorandum_ignored = Suppress(Literal(":") + LineEnd())
memorandum_headers = author & optional_collaborators & optional_date & title & optional_subtitle
memorandum = memorandum_identifier + memorandum_ignored + memorandum_headers + sections

## Document
document = problem_set | memorandum


# Parser Implementation
class EasyTeXParser(object):
    @staticmethod
    def parse_text(input_string):
        try:
            parsed_text = text.parseString(input_string)
        except ParseException as pex:
            raise ParseTextError("Error parsing text: '{}'. Exception raised: '{}'".format(input_string, pex))

        if parsed_text[0]:
            return parsed_text[0]
        else:
            raise ParseTextError("Error parsing text: '{}'".format(input_string))

    @staticmethod
    def parse_problem_set(parsed_block):
        # Check for author
        author = Author(parsed_block["author"][0])

        # Check for collaborators
        if parsed_block["collaborators"]:
            collaborators = [Collaborator(collab) for collab in parsed_block["collaborators"][0]]
        else:
            collaborators = None

        # Check for due date
        if parsed_block["due_date"]:
            due_date = DueDate(parsed_block["due_date"][0])
        else:
            due_date = None

        # Check for title
        if parsed_block["title"]:
            title = Title(parsed_block["title"][0])
        else:
            title = None

        # Check for course
        if parsed_block["course"]:
            course = Course(parsed_block["course"][0])
        else:
            course = None

        # Check for school
        if parsed_block["school"]:
            school = School(parsed_block["school"][0])
        else:
            school = None

        # Accumulate problems
        problems = list()
        for problem in parsed_block["problems"]:
            # Check for label
            if problem["label"]:
                label = Label(problem["label"][0])
            else:
                label = None

            # Strip leftmost whitespace from every line of statement and solution
            statement_stripped = [line.lstrip() for line in problem["statement"][0]]
            statement_txt = newline.join(statement_stripped)
            statement = Statement(statement_txt)

            solution_stripped = [line.lstrip() for line in problem["solution"][0]]
            solution_txt = newline.join(solution_stripped) + "\n"
            solution = Solution(solution_txt)

            problems.append(Problem(label, statement, solution))

        # Create and return problem set
        problem_set = ProblemSet(author, collaborators, due_date, title, course, school, problems)
        return problem_set

    @staticmethod
    def parse_memorandum(parsed_block):
        author = Author(parsed_block["author"][0])

        # Check for collaborators
        if parsed_block["collaborators"]:
            collaborators = [Collaborator(collab) for collab in parsed_block["collaborators"][0]]
        else:
            collaborators = None

        # Check for date
        if parsed_block["date"]:
            date = Date(parsed_block["date"][0])
        else:
            date = None

        title = Title(parsed_block["title"][0])

        # Check for subtitle
        if parsed_block["subtitle"]:
            subtitle = Subtitle(parsed_block["subtitle"][0])
        else:
            subtitle = None

        # Accumulate sections
        sections = list()
        for section in parsed_block["sections"]:
            section_title = Title(section["title"][0])

            # Strip leftmost whitespace from every line of content
            content_stripped = [line.lstrip() for line in section["content"][0]]
            content_txt = newline.join(content_stripped)
            content = Content(content_txt)

            sections.append(Section(section_title, content))

        # Create and return memorandum
        memorandum = Memorandum(author, collaborators, date, title, subtitle, sections)
        return memorandum

    def parse_document(self, input_string):
        try:
            indented_block = document.parseString(input_string)
        except ParseException as pex:
            raise ParseDocumentError("Error parsing document. Exception raised: '{}'".format(pex))

        if indented_block is None:
            raise ParseDocumentError("Error parsing document: found no indented block!".format(input_string))
        elif indented_block[0] == "memorandum":
            return self.parse_memorandum(indented_block)
        elif indented_block[0] == "problem_set":
            return self.parse_problem_set(indented_block)
        else:
            raise ParseDocumentError("Error parsing document: found no indented block!".format(input_string))

