# Write a function that meets these requirements.
#
# Name:       num_concat
# Parameters: two numerical parameters
# Returns:    the concatenated string conversions
#             of the numerical parameters
#
# Examples:
#     input:
parameter2 = 10
parameter1 = 3
#     returns: "310"
#     input:
parameter3 = 9238
parameter4 = 0
#     returns: "92380"

def num_concat(a, b):
    return str(a) + str(b)

print(num_concat(parameter1,parameter2))
print(num_concat(parameter3,parameter4))
