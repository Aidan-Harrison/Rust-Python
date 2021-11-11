# Runescape level system

# Create skills
# Set actions
# Add and store level ups
# Allow for multiple characters

class Character:
    def __init__(self, combatLvl = 3) -> None:
        self.combatLevel = combatLvl
    skills = {'Attack' : 1,
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

def Action(type):
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
    print("=RUNESCAPE=")
    while 1:
        c.PrintSkills()
        c.PickSkillToTrain()

Interface()