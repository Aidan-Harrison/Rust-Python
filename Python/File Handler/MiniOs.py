# Mini OS

import os

class User:
    def __init__(self) -> None:
        self.username = ''
        self.password = ''

users : User = [None]

def ReadFile(filePath):
    if not os.path.exists(filePath):
        print("Invalid or corrupt file!")
        return
    file = open(filePath, 'r')
    print(file.read())
    file.close()

def WriteToFile(filePath):
    file = open(filePath, 'a')
    newContent = input()
    file.write(newContent)
    file.close()

def DeleteFile(filePath):
    if os.path.exists(filePath):
        os.remove(filePath)

def Login():
    print("LOGIN")
    print("Enter your username: ", end='')
    userInput = input()
    for user in users:
        if userInput == user.username:
            break
    print("Enter your password: ", end='')
    for user in users:
        if userInput == user.password:
            break
    userInput = input()


def main() -> int:
    print("Load a file: ", end='')
    filePath = input()
    ReadFile(filePath)

    return 0

if __name__ == "__main__":
    main()