import unittest
import sys
import os
from src.query_parser import Query_Parser

class TestIsWhitespace(unittest.TestCase):

    inverted_index = {
        "dog": [1,2,3],
        "cat": [2,3,4],
        "hamster": [9,1,4]
    }
    documents = [1,2,3,4,9]
    query_parser = Query_Parser(inverted_index, documents)

    def test_single_whitespace(self):
        whitespace = " "
        self.assertTrue(self.query_parser.is_whitespace(whitespace))

    def test_not_whitespace(self):
        not_whitespace = "a"
        self.assertFalse(self.query_parser.is_whitespace(not_whitespace))

    def test_multiple_whitespace(self):
        whitespace = "      "
        self.assertTrue(self.query_parser.is_whitespace(whitespace))

    def test_not_all_whitespace(self):
        not_all_whitespace = "a      "
        self.assertFalse(self.query_parser.is_whitespace(not_all_whitespace))

class TestIsAlphanum(unittest.TestCase):
       
    inverted_index = {
        "dog": [1,2,3],
        "cat": [2,3,4],
        "hamster": [9,1,4]
    }
    documents = [1,2,3,4,9]
    query_parser = Query_Parser(inverted_index, documents)

    def test_single_alpha(self):
        alpha = "a"
        self.assertTrue(self.query_parser.is_alphanum(alpha))

    def test_single_num(self):
        num = "4"
        self.assertTrue(self.query_parser.is_alphanum(num))

    def test_multiple_alpha(self):
        alpha = "adjaRsj"
        self.assertTrue(self.query_parser.is_alphanum(alpha))

    def test_multiple_num(self):
        num = "47465555"
        self.assertTrue(self.query_parser.is_alphanum(num))

    def test_mixed_alphanum(self):
        alphanum = "0880ewgi3"
        self.assertTrue(self.query_parser.is_alphanum(alphanum))

    def test_non_alphanum(self):
        non_alphanum = "   oowe8 9987!"
        self.assertFalse(self.query_parser.is_alphanum(non_alphanum))

# run the tests
unittest.main()