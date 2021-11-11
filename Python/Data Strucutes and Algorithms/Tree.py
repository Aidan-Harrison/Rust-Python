# ===== Binary Tree Version 1 =====
class node:
    def __init__(self, k) -> None:
        self.key = k
    lChild = None
    rChild = None

    def PreOrder(self):
        print(self.key, end=' ')
        if self.lChild:
            self.lChild.PreOrder()
        if self.rChild:
            self.rChild.PreOrder()

    def InOrder(self):
        if self.lChild:
            self.lChild.InOrder()
        print(self.key, end=' ')
        if self.rChild:
            self.rChild.InOrder()

    def PostOrder(self):
        if self.lChild:
            self.lChild.PostOrder()
        if self.rChild:
            self.rChild.PostOrder()
        print(self.key, end=' ')

# ===== Binary Search Tree =====
class node2:
    def __init__(self, k) -> None:
        self.key = k
    lChild = None
    rChild = None

class BinaryTree:
    def __init__(self) -> None:
        pass

    def AddNode(self, k, node):
        if k < node.key:
            if node.lChild == None:
                node.lChild = node2(k)
            else:
                self.AddNode(self, k, node.lChild)
        elif k > node.key:
            if node.rChild == None:
                node.rChild = node2(k)
            else:
                self.AddNode(self, k, node.rChild)

    def Search(self, k, node):
        if node != None:
            if k == node.key:
                return node
            if k < node.key:
                return self.Search(self, k, node.lChild) # Check return!
            else:
                return self.Search(self, k, node.rChild)

    def Print(self, node): # Handle children, do 3 traversals instead
        while node != None:
            print(node.key)
            if node.lChild != None:
                print(node.lChild.key)
            if node.rChild != None:
                print(node.rChild.key)

    def PrintPreOrder(self, node):
        print(node.key, end=' ')
        if node.lChild:
            self.PrintPreOrder(self, node.lChild)
        if node.rChild:
            self.PrintPreOrder(self, node.rChild)

    def PrintInOrder(self, node):
        if node.lChild:
            self.PrintInOrder(self, node.lChild)
        print(node.key, end=' ')
        if node.rChild:
            self.PrintInOrder(self, node.rChild)

    def PrintPostOrder(self, node):
        if node.lChild:
            self.PrintInOrder(self, node.lChild)
        if node.rChild:
            self.PrintInOrder(self, node.rChild)
        print(node.key, end=' ')

# Binary Tree Version 1
root = node(4)
root.lChild = node(7)
root.rChild = node(3)

root.rChild.rChild = node(12)

print("Pre-Order:")
root.PreOrder()
print()
root.InOrder()
print()
root.PostOrder()
print()

# Binary Search Tree
bst = BinaryTree

n1 = node2(5)
n2 = node2(7)
n3 = node2(1)
n4 = node2(3)
n5 = node2(4)
n6 = node2(8)

bst.AddNode(bst, 5, n1)
bst.AddNode(bst, 7, n1)
bst.AddNode(bst, 1, n1)
bst.AddNode(bst, 3, n1)
bst.AddNode(bst, 4, n1)
bst.AddNode(bst, 8, n1)

bst.PrintPreOrder(bst, n1)
print()
bst.PrintInOrder(bst, n1)
print()
bst.PrintPostOrder(bst, n1)

