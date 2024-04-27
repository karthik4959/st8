import unittest
from word import WordCounter
# Unit testing for the functions
class TestWordCounter(unittest.TestCase):
        def test_count_uppercase(self):
            self.assertEqual(WordCounter.count_uppercase(self, "Hello World"), 2)
            self.assertEqual(WordCounter.count_uppercase(self, "NoUppercaseHere"), 3)
            self.assertEqual(WordCounter.count_uppercase(self, "ALLCAPS"), 7)

        def test_count_lowercase(self):
            self.assertEqual(WordCounter.count_lowercase(self, "Hello World"), 8)
            self.assertEqual(WordCounter.count_lowercase(self, "NoUppercaseHere"), 12)
            self.assertEqual(WordCounter.count_lowercase(self, "ALLLOWERCASE"), 0)

        def test_count_vowels(self):
            self.assertEqual(WordCounter.count_vowels(self, "Hello World"), 3)
            self.assertEqual(WordCounter.count_vowels(self, "NoUppercaseHere"), 7)
            self.assertEqual(WordCounter.count_vowels(self, "AEIOU"), 5)

        def test_count_total_chars(self):
            self.assertEqual(WordCounter.count_total_chars(self, "Hello World"), 11)
            self.assertEqual(WordCounter.count_total_chars(self, "NoUppercaseHere"), 15)
            self.assertEqual(WordCounter.count_total_chars(self, "AEIOU"), 5)

        def test_count_total_words(self):
            self.assertEqual(WordCounter.count_total_words(self, "Hello World"), 2)
            self.assertEqual(WordCounter.count_total_words(self, "NoUppercaseHere"), 1)
            self.assertEqual(WordCounter.count_total_words(self, "AEIOU"), 1)

if __name__ == "__main__":
    unittest.main()
