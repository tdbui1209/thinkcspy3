from unit_test import test

def remove(substring, s):
    result = ''
    idx = s.find(substring) # first letter's index of substring

    # Substring not in string, return string
    if idx == -1:
        return s
    
    # take slide exclude substring (first letter's index + length substring)
    result = s[:idx] + s[idx+len(substring):] 
    return result
            
def test_suite():
    test(remove("an", "banana") == "bana")
    test(remove("cyc", "bicycle") == "bile")
    test(remove("iss", "Mississippi") == "Missippi")
    test(remove("eggs", "bicycle") == "bicycle")

test_suite()
