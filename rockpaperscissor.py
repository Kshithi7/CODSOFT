import random

choose=["rock","paper","scissor"]
user_points=0
computer_points=0

def winner(user,computer):
 if user==computer:
     return "tie"
 elif(user=="rock"and computer=="scissor") or \
     (user=="paper"and computer=="rock") or \
     (user=="scissor"and computer=="paper"):
     return "user"
 else:
     return "computer"

print("Welcome to Rock, Paper, Scissor game!")
print("Instructions: Enter 'rock', 'paper', or 'scissor' to play.")
print("The game will display your scores after each round.")
print("Type 'yes' to play another round or 'no' to quit.")

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

    print(f"Scores - You: {user_points}, Computer: {computer_points}")

    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!.Come back soon")
