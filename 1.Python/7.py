"""
     7. Find Armstrong Numbers in the given range. 
"""
import math


def is_armstrong(val):

    num = val
    n = int(math.log10(num)) + 1
    sum = 0

    for _ in range(n):
        digit = num % 10
        sum += digit ** n
        num //= 10

    if val == sum:
        return True
    else:
        return False


n = int(input("Enter n: "))

for i in range(1, n + 1):
    if is_armstrong(i):
        print(i, end=", ")
