# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

#def has_quorum(attendees_list, members_list):
#    if attendees_list / members_list >= 0.5:
#        return "More than 50 percent were present."
#
#
#
#print(has_quorum(5, 10))

def has_quorum(attendees_list, members_list):
#test if number of ppl in attendees list is >= 0.5* ppl in members list
#number of ppl on the list
    attendees_num = len(attendees_list)
    members_num= len(members_list)

    if attendees_num >= 0.5 * members_num:
        return True
    else:
        return False


print(has_quorum(["kop","yu", "peter", "mary"],["peter","mary","john","xa", "kop","yu"]))
