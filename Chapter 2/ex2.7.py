hours_of_day = 24
current_time = 14 # 2pm
set_alarm = 5100
go_off = (current_time + set_alarm) % hours_of_day
print('The alarm goes off at', go_off, ': 00')
