from unit_test import test

def turn_clockwise(direction):
    if direction == 'N':
        return 'E'
    elif direction == 'E':
        return 'N'
    elif direction == 'N':
        return 'W'
    elif direction == 'W':
        return 'N'
    else:
        return None

def test_suite():
    '''Run the suite of tests for code in this module (this file)'''
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)

test_suite()
