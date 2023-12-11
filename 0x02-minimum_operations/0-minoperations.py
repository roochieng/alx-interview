#!/usr/bin/python3
""" Script that computes a minimum operations
    needed in a CopyAll - Paste task
"""


def minOperations(n):
    """
    Function for compute the minimum number
    of operations for task Copy All and Paste

    Args:
        n: input value
        factor_list: List to save the operations
    Return: the sum of the operations
    """
    if n < 2:
        return 0
    factor_list = []
    a = 1
    while n != 1:
        a += 1
        if n % a == 0:
            while n % a == 0:
                n /= a
                factor_list.append(a)
    return sum(factor_list)
