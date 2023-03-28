import sys
item_list = list()
item_price = list()
item_quantity = list()
amount_list = list()
counter_list = list()
manage_cart = True
addin_item_dashboard = True
total = 0
position = 0
total_amount = 0

print('Welcome to the Shopping Cart Program!')
print('')
while manage_cart == True:

    print("""Please select one of the following:
    1. Add item
    2. View cart
    3. Modify cart quantities
    4. Compute total
    5. Remove item
    6. Clear Cart
    7. Quit""")

    enter_action = int(input('Please enter an action: '))
    if enter_action == 1:
        while addin_item_dashboard == True:
             
            item = str(input('Enter item to add: '))
            if item.capitalize() in item_list:
                print('The item is already in the cart')
                addin_item_dashboard = True
                break
            else:
                item_list.append(item.capitalize())

            price = float(input('Enter item price: '))
            item_price.append(price)
            add_quantity = float(input('Enter item quantity: '))
            item_quantity.append(add_quantity)
            amount = price*add_quantity
            amount_list.append(amount)
            print()
            print(f'* {item.capitalize()} * has been added to the cart')

            continue_adding_items = input('Do you want to continue adding items to the cart? [YES or NO]: ')

            if continue_adding_items == 'yes':
                    addin_item_dashboard = True
            else:
                addin_item_dashboard = False
                break
        
    elif enter_action == 2:
        print('The contents of the shopping cart are:')
        print("+------------+--------------------+------------+-------------+-----------+")
        print("|ITEM NUMBER |ITEM                |QTY.        |PRICE        |AMOUNT     |")
        print("+------------+--------------------+------------+-------------------------+")
        counter = 1     
        for a, b, c, d in zip (item_list, item_quantity, item_price, amount_list):
            
            print("|  {:10}|{:<20}|{:>12.2f}|${:>12.2f}|${:>10.2f}|".format(counter, a, b, c, d))
            counter += 1
            
 
        print("+------------+--------------------+------------+-------------------------+")
        
        total = 0
        total_amount = 0

        for amount in amount_list:
            total += amount
            total_amount += 1
   
        print("|------------|--------------------|------------|TOTAL:       |${:>10.2f}|".format(total))
        print("+------------+--------------------+------------+-------------------------+")

    elif enter_action == 3:
        
        index = int(input("What quantity index do you want to update? "))
        new_qty = int(input("What is the new quantity? "))

        item_quantity[index] = new_qty
        if new_qty >= 0:
            amount_list[index] = item_price[index]*new_qty

        total = 0
        total_amount = 0

        for amount in amount_list:
            total += amount
            total_amount += 1

        print('\nQuantity updated successfully!')
        
        ##############################################################################
        # New Quantity purchase
        ##############################################################################

        print('\nThe new contents of the shopping cart are:')
        print("+------------+--------------------+------------+-------------+-----------+")
        print("|ITEM NUMBER |ITEM                |QTY.        |PRICE        |AMOUNT     |")
        print("+------------+--------------------+------------+-------------------------+")
        counter = 1     
        for a, b, c, d in zip (item_list, item_quantity, item_price, amount_list):
            
            print("|  {:10}|{:<20}|{:>12.2f}|${:>12.2f}|${:>10.2f}|".format(counter, a, b, c, d))
            counter += 1
            
 
        print("+------------+--------------------+------------+-------------------------+")
        print("|------------|--------------------|------------|TOTAL:       |${:>10.2f}|".format(total))
        print("+------------+--------------------+------------+-------------------------+")
        
        ################################################################################   
        
    elif enter_action == 4:

        total = 0
        total_amount = 0

        for amount in amount_list:
            total += amount
            total_amount += 1
       
        print(f'The total price of the items in the shopping cart is ${total:.2f}')
        print()

    elif enter_action == 5:
        delete_item = input('Enter the number of the item to delete: ')
        print()
        if delete_item.isdigit() and int(delete_item) <= counter:
            position = int(delete_item) - 1
            del item_list[position]
            del item_price[position]
            del item_quantity[position]
            del amount_list[position]
        
            print(f'* {delete_item} * deleted successfully')
        else:
             print('The article does not exist')
             print()

    elif enter_action == 6:
        delete_all = input('Are you sure you want to remove all items from the cart? [YES or NO]: ')
        delete_all = delete_all.lower()

        if delete_all == 'yes':
            item_list = []
            item_quantity = []
            item_price = []
            amount_list = []
            
            manage_cart == True
    
    elif enter_action == 7:
        user_exit = input('Are you sure you want to exit the cart? [YES or NO]: ')
        user_exit = user_exit.lower()
        if user_exit == 'yes':
             sys.exit('Thank you. Goodbye.')
        else:
             manage_cart = True
    
    else:
        print('Invalid input error, please enter a number between 1 and 7')
        print()
        manage_cart == True