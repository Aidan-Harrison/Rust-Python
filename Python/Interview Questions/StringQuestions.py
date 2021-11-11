# Longest common prefix

# Given an array such as:
#   ['apple', 'ape', 'april']
#   lcp = ap

# A prefix must contain the same characters, thus assuming we find a string in the array which does not match, we can discard it.
# We cannot sort it the elements themselves
# Example
#    Lets say we start iterating over the first string in the array, we can store the first letter and check that against all other elements in the array
#    If letters match, we can increase the prefix by appending that new letter.
#    When a letter does not match, we simply discard that word for now


def LongestCommonPrefixVersion1(array):
    size = len(array)

    if size == 0:
        return ""
    elif size == 1:
        return array[0]

    array.sort()

    # Find the minimum length the prefix has to be 
    length = min(len(array[0]), len(array[size-1]))

# Max Occuring Character

# "Hello World"
# MaxChar = 'l'

# Map
# 'H' | 1
# 'e' | 1
# 'l' | 3 => Max char
# 'o' | 2
# 'W' | 1
# 'r' | 1
# 'd' | 1

# Research
def MaxOccuringCharacter(str):
    max = -1
    c = ''
    charCount = [0] * 256

    for i in str:
        charCount[ord(i)]+=1

    for i in str:
        if max < charCount[ord(i)]:
            max = charCount[ord(i)]
            c = i
    return c

def MaxOccuringCharacterOther(str): # Do!
    # Using map
    map = []

# Find the first character that has a duplicate
def FindFirstRepeating(str):
    # Pushing the string to a map will give us the amount of times each char appears
    # Loop through the string and see which characters value exceeds 1
    map = {0 : 0}
    print(map)
    for i in str:
        map = {i, 0}
    print(map)

# Find the first character that does not have a duplicate
def FindFirstNonRepeatingChar(str):
    # Same as previous but a difference check
    pass

def Anagram(str1, str2):
    if len(str) != len(str):
        return False
    str1.sort()
    str2.sort()
    for i in str1:
        if i != str2[i]:
            return False



print(MaxOccuringCharacter("Hello World"))
FindFirstRepeating("Test")