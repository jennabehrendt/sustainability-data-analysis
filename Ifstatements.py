#!/usr/bin/env python3
# if <condition>:
#     <statement>
# to make multiple lines text, highight and press ctrl + ? or /
# indentation matters!! need 4 spaces (or tab)
x=3
if x <10:
    print("x below ten")
if x > 10:
    print ('x is greater than ten')
if x>1 and x <4:
    print('x is in range')
#every if statement needs a colon after the condition
#Can incorporate multiple statements into a block
x=4
if x<5:
    print('x is smaller than 5')
    print("this means it's not equal to five either")
    print('x is an integer')

# If-else evaluates statements. = is assigning a value, == is a comparison or check
gender = raw_input("Gender? ")
if gender == "male" or gender == "Male":
    print("Your cat is male")
else:
    print("Your cat is female")

age = raw_input("Age of your cat?")
if age < 5:
    print("Your cat is young.")
else:
    print("Your cat is adult.")
# < is just less than (ie: example above would generate your cat is an adult if you type in "5")
# Elif (else if) - evaluates several cases at once
x = 3
if x == 2:
    print('two')
elif x == 3:
    print('three')
elif x == 4:
    print('four')
else:
    print('something else')
#exercise
x = raw_input("Number?")
if x==1 and x==10:
    print("valid")
else:
    print ("invalid")

#check if there's a colon, or if you need an additional =sign
