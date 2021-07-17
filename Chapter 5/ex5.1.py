def num_to_dayname(num):
    names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday']
    if num not in range(7):
        return None
    else:
        return names[num]
