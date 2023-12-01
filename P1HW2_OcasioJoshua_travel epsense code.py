# A tool to calculate travel expences
# 09/03/2023
# CTI-110 P1HW2 - Travel Expense
# Joshua Ocasio
#

print('This program will calculate and display travel expences')
#
budget = float(input('Enter Budget:') )
#
destination = input('Enter your travel destination:') 
#
gas = float(input('How much do you think you will spend on gas?:')) 
#
accommodations = float(input('Estimate how much you will need for accommodations:'))
#                       
food = float(input(' How much mre money do you need for food?:'))
#
expenses = gas + accommodations + food
#
balance = budget - expenses
#Display results
print('------Travel Expenses-------')
print('destination', destination)
print('initial Budget', budget)
print('Gas', gas)
print('Accomodations', accommodations)
print('food', food)
print('expenses', expenses)
print('remaining Balance', balance)

             
