# -*- coding: utf-8 -*-


"""🟢 PART 1: NUMERIC EXERCISES (REGULAR PRACTICE) 🔹 A. Types & Conversion Exercise 1

Create:
an integer; a float

Print:
the value
the type of each
"""

x = 3
y=3.4
print(type(x))
print(type(y))

"""Exercise 2

Create a number as a string:

"25"


Convert it to an integer

Convert it to a float

Print all values and their types
"""

x = '25'
print((x))
print(type(x))

as_int = int(x)
print((as_int))
print(type(as_int))

as_float = float(x)
print((as_float))
print(type(as_float))

"""Exercise 3

Create: 10.7

Convert it to an integer

Print the result

👉 Observe what happened. : the decimal part has been removd
"""

x = 10.7
print((x))
print(type(x))

as_int = int(x)
print((as_int))

"""🔹 B. Math Operators
Exercise 4

Using numbers 10 and 3,

calculate and print: addition , subtraction, multiplication, division, floor division, modulus, power
"""

x = 10
y = 3
print("for the numbers x=10 and y=3, ")
addition = x+y
print(addition, "is the addition")
subtraction = x -y
print("the subtraction is ", subtraction)
multiplication = x*y
print(multiplication, "is the multiplication")
division = x/y
print("the division is ", division)
floor_div = x//y
print(floor_div, "is the floor division")
modulus = x%y
print("the modulus is", modulus)
power = x**y
print(power, "is the power of the two numbers")

"""Exercise 5

Create two numbers and print:

their sum

their difference

their remainder when divided
"""

x = 8
y= 3
print(x+y)
print(x-y)
print(x%y)

"""Exercise 6

Ask the user for two numbers and print:

addition result

multiplication result
"""

number_one = int(input("whats your first number?"))
number_two = int(input("whats your second number?"))
print("addition result is", number_one + number_two)
print("multiplication result is", number_one * number_two)

"""🔹 C. Rounding
Exercise 7

Create: -12.8

Apply and print: abs() ; round()
"""

x = -12.5
print(abs(x))
print(round(x))

"""Exercise 8

Create: 9.3


Print: ceil() result  ;  floor() result  ;  trunc() result
"""

import math

x = 9.3
print(math.ceil(x))
print(math.floor(x))
print(math.trunc(x))

"""Exercise 9

Create:

5.6789


Round it to:

2 decimal places

1 decimal place
"""

x = 5.6789
print(round(x,2))
print(round(x,1))

"""🔹 D. Advanced Math (math module)

(Import math once)

Exercise 10
Create: 10

Print:

sine , logarithm , cosine, square root
"""

x = 10
print(round(math.sin(x),3))
print(round(math.log(x),3))
print(math.cos(x))
print(math.sqrt(x))

"""🔹 E. Random Numbers
Exercise 13

Generate:

a random number between 0 and 1

print it
"""

import random
print(random.random())

"""Exercise 14

Generate:

a random integer between 1 and 10

print it
"""

import random
print(random.randint(1, 10))

"""Exercise 15

Generate two random integers and print:

their sum
"""

import random
generate_hello =random.randint(1, 10)
print(generate_hello)
print("the generated number is", generate_hello)

import random
generate = random.randint(1, 10)
generate_one = random.randint(1, 10)
print("the generated number is", generate)
print("the generated number is", generate_one)
print("the sum of the generated number is", generate + generate_one)

import random
generate = random.randint(1, 10)
generate_one = random.randint(1, 10)
print("the generated number is", generate)
print("the generated number is", generate_one)
print("the sum of the generated number is", generate + generate_one)

"""🔹 F. Validation
Exercise 16

Create:

10 . 10.5

Check and print:

whether it is an integer

whether it is an instance of int

whether it is an instance of float
"""

x= '10.5'
# print(x.is_integer())
print(isinstance(x, float))
print(isinstance(x, int))
print(x.isnumeric())
print(x.isdigit())

"""isdigit(): lso string method, use for, Simple positive integers, Fails on negatives

isnumeric()	is a string method that checks if all characters in a string are numeric, Fails on negatives & decimals, can recognise roman numerals and fractions

isinstance(): best when you already have a variable

.is_integer() checks whether a float number has no decimal part.

Exercise 18

Ask the user for a number

Convert it to integer

Print:

its type

whether it is an integer
"""

user = input("give me a number: ")
user_int = int(user)
print(type(user_int))