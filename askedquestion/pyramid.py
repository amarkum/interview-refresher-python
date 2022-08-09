"""
print a pyramid in python
"""

n = 15

# n is the input from the user
for i in range(1, n + 1, 2):
    stars = ""
    for j in range(n + 1 - i, 0, -2):
        stars += " "
    for k in range(0, i):
        stars += "*"
    print(stars)
