import random

print("OKAY lets play a game shall we i am gonna pick a number between 1-100 and you have to guess it ")

guessed_num = random.randint(0,100)

guesses_want = int(input("how many guesses do you want "))

for i in range(guesses_want):
    print(f"okay you are on your {i+1} guess")
    guess = int(input("gimmme your guess"))
    if guess > guessed_num:
        print("LOWERRRRR")
    elif guess < guessed_num:
        print("HIGHERRRRR")
    else:
        print("You ACTUALLY GOT it")
        break
else:
    print(f"i win my guess was {guessed_num}")
