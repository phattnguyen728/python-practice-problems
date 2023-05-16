# Write a function that meets these requirements.
#
# Name:       username_from_email
# Parameters: a valid email address as a string
# Returns:    the username portion of the email address
#
# The username portion of an email is the substring
# of the email address that appears before the @
#
# Examples
input1 = "basia@yahoo.com"
#      returns: "basia"
input2 = "basia.farid@yahoo.com"
#      returns: "basia.farid"
input3 = "basia_farid+test@yahoo.com"
#      returns: "basia_farid+test"

def user(email):
    return email.split("@")[0]

print(user(input1))
print(user(input2))
print(user(input3))
