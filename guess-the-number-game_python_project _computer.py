import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("Welcome to Guess the Number Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it.")
    
    while attempts < max_attempts:
        try:
            # Get player's guess
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            # Check if the guess is correct
            if guess == secret_number:
                print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
                return
            
            # Provide hints
            if guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
            
            # Show remaining attempts
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print(f"You have {remaining_attempts} attempts remaining.")
            
        except ValueError:
            print("Please enter a valid number!")
    
    # If all attempts are used
    print(f"\nGame Over! The number was {secret_number}.")
    print(f"You used all {max_attempts} attempts.")

if __name__ == "__main__":
    while True:
        guess_the_number()
        
        # Ask if player wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break
