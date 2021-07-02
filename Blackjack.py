from art import logo
import random as rand
import os 
card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
playerSum = 0
computer_hand = []
computerSum = 0
bIsPlaying = True

def drawCard():
    cardIndex = rand.randint(0,12)
    return card_deck[cardIndex]

def inital_draw():
    for i in range(2): #needs to be 2 initially
        player_hand.append(drawCard())
        computer_hand.append(drawCard())

def addScore(listOfCards):
    sum = 0
    bHasAce = False
    #first we add cards
    for i in listOfCards:
        sum += i
        if(i == 11): #check if we have ace
            bHasAce = True
    if(bHasAce and sum > 21): #if we have an ace in the deck and the sum is over 21, change it to 1 instead of 11
        sum -= 10
    return sum

def checkBlackjack(sum):
    """ Only use this func when checking initial deck! """
    if(sum == 21):
        return True
    else:
        return False

def IsScoreOver21(sum):
    if sum > 21:
        return True
    else:
        return False

def resetGame():
    player_hand = []
    playerSum = 0
    computer_hand = []
    computerSum = 0
    bIsPlaying = True


def initialRun():
    """Run this at the start of the game"""    
    os.system("cls") 
    resetGame()  
    inital_draw()
    print(logo)
    print("player: ",player_hand, " -> ","Computer ", computer_hand[0])
    playerSum = addScore(player_hand)
    computerSum = addScore(computer_hand) #first sum is just the first card of the computer
    print(f"Your score: {playerSum}, Computer score: {computer_hand[0]}") 

    if(checkBlackjack(playerSum)):
        print("Player has blackjack!")
        #run computer to check if he won
        bIsPlaying = False

def checkWinner(PlaySum, CompSum):
    if(PlaySum <= 21 and CompSum <= 21):
        if(PlaySum > CompSum):
            return "Player Wins!"
        elif(PlaySum < CompSum):
            return "Computer Wins!"
        elif(PlaySum == CompSum):
            return "DRAW!"
    elif(CompSum <= 21 and PlaySum > 21):
        return "Computer Wins!"
    elif(PlaySum <= 21 and CompSum > 21 ):
        return "Player Wins!"
    else:
        return "Both are over, if we are here. then we bugged"

### PlayZone
initialRun()
bIsComputerPLaying = True
while bIsPlaying:
    promt = input("Do you want to draw another card? Y/N: ").lower()
    if (promt == "y"):
        player_hand.append(drawCard()) #Draws new card
        playerSum = addScore(player_hand)
        if(IsScoreOver21(playerSum)):
            #player looses
            playerSum = addScore(player_hand)
            computerSum = addScore(computer_hand) #first sum is just the first card of the computer
            print("player: ",player_hand, " -> ","Computer ", computer_hand)
            print(f"Your score: {playerSum}, Computer score: {computerSum}") 
            print("You went over 21! Computer wins!")
            bIsPlaying = False
            bIsComputerPLaying = False
    elif(promt == "n"):
        #Do computer next
        bIsPlaying = False #Quit loop and announce winner.
        #Run computer steps!
    else:
        print("Try again bby, thats not the right question")
    if (bIsPlaying):
        os.system("cls")
        playerSum = addScore(player_hand)
        computerSum = addScore(computer_hand)
        print(logo)
        print("player: ",player_hand, " -> ","Computer ", computer_hand[0])
        print(f"Your score: {playerSum}, Computer score: {computer_hand[0]}") 
    else: #time for the computer to kick some ass
        while bIsComputerPLaying:
            print("Computer plays!")
            playerSum = addScore(player_hand)
            computerSum = addScore(computer_hand)
            os.system("cls")
            print(logo)
            print("player: ",player_hand, " -> ","Computer ", computer_hand)
            print(f"Your score: {playerSum}, Computer score: {computerSum}") 
            if (computerSum < playerSum and computerSum < 21):
                computer_hand.append(drawCard())
                computerSum = addScore(computer_hand)
                print(f"Computer draws a card: {computer_hand} with score: {computerSum}")
            else:
                bIsComputerPLaying = False

            if bIsComputerPLaying == False:
                print(checkWinner(playerSum,computerSum))

###

### TEST ZONE
"""
inital_draw()
print("player: ",player_hand, " -> ","Computer ", computer_hand)
print(f"sum of player: {addScore(player_hand)} and sum computer {addScore(computer_hand)}")
print(f"BJP: {checkBlackjack(addScore(player_hand))} and BJC: {checkBlackjack(addScore(computer_hand))}")
"""
###
"""TODO:
1. deal two cards to player and computer[v]
2. display both player card and one computer card[v]
    1. check for blackjack, if any one got a 10 + ace [v]
3. ask player if they want to hit or stand [v]
4. if less then 21, ask again
5. when player is done, let comp play
6. show second comp card, 
7. if less then player score, draw card again
8. if over 21, player wins
9. 

"""