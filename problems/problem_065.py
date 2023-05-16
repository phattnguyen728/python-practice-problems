# Write a function that meets these requirements.
#
# Name:       biggest_gap
# Parameters: a list of numbers that has at least
#             two numbers in it
# Returns:    the largest gap between any two
#             consecutive numbers in the list
#             (this will always be a positive number)
#
# Examples:
input1 = [1, 3, 5, 7]
#       result: 2 because they all have the same gap
input2 = [1, 11, 9, 20, 0]
#       result: 20 because from 20 to 0 is the biggest gap
input3 = [1, 3, 100, 103, 106]
#       result: 97 because from 3 to 100 is the biggest gap
#
# You may want to look at the built-in "abs" function


def biggest_gap(input):
    max_gap = abs(input[1] - input[0])
    for i in range(1, len(input) - 1):
        gap = abs(input[i + 1] - input[i])
        if gap > max_gap:
            max_gap = gap
    return max_gap

print(biggest_gap(input1))
print(biggest_gap(input2))
print(biggest_gap(input3))
