# Runescape level system

from os import remove, system, name

# Create skills
# Set actions
# Add and store level ups
# Allow for multiple characters

class Item:
    def __init__(self, name = 'Default Name') -> None:
        self.itemName = name
        self.index : int = 0

class Character:
    def __init__(self, combatLvl = 3) -> None:
        self.combatLevel = combatLvl
        self.bank = [Item] * 100
    
    skills = {'Attack' : 1, # Move to constructor??
            'Strength' : 1,
            'Defence': 1,
            'Prayer': 1,
            'Ranged': 1,
            'Magic': 1}

    def PrintSkills(self):
        print('Combat Level:', self.combatLevel)
        for name, level in self.skills.items():
            print(name + ':', level, '/ 99')

    def PickSkillToTrain(self):
        print('Make a choice: ', end='')
        choice = input()
        Action(choice)

    def PrintBank(self):

        for i in range(len(self.bank)):
            print(i.itemName, end='|')
            if i % 10 == 0:
                print('\n')

def Bank(char):
    char.PrintBank()

def Action(type):
    print('Press B to access bank')
    skillAction = ''
    if(type == 1):
        skillAction = 'Attacked'
    elif(type == 2):
        skillAction = 'Trained'
    elif(type == 3):
        skillAction = 'Blocked'
    elif(type == 4):
        skillAction = 'Buried Bones'
    elif(type == 5):
        skillAction = 'Hit'
    elif(type == 6):
        skillAction = 'Cast'
    print("You " + skillAction + " successfully")

c = Character(3)

def Interface():
    print('=RUNESCAPE=')
    while 1:
        c.PrintSkills()
        c.PickSkillToTrain()
    print('Pick an option')
    choice = input()
    if choice == 'b':
        Bank()

Interface()