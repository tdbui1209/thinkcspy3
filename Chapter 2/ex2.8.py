hours_of_day = 24
current_time = int(input('Current time? (24h) '))
set_alarm = int(input('Hours to wait? '))
go_off = (current_time + set_alarm) % hours_of_day
print('The alarm goes off at', go_off, ': 00')
