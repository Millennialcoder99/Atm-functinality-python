from main import *
#11111111111. input \\\
# In a classic chase, Tom is running after Jerry as Jerry has eaten Tom's favourite food.
# Jerry is running at a speed of X
# X metres per second while Tom is chasing him at a speed of Y
#  metres per second. Determine whether Tom will be able to catch Jerry.
# Note that initially Jerry is not at the same position as Tom.
# Take X of Jerry and Y of Tom from the user and make decision and
# print YES if tom can catch and NO if not.
# Sample Input
# 2 3
# 4 1
# 1 1
# 3 5
# from sys import int_info

# code
# x= int(input('input the jerry value speed :'))
# y = int(input('input the tom value :'))
#
# if y>x:
#     print('yes tom can catch jerry')
# else:
#     print(' No jerry reached before tom')
# 2222222222...

# Apple considers any iPhone with a battery health of 80
# 80% or above, to be in optimal condition.
# Given that your iPhone has X
# X%battery health, find whether it is in optimal condition.
# Take Battery Health from User and print YES if in optimal condition and NO if not.
# Sample Input
#
# Copy
# 97
# 42
# 80
# 10

# code
# x= int(input('put value of battery percentage'))
# if x >=80:
#     print('it is in optimal condition.')
# else:print('battery is not optimal for your phone ')

# 3333333333
#
# While purchasing certain items, a discount of 10 % is offered if the quantity purchased is more than 1000.
# If quantity and price per item are input through the keyboard, write a program to calculate the total expenses.

#
# qty = int(input('whats your qty'))
# price= int(input('whats your price'))
#
# if qty >= 1000:
#     dis = 10
# else:
#     dis =0
#
# total_dis = price*qty-(price*qty*dis/100)
# print(your total is after discount is {total_dis})




# my mind que :Change for new resume salary for employee #

# salary = int(input('salary :'))
# experience = int(input('whats your experience'))
#
# if experience >3:
#     discount = 5
# else:
#     discount  = 0
#
# your_total_salary = salary-salary*discount/100
# print('total salary of exp is {your_total_salary}')

# ###333333333333333
# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user
# for their salary and year of service and print the net bonus amount.

# salary = float(input("Enter salary : "))
# yos = int(input("Enter year of service : "))
# if yos>5:
#   print("Bonus is",(5/100)*salary)
# else:
#   print("No bonus")

#########4
# A University allows students to sit in the exam despite insufficient attendance if the students attendance is short
# due to some medical cause. Take Input from User whether he had medical cause (Y/N) and print the message you are
# allowed if medical cause == Y otherwise print you are not allowed.


# medical= input('yes/no')
# if medical == 'yes':
#     print('you are eligible')
# else:print('no you are not eligible')


#######5


# Write a program to check whether the last digit of the number is divisible by 3 or not.
# Take Number from user and your output must contain the number.

# input = int(input('put your no.'))
# if (input%10)%3 == 0:
#     print(f' {input}number is divisible by 3')
# else:print(f' {input}number is not divisible by 3')
#


#####6
# Write a program to display ‘Hello’ if the number entered by user is multiple of 5 otherwise prints ‘Bye’.
# number = int(input('put your number here'))
# if number %5==0:
#     print('hello')
# else:print('bye')

#######7
# Write a program to check whether a person is eligible for voting or not.(voting age >=18)

# input = int(input('enter your age'))
# if input>=18:
#     print('you are eligible for vote')
# else:print('you are njot eligible')

###########8
#Write a program to check whether a number entered by user is even or odd.
# input = int(input('enter your number'))
# if input%2==0:
#     print('number is even')
# else:print('odd')

###########9
# Write a program to check whether a given character is a vowel or a consonant.
# input = input("Enter a character: ")
# if input in "AEIOUaeiou":
#     print(input, "is a vowel")
# else:
#     print(input, "is a consonant")

#########11
# Write a program to check whether a given string is a valid email address
# (i.e., it contains exactly one "@" symbol and at least one "." after the "@").

# email = input("Enter an email address: ")
# if email.count("@") == 1 and "." in email[email.index("@"):]:
#     print("The email address is valid")
# else:
#     print("The email address is not valid")



#########12
# Write a program to calculate the electricity bill (accept number of unit from user)
# according to the following criteria :

# Unit                    Price
# First 100 Units      No charge
#
# Next 100 Units       5 Rs Per Unit
#
# After 200 Units      10 Rs Per Unit


# no_of_unit = int(input('Units : '))
# if(no_of_unit<=100):
#     bill = 0
# elif(no_of_unit>100 and no_of_unit<=200):
#     bill = no_of_unit * 5
# else:
#     bill =  no_of_unit * 10
# print(bill)
#


# no_of_unit = int(input('Units : '))
# if(no_of_unit<=100):
#     bill = 0
# elif(no_of_unit>100 and no_of_unit<=200):
#     bill = 0+(no_of_unit-100) * 5
# else:
#     bill = 0+500 + (no_of_unit - 200)*10
# print(bill)

##########13

# Write a program to accept percentage from the user and display the grade according to the following criteria:
#
# Mark          Grade
# >=90             A
#
# >=80 and <90     B
#
# >=60 and <80     C
#
# <60              D

# mark = float(input('enter your percentage :'))
# if mark >= 90:
#     print('you got grade A ')
# elif (mark>80 and mark<=90):
#     print('you got grade B ')
# elif (mark>60 and mark<=80):
#     print('you got grade C ')
# else:
#     print('you got grade D' )


#######14
# "Write a python program that will check for the following conditions:
# If the light is green – Car is allowed to go
# If the light is yellow – Car has to wait
# If the light is red – Car has to stop
# Other signal – unrecognized signal. Example black, blue, etc…"

# Light = input('color  signal')
# if Light == 'green':
#     print('Car is allowed to go')
# elif Light == 'yellow':
#     print('Car has to wait')
# elif Light == 'red':
#     print('car has to stop')
# else:print('Unrecgniswd signals')

####15

# # Write a program to check whether the given number is positive, zero or negative.
# number = int(input('enter the number'))
# if number>0:
#     print('number is positive')
# elif number<0:
#     print('number is negative')
# else:print('zero')

#######16

# # Calculate income tax for the given income by adhering to the below rules
# # Taxable Income        Rate (in %)
# # First Rs.10,0000         0
# # Next Rs. 10,0000       10
# # The remaining           20
#
#
# Taxable_income =float(input('salary income'))
# if Taxable_income<=100000:
#     tax = 0
# elif Taxable_income <=200000:
#     tax = (Taxable_income - 100000) * 0.10
# else: tax = (100000 * 0.10) + (Taxable_income - 200000) * 0.20
# print(tax)

####17
# Write a program to take a digit and print it is In words(only 0 - 9)
# For Example : enter digit : 5
#                         Five

# digit = int(input('Enter Digit : '))
# if digit >=0 and digit <= 9:
#     if digit == 0:
#         print('Zero')
#     elif digit == 1:
#         print('One')
#     elif digit == 2:
#         print('Two')
#     elif digit == 3:
#         print('Three')
#     elif digit == 4:
#         print('Four')
#     elif digit == 5:
#         print('Five')
#     elif digit == 6:
#         print('Six')
#     elif digit == 7:
#         print('Seven')
#     elif digit == 8:
#         print('Eight')
#     elif digit == 9:
#         print('Nine')
# else:
#     print('Digit is either less than 0 and greater than 9')

#####19
# Write a menu driven program for making a simple calculator.
# num1 = int(input('enter a first number='))
# num2 = int(input('enter a second number='))
#
# print('select 1 for addition')
# print('select 2 for substraction')
# print('select 3 for multiply')
# print('select 4 for division')
#
# choice= (input('what you want , select anyone from above'))
# if choice=='1':
#     print(f'addition of two number{num1} and {num2} is {num1+num2} ')
# elif choice=='2':
#     print(f'subs of two number{num1} and {num2} is {num1-num2} ')
# elif choice == '3':
#     print(f'multiply of two number{num1} and {num2} is {num1 * num2} ')
# elif choice == '4':
#     print(f'div of two number{num1} and {num2} is {num1 / num2} ')
# else:
#     print('SORRY, you have not opt from above')\

####own age process

# country1= input('enter you country name')
# if country1 == 'india':
#     age =int(input('enter your age'))
#     if age>=18:
#       voter_id=input('do you have your id')
#       if voter_id=='yes':
#           print('you are eligible for vote')
#       else:print('no id,  no vote')
#     else:print('your age is not valid')
# else:print('you are not an indian')

####20

# An institution has decided to admit new candidates in different streams on the following criteria:
#
# Total Marks Obtained                               Streams Offered
#
# 300 and above                                            Science
# 200 and above but less than 300                          Commerce
# Below 200 but not below 75                               Arts
# Otherwise                                                Admission is not granted,
#                                                          You have to appear in qualifying examination
#
# Write a program to input total marks obtained in an examination and print the stream
# allotted on the basis of above criteria.

# marks = int(input("Enter total marks obtained: "))
#
# if marks >= 300:
#     stream = "Science"
# elif marks >= 200 and marks < 300:
#     stream = "Commerce"
# elif marks >= 75 and marks < 200:
#     stream = "Arts"
# else:
#     stream = "Qualifying examination"
#
# print("Stream allotted: ", stream)

###########21
# A Scooter /motor cycle stand charges the following rates for the parking:
#
#        Hours                                                                  Rate
#
# First 4hours                                                 RS.5.00
# Every next hour upto5 hours                                  RS.3.00 per hour
# Any further hour above 9 hour                                RS.2.00 per hour
#
# Write a program to input the number of hours for which a two wheeler is parked.
# Calculate and print the parking charges to be paid by the customer.

# Input number of hours parked
# hours = int(input("Enter the number of hours parked: "))
#
# # Initialize parking charge
# charge = 0
#
# if hours <= 4:
#     charge = 5
# elif hours <= 9:
#     # Rs.5 for first 4 hours + Rs.3 per hour for next hours up to 9
#     charge = 5 + (hours - 4) * 3
# else:
#     # Rs.5 for first 4 hours + Rs.3 per hour for next 5 hours (5 to 9) = Rs.15
#     # Rs.2 for every hour above 9
#     charge = 5 + (5 * 3) + (hours - 9) * 2
#
# # Print the calculated charge
# print("Parking charges to be paid: Rs.", charge)

##########22

# Monthly Electricity bill is calculated as –
#
# Number of units Consumed                              Rate Per Unit
#
# <=100                                                       only meter rent Rs 200/-
# For next 200 units                                          Rs. 1.00 per unit
# For next 200 units                                          Rs 1.55 per unit
# For more than 500 units                                     Rs 2.10 per unit
#
# Write a program to take the consumer number, number of units consumed.
# Calculate bill amount. Print consumer number and total amount to be paid by the consumer.
# (Consumer number must be digits of length 5 and print appropriate message for incorrect input of consumer number).
#
# consumer_number = (input('enter consumer number: '))
# if not consumer_number.isdigit() or  len(consumer_number) != 5:
#     print('invalid consumer number')
# else:
#     unit_consumed = int(input('enter the unit'))
#     if unit_consumed <=100:
#         total_amount = 200
#     elif unit_consumed <=300:
#         total_amount = 200+(unit_consumed-100)*1
#     elif unit_consumed <=500:
#         total_amount= 200+200*1+(unit_consumed-300)*1.55
#     else:
#        total_amount = 200+200*1+200*1.55+(unit_consumed-500)*2.10
#     print("Consumer number:", consumer_number)
#     print("Total amount to be paid:", total_amount)

############23

# Write a menu driven program for three options. (Take input of option from user).
#
# i)     Area of circle
# ii)    Area of Rectangle
# iii)   Area of Square
#
# Print the area along with sides.
# print("Select an option:")
# print("1) Area of Circle")
# print("2) Area of Rectangle")
# print("3) Area of Square")
#
# option = input("Enter your choice (1/2/3): ")
#
# if option=="1":
#  radius = float(input("Enter the radius of the circle: "))
#  area_c = 3.14* radius ** 2
#  print(area_c)
#
# elif option=="2":
#     length = float(input('enter the length'))
#     breadth = float(input('enter the breadth'))
#     area_r = length*breadth
#     print(area_r)
# elif option=="3":
#  side=float(input('enter side of rectangle'))
#  area_s=(side**2)
#  print(area_s)
#
# else:print('no data')

# side1= float(input('enter side 1'))
# side2= float(input('enter side 2'))
# side3= float(input('enter side 3'))
#
# # first we will check if its triangle or not for that
# if side1+side2>side3 and side2+side3>side1 and side3+side1>side2:
#     if side1 == side2 == side3:
#         print("The triangle is an equilateral triangle.")
#         # check for isosceles triangle
#     elif side1 == side2 or side2 == side3 or side1 == side3:
#         print("The triangle is an isosceles triangle.")
#         # otherwise, it must be a scalene triangle
#     else:
#         print("The triangle is a scalene triangle.")
# else:
#     print("These sides do not form a triangle.")


###################################################   ATM  MACHINE PROJECT    #################################
# Now we will create a display screen of the atm along with a menu that will guide the user on the facilities a user
# can use from the machine.



# firstly, we will declare 3 variables. one for account balance, one for an account number, and one for the pin,
# # and initialize those variables
# pin='2473'
# account_balance=50000
# account_number='123456789'
#
# print('Welcome to Prince_Rupay atm')
# print('''1. Show account balance.
# 2 Cash withdrawal
# 3 Cash deposit
# 4 Pin Change''')
# ch=input('enter your choice:')
# # Now we will code for the 1st option i.e. if the user selects Show Account Balance
# if ch=='1':
#     x=input('enter your pin:')
#     account_blnce(pin,account_balance,x)
#
# # Now we will code for the 2nd option i.e. if the user selects for Cash Withdrawal.
# elif ch=='2':
#     x = input('enter your pin:')
#     cash_withdrawal = int(input('enter the amount you wish to withdraw:'))
#     cash_withdrwl(pin, account_balance, x, cash_withdrawal)
#
# # Now we will code for the 3rd option i.e. if the user selects for Cash Deposit.
# elif ch=='3':
#
#     account_details=input('enter the account details:')
#     cash_deposit(account_details,account_number)
#
#
# #
# # # Now we will code for the 4th option i.e. Pin Change.
# #
# #
# elif ch=='4':
#     x=input('enter your pin:')
#     pin_change(pin, x)
#
#
# # # If the user selects any option other than (1-4)code
# else:
#     print('you have entered wrong option')


# C:\Users\admin\PycharmProjects\PythonProject2\assigment.py


