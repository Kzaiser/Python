import time
import random

name = input("Type your name: ")
print("Welcome",  name, "to an adventure.")

points = random.randint(10, 20)
print("You have been allocated", points, "to spend on your stats.")

while points > 0:
    try:
        strength = eval(input("How strong are you on a scale of 1 to 10? "))
        points = points - strength
        smart = eval(input("How smart are you on a scale of 1 to 10? "))
        points = points - smart
        agile = eval(input("How agile are you on a scale of 1 to 10? "))
        points = points - agile
    except NameError:
        print("Invalid input")

print("You have", strength,"Strength.")
print("You have", smart, "Smarts.")
print("You have", agile, "Agility.")


answer = input("You're on a dirt road, you see two paths ahead of you. Do you go \'left\' or \'right?\' ").lower()

if answer == "left":
    answer = input("You arrive at a river, you can \'walk\' around it or \'swim\' across. ").lower()

    if answer == "swim" and strength < 5:
        print("You tried to swim across the river and drowned.")
    elif answer == "swim" and strength > 5:
        print("You tried to swim across the river...")
        time.sleep(2)
        print("And successfully make it across. You immediately run into a stranger. Do you \'talk\' to them or try to \'avoid\' them? ").lower()
    elif answer == "walk":
        print("You tried to find a way across the river, couldn't find one and died of starvation. Nice.")
    else:
        print("Not a valid option. You die from boredom.")
elif answer == "right":
    answer = input("You approach a rope bridge. It looks sketchy, do you still want to \'cross\' or \'return\' to where you came from? ").lower()
    
    if answer == "cross":
        answer = input("You carefully cross the bridge, despite almost falling a few times you successfully make it across. There are goblins in the way, do you choose to \'fight\' them or leave? ")
    elif answer == "return":
        answer = input("You turn around and there is a stranger standing in front of you. Do you \'talk\' to them or try to \'avoid\' them? ")
    else:
        print("Not a valid answer. You die of boredom")
else:
    print("You must choose left or right. ")