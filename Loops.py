#!/usr/bin/env python3
#FOR LOOP
#To repeat actions we can use a for loop.
#A for loop is written inside the code. A for loop can have 1 or more instructions. A for loop will repeat a code block. Repeation is continued until the stop condition is met. If the stop condition is not met it will loop infintely.
#These instructions (loop) is repeated until a condition is met.
city = ['Tokyo','New York','Toronto','Hong Kong']
print('Cities loop:')
for x in city:
    print('City: ' + x)

print('\n')  # newline

num = [1,2,3,4,5,6,7,8,9]
print('x^2 loop:')
for x in num:
    y = x * x
    print(str(x) + '*' + str(x) + '=' + str(y))
# loop is not a command. "for" defines x as what ever number the loop is currently at

print('\n')  # newline

clist = ['Canada','USA','Mexico','Australia']
print('Country List loop:')
for x in clist:
    print('Country: ' + x)

#adding in range to for function loops all values from 0 to entered value
print('\n')  # newline
print('Count from 0-100 loop:')
for x in range (101):
    print(x)

print('\n')  # newline
print('Multiplication Table')
number = [1,2,3,4,5]
for x in number:
    y=str(x*1) + " " + str(x*2) + " " + str(x*3) + " " + str(x*4) + " " + str(x*5)
    print(y)

#WHILE LOOP
# A while loop repeats code until the condition is met. 
# Unlike for loops, the number of iterations in it may be unknown. 
# A while loop always consists of a condition and a block of code.
# A while loop ends if and only if the condition is true, in contrast to a for loop that always has a finite countable number of steps.

print('\n')  # newline

x = 3                              
while x < 10:
    print(x)
    x = x + 1
#runs until x<10

print('\n')  # newline

clist = ["Canada","USA","Mexico"]
x = 0
while  x <= 2:
    print(clist[x])
    x = x + 1

print('\n')

x = 0
while x < 10:
    print ((x) + (x+1))
    x=x+1

print('\n')

numbers = [1,2,3,4,5,6]
index = 0
y=0
while index <6:
    y=numbers[index]+y
    index=index+1
print(y)

# ADD A COLON
print('\n')

x=0
y=0
while x <50:
    for z in range(100):
        y=x + z
    x=x+1
    print(y)

print('\n')

# Using a loop, output the largest number in the list of integers >0


listOfNumbers = [29, 4, 54, 108, 13, 250]
x=0
y=0
Bigun=0
while x < 6:
    y=listOfNumbers[x]
    if y > Bigun:
        Bigun = y
    x=x+1
print(Bigun)

