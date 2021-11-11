# Adjacency List (Array of linked-lists)
#   Index of array represents the vertex
#   each element in it's linked lists represents it's children

# Dictionary Based
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D']),
         'C': set(['A']),
         'D': set(['B'])}

# or a unsafe yet correct variant
graphArray = {'A': ['B', 'C'],
              'B': ['A', 'D'],
              'C': ['A'],
              'D': ['B']}

# Node Based
class listNode:
    def __init__(self, data) -> None:
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, numOfVerts) -> None:
        self.vertCount = numOfVerts
        self.graph = [None] * self.vertCount # Create an empty array of size vert count

    def AddEdge(self, start, dest):
        node = listNode(dest)
        node.next = self.graph[start]
        self.graph[start] = node

        node = listNode(start)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def PrintGraph(self):
        for i in range(self.vertCount):
            print("Vertex " + str(i) + ":", end='')
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end='')
                temp = temp.next
            print('\n')

# Adjacency List
graph = Graph(5)
graph.AddEdge(0, 1)
graph.AddEdge(0, 2)
graph.AddEdge(0, 3)
graph.AddEdge(1, 2)

# Adjacency Matrix (2D array of 1's and 0's)
class matrixNode:
    def __init__(self, data) -> None:
        self.vertex = data
        self.next = None

graph.PrintGraph()


# River Sizes
# This question is just a undirected graph which needs traversing
# Given an adjacency matrix, find the sizes of all the rivers
# A river is dictated by connected 1's either horizontal or vertical. NOT diagonal
# Therefore shapes like 'L' are valid

# Solution:
# Depth first search when encountering a 1, search for any adjacent 1, again, excluding diagonal.
# Mark any node visited in a global storage container else we will loop over the same 1's multiple times
# Count size of river using a simple counter variable, return it's size and push to array
# Repeat until entire matrix (Graph) has been traversed

adjMat = [[0] * 6 for i in range(6)] 

def AddEdge(src, des):
    adjMat[src][des] = 1
    adjMat[des][src] = 1

def GetUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    if i > 0 and not visited[i-1][j]: # Above
        unvisitedNeighbors.append([i-1,j])
    if i < len(matrix)-1 and not visited[i+1][j]: # Below
        unvisitedNeighbors.append([i+1,j])
    if j > 0 and not visited[i][j-1]: # Left
        unvisitedNeighbors.append([i,j-1])
    if j < len(matrix[0]) and not visited[i][j+1]: # Right
        unvisitedNeighbors.append([i,j+1])
    return unvisitedNeighbors

def Traverse(i, j, matrix, visited, sizes):
    curRiverSize = 0
    # Stack
    nodesToExplore = [[i,j]] # Have to first explore the location passed in
    while len(nodesToExplore): # While not zero
        curNode = nodesToExplore.pop()
        i = curNode[0]
        j = curNode[1]
        if visited[i][j]: # Nothing to do
            continue
        visited[i][j] = True
        if matrix[i][j] == 0: # Piece of land, skip it
            continue
        curRiverSize += 1
        unvisitedNeighbors = GetUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
    if curRiverSize > 0:
        sizes.append(curRiverSize)

def RiverSizes(matrix):
    rSizes = []
    isVisited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])): # Matrix is not always even
                if not isVisited[i][j]:
                    Traverse(i, j, matrix, isVisited, rSizes)
    return rSizes
    

AddEdge(0,1)
AddEdge(0,2)
AddEdge(2,4)
AddEdge(3,2)

print("River Sizes:")
print(RiverSizes(adjMat))