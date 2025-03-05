#Garrison Synnestvedt
#3 March 2025
#This program calculates the amount of bottles returned to a store every day,
#for a week, and executes a while loop statement to repeat the program until,
#the user wishes to terminate.


#This variable defines how many days the program will ask for the user input,
#about the number of bottles returned each day
nbr_of_days = 7

#The code is all packed into this first while loop in order to repeat as many,
#times as we want. Without it, the program only runs once.
while True:
    # Declare and initialize totalBottles, todayBottles, counter to 1
    #This ensures the values reset to 0 upon the user requesting to re-input data
    #Counter is set to 1 not 0 because it starts on day 1

    total_bottles = 0
    today_bottles = 0
    total_payout = 0
    counter = 1
    keep_going = 'y'
    
    #The loop should run for seven iterations
    #It does if counter is set to 1 and made less than or equal to nbr_of_days

    #This while loop allows for the bottle number input itself
    while counter <=nbr_of_days:  
   
        # Display prompt
        # Input the number of bottles returned today
        today_bottles = int(input(f'Enter number of bottles returned for day #{counter}: '))
    
        # Accumulate the total number of bottles
        total_bottles = total_bottles + today_bottles

        # Increment the counter
        counter = counter + 1

    #Calculate payout amount
    payout_per_bottle = .10
    total_payout = 0 #resets to 0 for multiple runs
    total_payout = total_bottles * payout_per_bottle

    print("The total number of bottles collected is", total_bottles)

    #This print is an f string so we can set the decimal place to just tenths,
    #otherwise it produces more decimals than necessary
    print(f"The total paid out is $ {total_payout:.1f}")

    keep_going = input("Do you want to enter another week's worth of data?\n(Enter y or n): ")

    #Here the break goes into effect if the user enters n
    if keep_going != 'y':
        break