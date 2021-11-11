# Dungeons and Dragons
import random

class Player: # Player's character
    # General
    name = ""
    backstory = ""
    # Stats
    strength = 1
    magic = 1
    agility = 1
    persuasion = 1
    luck = 1
    stats = [strength, magic, agility, persuasion, luck]



def CreateCharacter(p):
    p.name = input()
    print("Roll your stats: ")
    for i in range(5):
        p.stats[i] = random.randrange(1, 15)

def SetStoryParameters():
    print("Set the parameters which the story will generate off:")