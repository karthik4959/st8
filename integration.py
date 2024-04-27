import unittest
from word import WordCounter

class IntegrationTestWordCounter(unittest.TestCase):
    def test_integration(self):
        text = "Hello World"
        self.assertEqual(WordCounter.count_uppercase(self, text), 2)
        self.assertEqual(WordCounter.count_lowercase(self, text), 8)
        self.assertEqual(WordCounter.count_vowels(self, text), 3)
        self.assertEqual(WordCounter.count_total_chars(self, text), 11)
        self.assertEqual(WordCounter.count_total_words(self, text), 2)

if __name__ == "__main__":
    unittest.main()
