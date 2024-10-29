# a program that allows the user to enter two numbers, the program then determines and outputs the largest number
from userinputoutput import firstname

first = int(input("Enter your first number: "))
second = int(input("Enter your second number: "))

if first > second:
    print(first," is greater than ",second)
else:
    print(second," is greater than ",first)

