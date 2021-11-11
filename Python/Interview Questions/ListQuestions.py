# List definition
class node:
    def __init__(self, data) -> None:
        self.value = data
        self.next = None

class List:
    head = node(None) # Check!

# List Functions: ================================
def PrintList(head):
    while head != None:
        print(head.value, end='-')
        head = head.next

def AddNode(head, data):
    tempNode = node(data)
    if head == None:
        head = tempNode
    else:
        traverseNode = head
        while traverseNode.next != None:
            traverseNode = traverseNode.next
        traverseNode.next = tempNode
    return head

# ================================

def ReverseList(head):
    cur = head
    following = head
    prev = None
    while cur != None:
        following = following.next
        cur.next = prev
        prev = cur
        cur = following
    return prev

def PrintMid(head):
    # Need to know size of the list so we know how far to go
    traverseNode = head
    size = 0
    while traverseNode != None:
        traverseNode = traverseNode.next
        size += 1
    traverseNode = head
    for i in range(int(size/2)): # Important we cast to int to handle odd sized lists
        traverseNode = traverseNode.next
    print(traverseNode.value)

# Given two pieces of data to swap, swap them in a linked list
def SwapNodesNaive(head, x, y):
    if x == y:
        return
    array = []
    while head != None:
        array.append(head.value)
        head = head.next
    curX = 0
    curY = 0
    for i in range(len(array)):
        if array[i] == x:
            curX = i
        elif array[i] == y:
            curY = i
    #temp = array[curX]
    #array[curX] = array[curY]
    #array[curY] = temp

    array[curX], array[curY] = array[curY], array[curX] # Python way

    # Create new list based on swapped array
    root = None
    for i in array:
        root = AddNode(root, i)
    PrintList(root)
    print('\n')
        

def SwapNodes(head, x, y):
    if x == y:
        return

    xNodePrev = None
    xNode = head
    while xNode != None and xNode.value != x: # Find x Node
        xNodePrev = xNode
        xNode = xNode.next
    
    yNodePrev = None
    yNode = head
    while yNode != None and yNode.value != y:
        yNodePrev = yNode
        yNode = yNode.next

    if xNode or yNode == None:
        return

    # Check if x is head of list
    if xNodePrev != None:
        xNodePrev.next = yNode
    else:
        head = yNode

    if yNodePrev != None:
        yNodePrev.next = xNode
    else:
        head = xNode

    #Swap
    temp = xNode.next
    xNode.next = yNode.next
    yNode.next = temp  



# List
head = node(2)
n1 = node(4)
n2 = node(6)
n3 = node(8)
tail = node(10)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = tail

PrintList(head)
print('\n')
PrintMid(head)
SwapNodesNaive(head, 4, 10)
PrintList(head)