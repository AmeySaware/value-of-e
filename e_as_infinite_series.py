# Created by Amey Saware

"""
Euler's constant can be expressed by its Taylor series expansion. This program computes Taylor expansion of e up to given number of terms
"""

def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


def taylor(num):
    """
    Determines the taylor sum of given terms
    """
    sum = float(0)
    for term in range(num):
        sum += float(1)/fact(num)
        pass
    print sum
    pass

taylor(4)
