import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def game():
    l = {1: "Rock", 2: "Paper", 3: "Scissor"}

    print(Fore.MAGENTA + "Choose Game Mode:")
    print("1. Single Round")
    print("2. Best of 3")
    print("3. Best of 5")
    print("4. Endless Mode")
    mode = int(input("Enter your choice: "))

    # Set how many wins are needed
    if mode == 1:
        rounds_to_win = 1
    elif mode == 2:
        rounds_to_win = 2
    elif mode == 3:
        rounds_to_win = 3
    else:
        rounds_to_win = None  # endless mode

    user_score = 0
    computer_score = 0

    while True:
        user_choice = int(input(Fore.WHITE + "\nLet's Start (Choose One)\n1. Rock\n2. Paper\n3. Scissor\nChoose Number: "))
        computer_choice = random.randint(1, 3)

        print(Fore.CYAN + f"You chose: {l[user_choice]}")
        print(Fore.CYAN + f"Computer chose: {l[computer_choice]}")

        if user_choice == computer_choice:
            print(Fore.YELLOW + "It's a Draw!")
        else:
            if user_choice == 1 and computer_choice == 2:
                print(Fore.RED + "You Lose!")
                computer_score += 1
            elif user_choice == 1 and computer_choice == 3:
                print(Fore.GREEN + "You Win!")
                user_score += 1
            elif user_choice == 2 and computer_choice == 1:
                print(Fore.GREEN + "You Win!")
                user_score += 1
            elif user_choice == 2 and computer_choice == 3:
                print(Fore.RED + "You Lose!")
                computer_score += 1
            elif user_choice == 3 and computer_choice == 1:
                print(Fore.RED + "You Lose!")
                computer_score += 1
            elif user_choice == 3 and computer_choice == 2:
                print(Fore.GREEN + "You Win!")
                user_score += 1
            else:
                print(Fore.RED + "Something Went Wrong!!!!!!!!")

        print(Fore.CYAN + f"Scoreboard → You: {user_score} | Computer: {computer_score}")

        # Stop condition for best-of or single round
        if rounds_to_win:
            if user_score == rounds_to_win or computer_score == rounds_to_win:
                break
        else:
            # Endless mode → only stop when user says no
            again = input(Fore.MAGENTA + "Do you want to continue? (yes/no): ").lower()
            if again != "yes":
                break

    # Final Scoreboard
    print(Fore.MAGENTA + "\n----- FINAL SCOREBOARD -----")
    print(Fore.CYAN + f"You: {user_score}")
    print(Fore.CYAN + f"Computer: {computer_score}")

    if user_score > computer_score:
        print(Style.BRIGHT + Fore.GREEN + "You won the match!")
    elif user_score < computer_score:
        print(Style.BRIGHT + Fore.RED + "Computer won the match!")
    else:
        print(Style.BRIGHT + Fore.YELLOW + "It's a tie!")


# --- Main Menu ---
print(Fore.MAGENTA + "----WELCOME TO ROCK PAPER SCISSORS GAME----")
print("1. Play Game")
print("2. Exit")
choice = int(input("Enter your choice: "))

if choice == 1:
    game()
else:
    print(Fore.YELLOW + "Goodbye!")
