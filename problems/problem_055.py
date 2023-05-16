# Write a function that meets these requirements.
#
# Name:       simple_roman
# Parameters: one parameter that has a value from 1
#             to 10, inclusive
# Returns:    the Roman numeral equivalent of the
#             parameter value
#
# All examples
input1 = 1
#       returns: "I"
input2 = 2
#       returns: "II"
input3 = 3
#       returns: "III"
input4 = 4
#       returns: "IV"
input5 = 5
#       returns: "V"
input6 = 6
#       returns: "VI"
input7 = 7
#       returns: "VII"
input8 = 8
#       returns: "VIII"
input9 = 9
#       returns: "IX"
input10 = 10
#       returns:  "X"

def simple_roman(input):
    convert_to_roman = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X"
    }
    return convert_to_roman[input]

print(simple_roman(1))
print(simple_roman(2))
print(simple_roman(3))
print(simple_roman(4))
print(simple_roman(5))
print(simple_roman(6))
print(simple_roman(7))
print(simple_roman(8))
print(simple_roman(9))
print(simple_roman(10))
