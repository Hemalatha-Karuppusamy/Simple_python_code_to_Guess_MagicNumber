import random
magic = random.randint(1, 50)
count = 0

while True:
    count += 1
    user = int(input('Guess the number: '))

    if user < magic:
        print(f'{user} is too low! Try again')
    elif user > magic:
        print(f'{user} is too high Try again')
    else:
        print(f'Congratulations! {user} is the MAGIC NUMBER!!!')
        print(f'You guessed the correct number in {count} attempts')
        break