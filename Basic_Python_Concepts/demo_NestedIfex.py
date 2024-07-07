age = int(input('Enter your age: '))

if age>=18:
    score = int(input('Enter your exam score: '))
    if score>=40:
        print('You meet both the age and score criteria, you are qualified')
    else:
        print('You meet the age criteria but do not meet the score criteria')
else:
    print('You do not meet the age criteria, please try when you are above 18')
