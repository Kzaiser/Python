import time
import random

name = input("Type your name: ")
print("Welcome",  name, "to an adventure.")

points = random.randint(10, 20)
print("You have been allocated", points, "to spend on your stats.")

try:
    strength = eval(input("How strong are you on a scale of 1 to 10? "))
    points = points - strength
    print("Points left:", points)
    smart = eval(input("How smart are you on a scale of 1 to 10? "))
    points = points - smart
    print("Points left:", points)
    agile = eval(input("How agile are you on a scale of 1 to 10? "))
    points = points - agile
except NameError:
    print("Invalid input")

print("You have", strength,"Strength.")
print("You have", smart, "Smarts.")
print("You have", agile, "Agility.")


a = input("You're on a dirt road, you see two paths ahead of you. Do you go \'left\' or \'right?\' ").lower()

if a == "left":
    a = input("You arrive at a river, you can \'walk\' around it or \'swim\' across. ").lower()

    if a == "swim" and strength < 5:
        print("You tried to swim across the river and drowned.")
    elif a == "swim" and strength >= 5:
        print("You tried to swim across the river...")
        time.sleep(1)
        print("And successfully make it across. You immediately run into a stranger. Do you \'talk\' to them or try to \'avoid\' them? ")
        a2 = input().lower()
        if a2 == "talk":
            print("You talk to the stranger, He is startled and blows you up with a fireball.")
        elif a2 == "avoid":
            answer = input("You begin to walk away but you catch his attention. He calls you over and asks if you would like to \'purchase\' some weapons. Or you can just \'leave\'.")
        else:
            print("Not a valid option. you die of boredom.")
    elif a == "walk":
        print("You tried to find a way across the river, couldn't find one and died of starvation. Nice.")
    else:
        print("Not a valid option. You die from boredom.")
elif a == "right":
    a = input("You approach a rope bridge. It looks sketchy, do you still want to \'cross\' or \'return\' to where you came from? ").lower()
    
    if a == "cross":
        a = input("You carefully cross the bridge, despite almost falling a few times you successfully make it across. There are goblins in the way, do you choose to \'fight\' them or leave? ")
    elif a == "return":
        a = input("You turn around and there is a stranger standing in front of you. Do you \'talk\' to them or try to \'avoid\' them? ")
    else:
        print("Not a valid a. You die of boredom")
else:
    print("You must choose left or right. ")