# Garrison Synnestvedt
# CIS129
# Professor Griwzow
# 25 March 2025

'''
Hotdog Cookout Lab:
Students will be provided the Pseudocode, then they are to create this in Python.

Hot Dog Cookout Calculator

Assume that hot dogs come in packages of 10, and hot dog buns come in packages of 8. 
Design a modular program that calculates the number of packages of hot dogs and the number of 
packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. 
The program should ask the user for the number of people attending the cookout, and the 
number of hot dogs each person will be given. The program should display the following:

1. The minimum number of packages of hot dogs required.
2. The minimum number of packages of buns required
3. The number of hot dogs that will be left over
4. The number of buns that will be left over

Programming Exercise (Hotdog Cookout Calculator)
'''
# Import math module to run the ceiling function later
import math


# Global Constants

# Number of hot dogs in a package
DOGS = 10

# Number of buns in a package
BUNS = 8


# Defining the total hot dogs function module
def getTotalHotDogs():

    '''
    Gets the number of people attending and hotdogs per person,
    then calculates the total hotdogs needed.
    Returns:
        int: Total number of hotdogs needed
    '''

    # Number of people attending 
    people = int(input('Enter the number of people attending the cookout:\n'))

    # Number of hotdogs per person
    hotDogs = int(input('Enter the number of hot dogs for each person:\n'))

    # Calculate total number of hot dogs needed 
    total = people * hotDogs
    return total


# Defining the showResults module
def showResults(dogsLeft, minDogs, bunsLeft, minBuns):

    '''
    This module is is multiple print statements that when run show the 
    results of the calculations
    '''

    # Displays minimum packages of hot dogs needed
    print(f'Minimum packages of hot dogs needed: {minDogs}')

    # Displays minimum packages of buns needed
    print(f'Minimum packages of hot dog buns needed: {minBuns}')

    # Displays hot dogs left over
    print(f'Hot dogs left over: {dogsLeft}')

    # Displays buns left over
    print(f'Hot dog buns left over: {bunsLeft}')


# Defining the main module that runs the calculations
def main():

    '''
    Runs the actual calculations for how many packages of buns and hot dogs 
    are needed and left over based on the user input from the 
    getTotalHotDogs function
    '''
    
    # Change the total variable locally here
    total = getTotalHotDogs()

    # Constant DOGS minus calculated total
    dogsLeft = (DOGS - total % DOGS) % DOGS

    # total / DOGS with a ceiling function, 
    # returning highest integer
    minDogs = math.ceil(total / DOGS)

    # same calculations as dogsLeft
    bunsLeft = (BUNS - total % BUNS) % BUNS

    # same calculations as minDogs
    minBuns = math.ceil(total / BUNS)

    showResults(dogsLeft, minDogs, bunsLeft, minBuns)

main()
    
