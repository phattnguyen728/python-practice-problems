# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.


def find_second_largest(values):
    if len(values) <= 1:
        return None
    max_value = values[0]
    second_largest = None
    for value in values[1:]:
        if value > max_value:
            second_largest = max_value
            max_value = value
        elif second_largest is None or value > second_largest:
            second_largest = value
    return second_largest

