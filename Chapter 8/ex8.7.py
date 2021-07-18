from unit_test import test

def reverse(s):
    return s[::-1]

def test_suite():
    test(reverse("happy") == "yppah")
    test(reverse("Python") == "nohtyP")
    test(reverse("") == "")
    test(reverse("a") == "a")

test_suite()
