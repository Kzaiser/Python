import random

# r = random.randint(1, 100)

top_of_range = input("Type a number\n")
# print(r)

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Type a number larger than 0 next time.\n")
        quit()
else:
    print("Type a number next time.\n")
    quit()

r = random.randint(0, top_of_range)
# print(r)

while True:
    user_input = input("Guess the number: ")

    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print("Type a number next time.\n")
        continue

    if user_input == r:
        print("You guessed the number.\n")
        break
    else:
        if user_input < r % 10:
            print("You are close.\n")
        else:
            print("Try again\n")
            continue

