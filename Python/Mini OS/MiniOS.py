# Mini OS

# Add encryption and decrpytion
# Make file system universal

import os

class User:
    def __init__(self, username, password) -> None:
        self.username = "Default"
        self.password = "Default"

users : User = []
userInput = ''

def ReadFile(filePath):
    if not os.path.exists(filePath):
        print("Invalid or corrupt file!")
        return
    file = open(filePath, 'r')
    print(file.read())
    file.close()

def WriteToFile(filePath, data): # Change to be universal!
    file = open(filePath, 'a')
    file.write(data.username)
    file.write(data.password)
    file.close()

def DeleteFile(filePath):
    if os.path.exists(filePath):
        os.remove(filePath)

def CreateUser():
    username = '', password = ''
    print('Enter a username: ')
    userInput = input()
    username = userInput
    print('Enter a password: (Should contain numbers and symbols)')
    userInput = input()
    for i in userInput:
        pass
    password = userInput
    newUser = User(username, password)
    users.append(newUser) # Write data to file
    WriteToFile("Users.txt", newUser)

def Interface():
    print('===MINI OS===')

def Login():
    if(len(users) == 0):
        print('There are no existing users, creating one...')
        CreateUser()
        main()
    userInput = input()

def main() -> int:
    print('Load a file: ', end='')
    filePath = input()
    ReadFile(filePath)

    return 0

if __name__ == "__main__":
    main()