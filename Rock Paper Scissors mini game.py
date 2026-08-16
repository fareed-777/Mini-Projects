#rock, paper, scissors game
import random
count = 1
user_score = 0
comp_score = 0
round_num = 1
print("-" * 40)
print("WELCOME TO ROCK, PAPER, SCISSORS GAME!")
print("\033[1mTHIS IS 3 ROUNDS GAME!\033[0m")


while round_num <=3:
    print("-" * 40)
    user_input = input("Enter rock, paper, or scissors:").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer Selected : {computer_choice}")
    print(f"User Selected : {user_input}")

    if user_input == computer_choice:
        print(f"\033[93mBoth players selected {user_input} so its a tie!\033[0m")
        round_num += 1

    elif user_input == "rock":
        if computer_choice == "scissors":
            print("\033[92mUser Wins! Rock beats Scissors\033[0m")
            user_score += 1
            round_num += 1
        else: 
                print("\033[91mComputer Wins! Paper beats Rock\033[0m")
                comp_score += 1
                round_num += 1
    

    elif user_input == "paper":
        if computer_choice == "rock":
            print("\033[92mUser Wins! Paper beats Rock\033[0m")
            user_score += 1
            round_num += 1
        else:
                print("\033[91mComputer Wins! Scissors beats Paper\033[0m")
                comp_score += 1
                round_num += 1
    
    elif user_input == "scissors":
        if computer_choice == "paper":
            print("\033[92mUser Wins! Scissors beats Paper\033[0m")
            user_score += 1
            round_num += 1
        else:
            print("\033[91mComputer Wins! Rock beats Scissors\033[0m")
            comp_score += 1
            round_num += 1
    print(f"\033[93mScore - User: {user_score}, Computer: {comp_score}\033[0m")
    count += 1