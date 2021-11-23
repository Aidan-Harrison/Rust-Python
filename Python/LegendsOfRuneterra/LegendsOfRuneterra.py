# Convert card type to enum! | Import
# Convert region to enum! | Import
import random
import sys, pygame
from pygame import scrap
from pygame.constants import QUIT

# PyGame and Window setup========================================
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Legends of Runeterra')

background = pygame.Surface(window.get_size())
background = background.convert()
background.fill((0,0,0))

font = pygame.font.Font(None, 36)
title = font.render('Legends of Runeterra', 1, (255,255,255))
titlePos = title.get_rect()
titlePos.centerx = background.get_rect().centerx
background.blit(title, titlePos)

window.blit(background, (0,0))
pygame.display.flip()
#================================================================

class Card:
    type = 0
    region = 0
    def __init__(self, cost, name, power, tough) -> None:
        self.cardCost = cost
        self.cardName = name
        self.cardPower = power
        self.cardToughness = tough

# Shadow Isles Cards-
StestCard = Card(1, 'Shadow Test Card', 1, 1)
shadowIslesCards : Card = [StestCard]
# Piltover & Zaun Cards-
ZtestCard = Card(1, 'Zaun Test Card', 1, 1)
piltoverZaunCards : Card = [ZtestCard]

class Deck:
    def __init__(self, name) -> None:
        self.deckName = name
        self.cards : Card = [None] * 40

    def Draw(self):
        return self.cards[random.randrange(0, len(self.cards))]

def DeckBuilder():
    print('===DECK BUILDER===')
    genInput = input()
    newDeck = Deck(genInput)
    print('===Choose a region===')
    genInput = input()
    if genInput == '1':
        for i in shadowIslesCards:
            print(i.cardName)

def Game():
    # Base
    curTurn : int = 0
    yourNexusHealth : int = 20
    yourMana : int = 1
    enemyNexusHealth : int = 20
    enemyMana : int = 1
    # Board
    yourBoard : Card = [None] * 8
    enemyBoard : Card = [None] * 8
    # Starting hand:
    yourHand : Card = [None] * 4
    enemyHand : Card = [None] * 4
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        
        window.blit(background, (0,0))
        pygame.display.flip()

def PreGame():
    print('===PREGAME===')

def main() -> int:
    Game()

    return 0

if __name__ == '__main__':
    main()