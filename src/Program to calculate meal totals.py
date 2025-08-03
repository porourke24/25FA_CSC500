# Program to calculate meal totals and statistics for restaurant customers

# Charges for food for several customers
food_charges = [17.00, 25.00, 15.00, 22.00, 35.00,45.00]

# Calculate meals with tip (18%) and tax (7%) for each customer
meal_totals = []
for charge in food_charges:
    tip = charge * 0.18
    tax = charge * 0.07
    total = charge + tip + tax
    meal_totals.append(total)

num_customers = len(food_charges)
print(num_customers, 'customers purchased meals.')

lowest_total = min(meal_totals)
highest_total = max(meal_totals)

print('\nMeal totals ranged from $%.2f to $%.2f' % (lowest_total, highest_total))

# Calculate average meal charge and average total meal cost
average_charge = sum(food_charges) / num_customers
average_total = sum(meal_totals) / num_customers

print('Average food charge: $%.2f' % average_charge)
print('Average total price (with tip and tax): $%.2f' % average_total)
