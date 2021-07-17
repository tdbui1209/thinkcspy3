def num_to_dayname(num):
    names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday']
    if num not in range(7):
        return None
    else:
        return names[num]

def day_return(starting_day ,n_sleeps):
    return print('You will return on',
                 num_to_dayname((starting_day + n_sleeps) % 7))

starting_day = int(input('Leaving day number (example: Wednesday is 3): '))
n_sleeps = int(input('Return home after: '))
day_return(starting_day, n_sleeps)
