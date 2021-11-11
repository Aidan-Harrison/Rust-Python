# Adjacency List
class lGraph:
    pass


# Node Based
class Node:
    children = []
    def __init__(self, d = 0) -> None:
        self.data = d
        self.children = []
        self.isVisited = False
    
    def GetNeighbours(self): # Fix!
        for i in range(len(self.children)):
            print(self.children[i].data)

class Stack:
    top = -1
    stack = []

    def __init__(self, size) -> None:
        self.stack = [None] * size

    def IsFull(self):
        if self.top == size:
            return True
        return False

    def IsEmpty(self):
        if self.top == -1:
            return True
        return False

    def Push(self, data : Node):
        if self.IsFull():
            print("Stack is full!")
        else:
            self.top+=1
            self.stack[self.top] = data

    def Pop(self):
        if self.IsEmpty():
            print("Stack is empty!")
        else:
            element = self.stack[self.top]
            self.top-=1
            return element

    def Size(self):
        return self.top

class Graph:
    newStack = Stack(10)
    def __init__(self) -> None:
        pass

    def AddNode(self, node : Node, data):
        newNode = Node(data)
        node.children.append(data)

    def DFSIter(self, node : Node):
        self.newStack.Push(node)
        while not self.newStack.IsEmpty():
            self.newStack.Pop() # Don't always want to pop. Change! Only want to pop when node is not visited
            for child in node.children:
                if not child.isVisited:
                    print(child.data)
                    child.isVisited = True
                    self.newStack.Push(child)

    def DFSRecur(self, node : Node):
        node.isVisited = True
        print(node.data,end='-')
        for child in node.children:
            if not node.isVisited:
                self.DFSRecur(child)

# Adjacency Matrix
size = 6
adjMat = [[0] * size for i in range(size)]

def AddEdge(src, des):
    if src == des:
        print("Same vertex")
    else:
        adjMat[src][des] = 1
        adjMat[des][src] = 1

def DeleteEdge(src, des):
    if adjMat[src][des] == 0:
        print("No edge to remove")
    else:
        adjMat[src][des] = 0
        adjMat[des][src] = 0

def Print():
    for i in range(len(adjMat)):
        for j in range(len(adjMat)):
            print(adjMat[i][j], end=',')
        print()

# Node Based
newGraph = Graph()
root = Node(4)
newGraph.AddNode(root, 7)
newGraph.AddNode(root, 8)
newGraph.AddNode(root, 9)
newGraph.AddNode(root, 10)

# root.GetNeighbours()

newGraph.DFSIter(root)
newGraph.DFSRecur(root)

AddEdge(0,1)
AddEdge(1,2)
AddEdge(4,3)
AddEdge(4,5)
AddEdge(3,2)

DeleteEdge(1,2)
DeleteEdge(1,0)

Print()

