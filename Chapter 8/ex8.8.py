from unit_test import test

def mirror(s):
    return s + s[::-1]

def test_suite():
    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")

test_suite()
