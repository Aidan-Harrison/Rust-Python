# ============= Singly Linked List=============
class Node: # Re-DO this to use '__int__' and 'self'
    data = 0
    nextNode = Node

def PrintList(n):
    while(n != NULL):
        print(n.data)
        n = n.nextNode

def AddNode(prev, data, next):
    newNode = Node
    newNode.data = data
    prev.nextNode = data
    data.nextNode = next

def DelNode(prev, delNode):
    prev.nextNode = delNode.nextNode

head = Node()
one = Node()
two = Node()
tail = Node()

head.data = 5
one.data = 17
two.data = 2
tail.data = 9

head.nextNode = one
one.nextNode = two
two.nextNode = tail
tail.nextNode = NULL

PrintList(head)

# ============= Doubly Linked List=============
class dNode:
    data = 0
    nextNode = dNode
    prevNode = dNode

def PrintList(n):
    while(n != NULL):
        print(n.data)
        n = n.nextNode

def AddNode(prev, data, next): # Only need to provide one node?
    newNode = dNode
    newNode.data = data
    newNode.prevNode = prev
    newNode.nextNode = next

def DelNode(n):
    n.prevNode.nextNode = n.nextNode

# =============Stack=============
class stack:
    items[10] # Change
    top = -1

def IsFull(s):
    if s.top == 10:
        return True
    return False

def IsEmpty(s):
    if s.top == -1:
        return True
    return False

def Push(s, item):
    if IsFull(s):
        print("Stack is full, cannot push!")
        return
    else:
        s.top+=1;
        s.items[s.top] = item

def Pop(s):
    if IsEmpty(s):
        print("Stack is empty, cannot push!")
        return
    else:
        s.items[s.top] = 0
        s.top-=1;
        pass

# =============Queue=============
class queue:
    MAXSIZE : int = 10
    items[MAXSIZE]
    front : int = -1
    rear : int = 0

    def IsFull():
        return len(self.items) == MAXSIZE

    def IsEmpty():
        if front > rear:
            return True

    def Enqueue(data):
        if IsFull():
            print("Full!")
        else:
            self.rear += 1
            self.items[self.rear] = data

    def Dequeue():
        if IsEmpty():
            print("Empty!")
        else:
            self.items[self.front] = 0
            self.front -= 1

    def Front():
        return items[front]

    def Rear():
        return items[rear]

    def Print():
        for i in range(rear):
            print(items[i], ", ")

class CQueue:
    MAXSIZE : int = 10
    items[MAXSIZE]
    front : int = -1
    rear : int = -1

    def IsFull(q, rear):
        if rear + 1 % MAXSIZE == front:
            return True
        else:
            return False

    def IsEmpty():
        pass

# =============Graph=============
class graph:
    class gNode:
        data = 0

def DepthFirstSearch():
    pass

def BreadthFirstSearch():
    pass

# =============Binary Tree=============