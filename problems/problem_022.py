# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(is_workday, is_sunny):
    gear = []
    if (
        is_sunny == 'no'
        and is_workday == 'yes'
    ):
        gear.append('umbrella')
    if is_workday == 'yes':
        gear.append('laptop')
    if is_workday == 'no':
        gear.append('surfboard')

    return gear


print(gear_for_day('no', 'no'))
