import random

number = random.randint(1,10)
tries = 3
print("Can you win? Let's go!!")
for i in range(0,tries):
    guess = int(input("Guess the number: "))
    if guess == number:
        print("Awesome!!")
        print(f"You have guessed the number right. It's {number}")
        break
    else:
        tries = tries - 1
        print(f"Tries left:  {tries}")
if guess != number:
    print(f"Sorry, your guesses were incorrect. The number is {number}")

