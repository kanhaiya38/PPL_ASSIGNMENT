"""
    10. Find the first 10 numbers from geometric series
"""

a = float(input("Enter the first term of the Geometric Series: "))
r = float(input("Enter the Common Ratio of the Geometric Series: "))

print("First 10 numbers of Geometric Series are:")
for i in range(10):
    print(a * (r ** i), end=", ")
