import random

num = random.randint(1, 100)

while True:
    guess = int(input("Your guess (1–100): "))
    if guess < num:
        print("🔻 Too low")
    elif guess > num:
        print("🔺 Too high")
    else:
        print("🎯 Correct!")
        break
