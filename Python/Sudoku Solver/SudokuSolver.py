# Sudoku Solver
board = [
    [5,6,0, 0,0,0, 0,7,8],
    [1,3,7, 2,0,0, 0,0,0],
    [0,0,8, 5,0,6, 0,0,3],

    [0,1,6, 0,8,0, 5,0,4],
    [0,0,0, 9,0,4, 0,0,0],
    [7,0,9, 0,5,0, 8,3,0],

    [6,0,0, 3,0,5, 2,0,0],
    [0,0,0, 0,0,7, 3,4,1],
    [3,8,0, 0,0,0, 0,5,7]
]

def Solve():
    find = FindEmpty()
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10): # Loop from 1-9
        if IsValid(i, (row, col)):
            board[row][col] = i

            if Solve():
                return True
            
            board[row][col] = 0
    return False


def IsValid(num, pos):
    # Row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i: # Check if number exists in column, excluding itself
            return False
    # Column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # Region
    bo_X = pos[1] // 3
    bo_Y = pos[0] // 3

    for i in range(bo_Y * 3, bo_Y * 3 + 3):
        for j in range(bo_X * 3, bo_X * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def PrintBoard():
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end='')
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end='')

def FindEmpty():
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # Return 'Tuple' i, j | Position X and Y
    return False

PrintBoard()
Solve()
print("===========================")
PrintBoard()