# -*- coding: utf-8 -*-


# Quiz 1 Computer Programming 1

# Find all the prices of the items
item_1 = float(input("What is the price for item 1?"))
item_2 = float(input("What is the price for item 2?"))
item_3 = float(input("What is the price for item 3?"))

# Calculating the tip which is 16% of the item's price
tip1 = item_1 * .16
tip2 = item_2 * .16
tip3 = item_3 * .16

# Calculating sales tax which is 8% of the item price
sales_tax_1 = item_1 * .08
sales_tax_2 = item_2 * .08
sales_tax_3 = item_3 * .08

# Calculating the payable amount which is the item price plus tax plus tip
payable_amount_1 = item_1 + sales_tax_1 + tip1
payable_amount_2 = item_2 + sales_tax_2 + tip2
payable_amount_3 = item_3 + sales_tax_3 + tip3 

# Total amount is all the payable amounts put together
total_amount = payable_amount_1 + payable_amount_2 + payable_amount_3

# Printing the payable amounts for each price
print(payable_amount_1, "dollars is the total price for item 1")
print(payable_amount_2, "dollars is the total price for item 2")
print(payable_amount_3, "dollars is the total price for item 3")

# Printing the total amount for all items
print(total_amount, "dollars is the amount for all payable items")
