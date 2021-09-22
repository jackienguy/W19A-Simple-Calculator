from addition import add_two_numbers
from subtraction import subtract_two_numbers
from multiplication import multiply_two_numbers
from division import divide_two_numbers

operation = input("Enter math operation (+, -, *, /):")
num1 = int(input('Enter your first number (1,2,3, or 4): '))
num2 = int(input('Enter your second number (1,2,3, or 4) '))


if operation == '+':
    print (add_two_numbers(num1, num2))
elif operation == '-':
    print (subtract_two_numbers(num1, num2))
elif operation == '*':
    print (multiply_two_numbers(num1, num2))
elif operation == "/":
    print (divide_two_numbers(num1, num2))