from unit_test import test

def remove_all(substring, s):
    while True:
        idx = s.find(substring)
        if idx == -1:
            return s
        s = s[:idx] + s[idx+len(substring):]

def test_suite():
    test(remove_all("an", "banana") == "ba")
    test(remove_all("cyc", "bicycle") == "bile")
    test(remove_all("iss", "Mississippi") == "Mippi")
    test(remove_all("eggs", "bicycle") == "bicycle")

test_suite()
