import re


class WordCounter:
#function to count the number of upper case letters in the given string
"""
    def count_uppercase(self, text):
        return sum(1 for char in text if char.isupper())
"""
# Function to count total number of lower case letters in the given string
    def count_lowercase(self, text):
        return sum(1 for char in text if char.islower())
"""
    def count_vowels(self, text):
        vowels = 'aeiouAEIOU'
        return sum(1 for char in text if char in vowels)

    def count_total_chars(self, text):
        return len(text)

    def count_total_words(self, text):
        words = re.findall(r'\b\w+\b', text)
        return len(words)
"""