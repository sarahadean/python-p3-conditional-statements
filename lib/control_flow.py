#!/usr/bin/env python3

#takes two arguments: a username and password
# if username == 'admin' or 'ADMIN' and password is '12345'
#return access granted
#otherwise return 'access denied'
def admin_login(username, password):
    if (username == 'admin' or username == 'ADMIN') and password == '12345':
        return 'Access granted'
    else:
        return 'Access denied'


# Takes a temperature. If temperature <40 return "It's brisk out there!"
# If temperature >40 and =< 65 return "It's a little chilly out there!"
# if temp >85 return "It's too dang hot out there!"
# otherwise return "It's perfect out there!"
def hows_the_weather(temperature):
    if temperature <40:
        return "It's brisk out there!"
    elif temperature > 40 and temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


# Takes a number. 
# for multiples of 3, return 'Fizz' instead of a number
# for multiples of 5 return 'Buzz'
# for multiples of 3 and 5 return 'FizzBuzz'
# for all other numbers, return just the number
def fizzbuzz(num):
    if (num / 3).is_integer() and (num / 5).is_integer():
        return 'FizzBuzz'
    elif (num / 5).is_integer():
        return 'Buzz'
    elif  (num / 3).is_integer():
        return 'Fizz'
    else:
        return num
    
# Takes 3 args: an operator and 2 numbers
# if operator is +, -, * or /, return the value of calling the operation on the two numbers
#     otherwise output a messate saying "Invalid operation!" and return None
def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print('Invalid operation!')