import random
answer = random.randint(1, 100)
guess = 0
attempt = 0
while guess != answer:
    attempt += 1
    print('This is your ' + str(attempt) + ' attempt')
    guess = int(input("enter a number between 1 and 100: "))
    if guess < answer:
        print('More !')
    elif guess > answer:
        print('Fewer !')
print('It only worked ' + str(attempt) + ' attempt :)')
