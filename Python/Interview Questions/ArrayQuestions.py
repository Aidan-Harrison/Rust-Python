# ===== Reverse String =====
def Reverse(str, start, end):
    while start < end:
        temp = str[start]
        str[start] = str[end]
        str[end] = temp
        start += 1
        end -= 1
    return str

def ReverseString(str):
    print(Reverse(str, 0, len(str)-1))

def Palindrome(str):
    if len(str) == 0:
        return False
    elif len(str) == 1:
        return True
    else:
        tempStr = str
        revStr = Reverse(str, 0, len(str)-1)
        print(tempStr, '\n')
        print(revStr, '\n')
        if str == tempStr:
            return True
        return False        

# Using a dictionary (Map) we can qucikly find any character which has multiple instances
def MatchingCharacters(str):
    map = {}
    for i, char in enumerate(str):
        if char in map:
            continue
        map[char] = i

def MatchingCharStrings(str1, str2): # Fix!
    if len(str1) == 0 or len(str2) == 0:
        return ' '
    else:
        characters = []
        for i in range(len(str1)):
            if str1[i] in str2:
                characters.append(str1[i])
        return characters

# Only returns a single instance of a character | Fix!
def MatchingCharStringsUnique(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return ' '
    else:
        characters = []
        for i in range(len(str1)):
            pass
        return characters

def DigitsInString(str): # Assumes string isn't empty
    digits = []
    for i in range(len(str)):
        if str[i].isdigit():
            digits.append(str[i])
    return digits

def DigitsInStringOther(str):
    digits = [0,1,2,3,4,5,6,7,8,9]
    digitsInString = []
    for i in range(len(str)):
        if str[i] in digits:
            digitsInString.append(str[i])
    return digitsInString

def RemoveDuplicates(arr):
    if len(arr) == 0:
        return None
    else:
        pass

# Given a target, find two values whose sum is equal to the target, assuming there is ALWAYS a solution
def ReachTargetNaive(arr, target):
    values = []
    for i in arr:
        for j in arr:
            if i + j == target:
                values.append(i)
                values.append(j)
            if len(values) == 2:
                return values
            
# By sorting and creating two pointers we can reduce our answer down
def ReachTargetBetter(arr, target):
    arr.sort()
    left = 0
    right = len(arr)-1
    for i in arr:
        if arr[left] + arr[right] == target:
            return arr[left], arr[right]
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1

# Use map
def ReachTargetBest(arr, target):
    pass

def ThreeNumberSum(arr, target):
    left = 0
    right = len(arr)
    for i in range(len(arr)):
        if arr[i] + arr[left] + arr[right] == target:
            return arr[i],arr[left],arr[right]
        elif arr[i] + arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1

def SecondLargestElement(arr): # Check! | Seems correct
    l = arr[0] # Largest
    s = arr[1] # Second largest
    for i in range(2, len(arr)):
        if arr[i] > l:
            s = l
            l = arr[i]
    return l, s

# Assuming you are given the numbers 1 - 100, find the missing number (Only one missing)
def FindMissing(arr):
    # Find the difference greater then one, this must be where the missing number is
    diff = 0
    for i in range(len(arr)-1):
        fVal = arr[i]
        sVal = arr[i+1]
        if fVal > sVal:
            diff = fVal - sVal
            if diff > 1:
                return fVal-1
        else:
            diff = sVal - fVal
            if diff > 1:
                return sVal-1

def FindAllDuplicates(arr): # Use map!
    duplicates = []
    for i in arr:
        pass

def RemoveDuplicates(arr):
    # Find duplicate
    # Remove from array
    #   - Do so effectively
    #   - Want to shift all elements to fill gaps
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            del arr[i]

testString = ['H','e','l','l','o']
testNumber = [1,2,3,4,5,6,7,8,9]
testNumber2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20]

print("Reverse String:\n")
ReverseString(testString)
#print("Palindrome String:\n")
#print(Palindrome(testString))
MatchingCharacters(testString)
print(MatchingCharStrings("Hello World", "Hello World"))
print("Digits in String\n")
print(DigitsInString("Hello World 123"))
print("RemoveDuplicates\n")
print(RemoveDuplicates(testString))

print(SecondLargestElement(testNumber))
print(FindMissing(testNumber2))