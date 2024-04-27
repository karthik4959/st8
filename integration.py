import unittest
from word import WordCounter
# Integration testing for all teh functions
class IntegrationTestWordCounter(unittest.TestCase):
    def test_integration(self):
        text = "Hello World"
        self.assertEqual(WordCounter.count_uppercase(self, text), 2) # Test for Uppercase letters
        self.assertEqual(WordCounter.count_lowercase(self, text), 8) # Test for lowercase letters
        self.assertEqual(WordCounter.count_vowels(self, text), 3) # Test For vowels count
        self.assertEqual(WordCounter.count_total_chars(self, text), 11) # test for total characters count including spaces
        self.assertEqual(WordCounter.count_total_words(self, text), 2) # Test for total words in the String

if __name__ == "__main__":
    unittest.main()

