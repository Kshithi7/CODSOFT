# module to choose randomly
import random

# define the choices and intial scores
choose=["rock","paper","scissor"]
user_points=0
computer_points=0

# function to declare winner 
def winner(user,computer):
 if user==computer:
     return "tie"     # tie condition,no scores alloted
 elif(user=="rock"and computer=="scissor") or \
     (user=="paper"and computer=="rock") or \
     (user=="scissor"and computer=="paper"):
     return "user"                               # rules for the game            
 else:
     return "computer"

# user-interface comments/instructions
print("Welcome to Rock, Paper, Scissor game!")
print("Instructions: Enter 'rock', 'paper', or 'scissor' to play.")
print("The game will display your scores after each round.")
print("Type 'yes' to play another round or 'no' to quit.")

# score allocation of the game 
while True:
    user = input("Enter your choice (rock, paper, scissor): ").lower()
    if user not in choose:
        print("Invalid choice. Please try again.")
        continue

    computer= random.choice(choose)
    print(f"Computer chose: {computer}")

    result = winner(user, computer)
    if result == "user":
        print("You win this round!")
        user_points += 1
    elif result == "computer":
        print("Computer wins this round!")
        computer_points += 1
    else:
        print("It's a tie!")

# display scores of players each level
    print(f"Scores - You: {user_points}, Computer: {computer_points}")

# next game instructions
    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again != "yes":
        break

# application-exit comment
print("Thanks for playing!.Come back soon")
