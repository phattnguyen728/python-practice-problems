# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#

def calculate_sum(values):
    sum = 0
    if len(values) == 0:
        return None
    for num in values:
        sum += num
    return sum




print(calculate_sum([1, 1, 1, 1, 1, 1]))
