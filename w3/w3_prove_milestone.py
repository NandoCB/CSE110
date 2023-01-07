import time
print('Meal Price Calculator')

child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
children_number = int(input("How many children are there? "))
adult_number = int(input("How many children are there? "))
tax = float(input("What is the sales tax rate? "))

subtotal = ((child_meal*children_number)+(adult_meal*adult_number))

sales_tax_rate = (subtotal*(tax/100))

total = (subtotal + sales_tax_rate)



print('----------------Invoice----------------')
print (f"Date and time " + time.strftime("%c"))
print('Billing Detail')

print(f"Child's meal - Qty {children_number} - Price ${child_meal}")

print(f"Adult's meal - Qty {adult_number} - Price ${adult_meal}")

print(f'Sales tax rate:  + {tax}%')

print(f'Subtotal: ${round(subtotal, 2)}')
print(f'Sales Tax: ${round(sales_tax_rate, 2)}')
print(f'TOTAL: ${round(total, 2)}')

print('--------Thanks for your purchase-------')