# Min Max Difference
# In this problem you will be given an array/list of integers. You need to find the largest value and the smallest value in the array. Finally you need to return the difference (largest value - smallest value) of the two values.
# Example:
the_array = [15, 22, 84, 14, 88, 23]
# the_highest_value = 88
# the_smallest_number = 14
# the_difference = 74

import math

# This function will find the highest value.
def highest_value(array):
    the_highest_value = max(array)
    return the_highest_value

#This function will find the smallest value.
def smallest_value(array):
    the_smallest_value = min(array)
    return the_smallest_value

# This function will find the difference between
# highest and smallest value.
def difference(array):
    the_difference = highest_value(array) - smallest_value(array)
    return the_difference

# print(highest_value(the_array))
# print(smallest_value(the_array))
# print(difference(the_array))
