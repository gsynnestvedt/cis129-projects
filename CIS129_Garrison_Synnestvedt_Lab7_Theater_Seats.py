'''
Garrison Synnestvedt
CIS129
Professor Griwzow
4 April, 2025
'''

'''
This lab is for the theater seats. It will display a welcome message
and the relevant section information, then get user input on the number
of seats sold in each section. After each input, it will display the 
number of seats sold out of the total seats in the section, as well as
the income for that particular section. After all the input is gathered,
the final totals of tickets tickets sold and income from all the sections 
is displayed. To add new sections, all that needs to happen are to add new 
constant variables and their values, then add those constants to the lists
in main.
'''

'''
The main function controls the flow of the program. The constants are defined
here, and all other functions are called by the main function to get user input,
display welcome messages, etc.
'''
def main():

    # All the constants are defined here
    SECTION_A = 'A'
    SECTION_B = 'B'
    SECTION_C = 'C'

    PRICE_A = 20
    PRICE_B = 15
    PRICE_C = 10

    CAPACITY_A = 300
    CAPACITY_B = 500
    CAPACITY_C = 200

    # Lists from the values of the constants
    section_names = [SECTION_A, SECTION_B, SECTION_C]
    section_prices = [PRICE_A, PRICE_B, PRICE_C]
    section_capacities = [CAPACITY_A, CAPACITY_B, CAPACITY_C]
    
    # Calls the function to display welcome message
    display_welcome(section_names, section_prices, section_capacities)
    ticket_sales = []
    section_incomes = []
    total_tickets = 0
    total_income = 0

    # This processes each section to get ticket sales and calculate income
    for i in range(len(section_names)):
        tickets = get_valid_tickets(section_names[i], section_capacities[i])
        ticket_sales.append(tickets)

        income = calculate_income(tickets, section_prices[i])
        section_incomes.append(income)

        total_tickets += tickets
        total_income += income


        display_section_subtotal(section_names[i], tickets, section_capacities[i], income)

    '''
    This is outside of the loop so it only displays
    at the end of all the user input
    '''
    final_totals(total_tickets, total_income)

   
# Gets and vaildates the number of tickets sold in a section
def get_valid_tickets(section_names, max_capacity):

    # Inital value outside valid range
    tickets = -1

    # Keep loop going until input is valid
    while tickets < 0 or tickets > max_capacity:
        user_input = input(f'Enter the number of tickets sold for section {section_names}:')
        if user_input.strip() == '':
            print('Error. Please enter a number.')
            continue

        valid_number = True

        # This accounts for a negative number check
        if user_input and user_input[0] == '-':

            for char in user_input[1:]:
                if char not in '0123456789':
                    valid_number = False
                    break
        else:
            for char in user_input:
                if char not in '01234567889':
                    valid_number = False
                    break
    
        if not valid_number:
            print('Error. Please enter a valid number')
            continue

        # Ensures user only enters an integer
        tickets = int(user_input)

        if tickets < 0:
            print('Error. Number of tickets cannot be negative.')
        elif tickets > max_capacity:
            print(f'Error. Section {section_names} only has {max_capacity} seats.')

    return tickets

# Calculates income from ticket sales
def calculate_income(num_tickets, ticket_prices):
    income = num_tickets * ticket_prices
    return income

# Displays the section subtotals
def display_section_subtotal(section_names, tickets_sold, section_capacity, section_income):
    print(f'Section {section_names}: {tickets_sold} of {section_capacity} seats sold.')
    print(f'Income from Section {section_names}: ${section_income:.2f}')
    print()

def final_totals(total_tickets, total_income):
    print('Final Totals:')
    print(f'Total tickets sold: {total_tickets}')
    print(f'Total income from all sections: ${total_income:.2f}')

# Displays the welcome message and section information
def display_welcome(section_names, section_prices, section_capacities):
    print('Welcome to the Theater Ticket Sales Program')
    print('Section Information')
    for i in range(len(section_names)):
        print(f'Section {section_names[i]}: {section_capacities[i]} seats at ${section_prices[i]} each')
    print('Please enter the number of tickets sold for each section.')
    
main()