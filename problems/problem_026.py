# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average

def calculate_grade(values):
    if values == 100:
        return f"{values}!!! Why you no get A+++!!!"
    elif values > 95 and values < 100:
        return f"{values}!!! Why you no get A+!!!"
    elif values >= 90 and values <= 95:
        return f"{values}!!! A MINUS!!! Go to your room!!!"
    elif values >= 80 and values < 90:
        return f"{values}!!! B!!! You DISAPPOINT ME!!!"
    elif values >= 70 and values < 80:
        return f"{values}!!! C!!! You grounded until you DOCTOR!!!"
    elif values >= 60 and values < 70:
        return f"{values}!!! D!!! Why you no like Jimmy!!! He 14 and He DOCTOR!!!"
    else:
        return f"{values}!!! F!!! You no longer my child, get out da house!!!"

print(calculate_grade(59))
