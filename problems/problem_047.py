# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"

def check_password(password):
    has_lowercase_letter = False
    has_uppercase_letter = False
    has_digit = False
    has_special_char = False
    for character in password:
        if character.isalpha():
            if character.isupper():
                has_uppercase_letter = True
            else:
                has_lowercase_letter = True
        elif character.isdigit():
            has_digit = True
        elif character == "$" or character == "!" or character == "@":
            has_special_char = True
    return (
        len(password) >= 6
        and len(password) <= 12
        and has_lowercase_letter
        and has_uppercase_letter
        and has_digit
        and has_special_char
    )

print(check_password("asdfasd"))
print(check_password("asdfaDd"))
print(check_password("asdf"))
print(check_password("asdfasdfasdfasd"))
print(check_password("a!sdfasd"))
print(check_password("asdfasD1@"))
