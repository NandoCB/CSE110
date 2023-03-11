
print('Welcome to the Lists of Numbers')

print("Enter a list of numbers, type 0 when finished.")

numbers = []
number = -1

while number != 0:
    number = int(input("Enter number: "))

    if number != 0:
        numbers.append(number)

sum = 0

for number in numbers:
    sum += number

print(f"The total of the sum is: {sum}")
print()

###############################################################
count = len(numbers)
average = sum / count

print(f"The average is: {average}")
print()
########################################################
bigger_number = -1

for number in numbers:
    if number > bigger_number:
        bigger_number = number

print(f"The largest number is: {bigger_number}")


############################################################

smallest_number = 999999999999999999999

for number in numbers:
    if number > 0 and number < smallest_number:
        smallest_number = number
print(f"The smallest positive number is: {smallest_number}")

#################################################################

new_sorted_list = sorted(numbers)

print("The sorted list is:")
for number in new_sorted_list:
    print(number)
