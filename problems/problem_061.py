# Write a function that meets these requirements.
#
# Name:       remove_duplicates
# Parameters: a list of values
# Returns:    a copy of the list removing all
#             duplicate values and keeping the
#             original order
#
# Examples:
input1 = [1, 1, 1, 1]
#       returns: [1]
input2 = [1, 2, 2, 1]
#       returns: [1, 2]
input3 = [1, 3, 3, 20, 3, 2, 2]
#       returns: [1, 3, 20, 2]

def remove_duplicates(input):
    result = []
    for value in input:
        if value not in result:
            result.append(value)
    return result

print(remove_duplicates(input1))
print(remove_duplicates(input2))
print(remove_duplicates(input3))
