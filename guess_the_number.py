import random
secret_number = random.randint(1,100)
print("I'm thhinking of a number between 1 and 100. Can you guess it?")
while True:
    try:
        guess = int(input("Take a guess: "))
        if guess < secret_number:
            print("Too low. Try again!")
        elif guess > secret_number:
            print("Too high. Try again!")
        else:
            print(f"Congratulations! You guessed the number: {secret_number}")
            break
    except ValueError:
            print("Please enter a valid number.")
    
print(f"The secret number was {secret_number}. Thanks for playing!")