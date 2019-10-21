# Unit 1 Lesson 2 Test script
# Author: Chris Proctor and Jacob Wolf
# --------------------
# YOU DO NOT NEED TO UNDERSTAND THIS CODE RIGHT NOW!
# This script imports all the functions from your homework and tests them out. Hopefully they work!
# Testing is really important in computer science, so some nice functions are provided. We'll use them.

import unittest

from homework_01_02 import *

class TestHomework_01_02(unittest.TestCase):

    def test_has_five_letters(self):
        self.assertTrue(has_five_letters("level"))
        self.assertTrue(has_five_letters("donut"))
        self.assertFalse(has_five_letters("levels"))
        self.assertFalse(has_five_letters("help"))
        self.assertFalse(has_five_letters(""))

    def test_count_five_letter_words(self):
        self.assertEqual(count_five_letter_words(["red","green","blue","orange"]), 1)
        self.assertEqual(count_five_letter_words(["apple", "peach", "plums"]), 3)
        self.assertEqual(count_five_letter_words(["tea","coffee","milk","soda"]), 0)
        self.assertEqual(count_five_letter_words(["","","",""]), 0)

    def test_average(self):
        self.assertEqual(average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(average([1]), 1.0)
        self.assertEqual(average([0]), 0.0)
        self.assertEqual(average([2, 6, 3, 11]), 5.5)

    def test_average(self):
        self.assertEqual(average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(average([1]), 1.0)
        self.assertEqual(average([0]), 0.0)
        self.assertEqual(average([2, 6, 3, 11]), 5.5)

    def test_average_word_length(self):
        self.assertEqual(average_word_length(["blue"]), 4.0)
        self.assertEqual(average_word_length(["tea","coffee","milk","soda"]), 4.25)
        self.assertEqual(average_word_length(get_words()), 6.5888)



# This runs all the tests.
unittest.main()
