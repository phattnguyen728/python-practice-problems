# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):
    if len(values) == 0:
        return None
    mv = values[0]
    for blah in values:
        if blah > mv:
            mv = blah
    return mv


print(max_in_list([11, 22, 33, 55]))
