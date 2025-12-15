from solution import longest_palindromic_substring


def test_basic_palindrome():
assert longest_palindromic_substring("babad") in {"bab", "aba"}




def test_single_char():
assert longest_palindromic_substring("a") == "a"




def test_empty():
assert longest_palindromic_substring("") == ""