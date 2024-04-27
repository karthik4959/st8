from word import WordCounter

wordcounter = WordCounter()

# Test case for the uppercase count function

def test_count_uppercase():
    text = "HEllo, World" # In put for the test
    expected_result = 3 # Expected out put
    result = wordcounter.count_uppercase(text) # Result for the test
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"

# Test case for the lowercase count function
def test_count_lowercase():
    text = "Hello, World" # input for the test
    expected_result = 8 # expected out put
    result = wordcounter.count_lowercase(text) # results for the test
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"


def test_count_vowels():
    text = "Hello, World" # Input for the test
    expected_result = 3 # expected out put for the test
    result = wordcounter.count_vowels(text) # Result for the test
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}" # print statement


def test_count_total_chars():
    text = "Hello, World" # input for the test
    expected_result = 12 # Expected output for the test
    result = wordcounter.count_total_chars(text) # Results for the test case
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}" # Print statement


def test_count_total_words():
    text = "Hello, World vvvv" # input for the test case
    expected_result = 3 # Input for the test case
    result = wordcounter.count_total_words(text) # result for the test case
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"