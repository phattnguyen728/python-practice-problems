# Write a function that meets these requirements.
#
# Name:       shift_letters
# Parameters: a string containing a single word
# Returns:    a new string with all letters replaced
#             by the next letter in the alphabet
#
# If the letter "Z" or "z" appear in the string, then
# they would get replaced by "A" or "a", respectively.
#
# Examples:
inputs1 = "import"
#       result:  "jnqpsu"
inputs2 = "ABBA"
#       result:  "BCCB"
inputs3 = "Kala"
#       result:  "Lbmb"
inputs4 = "zap"
#       result:  "abq"
#
# You may want to look at the built-in Python functions
# "ord" and "chr" for this problem

def next_letter(word):
    new_word = ""
    for letter in word:
        if letter == "Z":
            new_letter = "A"
        elif letter == "z":
            new_letter = "a"
        else:
            new_letter = chr(ord(letter) + 1)
        new_word += new_letter
    return new_word

print(next_letter(inputs1))
print(next_letter(inputs2))
print(next_letter(inputs3))
print(next_letter(inputs4))
