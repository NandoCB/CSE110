import time

employee_name = input('Enter your full name: ')
employee_number = int(input('Enter your employee number: '))
user_var = 'User1'
password_var = 'a1234'

for i in range(2):
    user_sistem = input('Enter your username: ')
    if user_sistem == user_var:
        for i in range(2):
            password_sistem = input('Enter your password: ')
            if password_sistem == password_var:
                print('Welcome')
                
       


                print('Meal Price Calculator')

                child_meal = float(input("What is the price of a child's meal? "))
                adult_meal = float(input("What is the price of an adult's meal? "))
                children_number = int(input("How many children are there? "))
                adult_number = int(input("How many children are there? "))
                tax = float(input("What is the sales tax rate? "))
                

                subtotal = ((child_meal*children_number)+(adult_meal*adult_number))
                sales_tax_rate = (subtotal*(tax/100))
                total = (subtotal + sales_tax_rate)
                print(f'TOTAL: ${round(total, 2)}')
                customer_payment = float(input('Cash delivered by customer: '))
                print('')

                grocery_return = (customer_payment - total) 

                print('----------------Invoice----------------')
                print (f"Date and time " + time.strftime("%c"))
                print('Billing Detail')

                print(f"Child's meal - Qty {children_number} - Price ${child_meal}")

                print(f"Adult's meal - Qty {adult_number} - Price ${adult_meal}")

                print(f'Sales tax rate:  + {tax}%')

                print(f'Subtotal: ${round(subtotal, 2)}')
                print(f'Sales Tax: ${round(sales_tax_rate, 2)}')
                print(f'TOTAL: ${round(total, 2)}')

                print(f'Cash by customer ${customer_payment}')
                print(f'Change ${grocery_return}')
                print('')
                print(f'''You were treated by {employee_name}\nOfficial number: {employee_number}''')
                print('')
                print('--------Thanks for your purchase-------')
                exit()
            
            else:
                print('Password error: Wrong password, please check')
    else:
        print('User error: Wrong user, please check')