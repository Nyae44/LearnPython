import unittest
from unittest import result
import cap

# We create a class and inherit Testcase from the unittest library
class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Monty Python')
if __name__ == '__main__':
    unittest.main()
    