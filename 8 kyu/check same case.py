# Write a function that will check if two given characters are the same case.

# If either of the characters is not a letter, return -1
# If both characters are the same case, return 1
# If both characters are letters, but not the same case, return 0


def same_case(a, b):
    if a.isalpha() and b.isalpha():
        if (a.isupper() and b.isupper()) or (a.islower() and b.islower()):
            return 1
        else:
            return 0
    else:
        return -1


same_case('C', 'B')
same_case('b', 'a')
same_case('A', 's')
same_case('c', 'B')
same_case('\t', 'Z')
same_case('H', ':')

# def same_case(a, b):
#     return a.isupper() == b.isupper() if a.isalpha() and b.isalpha() else -1