from time import sleep
print('Welcome to CSE 110')

name = input('What is your name? ')
surname = input ('What is your last name? ')

for i in range(3, 0, -1):
    print(i, flush=True)
    sleep(0.5)

print(f' Welcome! \n Your name is {surname}, {name} {surname}.')