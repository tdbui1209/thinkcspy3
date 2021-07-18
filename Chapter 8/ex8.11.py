from unit_test import test

def count(substring, s):
    idx = 0
    count = 0
    while idx < len(s):
        if s[idx:idx+len(substring)] == substring:
            count += 1
        idx += 1
    return count

def test_suite():
    test(count("is", "Mississippi") == 2)
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2)
    test(count("nana", "banana") == 1)
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)

test_suite()
