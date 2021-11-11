import math
# =============================== SEARCHING ALGORITHMS ===============================
def LinearSearch(array, target):
    totalFound : int = 0
    for x in array:
        if array[x] == target:
            totalFound += 1
    if totalFound == 0:
        return "None found!\n"
    return totalFound

data = [1,2,3,4,5,6,7,8,9,10]
#print(LinearSearch(data, 7));

def BinarySearch(array, start, end, target):
    array.sort()
    left = start
    right = end
    while(left <= right):
        mid = left + (right - left) // 2
        if(array[mid] == target): return array[mid]
        elif(array[mid] < target): left = mid + 1
        else: right = mid - 1
    return "Not found!\n"

# Assuming already sorted
def BinarySearchRecursive(arr, left, right, target):
    while(left <= right):
        mid = left + (right - left) // 2
        if(arr[mid] == target): return arr[mid]
        elif(arr[mid] < target):
            left = mid+1 
            BinarySearchRecursive(arr, left, right, target)
        else:
            right = mid-1 
            BinarySearchRecursive(arr, left, right, target)
    return "Not Found!\n"

data = [2,7,2,6,12,41,52,1,25,125,115,51,9,1,81,5,]

print(BinarySearch(data, 0, 16, 115))
print(BinarySearchRecursive(data, 0, 16, 115))
