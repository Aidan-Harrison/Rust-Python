# General programming problems
def ReverseString(str):
    revString = ""
    for x in range(len(str)-1, -1, -1):
        revString += str[x]
    return revString

def Palindrome(str):
    if str == ReverseString(str):
        return True
    else:
        return False

def RiverFinder(field):
    return

def Anagram(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return False
    if len(str1) != len(str2):
        return False
    anagram = ""
    for i in str1:
        anagram += str1[i]
    if anagram == str2:
        return True
    return False

def Pyramid():
    return

def SumOfIntegers(integers):
    sum = 0
    for x in integers:
        sum += x
    return sum

def ArraySearch(arr): # Searches through an array, vertically, horizontally and diagonally
    return

ReverseString("Hello World")
print(Palindrome("Hello World"))
print(Palindrome("racecar"))
print(SumOfIntegers([1,2,3,4,5,6]))
ArraySearch([1,2,3,4,5,6])