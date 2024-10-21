import re


class WordCounter:
 #Method to count total number of uppercase letters in the given string
    def count_uppercase(self, text):
        return sum(1 for char in text if char.isupper())
#Method to count total number of lowercase letters in the given string
    def count_lowercase(self, text):
        return sum(1 for char in text if char.islower())
# Method to count total number of vowels in teh given string
    def count_vowels(self, text):
        vowels = 'aeiouAEIOU'
        return sum(1 for char in text if char in vowels)
# Method to count total number of characters in the given string including spaces and special characters
    def count_total_chars(self, text):
        return len(text)
# Method to count total number of words in the given string
    def count_total_words(self, text):
        words = re.findall(r'\b\w+\b', text)
        return len(words)
