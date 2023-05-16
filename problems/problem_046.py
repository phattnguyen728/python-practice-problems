# Complete the make_sentences function that accepts three
# lists.
#   * subjects contains a list of subjects for three-word sentences
#   * verbs contains a list of verbs for three-word sentences
#   * objects contains a list of objects for three-word sentences
# The make_sentences function should return all possible sentences
# that can be made from the words in each list
#
# Examples:
s1 = ["I"]
v1 = ["play"]
o1 = ["Portal"]
#     returns:  ["I play Portal"]
s2 = ["I", "You"]
v2 = ["play"]
o2 = ["Portal", "Sable"]
#     returns:  ["I play Portal", "I play Sable",
#                "You play Portal", "You play Sable"]
s3 = ["I", "You"]
v3 = ["play", "watch"]
o3 = ["Portal", "Sable"]
#     returns:  ["I play Portal", "I play Sable",
#                "I watch Portal", "I watch Sable",
#                "You play Portal", "You play Sable"
#                "You watch Portal", "You watch Sable"]
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

def make_sentences(subjects, verbs, objects):
    sentences = []
    for subject in subjects:
        for verb in verbs:
            for object in objects:
                sentence = f"{subject} {verb} {object}"
                sentences.append(sentence)
    return sentences

print(make_sentences(s1, v1, o3))
print(make_sentences(s2, v2, o2))
print(make_sentences(s3, v3, o3))
