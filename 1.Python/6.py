"""
    6. Find the first 10 pairs of amicable numbers.
"""


def sum_divisors(n):
    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
    return total


count = 0
for i in range(1, 100000):
    a = sum_divisors(i)
    b = sum_divisors(a)
    if a <= i:
        continue
    if b == i:
        print(i, ",", a)
        count += 1
    if count == 9:
        break
