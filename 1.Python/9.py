"""
     9. Find the first 10 harmonic divisor numbers.
"""

import statistics
divisor = []
harmonic_nums = []
count = 0
for i in range(1, 10000):
    if count >= 10:
        break
    divisor = [j for j in range(1, i + 1) if i % j == 0]
    num = (statistics.harmonic_mean(divisor))
    if int(num) == num:
        harmonic_nums.append(int(i))

print(*harmonic_nums, sep=", ")
