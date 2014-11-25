__author__ = 'Paul Dapolito'

import unittest

from parser.parser import EasyTeXParser
from interpreters.interpreter import EasyTeXInterpreter


class EasyTeXParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = EasyTeXParser()
        self.interpreter = EasyTeXInterpreter()

    def validate_test(self):
        self.assertEqual(1, 1)

    # Problem Set Tests
    ## Test a problem set with one problem and all optional fields filled
    def test_that_problem_set_can_have_one_problem(self):
        input_string = open("test_text_files/problem_sets/full_problem_set_1/full_problem_set_1.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/full_problem_set_1/full_problem_set_1.tex").read()

        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and all optional fields filled
    def test_that_problem_set_can_have_multiple_problems(self):
        input_string = open("test_text_files/problem_sets/full_problem_set_2/full_problem_set_2.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/full_problem_set_2/full_problem_set_2.tex").read()

        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems that are missing labels and all other optional fields filled
    def test_that_problem_set_problems_can_exclude_labels(self):
        input_string = open("test_text_files/problem_sets/full_problem_set_3/full_problem_set_3.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/full_problem_set_3/full_problem_set_3.tex").read()

        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and all optional fields filled in an alternate order
    def test_that_problem_set_header_fields_can_be_reordered(self):
        input_string = open("test_text_files/problem_sets/full_problem_set_4/full_problem_set_4.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/full_problem_set_4/full_problem_set_4.tex").read()

        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and no collaborators
    def test_that_problem_set_collaborators_are_optional(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_1/partial_problem_set_1.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/partial_problem_set_1/partial_problem_set_1.tex").read()
        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and no due date
    def test_that_problem_set_due_date_is_optional(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_2/partial_problem_set_2.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/partial_problem_set_2/partial_problem_set_2.tex").read()
        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and no title
    def test_that_problem_set_title_is_optional(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_3/partial_problem_set_3.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/partial_problem_set_3/partial_problem_set_3.tex").read()
        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and no course
    def test_that_problem_set_course_is_optional(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_4/partial_problem_set_4.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/partial_problem_set_4/partial_problem_set_4.tex").read()
        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and no school
    def test_that_problem_set_school_is_optional(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_5/partial_problem_set_5.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/partial_problem_set_5/partial_problem_set_5.tex").read()
        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and no school, course, or title
    def test_that_problem_set_can_exclude_school_course_and_title(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_6/partial_problem_set_6.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/partial_problem_set_6/partial_problem_set_6.tex").read()
        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and no collaborators or due date
    def test_that_problem_set_can_exclude_collaborators_and_due_date(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_7/partial_problem_set_7.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/partial_problem_set_7/partial_problem_set_7.tex").read()
        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and no optional fields filled
    def test_that_problem_set_can_exclude_all_optional_fields(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_8/partial_problem_set_8.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/partial_problem_set_8/partial_problem_set_8.tex").read()
        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems that are missing labels and no optional fields filled
    def test_that_problem_set_and_problems_can_exclude_all_optional_fields(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_9/partial_problem_set_9.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/partial_problem_set_9/partial_problem_set_9.tex").read()
        self.assertEqual(interpreted_problem_set, expected_tex_file)

    # Memorandum Tests
    ## Test a memorandum with one section and all optional fields filled
    def test_that_memorandum_can_have_one_section(self):
        input_string = open("test_text_files/memorandums/full_memorandum_1/full_memorandum_1.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        interpreted_memorandum = self.interpreter.interpret_document(parsed_memorandum)
        expected_tex_file = open("test_text_files/memorandums/full_memorandum_1/full_memorandum_1.tex").read()
        self.assertEqual(interpreted_memorandum, expected_tex_file)

    ## Test a memorandum with two sections and all optional fields filled
    def test_that_memorandum_can_have_multiple_sections(self):
        input_string = open("test_text_files/memorandums/full_memorandum_2/full_memorandum_2.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        interpreted_memorandum = self.interpreter.interpret_document(parsed_memorandum)
        expected_tex_file = open("test_text_files/memorandums/full_memorandum_2/full_memorandum_2.tex").read()
        self.assertEqual(interpreted_memorandum, expected_tex_file)

    ## Test a memorandum with two sections and all optional fields filled in an alternate order
    def test_that_memorandum_header_fields_can_be_reordered(self):
        input_string = open("test_text_files/memorandums/full_memorandum_3/full_memorandum_3.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        interpreted_memorandum = self.interpreter.interpret_document(parsed_memorandum)
        expected_tex_file = open("test_text_files/memorandums/full_memorandum_3/full_memorandum_3.tex").read()
        self.assertEqual(interpreted_memorandum, expected_tex_file)

    ## Test a memorandum with two sections and no collaborators
    def test_that_memorandum_collaborators_are_optional(self):
        input_string = open("test_text_files/memorandums/partial_memorandum_1/partial_memorandum_1.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        interpreted_memorandum = self.interpreter.interpret_document(parsed_memorandum)
        expected_tex_file = open("test_text_files/memorandums/partial_memorandum_1/partial_memorandum_1.tex").read()
        self.assertEqual(interpreted_memorandum, expected_tex_file)

    ## Test a memorandum with two sections and no date
    def test_that_memorandum_date_is_optional(self):
        input_string = open("test_text_files/memorandums/partial_memorandum_2/partial_memorandum_2.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        interpreted_memorandum = self.interpreter.interpret_document(parsed_memorandum)
        expected_tex_file = open("test_text_files/memorandums/partial_memorandum_2/partial_memorandum_2.tex").read()
        self.assertEqual(interpreted_memorandum, expected_tex_file)

    ## Test a memorandum with two sections and no subtitle
    def test_that_memorandum_subtitle_is_optional(self):
        input_string = open("test_text_files/memorandums/partial_memorandum_3/partial_memorandum_3.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        interpreted_memorandum = self.interpreter.interpret_document(parsed_memorandum)
        expected_tex_file = open("test_text_files/memorandums/partial_memorandum_3/partial_memorandum_3.tex").read()
        self.assertEqual(interpreted_memorandum, expected_tex_file)

    ## Test a memorandum with two sections and no collaborators or date
    def test_that_memorandum_can_exclude_collaborators_and_date(self):
        input_string = open("test_text_files/memorandums/partial_memorandum_4/partial_memorandum_4.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        interpreted_memorandum = self.interpreter.interpret_document(parsed_memorandum)
        expected_tex_file = open("test_text_files/memorandums/partial_memorandum_4/partial_memorandum_4.tex").read()
        self.assertEqual(interpreted_memorandum, expected_tex_file)

    ## Test a memorandum with two sections and no optional fields filled
    def test_that_memorandum_can_exclude_all_optional_fields(self):
        input_string = open("test_text_files/memorandums/partial_memorandum_5/partial_memorandum_5.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        interpreted_memorandum = self.interpreter.interpret_document(parsed_memorandum)
        expected_tex_file = open("test_text_files/memorandums/partial_memorandum_5/partial_memorandum_5.tex").read()
        self.assertEqual(interpreted_memorandum, expected_tex_file)
