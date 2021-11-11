# Tic-Tac-Toe

grid = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
gameOver = False

def PrintGame():
    for i in range(3):
        for j in range(3):
            print(grid[i][j], ' | ')
        print('\n')

def TicTacToe():
    while(gameOver == False):
        PrintGame()
        inputX = input()
        inputY = input()

        if grid[0][0] == 'X' and grid[0][1] == 'X' and grid[0][2] == 'X': print('X Wins!')
        if grid[0][0] == 'X' and grid[1][0] == 'X' and grid[2][0] == 'X': print('X Wins!')
        if grid[1][0] == 'X' and grid[1][1] == 'X' and grid[1][2] == 'X': print('X Wins!')
        if grid[0][1] == 'X' and grid[1][1] == 'X' and grid[2][1] == 'X': print('X Wins!')
        if grid[2][0] == 'X' and grid[2][1] == 'X' and grid[2][2] == 'X': print('X Wins!')
        if grid[0][0] == 'X' and grid[1][1] == 'X' and grid[2][2] == 'X': print('X Wins!')
        if grid[0][2] == 'X' and grid[1][1] == 'X' and grid[2][0] == 'X': print('X Wins!')

        if grid[0][0] == 'O' and grid[0][1] == 'O' and grid[0][2] == 'O': print('O Wins!')
        if grid[0][0] == 'O' and grid[1][0] == 'O' and grid[2][0] == 'O': print('O Wins!')
        if grid[1][0] == 'O' and grid[1][1] == 'O' and grid[1][2] == 'O': print('O Wins!')
        if grid[0][1] == 'O' and grid[1][1] == 'O' and grid[2][1] == 'O': print('O Wins!')
        if grid[2][0] == 'O' and grid[2][1] == 'O' and grid[2][2] == 'O': print('O Wins!')
        if grid[0][0] == 'O' and grid[1][1] == 'O' and grid[2][2] == 'O': print('O Wins!')
        if grid[0][2] == 'O' and grid[1][1] == 'O' and grid[2][0] == 'O': print('O Wins!')