from unit_test import test

def remove_letter(letter, s):
    result = ''
    for char in s:
        if char != letter:
            result += char
    # Comprehensions
    # result = 'char if char != letter for char in s'
    return result

def test_suite():
    test(remove_letter("a", "apple") == "pple")
    test(remove_letter("a", "banana") == "bnn")
    test(remove_letter("z", "banana") == "banana")
    test(remove_letter("i", "Mississippi") == "Msssspp")
    test(remove_letter("b", "") == "")
    test(remove_letter("b", "c") == "c")

test_suite()
