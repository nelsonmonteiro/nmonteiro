from django.test import TestCase
from .models import Function
from .utils import parse_function
from .exceptions import ParseException


class AnimalTestCase(TestCase):
    def setUp(self):
        Function.objects.create(syntax="f2 + f5")       # function_1
        Function.objects.create(syntax="5 - f4")        # function_2
        Function.objects.create(syntax="f1 * f2")       # function_3
        Function.objects.create(syntax="x")             # function_4
        Function.objects.create(syntax="90 + 1")        # function_5
        Function.objects.create(syntax="f6")            # function_6
        Function.objects.create(syntax="f1 + f1")       # function_7
        Function.objects.create(syntax="f9")            # function_8
        Function.objects.create(syntax="f1 + f10")      # function_9
        Function.objects.create(syntax="f8")            # function_10
        Function.objects.create(syntax="f102")          # function_11

    def test_parser_valid_cases(self):
        functions = Function.objects.all()
        function_1 = functions[0]
        function_3 = functions[2]
        function_7 = functions[6]
        self.assertEqual(function_1.parse(), '(5 - (x)) + (90 + 1)')
        self.assertEqual(function_3.parse(), '((5 - (x)) + (90 + 1)) * (5 - (x))')
        self.assertEqual(function_7.parse(), '((5 - (x)) + (90 + 1)) + ((5 - (x)) + (90 + 1))')

    def test_parser_recursion_errors(self):
        functions = Function.objects.all()
        function_6 = functions[5]
        function_8 = functions[7]
        with self.assertRaises(ParseException):
            function_8.parse()
        with self.assertRaises(ParseException):
            function_6.parse()

    def test_parser_unknown_function(self):
        functions = Function.objects.all()
        function_11 = functions[10]
        with self.assertRaises(ParseException):
            function_11.parse()

    def test_parser_from_string(self):
        self.assertEquals(parse_function('f2 + f2'), '(5 - (x)) + (5 - (x))')

        with self.assertRaises(ParseException):
            parse_function('f8')

        with self.assertRaises(ParseException):
            parse_function('f1230')
