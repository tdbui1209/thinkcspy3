xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# a) Write a loop that prints each of the numbers on a new line.

for i in xs:
    print(i)

print('*****************************************************************')
# b) Write a loop that prints each number and its square on a new line.

for i in xs:
    print(i, i**2)

print('*****************************************************************')
# c) Write a loop that adds all the numbers from the list
# into a variable called total.

total = 0
for i in xs:
    total = total + i
print('total =', total)

print('*****************************************************************')
# d) Print the product of all the numbers in the list.

product = 1
for i in xs:
    product = product * i
print('product =', product)
