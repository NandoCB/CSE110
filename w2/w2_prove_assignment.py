from time import sleep

print('Welcome to Word Games')
print("Let's create a fun Mad Lib")
repeat = True

while repeat == True:

    adjective = input('Please enter an adjective for example "Happy": ')
    animal = input('Please enter an animal for example "Dog": ')
    verb0 = input('Please enter a verb for example "Sneeze": ')
    exclamation = input('Please enter an exclamation for example "hooray": ')
    verb1 = input('Please enter a verb for example "read": ')
    verb2 = input('Please enter a verb for example "drive": ')
    print ('\n')
    list = adjective, animal, verb0, exclamation, verb1, verb2
    print(f'The words you chose were {list} \n are you sure you want to use these words? \n')

    reply = input(('Please type [yes] to continue, [no] to re-enter the words or [exit]: to end the program: '))

    if reply == ('yes'):
            repeat = False
            print("OK let's create your story!")

            for i in range(3, 0, -1):
                print(i, flush=True)
                sleep(0.5)

            print (f"""The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb0} down the hallway.
        {exclamation}! I yelled. But all I could think to do was to {verb1} over and over. Miraculously, that caused it to stop, but not before it tried to {verb2}
        right in front of my family.""")
    if reply == ('exit'):
            exit('Thank you!')

    if reply.upper() == ('no'):
        continue
    if repeat == True:
        print(" Nothing happened here! \n Let's write the words again.\n")
    

     

    