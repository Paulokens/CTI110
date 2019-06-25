# Meal and Tip calculator
# 06/23/2019
# CTI-110 P2HW2 - Meal Tip calculator
# Pierre Paul
#

# Get the charge for the food.
food_charge = float(input('Enter the charge for the food: '))

# Create three variables for the tip amounts.
tip_amount1 = food_charge * 0.15
tip_amount2 = food_charge * 0.18
tip_amount3 = food_charge * 0.20

# Create three variables for the meal's total cost.
meal_total_cost1 = food_charge + tip_amount1
meal_total_cost2 = food_charge + tip_amount2
meal_total_cost3 = food_charge + tip_amount3

# Display the result.
print("For a 15% tip, the tip amount is",format(tip_amount1,',.2f'), "and the meal's total cost is",format (meal_total_cost1,",.2f"))
print("For an 18% tip, the tip amount is", format(tip_amount2,',.2f'), "and the meal's total cost is",format (meal_total_cost2,",.2f"))
print("For a 20% tip, the tip amount is", format(tip_amount3, ',.2f'), "and the meal's total cost is",format (meal_total_cost3,",.2f"))
