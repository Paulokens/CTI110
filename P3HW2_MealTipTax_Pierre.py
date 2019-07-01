# CTI-110 
# P3HW2 - MealTipTax 
# Paul Pierre 
# 06/30/2019
#

#Pseudocode
#
#Get the charge for the meal.
#Get the tip percentage.
#Create the variables for the tip, tax and total amounts.
#Alternative decision structure to calculate and display the results or to display the error message.

#Get the charge for the meal and the tip percentage.
food_charge = float(input('Enter the charge for the meal: '))
tip_percentage = float(input('Enter the tip percentage you would like to consider (15% or 18% or 20%): '))

#Variables for tip, tax and total amounts
tip_amount = food_charge * ( tip_percentage / 100 )
sales_tax_amount = food_charge * 0.07
total_amount = food_charge + tip_amount + sales_tax_amount


#Alternative decision structure.
if (tip_percentage == 15 or tip_percentage == 18) or (tip_percentage == 20):
    print(' Tip  :',format(tip_amount,',.2f'),'\n','Tax  :',format(sales_tax_amount,',.2f'),'\n','Total:',format(total_amount,',.2f'))

else: print('Error! You enter a wrong tip percentage.')
