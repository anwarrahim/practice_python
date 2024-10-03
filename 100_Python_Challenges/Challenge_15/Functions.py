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
def calculate
