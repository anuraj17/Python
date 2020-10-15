"""
Wednesday, October 14, 2020 at 5:23:11 PM
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""

target = [2, 5, 1, 3, 4, 7]
n = 3

for i in range(0, n):
    print(target[i])
    print(target[i + n])