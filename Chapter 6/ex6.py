from unit_test import test

# ex9.1
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

# ex9.2
def day_name(num):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday']
    if num not in range(7):
        return None
    else:
        return days[num]

# ex9.3
def day_num(name):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday']
    if name not in days:
        return None
    return days.index(name)

# ex9.4
def day_add(current_day, delta):
    resulting_day_num = (day_num(current_day) + delta)
    resulting_day = day_name(resulting_day_num % 7)
    return resulting_day
    
# ex9.5 & 9.6
def days_in_month(name):
    thirty_one_days = ['January', 'March', 'May', 'July', 'August', 'October',
                       'December']
    thirty_days = ['April', 'June', 'September', 'November']
    twenty_eight_days = 'February'
    if name in thirty_one_days:
        return 31
    elif name in thirty_days:
        return 30
    elif name in twenty_eight_days:
        return 28
    else:
        return None
    
# ex9.7 & 9.8
def to_secs(hours, minutes, seconds):
    return int(hours * 3600 + minutes * 60 + seconds)

# ---------------------Unit test----------------------
def test_suite():
    '''Run the suite of tests for code in this module (this file)'''
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)
    test(day_add("Monday", 4) == "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433,0,0) == 8758)
    
test_suite()
