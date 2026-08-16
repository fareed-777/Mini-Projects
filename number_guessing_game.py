import random
secret_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I have selected a secret number between 1 and 100.")
print("Try to guess the number in as few attempts as possible.")


guess_correct = False

while not guess_correct:

    user_input = input("Enter your guess (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Thank you for playing! Goodbye!")
        guess_correct = True
    else:
        user_guess = int(user_input)
        if user_guess < secret_number:
            print("Your guess is too low. Try again.")
        elif user_guess > secret_number:
            print("Your guess is too high. Try again.")
        elif user_guess == secret_number:
            print("Congratulations! You've guessed the secret number!")
            guess_correct = True














        # user_guess < secret_number:
    #     print("Your guess is too low. Try again.")
    # elif user_guess > secret_number:
    #     print("Your guess is too high. Try again.")
    # elif user_guess == secret_number:
    #     print("Congratulations! You've guessed the secret number!")
    #     guess_correct = True
    # elif user_guess == 'exit':
    #     print("Thank you for playing! Goodbye!")
    #     guess_correct = True
    # guess_correct = True


