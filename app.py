import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_player_choice():
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please try again.")

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def play_round():
    computer_choice = get_computer_choice()
    player_choice = get_player_choice()
    result = determine_winner(player_choice, computer_choice)
    
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {player_choice}")
    
    if result == "win":
        print("You win!")
    elif result == "lose":
        print("You lose!")
    else:
        print("It's a tie!")
    
    return result

def play_game():
    score = {"win": 0, "lose": 0, "tie": 0}
    
    while True:
        result = play_round()
        score[result] += 1
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    
    print("Final score:")
    print(f"Wins: {score['win']}")
    print(f"Losses: {score['lose']}")
    print(f"Ties: {score['tie']}")

if __name__ == "__main__":
    play_game()