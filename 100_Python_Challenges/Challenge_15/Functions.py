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
