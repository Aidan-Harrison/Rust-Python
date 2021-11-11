# State Machine

# === RC CAR ===
engineOn = False
isReverse = False
wheelRotation : float = 0.0
curPower : float = 0.0 # (UNSIGNED)
curSpeed : float = 0.0 # (UNSIGNED)

class KeyboardParser:
    top = -1
    SIZE = 20
    def __init__(self) -> None:
        self.inputStack = []

    def IsFull(self):
        if self.top == self.SIZE:
            return True
        return False

    def IsEmpty(self):
        if self.top == -1:
            return True
        return False

    def Push(self, key):
        if self.IsFull():
            print("Keyboard input is full!")
            return
        self.inputStack.append(key)
        self.top += 1

    def Pop(self):
        if self.IsEmpty():
            print("Keyboard input is full!")
            return
        curKey = self.inputStack[self.top]
        self.inputStack[self.top] = 0 
        self.top -= 1
        return curKey

    def Parse(self):
        curKey = self.Pop()
        if curKey == 119: # W
            global curPower
            curPower += 0.5
        elif curKey == 115: # S
            global curPower
            curPower -= 0.5
            if curPower <= 0.0: # Use clamp() instead
                curPower = 0.0
        elif curKey == 115: # A
            pass
        elif curKey == 115: # D
            pass

    def Peek(self):
        print(self.inputStack[self.top])

kP = KeyboardParser()

def CarState():
    print("===CAR===")
    print("Engine State: ", engineOn)
    print("Wheel Rotation: ", wheelRotation)
    print("Current Power: ", curPower)
    print("Speed: ", curSpeed)   

def Machine():
    while 1:
        CarState()
        curInput = 0
        curInput = input()
        kP.Push(ord(curInput))
        kP.Parse()

def main():
    Machine()

if __name__ == "__main__":
    main()