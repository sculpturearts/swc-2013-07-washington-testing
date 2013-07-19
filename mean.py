#!/usr/bin/env python

def mean(numlist):
    """Calculate the mean of the values in numlist

Input
=====
`numlist` (`list` or `tuple`) - List of values whose mean will be calculated

Output
======
(`float`) - Mean of the values in numlist
"""
    if len(numlist) == 0:
        return "A zero length number list was provided. Try again." 
    try :
        total = sum(numlist)
        length = len(numlist)
    except TypeError :
        raise TypeError("The list was not numbers.")
    except ZeroDivisionError :
        raise ZeroDivisionError("Doh! Empty list provided.")
    except NameError :
        raise NameError("Undefined variable.")
    except :
        print "Something unknown happened with the list."
    return float(total)/length
if __name__ == "__main__":
    mean([])
