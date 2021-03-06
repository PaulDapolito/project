__author__ = 'Paul Dapolito'

import unittest
import os

from source.parser.parser import EasyTeXParser

from source.ir.shared.author import Author
from source.ir.shared.collaborator import Collaborator
from source.ir.memorandums.date import Date
from source.ir.shared.title import Title
from source.ir.memorandums.subtitle import Subtitle

from source.ir.problem_sets.school import School
from source.ir.problem_sets.course import Course
from source.ir.problem_sets.due_date import DueDate

from source.ir.shared.package import Package

from source.ir.problem_sets.label import Label
from source.ir.problem_sets.statement import Statement
from source.ir.problem_sets.solution import Solution
from source.ir.problem_sets.problem import Problem

from source.ir.memorandums.content import Content
from source.ir.memorandums.section import Section

from source.ir.problem_sets.problem_set import ProblemSet
from source.ir.memorandums.memorandum import Memorandum

from source.errors.parser.parse_document_error import ParseDocumentError

base_path = os.path.dirname(__file__)


class EasyTeXParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = EasyTeXParser()

    def validate_test(self):
        self.assertEqual(1, 1)

    # Text Tests
    def test_that_basic_text_can_be_parsed(self):
        input_string = "Basic"
        parsed_string = self.parser.parse_text(input_string)

        self.assertEqual(input_string, parsed_string)

    def test_that_text_with_spaces_can_be_parsed(self):
        input_string = "One Space"
        parsed_string = self.parser.parse_text(input_string)

        self.assertEqual(input_string, parsed_string)

    def test_that_text_with_symbols_can_be_parsed(self):
        input_string = "\\textbf{Hello World}"
        parsed_string = self.parser.parse_text(input_string)

        self.assertEqual(input_string, parsed_string)

    # Problem Set Tests
    ## Test a problem set with one problem and all optional fields filled
    def test_that_problem_set_can_have_one_problem(self):
        folder_path = base_path + "/test_text_files/problem_sets/full_problem_set_1/"

        input_string = open(folder_path + "full_problem_set_1.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open(folder_path + "due_date.txt").read())

        title = Title(open(folder_path + "title.txt").read())
        course = Course(open(folder_path + "course.txt").read())
        school = School(open(folder_path + "school.txt").read())

        problem_1_label_txt = open(folder_path + "problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open(folder_path + "problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open(folder_path + "problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        self.assertEqual(
            ProblemSet(author=author, collaborators=collaborators, due_date=due_date, title=title,
                       course=course, school=school, problems=[problem]),
            parsed_problem_set)

    ## Test a problem set with two problems and all optional fields filled
    def test_that_problem_set_can_have_multiple_problems(self):
        folder_path = base_path + "/test_text_files/problem_sets/full_problem_set_2/"

        input_string = open(folder_path + "full_problem_set_2.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open(folder_path + "due_date.txt").read())

        title = Title(open(folder_path + "title.txt").read())
        course = Course(open(folder_path + "course.txt").read())
        school = School(open(folder_path + "school.txt").read())

        problem_1_label_txt = open(folder_path + "problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open(folder_path + "problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open(folder_path + "problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open(folder_path + "problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open(folder_path + "problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open(folder_path + "problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author=author, collaborators=collaborators, due_date=due_date, title=title,
                       course=course, school=school, problems=[problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems that are missing labels and all other optional fields filled
    def test_that_problem_set_problems_can_exclude_labels(self):
        folder_path = base_path + "/test_text_files/problem_sets/full_problem_set_3/"

        input_string = open(folder_path + "full_problem_set_3.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open(folder_path + "due_date.txt").read())

        title = Title(open(folder_path + "title.txt").read())
        course = Course(open(folder_path + "course.txt").read())
        school = School(open(folder_path + "school.txt").read())

        problem_1_label = None

        problem_1_statement_txt = open(folder_path + "problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open(folder_path + "problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label = None

        problem_2_statement_txt = open(folder_path + "problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open(folder_path + "problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author=author, collaborators=collaborators, due_date=due_date, title=title,
                       course=course, school=school, problems=[problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and all optional fields filled in an alternate order
    def test_that_problem_set_header_fields_can_be_reordered(self):
        folder_path = base_path + "/test_text_files/problem_sets/full_problem_set_4/"

        input_string = open(folder_path + "full_problem_set_4.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open(folder_path + "due_date.txt").read())

        title = Title(open(folder_path + "title.txt").read())
        course = Course(open(folder_path + "course.txt").read())
        school = School(open(folder_path + "school.txt").read())

        packages_txt = open(folder_path + "packages.txt").read().split(", ")
        packages = [Package(package) for package in packages_txt]

        problem_1_label_txt = open(folder_path + "problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open(folder_path + "problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open(folder_path + "problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open(folder_path + "problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open(folder_path + "problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open(folder_path + "problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author=author, collaborators=collaborators, due_date=due_date, title=title,
                       course=course, school=school, packages=packages, problems=[problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems, all optional fields filled, and one package included
    def test_that_problem_set_can_include_one_package(self):
        folder_path = base_path + "/test_text_files/problem_sets/full_problem_set_4/"

        input_string = open(folder_path + "full_problem_set_4.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open(folder_path + "due_date.txt").read())

        title = Title(open(folder_path + "title.txt").read())
        course = Course(open(folder_path + "course.txt").read())
        school = School(open(folder_path + "school.txt").read())

        packages_txt = open(folder_path + "packages.txt").read().split(", ")
        packages = [Package(package) for package in packages_txt]

        problem_1_label_txt = open(folder_path + "problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open(folder_path + "problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open(folder_path + "problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open(folder_path + "problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open(folder_path + "problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open(folder_path + "problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author=author, collaborators=collaborators, due_date=due_date, title=title,
                       course=course, school=school, packages=packages, problems=[problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems, all optional fields filled, and multiple packages included
    def test_that_problem_set_can_include_multiple_packages(self):
        folder_path = base_path + "/test_text_files/problem_sets/full_problem_set_5/"

        input_string = open(folder_path + "full_problem_set_5.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open(folder_path + "due_date.txt").read())

        title = Title(open(folder_path + "title.txt").read())
        course = Course(open(folder_path + "course.txt").read())
        school = School(open(folder_path + "school.txt").read())

        packages_txt = open(folder_path + "packages.txt").read().split(", ")
        packages = [Package(package) for package in packages_txt]

        problem_1_label_txt = open(folder_path + "problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open(folder_path + "problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open(folder_path + "problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open(folder_path + "problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open(folder_path + "problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open(folder_path + "problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author=author, collaborators=collaborators, due_date=due_date, title=title,
                       course=course, school=school, packages=packages, problems=[problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and no collaborators
    def test_that_problem_set_collaborators_are_optional(self):
        folder_path = base_path + "/test_text_files/problem_sets/partial_problem_set_1/"
        input_string = open(folder_path + "partial_problem_set_1.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators = None

        due_date = DueDate(open(folder_path + "due_date.txt").read())

        title = Title(open(folder_path + "title.txt").read())
        course = Course(open(folder_path + "course.txt").read())
        school = School(open(folder_path + "school.txt").read())

        problem_1_label_txt = open(folder_path + "problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open(folder_path + "problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open(folder_path + "problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open(folder_path + "problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open(folder_path + "problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open(folder_path + "problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author=author, collaborators=collaborators, due_date=due_date, title=title,
                       course=course, school=school, problems=[problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and one collaborator
    def test_that_problem_set_can_have_one_collaborator(self):
        folder_path = base_path + "/test_text_files/problem_sets/full_problem_set_5/"

        input_string = open(folder_path + "full_problem_set_5.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open(folder_path + "due_date.txt").read())

        title = Title(open(folder_path + "title.txt").read())
        course = Course(open(folder_path + "course.txt").read())
        school = School(open(folder_path + "school.txt").read())

        packages_txt = open(folder_path + "packages.txt").read().split(", ")
        packages = [Package(package) for package in packages_txt]

        problem_1_label_txt = open(folder_path + "problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open(folder_path + "problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open(folder_path + "problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open(folder_path + "problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open(folder_path + "problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open(folder_path + "problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author=author, collaborators=collaborators, due_date=due_date, title=title,
                       course=course, school=school, packages=packages, problems=[problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and multiple collaborators
    def test_that_problem_set_can_have_multiple_collaborators(self):
        folder_path = base_path + "/test_text_files/problem_sets/full_problem_set_4/"

        input_string = open(folder_path + "full_problem_set_4.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open(folder_path + "due_date.txt").read())

        title = Title(open(folder_path + "title.txt").read())
        course = Course(open(folder_path + "course.txt").read())
        school = School(open(folder_path + "school.txt").read())

        packages_txt = open(folder_path + "packages.txt").read().split(", ")
        packages = [Package(package) for package in packages_txt]

        problem_1_label_txt = open(folder_path + "problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open(folder_path + "problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open(folder_path + "problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open(folder_path + "problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open(folder_path + "problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open(folder_path + "problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author=author, collaborators=collaborators, due_date=due_date, title=title,
                       course=course, school=school, packages=packages, problems=[problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and no due date
    def test_that_problem_set_due_date_is_optional(self):
        folder_path = base_path + "/test_text_files/problem_sets/partial_problem_set_2/"
        input_string = open(folder_path + "partial_problem_set_2.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = None

        title = Title(open(folder_path + "title.txt").read())
        course = Course(open(folder_path + "course.txt").read())
        school = School(open(folder_path + "school.txt").read())

        problem_1_label_txt = open(folder_path + "problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open(folder_path + "problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open(folder_path + "problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open(folder_path + "problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open(folder_path + "problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open(folder_path + "problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author=author, collaborators=collaborators, due_date=due_date, title=title,
                       course=course, school=school, problems=[problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and no title
    def test_that_problem_set_title_is_optional(self):
        folder_path = base_path + "/test_text_files/problem_sets/partial_problem_set_3/"
        input_string = open(folder_path + "partial_problem_set_3.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open(folder_path + "due_date.txt").read())

        title = None
        course = Course(open(folder_path + "course.txt").read())
        school = School(open(folder_path + "school.txt").read())

        problem_1_label_txt = open(folder_path + "problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open(folder_path + "problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open(folder_path + "problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open(folder_path + "problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open(folder_path + "problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open(folder_path + "problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author=author, collaborators=collaborators, due_date=due_date, title=title,
                       course=course, school=school, problems=[problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and no course
    def test_that_problem_set_course_is_optional(self):
        folder_path = base_path + "/test_text_files/problem_sets/partial_problem_set_4/"
        input_string = open(folder_path + "partial_problem_set_4.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open(folder_path + "due_date.txt").read())

        title = Title(open(folder_path + "title.txt").read())
        course = None
        school = School(open(folder_path + "school.txt").read())

        problem_1_label_txt = open(folder_path + "problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open(folder_path + "problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open(folder_path + "problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open(folder_path + "problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open(folder_path + "problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open(folder_path + "problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author=author, collaborators=collaborators, due_date=due_date, title=title,
                       course=course, school=school, problems=[problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and no school
    def test_that_problem_set_school_is_optional(self):
        folder_path = base_path + "/test_text_files/problem_sets/partial_problem_set_5/"
        input_string = open(folder_path + "partial_problem_set_5.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open(folder_path + "due_date.txt").read())

        title = Title(open(folder_path + "title.txt").read())
        course = Course(open(folder_path + "course.txt").read())
        school = None

        problem_1_label_txt = open(folder_path + "problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open(folder_path + "problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open(folder_path + "problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open(folder_path + "problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open(folder_path + "problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open(folder_path + "problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author=author, collaborators=collaborators, due_date=due_date, title=title,
                       course=course, school=school, problems=[problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and no school, no course, and no title
    def test_that_problem_set_can_exclude_school_course_and_title(self):
        folder_path = base_path + "/test_text_files/problem_sets/partial_problem_set_6/"
        input_string = open(folder_path + "partial_problem_set_6.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open(folder_path + "due_date.txt").read())

        title = None
        course = None
        school = None

        problem_1_label_txt = open(folder_path + "problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open(folder_path + "problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open(folder_path + "problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open(folder_path + "problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open(folder_path + "problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open(folder_path + "problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author=author, collaborators=collaborators, due_date=due_date, title=title,
                       course=course, school=school, problems=[problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and no collaborators and no due date
    def test_that_problem_set_can_exclude_collaborators_and_due_date(self):
        folder_path = base_path + "/test_text_files/problem_sets/partial_problem_set_7/"
        input_string = open(folder_path + "partial_problem_set_7.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators = None
        due_date = None

        title = Title(open(folder_path + "title.txt").read())
        course = Course(open(folder_path + "course.txt").read())
        school = School(open(folder_path + "school.txt").read())

        problem_1_label_txt = open(folder_path + "problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open(folder_path + "problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open(folder_path + "problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open(folder_path + "problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open(folder_path + "problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open(folder_path + "problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author=author, collaborators=collaborators, due_date=due_date, title=title,
                       course=course, school=school, problems=[problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and no optional fields filled
    def test_that_problem_set_can_exclude_all_optional_fields(self):
        folder_path = base_path + "/test_text_files/problem_sets/partial_problem_set_8/"
        input_string = open(folder_path + "partial_problem_set_8.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators = None
        due_date = None
        title = None
        course = None
        school = None

        problem_1_label_txt = open(folder_path + "problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open(folder_path + "problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open(folder_path + "problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open(folder_path + "problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open(folder_path + "problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open(folder_path + "problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author=author, collaborators=collaborators, due_date=due_date, title=title,
                       course=course, school=school, problems=[problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems that are missing labels and no optional fields filled
    def test_that_problem_set_and_problems_can_exclude_all_optional_fields(self):
        folder_path = base_path + "/test_text_files/problem_sets/partial_problem_set_9/"
        input_string = open(folder_path + "partial_problem_set_9.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators = None
        due_date = None
        title = None
        course = None
        school = None

        problem_1_label = None

        problem_1_statement_txt = open(folder_path + "problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open(folder_path + "problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label = None

        problem_2_statement_txt = open(folder_path + "problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open(folder_path + "problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author=author, collaborators=collaborators, due_date=due_date, title=title,
                       course=course, school=school, problems=[problem_1, problem_2]),
            parsed_problem_set)

    # Memorandum Tests
    ## Test a memorandum with one section and all optional fields filled
    def test_that_memorandum_can_have_one_section(self):
        folder_path = base_path + "/test_text_files/memorandums/full_memorandum_1/"
        input_string = open(folder_path + "full_memorandum_1.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        date = Date(open(folder_path + "date.txt").read())
        title = Title(open(folder_path + "title.txt").read())
        subtitle = Subtitle(open(folder_path + "subtitle.txt").read())

        section_1_title = Title(open(folder_path + "section_1_title.txt").read())
        section_1_content = Content(open(folder_path + "section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        self.assertEqual(
            Memorandum(author=author, collaborators=collaborators, date=date, 
                       title=title, subtitle=subtitle, sections=[section_1]),
            parsed_memorandum
        )

    ## Test a memorandum with two sections and all optional fields filled
    def test_that_memorandum_can_have_multiple_sections(self):
        folder_path = base_path + "/test_text_files/memorandums/full_memorandum_2/"
        input_string = open(folder_path + "full_memorandum_2.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        date = Date(open(folder_path + "date.txt").read())
        title = Title(open(folder_path + "title.txt").read())
        subtitle = Subtitle(open(folder_path + "subtitle.txt").read())

        section_1_title = Title(open(folder_path + "section_1_title.txt").read())
        section_1_content = Content(open(folder_path + "section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        section_2_title = Title(open(folder_path + "section_2_title.txt").read())
        section_2_content = Content(open(folder_path + "section_2_content.txt").read())
        section_2 = Section(section_2_title, section_2_content)

        self.assertEqual(
            Memorandum(author=author, collaborators=collaborators, date=date, 
                       title=title, subtitle=subtitle, sections=[section_1, section_2]),
            parsed_memorandum
        )

    ## Test a memorandum with two sections and all optional fields filled in an alternate order
    def test_that_memorandum_header_fields_can_be_reordered(self):
        folder_path = base_path + "/test_text_files/memorandums/full_memorandum_3/"
        input_string = open(folder_path + "full_memorandum_3.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        date = Date(open(folder_path + "date.txt").read())
        title = Title(open(folder_path + "title.txt").read())
        subtitle = Subtitle(open(folder_path + "subtitle.txt").read())

        section_1_title = Title(open(folder_path + "section_1_title.txt").read())
        section_1_content = Content(open(folder_path + "section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        section_2_title = Title(open(folder_path + "section_2_title.txt").read())
        section_2_content = Content(open(folder_path + "section_2_content.txt").read())
        section_2 = Section(section_2_title, section_2_content)

        self.assertEqual(
            Memorandum(author=author, collaborators=collaborators, date=date, 
                       title=title, subtitle=subtitle, sections=[section_1, section_2]),
            parsed_memorandum
        )

    ## Test a memorandum with two sections, all optional fields filled, and one package included
    def test_that_memorandum_can_include_one_package(self):
        folder_path = base_path + "/test_text_files/memorandums/full_memorandum_4/"
        input_string = open(folder_path + "full_memorandum_4.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        date = Date(open(folder_path + "date.txt").read())
        title = Title(open(folder_path + "title.txt").read())
        subtitle = Subtitle(open(folder_path + "subtitle.txt").read())

        packages_txt = open(folder_path + "packages.txt").read().split(", ")
        packages = [Package(package) for package in packages_txt]

        section_1_title = Title(open(folder_path + "section_1_title.txt").read())
        section_1_content = Content(open(folder_path + "section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        section_2_title = Title(open(folder_path + "section_2_title.txt").read())
        section_2_content = Content(open(folder_path + "section_2_content.txt").read())
        section_2 = Section(section_2_title, section_2_content)

        self.assertEqual(
            Memorandum(author=author, collaborators=collaborators, date=date,
                       title=title, subtitle=subtitle, packages=packages, sections=[section_1, section_2]),
            parsed_memorandum
        )

    ## Test a memorandum with two sections, all optional fields filled, and multiple packages included
    def test_that_memorandum_can_include_multiple_packages(self):
        folder_path = base_path + "/test_text_files/memorandums/full_memorandum_5/"
        input_string = open(folder_path + "full_memorandum_5.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        date = Date(open(folder_path + "date.txt").read())
        title = Title(open(folder_path + "title.txt").read())
        subtitle = Subtitle(open(folder_path + "subtitle.txt").read())

        packages_txt = open(folder_path + "packages.txt").read().split(", ")
        packages = [Package(package) for package in packages_txt]

        section_1_title = Title(open(folder_path + "section_1_title.txt").read())
        section_1_content = Content(open(folder_path + "section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        self.assertEqual(
            Memorandum(author=author, collaborators=collaborators, date=date,
                       title=title, subtitle=subtitle, packages=packages, sections=[section_1]),
            parsed_memorandum
        )

    ## Test a memorandum with two sections, all optional fields filled, and only one collaborator
    def test_that_memorandum_can_have_one_collaborator(self):
        folder_path = base_path + "/test_text_files/memorandums/full_memorandum_5/"
        input_string = open(folder_path + "full_memorandum_5.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        date = Date(open(folder_path + "date.txt").read())
        title = Title(open(folder_path + "title.txt").read())
        subtitle = Subtitle(open(folder_path + "subtitle.txt").read())

        packages_txt = open(folder_path + "packages.txt").read().split(", ")
        packages = [Package(package) for package in packages_txt]

        section_1_title = Title(open(folder_path + "section_1_title.txt").read())
        section_1_content = Content(open(folder_path + "section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        self.assertEqual(
            Memorandum(author=author, collaborators=collaborators, date=date,
                       title=title, subtitle=subtitle, packages=packages, sections=[section_1]),
            parsed_memorandum
        )

    ## Test a memorandum with two sections, all optional fields filled, and multiple collaborators
    def test_that_memorandum_can_have_multiple_collaborators(self):
        folder_path = base_path + "/test_text_files/memorandums/full_memorandum_4/"
        input_string = open(folder_path + "full_memorandum_4.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        date = Date(open(folder_path + "date.txt").read())
        title = Title(open(folder_path + "title.txt").read())
        subtitle = Subtitle(open(folder_path + "subtitle.txt").read())

        packages_txt = open(folder_path + "packages.txt").read().split(", ")
        packages = [Package(package) for package in packages_txt]

        section_1_title = Title(open(folder_path + "section_1_title.txt").read())
        section_1_content = Content(open(folder_path + "section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        section_2_title = Title(open(folder_path + "section_2_title.txt").read())
        section_2_content = Content(open(folder_path + "section_2_content.txt").read())
        section_2 = Section(section_2_title, section_2_content)

        self.assertEqual(
            Memorandum(author=author, collaborators=collaborators, date=date,
                       title=title, subtitle=subtitle, packages=packages, sections=[section_1, section_2]),
            parsed_memorandum
        )

    ## Test a memorandum with two sections and no collaborators
    def test_that_memorandum_collaborators_are_optional(self):
        folder_path = base_path + "/test_text_files/memorandums/partial_memorandum_1/"
        input_string = open(folder_path + "partial_memorandum_1.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators = None

        date = Date(open(folder_path + "date.txt").read())
        title = Title(open(folder_path + "title.txt").read())
        subtitle = Subtitle(open(folder_path + "subtitle.txt").read())

        section_1_title = Title(open(folder_path + "section_1_title.txt").read())
        section_1_content = Content(open(folder_path + "section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        section_2_title = Title(open(folder_path + "section_2_title.txt").read())
        section_2_content = Content(open(folder_path + "section_2_content.txt").read())
        section_2 = Section(section_2_title, section_2_content)

        self.assertEqual(
            Memorandum(author=author, collaborators=collaborators, date=date, 
                       title=title, subtitle=subtitle, sections=[section_1, section_2]),
            parsed_memorandum
        )

    ## Test a memorandum with two sections and no date
    def test_that_memorandum_date_is_optional(self):
        folder_path = base_path + "/test_text_files/memorandums/partial_memorandum_2/"
        input_string = open(folder_path + "partial_memorandum_2.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        date = None
        title = Title(open(folder_path + "title.txt").read())
        subtitle = Subtitle(open(folder_path + "subtitle.txt").read())

        section_1_title = Title(open(folder_path + "section_1_title.txt").read())
        section_1_content = Content(open(folder_path + "section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        section_2_title = Title(open(folder_path + "section_2_title.txt").read())
        section_2_content = Content(open(folder_path + "section_2_content.txt").read())
        section_2 = Section(section_2_title, section_2_content)

        self.assertEqual(
            Memorandum(author=author, collaborators=collaborators, date=date, 
                       title=title, subtitle=subtitle, sections=[section_1, section_2]),
            parsed_memorandum
        )

    ## Test a memorandum with two sections and no subtitle
    def test_that_memorandum_subtitle_is_optional(self):
        folder_path = base_path + "/test_text_files/memorandums/partial_memorandum_3/"
        input_string = open(folder_path + "partial_memorandum_3.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators_txt = open(folder_path + "collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        date = Date(open(folder_path + "date.txt").read())
        title = Title(open(folder_path + "title.txt").read())
        subtitle = None

        section_1_title = Title(open(folder_path + "section_1_title.txt").read())
        section_1_content = Content(open(folder_path + "section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        section_2_title = Title(open(folder_path + "section_2_title.txt").read())
        section_2_content = Content(open(folder_path + "section_2_content.txt").read())
        section_2 = Section(section_2_title, section_2_content)

        self.assertEqual(
            Memorandum(author=author, collaborators=collaborators, date=date, 
                       title=title, subtitle=subtitle, sections=[section_1, section_2]),
            parsed_memorandum
        )

    ## Test a memorandum with two sections and no collaborators and no date
    def test_that_memorandum_can_exclude_collaborators_and_date(self):
        folder_path = base_path + "/test_text_files/memorandums/partial_memorandum_4/"
        input_string = open(folder_path + "partial_memorandum_4.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators = None

        date = None
        title = Title(open(folder_path + "title.txt").read())
        subtitle = Subtitle(open(folder_path + "subtitle.txt").read())

        section_1_title = Title(open(folder_path + "section_1_title.txt").read())
        section_1_content = Content(open(folder_path + "section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        section_2_title = Title(open(folder_path + "section_2_title.txt").read())
        section_2_content = Content(open(folder_path + "section_2_content.txt").read())
        section_2 = Section(section_2_title, section_2_content)

        self.assertEqual(
            Memorandum(author=author, collaborators=collaborators, date=date, 
                       title=title, subtitle=subtitle, sections=[section_1, section_2]),
            parsed_memorandum
        )

    ## Test a memorandum with two sections and no optional fields filled
    def test_that_memorandum_can_exclude_all_optional_fields(self):
        folder_path = base_path + "/test_text_files/memorandums/partial_memorandum_5/"
        input_string = open(folder_path + "partial_memorandum_5.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open(folder_path + "author.txt").read())

        collaborators = None

        date = None
        title = Title(open(folder_path + "title.txt").read())
        subtitle = None

        section_1_title = Title(open(folder_path + "section_1_title.txt").read())
        section_1_content = Content(open(folder_path + "section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        section_2_title = Title(open(folder_path + "section_2_title.txt").read())
        section_2_content = Content(open(folder_path + "section_2_content.txt").read())
        section_2 = Section(section_2_title, section_2_content)

        self.assertEqual(
            Memorandum(author=author, collaborators=collaborators, date=date, 
                       title=title, subtitle=subtitle, sections=[section_1, section_2]),
            parsed_memorandum
        )

    # Failure Tests
    ## Test that a problem set with no author does not parse
    def test_that_problem_set_author_is_required(self):
        folder_path = base_path + "/test_text_files/problem_sets/invalid_problem_set_1/"
        input_string = open(folder_path + "invalid_problem_set_1.txt").read()
        self.assertRaises(ParseDocumentError, self.parser.parse_document, input_string)

    ## Test that a problem set with no problems does not parse
    def test_that_problem_set_must_have_problems(self):
        folder_path = base_path + "/test_text_files/problem_sets/invalid_problem_set_2/"
        input_string = open(folder_path + "invalid_problem_set_2.txt").read()
        self.assertRaises(ParseDocumentError, self.parser.parse_document, input_string)

    ## Test that a problem set's header fields must be indented correctly
    def test_that_problem_set_headers_must_be_indented(self):
        folder_path = base_path + "/test_text_files/problem_sets/invalid_problem_set_3/"
        input_string = open(folder_path + "invalid_problem_set_3.txt").read()
        self.assertRaises(ParseDocumentError, self.parser.parse_document, input_string)

    ## Tests that a problem set's problems must be indented correctly
    def test_that_problem_set_problems_must_be_indented(self):
        folder_path = base_path + "/test_text_files/problem_sets/invalid_problem_set_4/"
        input_string = open(folder_path + "invalid_problem_set_4.txt").read()
        self.assertRaises(ParseDocumentError, self.parser.parse_document, input_string)

    ## Test that a memorandum with no author does not parse
    def test_that_memorandum_author_is_required(self):
        folder_path = base_path + "/test_text_files/memorandums/invalid_memorandum_1/"
        input_string = open(folder_path + "invalid_memorandum_1.txt").read()
        self.assertRaises(ParseDocumentError, self.parser.parse_document, input_string)

    ## Test that a memorandum with no title does not parse
    def test_that_memorandum_title_is_required(self):
        folder_path = base_path + "/test_text_files/memorandums/invalid_memorandum_2/"
        input_string = open(folder_path + "invalid_memorandum_2.txt").read()
        self.assertRaises(ParseDocumentError, self.parser.parse_document, input_string)

    ## Test that a memorandum with no sections does not parse
    def test_that_memorandum_must_have_sections(self):
        folder_path = base_path + "/test_text_files/memorandums/invalid_memorandum_3/"
        input_string = open(folder_path + "invalid_memorandum_3.txt").read()
        self.assertRaises(ParseDocumentError, self.parser.parse_document, input_string)

    ## Test that a memorandum's header fields must be indented correctly
    def test_that_memorandum_headers_must_be_indented(self):
        folder_path = base_path + "/test_text_files/memorandums/invalid_memorandum_4/"
        input_string = open(folder_path + "invalid_memorandum_4.txt").read()
        self.assertRaises(ParseDocumentError, self.parser.parse_document, input_string)

    ## Test that a memorandum's sections must be indented correctly
    def test_that_memorandum_sections_must_be_indented(self):
        folder_path = base_path + "/test_text_files/memorandums/invalid_memorandum_5/"
        input_string = open(folder_path + "invalid_memorandum_5.txt").read()
        self.assertRaises(ParseDocumentError, self.parser.parse_document, input_string)
