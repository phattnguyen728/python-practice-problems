# Complete the is_inside_bounds function which takes an x
# coordinate and a y coordinate, and then tests each to
# make sure they're between 0 and 10, inclusive.

def is_inside_bounds(x, y):
    if x in range(0, 10) and y in range(0,10):
        return 'inclusive'
    else:
        return 'Out of Bounds!!!'


print(is_inside_bounds(0,10))
