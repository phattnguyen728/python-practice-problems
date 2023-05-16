# Write a function that meets these requirements.
#
# Name:       sum_fraction_sequence
# Parameters: a number
# Returns:    the sum of the fractions of the
#             form 1/2+2/3+3/4+...+number/number+1
#
# Examples:
input1 = 1
#       returns: 1/2
input2 = 2
#       returns: 1/2 + 2/3
input3 = 3
#       returns: 1/2 + 2/3 + 3/4

def sum_frac_seq(input):
    sum = 0
    for i in range(1, input + 1):
        sum += i / (i + 1)
    return sum

print(sum_frac_seq(input1))
print(sum_frac_seq(input2))
print(sum_frac_seq(input3))
