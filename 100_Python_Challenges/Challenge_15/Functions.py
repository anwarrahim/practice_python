from itertools import count

import numpy as np
from dask.array import minimum
from skimage.filters.rank import maximum

"""
Task 1:
Write a function square that takes a number as input and returns its square.
"""
def square(num):
    return num ** 2
area = square(5)
print(area)

"""
Task 2:
Write a function is_prime that takes a number as input and returns True if it's prime, and False otherwise.
"""
def is_prime(num):
    if num <=1:
        return False
    for i in range(2, int(num ** 1.5) +1):
        if num % i !=0:
            return True
        else:
          return False

print(is_prime(6))

"""
Task 3:
Write a function greet_multiple that takes a list of names as input and prints a personalized greeting message for each name.
"""

def greet(name):
    print("Hi "+ ""+name + ", How are you? I want to tell you about tommorow plan")

greet('Anwar Rahim')
greet("maaz khan")

"""
Task 4:
Write a function calculate_total that takes a list of numbers as input and returns their total sum.
"""
def calculate(a, b, c):
    return a+b+c
total = calculate(2,5,6)
print(total)



"""
Task 5:
Write a function convert_temperature that takes a temperature in Celsius as input and returns the equivalent temperature in Fahrenheit.
"""

def convert_temp(celsius):
    return (celsius * 1.8) + 32
Fahrenheit = int(convert_temp(45))
print(Fahrenheit)

"""
Task 6:
Write a function find_max that takes a list of numbers as input and returns the largest number in the list.
"""
def find_max():
    numbers = [2,4,6,74,76,85,88]
    maximum = max(numbers)
    print(maximum)
find_max()
find_max()

# other method

def find_min(numbers):
    if not numbers:
        return None
    count = 0
    minimum = numbers[0]
    for number in numbers:
        count +=1
        if number < minimum:
            minimum = number
    print(f"Number of iterations: {count}")
    return minimum

numbers = [5,3,6,3,1,7,8]

print(find_min(numbers))

"""
Use format() method to insert values into your string, indicated by braces.

"""
name ='Anwar Rahim'
age = 24
print('my name is {} and my age is {} year old'.format(name,age))