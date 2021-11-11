# Sorting algorithms | Assumes all arrays have data

# ====== Bubble Sort ======
def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Stops checking once sorted
def BubbleSortBetter(arr):
    hasSwapped = True
    while(hasSwapped):
        hasSwapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                hasSwapped = True

def BubbleSortBest(arr):
    hasSwapped = True
    nIterations = 0
    while(hasSwapped):
        hasSwapped = False
        for i in range(len(arr) - nIterations - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                hasSwapped = True
        nIterations += 1

testArray = [6,4,69,2,62,96,99,14,7,214,111,243,1,5]

# ====== Selection Sort ======
def SelectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]: # New minimum
                min = j
        if min != i: # Can't swap something with itself
            arr[i], arr[min], arr[min], arr[i]

def InsertionSort(arr):
    for i in range(len(arr)):
        choice = i
        while choice > 0 and arr[choice-1] > arr[choice]: # Cannot be the first index as we have to check before
            arr[choice-1], arr[choice] = arr[choice], arr[choice-1]
            choice -= 1

def InsertionSortFast(arr):
    pass

# ====== Quick Sort ======
def Partition(arr, left, right):
    i = left - 1
    for j in range(left, right):
        if arr[j] < arr[right]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1 # Return pivot, which is now in the correct location

def QuickSort(arr, left, right):
    if left < right:
        pivot = Partition(arr, left, right)

        # Do sub-arrays
        QuickSort(arr, left, pivot-1)
        QuickSort(arr, pivot+1, right)

# ===== Merge Sort =====
def MergeSort(arr):
    if len(arr) > 1: # Not single element
        r = len(arr)//2
        l = arr[:r]
        m = arr[r:]

        MergeSort(l)
        MergeSort(m)

        i = j = k = 0 # Create three pointers and set them to 0

        while i < len(l) and j < len(m):
            if l[i] < m[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = m[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(m):
            arr[k] = m[j]
            j += 1
            k += 1

# ===== Heap Sort =====
heap = [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# Check!
# Left Child = 2i + 1
# Right Child = 2i + 2
# Parent = i-1/1
def Heapify(arr):
    pass

def HeapSort(heap):
    pass

# Comment out:

#BubbleSort(testArray)
#BubbleSortBetter(testArray)
#BubbleSortBest(testArray)

#SelectionSort(testArray)

#InsertionSort(testArray)

#QuickSort(testArray, 0, len(testArray)-1)

MergeSort(testArray)

print(testArray)