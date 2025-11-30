import random 

# Corrected spelling
options = ("rock", "paper", "scissors") 

running = True # Corrected variable name

while running:
    player = None
    computer = random.choice(options) # Corrected variable name

    while player not in options:
       # Added .lower() so "Rock" becomes "rock"
       player = input("Enter your choice (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win :)")
    elif player == "paper" and computer == "rock":
        print("You win :)")
    elif player == "scissors" and computer == "paper":
        print("You win :)")
    else:
        print("You lose :(")
        
    play_again = input("Play again? (y/n): ").lower()
    
    if play_again != "y":
        running = False

print("Thanks for playing!")
