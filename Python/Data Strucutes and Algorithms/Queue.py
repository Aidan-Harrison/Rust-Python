# Version 1 | Python Advantage
class Queue:
    def __init__(self) -> None:
        self.queue = []

    def Enqueue(self, item):
        self.queue.append(item)

    def Dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0) # Check! pop

    def Print(self):
        print(self.queue)

    def Size(self):
        return len(self.queue)

# Version 2 | Standard
class Queue2:
    def __init__(self, size) -> None:
        self.front = -1
        self.rear = -1
        self.queue = [0] * size

    def IsFull(self):
        if self.front == 0 and self.rear == len(self.queue) - 1:
            return True
        return False

    def IsEmpty(self):
        if self.front == -1:
            return True
        return False

    def Enqueue(self, item):
        if self.IsFull():
            print("Queue is full!")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = item

    def Dequeue(self):
        if self.IsEmpty():
            print("Queue is empty!")
        else:
            element = self.queue[self.front]
            if self.front >= self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front += 1
            return element

    def Print(self):
        print('[',end='')
        for i in range(self.front, self.rear):
            print(self.queue[i],end=',')
        print(']',end='')

q = Queue()

q.Enqueue(5)
q.Enqueue(6)
q.Enqueue(7)
q.Enqueue(8)
q.Enqueue(9)
q.Enqueue(10)

print(q.Size())

q.Print()

# ======
print("Standard Version:")
q2 = Queue2(6)

q2.Enqueue(5)
q2.Enqueue(6)
q2.Enqueue(7)
q2.Enqueue(8)
q2.Enqueue(9)
q2.Enqueue(10)

q2.Print()
print()
print(q2.Dequeue())
print(q2.Dequeue())
q2.Print()