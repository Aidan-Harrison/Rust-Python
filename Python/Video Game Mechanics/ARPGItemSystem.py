# ARPG ITEM SYSTEM

# Modules
import random

# Global Prefixes
gPrefixes = ['Lamenting ', 'Seething ', 'Ridden ', 'Tarnished ', 'Branded ', 'Imbued ']

# Specific Prefixes
swordPrefixes = ['Sharp ', 'Blunt ', 'Prestine ', 'Flawless ', 'Nimble ']
daggerPrefixes = ['Sharp ', 'Blunt ', 'Prestine ', 'Flawless ', 'Nimble ']

# Implict Names
swordBaseNames = ['Broad Sword', 'Steel Longsword', 'Twisted Sword', 'Coiled Sword', 'Plate Sword', 'Serrated Sword', 'Rapier', 'Katana']
daggerBaseNames = ['Shank', 'Iron Dagger', 'Glass Pick', 'Sacrifical Dagger', 'Gut Knife']

# Suffixes
suffixes = [' of Lothric', ' of Repentence', ' of Eternity', ' of Divinity', ' of Hatred', ' of Heroism', ' of Light', ' of Dark', ' of Chaos', ' of Order']

class Player:
    def __init__(self) -> None:
        self.playerName = ''
        self.inventory = [[None] * 3 for i in range(3)] # Change?

class CraftingItem:
    def __init__(self) -> None:
        self.craftingItemName = ''
    
    def Use():
        pass

class AgonyOrb(CraftingItem):
    def __init__(self) -> None:
        super().__init__()

class Item:
    def __init__(self, name = '') -> None:
        self.itemName = name
        self.type = 0
    stats = {'Attack' : 0,
             'Defence': 0,
             'Speed': 0,}

    def Print(self):
        print('-----------', self.itemName, '-----------')
        for attribute, value in self.stats.items():
            print(attribute, ':', value)
        print('-----------------------------------------')

def Generate(): # Handle global prefixes | Optimise and clean-up!?
    choice = random.randint(0,1)
    suffix = random.randint(0, len(suffixes)-1)
    prefix = random.randint(0, 1) # Amount of base prefixes
    if prefix == 0:
        base = random.randint(0, len(swordBaseNames)-1)
        prefix = random.randint(0, len(swordPrefixes)-1)
        newItem = Item(swordPrefixes[prefix] + swordBaseNames[base] + suffixes[suffix])
    elif prefix == 1:
        base = random.randint(0, len(daggerBaseNames)-1)
        prefix = random.randint(0, len(daggerPrefixes)-1)
        newItem = Item(daggerPrefixes[prefix] + daggerBaseNames[base] + suffixes[suffix])
    print(newItem.itemName)

def Craft():
    print('Pick a crafting item:')
    choice = input()

def Interface():
    print('Make a choice:\n1) Generate Item\n2) Craft Item')
    choice = input()
    if choice == 1:
        Generate()
    elif choice == 2:
        Craft()

def Main():
    random.seed() # Check!
    Interface()

if __name__ == '__main__':
    Main()