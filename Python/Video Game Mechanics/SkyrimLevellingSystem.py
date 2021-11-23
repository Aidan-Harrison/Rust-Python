# Skyrim levelling system

# Skill Name | Level
GlobalSkills = {'Destruction': 1,
'Conjuration': 1,
'Alteration': 1,
'Restoration': 1,
}

class SkillNode:
    def __init__(self) -> None:
        self.name = 'Default Node'
        self.description = ''

class Skill:
    def __init__(self, nodeCount : int = 10) -> None:
        self.name = 'Default Skill'
        self.curLevel = 1
        self.nodes[SkillNode] * nodeCount

    def Tree(self):
        for i in self.nodes:
            print(i.name)

    def GetName(self):
        return self.name

class Player:
    level = 0
    def __init__(self) -> None:
        self.skills = [Skill] * 16
        self.Setup()

    def Setup(self):
        for name, level in GlobalSkills:
            print(name, '|', level)

    def Print(self):
        for i in self.skills:
            i.GetName()

p = Player()

def Interface():
    p.Print()

def main() -> int:
    Interface()

    return 0

if __name__ == "__main__":
    main()