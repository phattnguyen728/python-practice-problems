# Write a function that meets these requirements.
#
# Name:       only_odds
# Parameters: a list of numbers
# Returns:    a copy of the list that only includes the
#             odd numbers from the original list
#
# Examples:
input1 = [1, 2, 3, 4]
#       returns: [1, 3]
input2 = [2, 4, 6, 8]
#       returns: []
input3 = [1, 3, 5, 7]
#       returns: [1, 3, 5, 7]


def odds(numbers):
    result = []
    for num in numbers:
        if num % 2 == 1:
            result.append(num)
    return result

print(odds(input1))
print(odds(input2))
print(odds(input3))
