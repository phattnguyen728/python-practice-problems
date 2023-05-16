# Write a function that meets these requirements.
#
# Name:       group_cities_by_state
# Parameters: a list of cities in the format "«name», «st»"
#             where «name» is the name of the city, followed
#             by a comma and a space, then the two-letter
#             abbreviation of the state
# Returns:    a dictionary whose keys are the two letter
#             abbreviations of the states in the list and
#             whose values are a list of the cities appearing
#             in that list for that state
#
# In the items in the input, there will only be one comma.
#
# Examples:
input1 = ["San Antonio, TX"]
#       returns: {"TX": ["San Antonio"]}
input2 = ["Springfield, MA", "Boston, MA"]
#       returns: {"MA": ["Springfield", "Boston"]}
input3 = ["Cleveland, OH", "Columbus, OH", "Chicago, IL"]
#       returns: {"OH": ["Cleveland", "Columbus"], "IL": ["Chicago"]}
#
# You may want to look up the ".strip()" method for the string.

def group_cities_by_state(input):
    result = {}
    for city in input:
        name, state = city.split(",")
        state = state.strip()
        if state not in result:
            result[state] = []
        result[state].append(name)
    return result

print(group_cities_by_state(input1))
print(group_cities_by_state(input2))
print(group_cities_by_state(input3))
