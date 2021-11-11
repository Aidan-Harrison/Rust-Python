# Add file handling!

import time

class Macro:
    name = 'Default Macro'
    def __init__(self) -> None:
        self.macro = [0]
    
    def Parse(self, data):
        pass

    def Add(self, data):
        self.macro.append(data)

    def Run(self):
        for i in self.macro:
            time.sleep(1)
            self.Parse(i) # Check!

class KeyboardHandler:
    top = -1
    SIZE = 20
    def __init__(self) -> None:
        self.inputStack = ['0'] * self.SIZE
    
    def IsFull(self):
        if self.top == self.SIZE:
            return True
        return False

    def IsEmpty(self):
        if self.top == -1:
            return True
        return False
    
    def Push(self, data):
        if self.IsFull():
            print("Input stack is full!")
            return
        self.top+=1
        self.inputStack[self.top] = data
    
    def Pop(self):
        if self.IsEmpty():
            print("Input stack is empty!")
            return
        key = self.inputStack[self.top]
        self.inputStack[self.top] = 0
        self.top-=1
        return key
    
    def Peek(self):
        return self.inputStack[self.top]

    def Print(self):
        for i in self.inputStack:
            print(i)

macros : Macro = []
kH = KeyboardHandler()

def Interface():
    print("===Macro Creator===")
    print("1) Add Macro  2) Run Macro  3) Delete Macro  4) Run from file")
    choice = input()
    if choice == '1':
        isWriting = True
        newMac = Macro()
        print("Enter keys of Macro, (Enter '¬' to stop)")
        while(isWriting):
            choice = input()
            if choice == '¬':
                isWriting = False
            kH.Push(choice)
        for i in range(kH.SIZE):
            newMac.Add(kH.Pop())
        macros.append(newMac)
    elif choice == '2':
        if len(macros) == 0:
            print("You have not added any macros!")
            Interface()
        print("Pick a macro to run:")
        for m in macros:
            print(m.name)
        choice = input()
        macros[choice].Run()
    elif choice == '3':
        if len(macros) == 0:
            print("You have no macros to delete!")
            Interface()
        print("Choose a Macro to delete:")
        for i in range(len(macros)):
            print(i, ') ', macros[i].name)
    elif choice == 4:
        pass

def main():
    Interface()

    return 0

if __name__ == "__main__":
    main()