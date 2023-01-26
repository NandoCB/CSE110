score = int(input('What is your grade percent? '))

sing = ""
score_last_digit = score % 10

if score_last_digit < 7:
    sign = "-"
elif score_last_digit >= 3:
    sign = "+"
else:
    sign = ""

if score >= 93:
    sign = ""

if score >= 0 and score <= 59:
    print (f'Your grade percent is {score}% and your letter grade is: F{sign}')
elif score >= 60 and score <= 69:
    print (f'Your grade percent is {score}% and your letter grade is: D{sign}')
elif score >= 70 and score <= 79:
    print (f'Your grade percent is {score}% and your letter grade is: C{sign}')
elif score >= 80 and score <= 89 :
    print (f'Your grade percent is {score}% and your letter grade is: B{sign}')
elif score >= 90 and score <= 100:
    print (f'Your grade percent is {score}% and your letter grade is: A{sign}')

if score >= 70:
    print("Congratulations! You passed the class!")
else:
    print("Stay focused and you'll get it next time!")



"""
A >= 90     90 - 100

B >= 80     80 - 89

C >= 70     70 - 79

D >= 60     60 - 69

F < 60       0 - 59
"""