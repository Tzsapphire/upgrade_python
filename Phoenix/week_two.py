# You are going to get input from a student. 
# And then tell them their class of grade. 
# Ensure that you are able to filter out wrong input
#     3.5- 4.00 – First Class Honours
#     3.0-3.49 – Second Class Honours (Upper Division)
#     2.0-2.99 – Second Class Honours (Lower Division)
#     1.0-1.99 – Third Class Honours

# grade = input("Please whats your GPA=")
# grade = float(grade)
# if grade >= 3.5 and grade <= 4.0 :
#     print("First Class Honours")
# elif grade >= 3.0 and grade <= 3.49 :
#     print("Second Class Honours (Upper Division)")
# elif grade >= 2.0 and grade <= 2.99 :
#     print("Second Class Honours (Lower Division)")
# elif grade >= 1.0 and grade <= 1.99 :
#     print("Third Class Honours")
# else : 
#     print("You are not a student")


# Write a Python program that iterates through integers from 1 to 100. 
# For each multiple of three, print "Fizz" instead of the number; 
# for each multiple of five, print "Buzz". 
# For numbers that are multiples of both three and five, print "FizzBuzz".

# not_multiple = []
# multiple_three = []
# multiple_five = []
# multiple_fifteen = []
# for in_t in range(1, 101):
#     if in_t % 5 ==0 and in_t % 3 ==0 : 
#         multiple_fifteen.append(in_t)
#         # print("FizzBuzz")
#     elif in_t % 5 ==0:
#         multiple_five.append(in_t)
#         # print("Buzz")
#     elif in_t % 3 ==0:
#         multiple_three.append(in_t)
#         # print("Fizz")
#     else : 
#         not_multiple.append(in_t)
        
# print("The non multiples of five, three and fifteen are :",not_multiple)
# print(" The count of non multiples of five, three and fifteen is :", len(not_multiple))
# print(" The multiples of fifteen are :", multiple_fifteen)
# print(" The count of multiples of fifteen is :", len(multiple_fifteen))
# print(" The multiples of five are :", multiple_five)
# print(" The count of multiples of five is :", len(multiple_five))
# print(" The multiples of three are :", multiple_three)
# print(" The count of multiples of three is :", len(multiple_three))

