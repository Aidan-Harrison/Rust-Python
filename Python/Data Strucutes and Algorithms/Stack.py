class Stack:
    def __init__(self, size) -> None:
        self.top = -1
        self.stack = [0] * size

    def IsFull(self):
        if self.top == len(self.stack):
            return True
        return False

    def IsEmpty(self):
        if self.top == -1:
            return True
        return False

    def Push(self, item):
        if self.IsFull():
            print("Stack is full!")
        else:
            self.top += 1
            self.stack[self.top] = item

    def Pop(self):
        if self.IsEmpty():
            print("Stack is empty!") 
        else:
            element = self.stack[self.top]
            self.top -= 1
            return self.stack[self.top]

    def Size(self):
        return self.top

    def Print(self):
        for i in range(self.top+1):
            print(self.stack[i], end=',') 

s = Stack(6)

s.Push(5)
s.Push(6)
s.Push(7)
s.Push(8)
s.Push(9)
s.Push(10)

s.Print()

print()
s.Pop()

s.Print()