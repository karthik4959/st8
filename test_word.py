from word import WordCounter

wordcounter = WordCounter()


def test_count_uppercase():
    text = "HEllo, World"
    expected_result = 3
    result = wordcounter.count_uppercase(text)
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"


def test_count_lowercase():
    text = "Hello, World"
    expected_result = 8
    result = wordcounter.count_lowercase(text)
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"


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
