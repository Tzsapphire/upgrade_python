# FOR LOOPS

# Task 1
# Given the list below
# sales = [120,450,800,50,900,300]
# Write a Python code that classifies items in the list as Low, Medium, or High. 

# Solution
# Print the list of sales
sales = [120, 450, 800, 50, 900, 300]

# create variables for storing the categories of prices
low =[]
medium = []
high = []

# loop through each prices in the sales list
for price in sales:
# create the conditions for the loop and append to empty list
    if price < 300:
        low.append(price)
        print(price, "is low")
    elif 300 <= price <= 700:
        medium.append(price)
        print(price, "is Medium")
    else:
        high.append(price)
        print(price, "is High")
print(f'Low prices are :{low}, \n Medium prices are :{medium}, \n High prices are :{high}')


# Task 1b
# Also, do a count of items based on this classification and finally give a sum of items in each classification
# Key: less than 300 – low; > 300 <= 700 medium ; > 700 that's high



# Task 2
# From temperatures = [30,22,35,19,40], print those above average.
temperatures = [30, 22, 35, 19, 40]
average = sum(temperatures) / len(temperatures)
print('the average of these temperatures is: ', average)
for temperature in temperatures:
    if temperature > average:
        print ('above average temperatures are: ', temperature)



# Task 3
# Given numbers = [12, 7, 9, 20, 33, 14, 5], print only even numbers and store them in a new list.

# Solution
# Create the list of numbers
numbers = [12, 7, 9, 20, 33, 14, 5]

# create variable for storing even numbers
even_numbers = []

# loop through numbers and condition for the even numbers
for number in numbers: 
    if number % 2 ==0:
# store the even numbers in the container designed
        even_numbers.append(number)
        print(number)
print('The list of even numbers are: ', even_numbers)