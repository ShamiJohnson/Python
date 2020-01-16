""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
from random import *

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

def main():
  clearDeck()

  for i in range(5):
    assignCard(PLAYER)
    assignCard(COMP)

  showDeck()                        
  showHand(PLAYER)
  showHand(COMP)


def clearDeck():
    for card in cardLoc:
        cardLoc[card]=0         #setting cards to zero

def assignCard(PLAYER):
    RANDOM=randrange(0,52)      #choose random card via random number
    if cardLoc[RANDOM]==0:      #checking to see if the location is 0 or not 
        cardLoc[RANDOM]=PLAYER  #create a string
    else:                       #if the condition does not meet then, also creates a loop
        assignCard(PLAYER)      #creating a loop
        
def assignCard(COMP):
    RANDOM=randrange(0,52)      #choosing a random card through random number
    if cardLoc[RANDOM]==0:      #checking to see if the location is 0 or not
        cardLoc[RANDOM]=COMP    #creating a string for computer
    else:                       #if the condition does not meet then, also creates a loop
        assignCard(COMP)        #creating loop
            

def showDeck():
    for card in range(52):      #choosing the cards below 0
        RANK=card%13            #find the rank
        RANK=rankName[RANK]     #creating string to find the rank of cards
        SUIT=card//13           #formula to find suit
        SUIT=suitName[SUIT]
        
        print("{}    {} of {}      {}".format(card,RANK,SUIT,playerName[cardLoc[card]]))                   

def showHand(PLAYER):
    print("\nPlayer's cards")   #printing players cards 
    for card in range(0,52):    #loop
        if cardLoc[card]==PLAYER: #if statement
             RANK=card%13        #rank formula
             RANK=rankName[RANK] #finding rank
             SUIT=card//13       #suit formula
             SUIT=suitName[SUIT] #finding suit
             print("{} of {}".format(RANK,SUIT))

             
def showHand(COMP):
    print("\ncomp's cards")     #printing computers cards
    for card in range(0,52):    #loop
        if cardLoc[card]==COMP: #write 'if' statement to run the program if true
             RANK=card%13       #rank formula
             RANK=rankName[RANK] #finding rank
             SUIT=card//13      #suit formula
             SUIT=suitName[SUIT] #finding suit
             print("{} of {}".format(RANK,SUIT))  

main() 


    
       
