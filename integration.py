import unittest
from word import WordCounter


# Integration testing for all the functions
class IntegrationTestWordCounter(unittest.TestCase):
    def test_integration(self):
        text = "Hello World"

        # Test the integration by passing the output of one function as input to the next function
        lowercase_count = WordCounter.count_lowercase(self, text)
        uppercase_count = WordCounter.count_uppercase(self, text)
        vowel_count = WordCounter.count_vowels(self, text)
        total_chars_count = WordCounter.count_total_chars(self, text)
        total_words_count = WordCounter.count_total_words(self, text)

        # Verify the results
        self.assertEqual(uppercase_count, 2)  # Test for Uppercase letters
        self.assertEqual(lowercase_count, 8)  # Test for lowercase letters
        self.assertEqual(vowel_count, 3)  # Test For vowels count
        self.assertEqual(total_chars_count, 11)  # Test for total characters count including spaces
        self.assertEqual(total_words_count, 2)  # Test for total words in the String


if __name__ == "__main__":
    unittest.main()
