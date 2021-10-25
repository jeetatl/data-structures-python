import unittest

from jeetatl.coding_lib import anagram
from jeetatl.coding_lib.descending_frequency import DescendingFrequency


class TestDescendingFrequency(unittest.TestCase):
    def test_input_and_output_strings_are_anagrams(self):
        input_string = '1234asdfasdfasdf'
        output_string = DescendingFrequency.frequency_sort(input_string)
        self.assertTrue(anagram.is_anagram(input_string, output_string))


if __name__ == '__main__':
    unittest.main()
