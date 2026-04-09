# -*- coding: utf-8 -*-
"""One.ipynb

Level 1
Ask the user for two numbers and:

print their sum, difference, product, division

👉 Hint: convert input to int or float.
"""

first_number = input("Enter your first number:")
second_number = input("Enter your second number:")

total = int(first_number) + int(second_number)
print("the sum of your numbers is", total)

difference = int(first_number) - int(second_number)
print("the difference of your numbers is", difference)

product = int(first_number) * int(second_number)
print("the product of your numbers is", product)

division = int(first_number) / int(second_number)
print(f"The division of your numbers is {division}")

"""Age in the Future

Ask: name, current age

Print: “Hello John, in 5 years you will be 30”
"""

name = input("hey, what is your name: ")
age = input("and your age?: ")
plus_years = 7
print(f"Hello {name}, in {plus_years} years you will be {int(age) + plus_years} years old")
print("Hello", name, ", in 7 years you will be", int(age) + plus_years, "years old")

"""Even or Odd

Ask for a number and print:

"Even" if divisible by 2

"Odd" otherwise

👉 Hint: %
"""

number = input("whats your number: ")
remainder = int(number) % 2
number_true = int(number) % 2 ==0
print("The remainder of your number when divided by 2 is ", remainder)
# print(type(remainder))
print("Is your number an even number? Answer is: ", number_true)



"""Temperature Converter

Ask for temperature in Celsius and convert to Fahrenheit
Formula:F = (C * 9/5) + 32
"""

celsius_temp = int(input("whats the temperature n celsius:"))
conversion = (celsius_temp * 9/5) +32
print("The temperature in Fahrenheit will be:", conversion)

"""==> List Index Practice

Create this list:

colors = ["red", "blue", "green", "yellow"]


Print:

- the first color

- the last color

- the total number of colors (you can use len())
"""

colors =  ["red", "blue", "green", "yellow"]
print("The first color is: ", colors[0])
print(colors[-1])
color_total= len(colors)
print("The total number of colors in this list is:", color_total)

"""Tuple Basics

Create a tuple:

person = ("John", 25, "Nigeria")

Print: name, age, country
"""

person = ("John", 25, "Nigeria")
print("His name is", person[0], "." "He is", person[1], "years old and he comes from", person[2], "." )
print(f"His name is {person[0]}. He is {person[1]} years old and he comes from {person[2]}.")

"""7️⃣ Dictionary Lookup

Create:

student = {
    "name": "Aisha",
    "age": 21,
    "course": "Computer Science"
}


Print a sentence using values from the dictionary:

“Aisha is 21 years old and studies Computer Science”
"""

student = { "name": "Aisha", "age": 21, "course": "Computer Science" }

"""8️⃣ Set Thinking

Create a set of numbers:

numbers = {1, 2, 3, 3, 4, 5}


Print the set and observe what happened.

👉 Question to answer in comments:

Why is 3 not repeated?
"""

numbers = {1, 2, 3, 3, 4, 5}
print(numbers)

print("""Why is 3 not repeated?
'because numbers is a set, and so does not allow repeated values/duplicates'
""")

"""9️⃣ Simple Login Check

Set:

saved_password = "python123"


Ask the user for a password.

If it matches → print "Access granted"

Else → print "Access denied"


"""





"""
🔟 Shopping Bill

Ask for: price of item,

quantity

Calculate and print:

total cost

Bonus:

if total > 100, print "You get a discount!"
"""

price = int(input("item_price ="))
quantity = int(input("quantity is "))
cost = price * quantity
print("The total cost is", cost)

"""1️⃣1️⃣ Student Score Report

Ask for:

name

score (0–100)

Print:

name

score

"Pass" if score ≥ 50

"Fail" otherwise
"""

name = str(input("what is your name?"))
score = int(input("what is your score?"))
print(name + ", " + str(score))
print("Is his score >= 50?", score >= 50)

"""1️⃣2️⃣ Average of 3 Numbers

Ask for 3 numbers.

store them in a list

calculate the average

print result
"""

number_one = input("first number:")
number_two = input("first number:")
number_three = input("first number:")
average_no = int(number_one + number_two + number_three) / 3
print("The average of your three numbers are ", average_no)

number_one = int(input("first number:"))
number_two = int(input("first number:"))
number_three = int(input("first number:"))
average_no = (number_one + number_two + number_three) / 3
print("The average of your three numbers are ", average_no)

"""
1️⃣3️⃣ Currency Converter

Ask for:

amount in USD

Assume:

rate = 1500  # 1 USD = 1500 NGN


Convert and print NGN value."""

amount_usd = int(input("The amount in USD: "))
ngn_value = amount_usd * 1500
print("The NGN value is", ngn_value)

"""
1️⃣4️⃣ Personal Profile

Ask user for:

name, age, height

Store everything in a dictionary, then print a clean profile summary."""

name = input("name =")
age = input("age =")
height = input("height =")
profile = dict(name, age, height)

"""This time solve with dictionary functions::

Even or Odd

Ask for a number and print:

"Even" if divisible by 2

"Odd" otherwise

👉 Hint: %

This time solve with if/else clause

Even or Odd

Ask for a number and print:

"Even" if divisible by 2

"Odd" otherwise

👉 Hint: %
"""



number = "+49 (176) 123-4567"
print(number.replace("+", "00").replace("(", "").replace(")", "").replace(" ", "").replace("-", ""))