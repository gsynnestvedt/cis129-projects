# Garrison Synnestvedt
# CIS129
# Professor Griwzow
# 28 March, 2025

# Lab 7-3 The Dice Game
# add libraries needed
import random

# the main function
def main():
    print()

    #initialize variables
    endProgram = 'no'
    playerOne = 'NO NAME'
    playerTwo = 'NO NAME'

    #call to inputNames
    playerOne, playerTwo = inputNames(playerOne, playerTwo)

    #while loop to program again
    while endProgram == 'no':
        
        #populate variables
        winnerName = 'NO NAME'
        p1number = '0'
        p2number = '0'

        #call to rollDice
        winnerName = rollDice(p1number, p2number, playerOne, playerTwo, winnerName)

        #call to displayInfo
        displayInfo(winnerName)

        endProgram = input('Do you want to end program? (yes/no): ')

# this function gets the players names
def inputNames(playerOne, playerTwo):
    playerOne = str(input('Enter name for player 1:\n'))
    playerTwo = str(input('Enter name for player 2:\n'))
    return playerOne, playerTwo

# this function will get the random values
def rollDice(p1number, p2number, playerOne, playerTwo, winnerName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)

    if p1number > p2number:
        winnerName = playerOne
    elif p2number > p1number:
        winnerName = playerTwo
    else:
        winnerName = 'TIE'
    return winnerName

# this function displays the winner
def displayInfo(winnerName):
    if winnerName == 'TIE':
        print('The game is a tie!')
    else:
        print(f'The winner is {winnerName}!')

# calls main
main()

