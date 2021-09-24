import random
print('Hello. What is your name?')
name = input()
secretNumber = random.randint(1,100)
print('Well, '+name+'. I am thinking a number between 1 to 100')

for guessesTaken in range(1,7):
    print('Take a guess. Be carefull! you just have '+str(7-guessesTaken)+' chances.')
    number = input()
    guess = int(number)     
    if guess>secretNumber:
        print('Your guess is too high')
    elif guess<secretNumber:
        print('Your guess is too low')
    else:
        break
    
if guess ==  secretNumber:
    print('Good job, ' + name +'! You guessed my number in '+str(guessesTaken)+' guesses!')
else:
    print('Nope. The number I was thinking of was '+str(secretNumber))
