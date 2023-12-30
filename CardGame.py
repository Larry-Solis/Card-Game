from random import randint
import time
import os
import cowsay

cardDeck=["A",2,3,4,5,6,7,8,9,"J","Q","K","A",2,3,4,5,6,7,8,9,"J","Q","K","A",2,3,4,5,6,7,8,9,"J","Q","K","A",2,3,4,5,6,7,8,9,"J","Q","K"]
computerHand=[]
PlayerHand=[]

#Player card generators
def playerCardGenerator(cards,value):
    for x in range(cards):
        print("    *¯¯¯¯¯¯¯¯¯¯¯¯¯*       ",end="")
    print("")
    for s in range(4):
        for x in range(cards):
            print("    |             |       ",end="")
        print("")
        #Shows the symbols of all the cards
        if(s==1):
            for x in range((len(PlayerHand))):
                print(f"    |      {PlayerHand[x-1]}      |       ",end="")
            print("\n",end="")
    for x in range(cards):
        print("    *_____________*       ",end="")
    print(f"\n\nPlayer Hand: {value}\n")  

#computer card generators
def computerCardGenerator(cards,value,state):
    #card drawer as game is on
    if(state=="continue"):
        print(f"Computer Card Value: ?\n")
        for x in range(cards):
            print("    *¯¯¯¯¯¯¯¯¯¯¯¯¯*       ",end="")
        print("")
        for s in range(4):
            for x in range(cards):
                print("    |             |       ",end="")
            print("")
            
            #Reveals only one card of the two
            if(s==1):
                print(f"    |      {computerHand[cards-1]}      |       ",end="")
                print("    |      ?      |       ",end="")
                print("\n",end="")
                continue
        for x in range(cards):
            print("    *_____________*       ",end="")
        print("\n\n")
        
    #Card drawer for when game has ended
    if(state=="end"):
        print(f"Computer Shown Card Value:{value}\n")
        for x in range(cards):
            print("    *¯¯¯¯¯¯¯¯¯¯¯¯¯*       ",end="")
        print("")
        for s in range(4):
            for x in range(cards):
                print("    |             |       ",end="")
            print("")
            #Reveals all symbols for cards held by computer
            if(s==1):
                for x in range((len(computerHand))):
                    print(f"    |      {computerHand[x-1]}      |       ",end="")
                print("\n",end="")
        for x in range(cards):
            print("    *_____________*       ",end="")
        print("\n\n")

def ValueCalculator(State,hand):
    value=0
    #value counted before end game with no Aces
    if(State=="continue"):
        for x in range(len(hand)):
            if(type(hand[x])==int):
                value+=hand[x]
            if(hand[x] in ["J","Q","K"]):
                value+=10
        return(value)
    
    #value counted at end game with Aces counted
    if(State=="end"):
        for x in range(len(hand)):
            if(type(hand[x])==int):
                value+=hand[x]
            if(hand[x]=="A"):
                AceValue=input("Would You Like The Ace To Equal 1 or 11?: ")
                while(AceValue not in ["1","11"]):
                    print(f"{AceValue} is a invalid input. Enter `1` or `11`")
                    AceValue=input("Would You Like The Ace To Equal 1 or 11?")
                if(AceValue=="1"):
                    value+=1
                if(AceValue=="11"):
                    value+=11
            if(hand[x] in ["J","Q","K"]):
                value+=10
        return(value)

#decides who wins at end game
def gameDecider(value1,value2):
    time.sleep(1)
    if(value1>value2 and value1<=21):
        print("Congrats You Won!")
        cowsay.cow("Moo")
    else:
        print("Computer Won!")
        cowsay.cow("Moo")

def GameStarter():
    os.system('clear') 
    print("\n\t\tWould you like to play 21?\n")
    Response=input("\t\t      Type Yes or No: ")
    while(Response.lower() not in ["yes", "no"]):
        os.system("clear")
        print("\n                 Invalid Response Try Again\n")
        print("               Response Needs To Be Yes or No\n")
        Response=input("\t           Input Answer here:")
    os.system('clear')
    
    #Acceptance of Game
    while(Response.lower()=="yes"):
        print("\t           Great Lets Play Then!\n")
        cowsay.cow("\tAces are counted after the game")
        time.sleep(0)
        os.system('clear')
        
        #draws card from deck into hand
        for x in range(2):
            PlayerHand.append(cardDeck.pop(randint(0,len(cardDeck)-1)))
            computerHand.append(cardDeck.pop(randint(0,len(cardDeck)-1)))
            
        #Generates cards
        computerCardGenerator(len(computerHand),computerHand[0],"continue")
        playerCardGenerator(len(PlayerHand),ValueCalculator("continue",PlayerHand))
        anotherCard=input("Would you like another card? (yes) (no): ")

        #Insures Proper Response
        while(anotherCard not in ["yes","no"]):
            print(f"{anotherCard} was invalid. Enter yes or no.")
            anotherCard=input("Would you like another card? (yes) (no): ")

        #Matains a loop asking player if more cards are wanted
        while(anotherCard=="yes"):
            PlayerHand.append(cardDeck[randint(0,len(cardDeck)-1)])
            computerCardGenerator((len(computerHand)),ValueCalculator("continue",computerHand),"continue")
            playerCardGenerator((len(PlayerHand)),ValueCalculator("continue",PlayerHand))
            
            if(ValueCalculator("continue",PlayerHand)<=21):
                anotherCard=input("Would you like another card? (yes) (no): ")
            else:
                anotherCard="no"
                print("You Busted")
                continue
        #occurs when no cards wanted
        if(anotherCard=="no"):
            os.system('clear')
            ComputerValue=ValueCalculator("end",computerHand)
            playerValue=ValueCalculator("end",PlayerHand)
            computerCardGenerator((len(computerHand)),ComputerValue,"end")
            playerCardGenerator((len(PlayerHand)),playerValue)
        #Determines winnner
        gameDecider(playerValue,ComputerValue)
        
        #asks wether another round is wanted
        Response=input("Would You like to play again?  (yes) (no): ")
        while(Response.lower() not in ["yes", "no"]):
            print("\n                 Invalid Response Try Again\n")
            print("               Response Needs To Be Yes or No\n")
            Response=input("\t           Input Answer here:")
        PlayerHand.clear()
        computerHand.clear()
        os.system('clear')
    
    #Rejection of Game
    if(Response.lower()=="no"):
        print("\t           Maybe Some Other Time Then\n")
        cowsay.cow("MOO")
        time.sleep(3)
        os.system('clear')
GameStarter()