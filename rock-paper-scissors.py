import random
print("Welcome to rock,paper,scissors game :)")
game_choices = ["rock", "paper", "scissors"]
computer_score = 0
user_score = 0
while True:

    if user_score == 3 or computer_score == 3:
        if user_score == 3:
            print("You win :)")
        else:
            print("You lose :(")
        answer = input("Do you want to play again?: Yes/No: ")
        if answer == "No":
            print("Thanks for playing!")
            break
        else:
            computer_score = 0
            user_score = 0
    computer = random.choice(game_choices)
    user = input("What is your choice? rock/paper/scissors: ")
    while user not in game_choices:
        print("Wrong answer!")
        user = input("What is your choice?: ")
    print("computer choice is: ", computer)
    print("user choice is: ", user)
    if computer == 'rock':
        if user == 'paper':
            print("You won a point!")
            user_score += 1
            print("User score: ", user_score)
            print("computer score: ", computer_score)
        elif user == 'scissors':
            print("computer wins a point!")
            computer_score += 1
            print("User score: ", user_score)
            print("computer score: ", computer_score)
        else:
            print("Tie")
    elif computer == 'scissors':
        if user == 'rock':
            print("You won a point!")
            user_score += 1
            print("User score: ", user_score)
            print("computer score: ", computer_score)
        elif user == 'paper':
            print("computer wins a point!")
            computer_score += 1
            print("User score: ", user_score)
            print("computer score: ", computer_score)
        else:
            print("Tie")
    elif computer == 'paper':
        if user == 'rock':
            print("computer wins a point!")
            computer_score += 1
            print("User score: ", user_score)
            print("computer score: ", computer_score)
        elif user == 'scissors':
            print("You win a point!")
            user_score += 1
            print("User score: ", user_score)
            print("computer score: ", computer_score)
        else:
            print("Tie!")
