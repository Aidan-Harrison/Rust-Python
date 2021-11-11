class Node:
    def __init__(self, d = '') -> None:
        self.data = d
        self.children = [None]

class Trie:
    def __init__(self, r : Node) -> None:
        self.root = r

    def Insert(self, node, data): # Won't work!
        for i in node.children:
            if i == None:
                newNode = Node(data)
            else:
                self.Insert(i, data)

    def Search(self): # Find prefixes
        pass

    def Delete(self):
        pass

    def Print(self):
        for i in self.root.children:
            if i != None:
                print(i.data, end='-')

# Nodes
root = Node('c')
n2 = Node('a')
n3 = Node('t')

trie = Trie(root)