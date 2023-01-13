print('ID Badge Generator')
print('Please enter the following information: ')
print('\n')

name = input('First name: ')
last_name = input('Last name: ')
email = input('Email address: ')
phone = input('Phone number: ')
job_title = input('Job title: ')
id_num = input('ID Number: ')

print('The ID Card is:')

print('------------------------------------------------------------')
print(f'{last_name}, { name}')
print(job_title)
print(f'ID: {id_num}')
print('\n')
print(email)
print(phone)
print('------------------------------------------------------------')

print('Create your password to access the system')
print("""#Remember the password to establish must contain the following characteristics:\n
#1. The password must have between 6 and 12 characters.\n
#2. The password must contain some special character.\n
#3. Password must contain some capital letter.\n
#4. The password must contain some lower case.\n
#5. The password must contain some digit.\n""")

from string import punctuation

def password_validator (cts) :

    if 5 < len(cts) < 13:
        if any ([c.isdigit() for c in cts]):
            if any ([c.islower() for c in cts]):
                if any ([c.isupper() for c in cts]):
                    if any ([True if c in punctuation else False for c in cts]):
                        print ('Password set successfully')
                        return True
                    else:
                        print('The password must contain some special character')
                else:
                    print('Password must contain some capital letter')
            else:
                print('The password must contain some lower case')
        else:
            ('The password must contain some digit')
    else:
        print('The password must have between 6 and 12 characters')
    return False

attempts = 0

while True:
    password = input('Enter your Password: ')
    attempts +=1

    if password_validator(password):
        print('------------------------------------------------------------')
        print('\n')
        print('The entered password has been {}' .format(password))
        print('\n')
        print('------------------------------------------------------------')
        break
    elif attempts > 5:
        password = None
        print('Error')
        print('------------------------------------------------------------')
        print('\n')
        print('Failed to set a password')
        print('\n')
        print('------------------------------------------------------------')
        break
