from word import WordCounter

wordcounter = WordCounter()

# Test case for the uppercase count function
"""
def test_count_uppercase():
    text = "HEllo, World" # In put for the test
    expected_result = 3 # Expected out put
    result = wordcounter.count_uppercase(text) # Result for the test
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"
"""
# Test case for the lowercase count function
def test_count_lowercase():
    text = "Hello, World" # input for the test
    expected_result = 8 # expected out put
    result = wordcounter.count_lowercase(text) # results for the test
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"

"""
def test_count_vowels():
    text = "Hello, World"
    expected_result = 3
    result = wordcounter.count_vowels(text)
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"


def test_count_total_chars():
    text = "Hello, World"
    expected_result = 12
    result = wordcounter.count_total_chars(text)
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"


def test_count_total_words():
    text = "Hello, World vvvv"
    expected_result = 3
    result = wordcounter.count_total_words(text)
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"
"""