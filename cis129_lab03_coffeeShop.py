
#Start with program documentation.
#First we declare the constants in this program,
#which are the prices of the items themselves and the tax rate.
#When I merged to github, I had other things in the program that I did not write
#such as this: <<<<<<< HEAD I do not know what it means, so I deleted it.
#I do not know if that will affect the code.
price_coffee = 5.00
price_muffin = 4.00
price_scone = 3.00
price_eggsand = 6.00
tax_rate = .06

#Here we begin to build the actual receipt with asterisks and all
#I just printed the asterisks and dashed lines.
print('***************************************')
print('My Coffee and Muffin Shop')

#This is where we will get the input from the customer to do the program.
#Items will be integers because customers are buying whole items.
num_coffees = int(input('Number of coffees bought?\n'))
num_muffins = int(input('Number of muffins bought?\n'))
num_scones = int(input('Number of scones bought?\n'))
num_eggsands = int(input('Number of egg sandwiches bought?\n'))
print('***************************************\n')

#Processsing part to calculate the total cost.
#Assigning variable for subtotal, tax, and total.
#as well as the arithmetic to be performed for the total.
#Also assigned variables for total_items so that we can do
#f strings to manipulate text based on the amounts.
#The same goes for the item_word variables, the word will change
#based on the amount ordered.
total_coffees = (num_coffees * price_coffee)
total_muffins = (num_muffins * price_muffin)
total_scones = (num_scones * price_scone)
total_eggsands = (num_eggsands * price_eggsand)
coffee_word = 'Coffee' if num_coffees == 1 else 'Coffees'
muffin_word = 'Muffin' if num_muffins == 1 else 'Muffins'
scone_word = 'Scone' if num_scones == 1 else 'Scones'
eggsand_word = 'Egg Sandwich' if num_eggsands == 1 else 'Egg Sandwiches'
subtotal = (total_coffees + total_muffins + total_scones + total_eggsands0
tax = subtotal * tax_rate
total = subtotal + tax

#Output: Display reciept to customer
#I use the :.2f to tell the program the decimal places the number
#should go to
#The receipt will display the number of coffes, which word, and the
#total, based on the inital input given by the user
#I am trying to keep the actual reciept part different from the parts defining things
#so I moved the asterisk line down here and I will see if it will still work
print('***************************************')
print('My Coffee and Muffin Shop Receipt')
print(f'{num_coffees} {coffee_word} at $5 each: ${total_coffees:.2f}')
print(f'{num_muffins} {muffin_word} at $4 each: ${total_muffins:.2f}')
print(f'{num_scones} {scone_word} at $3 each: ${total_scones:.2f}')
print(f'{num_eggsands} {eggsand_word} at $6 each: ${total_eggsands:.2f}')
if tax < 1.00:
  print(f'6% tax: $ {str(tax)[1:]}')
else:
  print(f'6% tax: ${tax:.2f}')
print('---------')
print(f'Total: ${total:.2f}')
print('***************************************')
print('Thank You, Come Again!')

