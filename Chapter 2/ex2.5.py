# The formula of Periodic compounding
#
# A = P * (1 + r / n)**(n*t)
#
# A = final amount
# P = principal amount
# r = annual nominal interest rate
# n = number of times the interest is compounded per year
# t = number of year

P = 10000
r = 0.08 # 8%
n = 12
t = int(input('How many year do you want to deposite? '))
A = P * (1 + r / n)**(n*t)
print('Final amount after', t, 'year with', r, '% interest:', A, '$')
