#Iteration 2
import random
import math
import time

#list of bot names
bots = ["Coco McCrea", "Sebastian Maximus", "Geronimo", "Bartholomew Bunglerick"]

#deck of cards, simplified to one seed, chances are the same if i were to put all seeds. picture cards have values of 10
deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]

#after completing Iteration 1, i realised that simulation mode would be easier to develop with functions, fixing up singleplayer and multiplayer as well. Two birds with one stone

#function for card being drawn
def hitCard(hand):
    print("-"*30)
    card = random.choice(deck)
    print("Your new card is:",card)
    hand.append(card)
    print("Your hand is:",hand,"(",sum(hand),")")
   

#function to check if  player total is over 21 (loss check)
def checkDeath(player, total):
    if total > 21:
        print(player,"has lost as they've gone over 21 with the score of", total)
        return("loss")
   
#function to have bot hit/stand
def botHitStand(total):
    if total < 17:
        dealerHand.append(random.choice(deck))
        print("-"*30)
        print(botName,"hits")
        print(botName,"hand is:",dealerHand,"(",sum(dealerHand),")")
        time.sleep(1)
        print("-"*30)
        return("hit")
    else:
        print(botName,"is happy with the score of",sum(dealerHand),"and decided to skip")
        return("stand")
           
#prints out the dealer's and player's hands      
def hands(playerOne, playerTwo, handOne, handTwo):
    print(f"{playerTwo} hand is:{handTwo} ({sum(handTwo)})")
    print(f"{playerOne} hand is:{handOne} ({sum(handOne)})")
    print("-"*30)
   
#function to see who is closer to 21
def closerToWinCheck(totalOne, playerOne, totalTwo, playerTwo):
    if totalOne > totalTwo:
        print(f"{playerOne} has won against {playerTwo}, as {playerOne} is closer to 21 with the score of {totalOne}")
        print("-"*30)
    elif totalOne < totalTwo:
        print(f"{playerTwo} has won against {playerOne}, as {playerTwo} is closer to 21 with the score of {totalTwo}")
        print("-"*30)
    else:
        print(f"There has been a draw between {playerOne} and {playerTwo}")
        print("-"*30)
        return("draw") #can be used to decide for coin flip or smth

#adds initial cards to dealer's and player's hands
def initialCards(handOne, handTwo):
    for i in range(2):
        handOne.append(random.choice(deck))
        handTwo.append(random.choice(deck))
   
   
   
   
   
   
       
#start of code
print("-"*30)
mode = int(input("Hello and welcome to blackjack,\n1) Single player\n2) Multiplayer\n3) Simulation play\n4) Quit game "))
print("-"*30)
while mode != 4:
    if mode == 1:
        #singelplayer
       
        #player's cards in singleplayer
        singlePlayerHand = []
        #dealer's cards in singleplayer
        dealerHand = []
       
        botName = random.choice(bots)
        print("Your opponent, the dealer, is", botName)
        singlePlayerName = input("State your username: ")
       
        #adds initial cards to dealer's and player's hands
        initialCards(singlePlayerHand, dealerHand)
       
        #prints out the dealer's and the player's hands
        hands(singlePlayerName, botName, singlePlayerHand, dealerHand)

       
        hit = int(input("To hit (1) \nTo stand (2):"))
        while hit == 1:
            hitCard(singlePlayerHand)
            print("-"*30)
            if checkDeath(singlePlayerName, sum(singlePlayerHand)) == "loss": #if player goes over 21, they lose. calls function to check
                print("-"*30)
                hit = 0 #to have it leave the while loop
                mode = int(input("Hello and welcome to blackjack,\n1) Single player\n2) Multiplayer\n3) Simulation play\n4) Quit game "))
            else:
                hit = int(input("To hit (1) \nTo stand (2):"))
        while hit == 2:
            if checkDeath(botName, sum(dealerHand)) == "loss":
                print("-"*30)
                print("You won against", botName)
                hit = 0 #to have it leave the while loop
                mode = int(input("Hello and welcome to blackjack,\n1) Single player\n2) Multiplayer\n3) Simulation play\n4) Quit game "))
            else:
                if botHitStand(sum(dealerHand)) == "stand":
                    print("-"*30)
                    hit = 0 #to have it leave the while loop
                    closerToWinCheck(sum(singlePlayerHand), singlePlayerName, sum(dealerHand), botName) #function to see who is closer to 21
                    mode = int(input("Hello and welcome to blackjack,\n1) Single player\n2) Multiplayer\n3) Simulation play\n4) Quit game "))
                   
                   
                   
    elif mode == 2:
        #multiplayer
       
        #player one's cards
        playerOneHand = []
       
        #player two's cards
        playerTwoHand = []
       
        playerOneName = input("Please enter player 1 name (dealer for the round): ")
        playerTwoName = input("Please enter player 2 name: ")
       
        #adds initial cards to players'hands
        initialCards(playerOneHand, playerTwoHand)
       
        #prints out the dealer's and the player's hands
        hands(playerOneName, playerTwoName, playerOneHand, playerTwoHand)
       
       
        hit = int(input(f"{playerTwoName}'s turn ({sum(playerTwoHand)}): \nTo hit (1) \nTo stand (2):"))
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    elif mode == 3: #simulation
        pass
    else:
        print("please enter an available option")
        print("-"*30)
        mode = int(input("Hello and welcome to blackjack,\n1) Single player\n2) Multiplayer\n3) Simulation play\n4) Quit game "))
        print("-"*30)