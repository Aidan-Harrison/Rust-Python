import math

# Babbage Python
def Add(a, b, c = 0, d = 0):  return  a + b
def Sub(a, b, c = 0, d = 0):  return a - b
def Mult(a, b, c = 0, d = 0): return a * b
def Div(a, b, c = 0, d = 0):  return a / b

def printLoop(object, amount : int):
    for x in range(amount):
        print(object[x])

def printLine(amount : int = 1):
    for x in range(amount):
        print('-', end = '')

def floor(value : float):
    return int(value)

def max(a, b): # Based on first value
    if a > b: return a
    else: return b

def maxArray(array, size : int):
    array.sort() # Check!
    largest = 0
    for x in range(size):
        if array[x] > array[x + 1]:
            largest = array[x]
    return largest

class Square:
    m_A : float = 0 
    m_B : float = 0
    m_C : float = 0 
    m_D : float = 0
    sides = [m_A,m_B,m_C,m_D]
    def SetSquare(self, a : float, b : float, c : float, d : float):
        Square.sides[0] = a # Remove need for 'Sqaure.'
        Square.sides[1] = b
        Square.sides[2] = c
        Square.sides[3] = d
    def Perimeter():
        return Square.sides[0] + Square.sides[1] + Square.sides[2] + Square.sides[3]

values = [4,7,12,3,8,1]
print(maxArray(values, 5))