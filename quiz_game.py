import random

print("Welcome to the quiz game!")

questions = ['q1', 'q2', 'q3']
playing = input("Do you want to play?\n")
score = 0

if playing.lower() != str.lower("Yes"):
    quit()

print("Okay, let's play!\n")



while score != -1:
    random_item = random.choice(questions)
    
    print("Your score is currently: ", score, "\n")
    if random_item == questions[0]:
        answer = input("What does CPU stand for?\n")

        if answer.lower() == str.lower("Central Processing Unit"):
            print("Correct!")
            score += 1
        else:
            print("Incorrect, it stands for Central Processing Unit. -1 points\n")
            score -= 1
    
    if random_item == questions[1]:
        answer = input("What does GPU stand for?\n")

    
        if answer.lower() == str.lower("Graphics Processing Unit"):
            print("Correct!")
            score += 1
        else:
            print("Incorrect, it stands for Graphics Processing Unit. -1 points\n")
            score -= 1
    
    if random_item == questions[2]:
        answer = input("What does RAM stand for?\n")

    
        if answer.lower() == str.lower("Random Access Memory"):
            print("Correct!")
            score += 1
        else:
            print("Incorrect, it stands for Random Access Memeory. -1 points\n")
            score -= 1
    

print("Game Over! You lost too many points.\n")