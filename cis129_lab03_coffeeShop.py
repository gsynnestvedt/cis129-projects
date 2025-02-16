<<<<<<< HEAD
#Start with program documentation
#First we declare the constants in this program,
#which are the prices of the items themselves and the tax rate

price_coffee = 5.00
price_muffin = 4.00
tax_rate = .06

#Here we begin to build the actual receipt with asterisks and all
#I just printed the asterisks and dashed lines

print('***************************************')
print('My Coffee and Muffin Shop')

#Input: Get input from the customer
#Items will be integers because customers are buying whole items
#This coffee shop does not sell floating point items

num_coffees = int(input('Number of coffees bought?\n'))
num_muffins = int(input('Number of muffins bought?\n'))
print('***************************************\n')

#Processing: Calculate the total cost
#Assigning variable for subtotal, tax, and total
#As well as the arithmetic to be performed for the total
#Also assigned variables for total_items so that we can do
#f strings to manipulate text based on the amounts
#The same goes for the item_word variables, the word will change
#based on the amount ordered

print('***************************************')
total_coffees = (num_coffees * price_coffee)
total_muffins = (num_muffins * price_muffin)
coffee_word = 'Coffee' if num_coffees == 1 else 'Coffees'
muffin_word = 'Muffin' if num_muffins == 1 else 'Muffins'
subtotal = (total_coffees + total_muffins)
tax = subtotal * tax_rate
total = subtotal + tax

#Output: Display reciept to customer
#I use the :.2f to tell the program the decimal places the number
#should go to
#The receipt will display the number of coffes, which word, and the
#total, based on the inital input given by the user
print('My Coffee and Muffin Shop Receipt')
print(f'{num_coffees} {coffee_word} at $5 each: ${total_coffees:.2f}')
print(f'{num_muffins} {muffin_word} at $4 each: ${total_muffins:.2f}')
print(f'6% tax: ${tax:.2f}')
print('---------')
print(f"Total: ${total:.2f}")
print('***************************************')
=======

>>>>>>> 7277bd6f92b5e343a28cdb52f2ab117c4a05fc8a
