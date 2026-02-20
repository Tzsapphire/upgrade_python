# Given the list below
# sales = [120,450,800,50,900,300]
# Write a Python code that classifies items in the list as Low, Medium, or High. 

sales = [120, 450, 800, 50, 900, 300]
low =[]
for price in sales:
    if price < 300:
        print ('Low')
    elif 300 <= price <= 700:
        print ('Medium')
    else:
        print('High')


# Also, do a count of items based on this classification and finally give a sum of items in each classification
# Key: less than 300 – low
#        > 300 <= 700 medium
# > 700 that's high

# From temperatures = [30,22,35,19,40], print those above average.
temperatures = [30, 22, 35, 19, 40]
average = sum(temperatures) / len(temperatures)
for temperature in temperatures:
    if temperature > average:
        print (temperature)

# Given numbers = [12, 7, 9, 20, 33, 14, 5], print only even numbers and store them in a new list.
numbers = [12, 7, 9, 20, 33, 14, 5]
for number in numbers: 
    if number % 2 ==0:
        print(number)
