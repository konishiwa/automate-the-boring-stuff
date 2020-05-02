#Chapter 1: Python Basics - Dissecting Your Program

# Any text for the rest of the line following a hash mark (#) is part of a comment.
# You can use comments for various things like describing variables/methods, debugging, etc!

# print() function displays the string value inside its parentheses on the screen.
print('Hello World!') # prints Hello World!
print() # prints an empty line
# argument - value passed into a function
myName = 'Ruka'
print('Hello My Name is: ' + myName)

# pass the len() function a string value (or a variable containing a string), 
# and the function evaluates to the integer value of the number of characters in that string.
print(len(myName)) # will print out 4 characters
print(len('')) # will print 0 charaters

#The following will result in a TypeError: 
number = 100
# print('I am ' + 29 + ' years old.')
# print('I am ' + number + ' years old.')

# use str() to change an int to a string
# this method can be used when you want to concatenate a number and a string
print('I am ' + str(100) + ' years old.')
print('I am ' + str(number) + ' years old.')

# str(), int(), and float() functions will evaluate to the string, integer, 
# and floating-point forms of the value you pass, respectively. 
# int() function is also helpful if you have a number as a string value 
# that you want to use in some mathematics
print(str(0))
print(int('-99'))
print(float('3.14'))

# input() function can be used to get user input
# input() function always returns a string
name = input("what is your name?")
print("Hello, " + name)
number = input("enter a number")
number = int(number) + 3 
print("Your number + 3 is " + str(number))
#The int() function is also useful if you need to round a floating-point number down.
floatnum = 12.4 
print('The floatnum as an int: ' + str(int(floatnum)))

# TEXT AND NUMBER EQUIVALENCE
# Although the string value of a number is considered a 
# completely different value from the integer or floating-point version, 
# an integer can be equal to a floating point.
42 == '42' # False 
42 == 42.0 # True
42.0 == 0042.000 # True
