class Node:
    def __init__(self, d) -> None:
        self.data = d
        self.lChild = None
        self.rChild = None

class Heap:
    def __init__(self) -> None:
        pass

    def AddNode(self, k, node):
        if k < node.data:
            if node.lChild == None:
                newNode = Node(k)
            else:
                self.AddNode(node.lChild)
        elif k > node.data:
            if node.rChild == None:
                newNode = Node(k)
            else:
                self.AddNode(node.rChild)

    def Search(self, k, node):
        if node != None:
            if k == node.data:
                return node
            elif k < node.data:
                self.Search(k, node.lChild)
            else:
                self.Search(k, node.rChild)

    def Print(self):
        pass

def Heapify(array):
    #  
    pass

testArray = [1,2,3,4,5,6,7,8,9,10]