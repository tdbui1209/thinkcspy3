from unit_test import test

def reverse(s):
    return s[::-1]

def is_palindrome(s):
    reverse_s = reverse(s)
    if s == reverse_s:
        return True

def test_suite():
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome(""))
        
test_suite()
