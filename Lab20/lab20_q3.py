secret_number = 69
attempts = 0

while True:
    guess=int(input("Guess the number (1-50): "))
    attempts += 1

    if guess == secret_number:
        print("Perfect")
        print(f"You got it in {attempts} attempt.")
        break
    elif guess > secret_number:
        print("Too high")
    else:
        print("Too low")

    if attempts == 7:
        print("OUT OF ATTEMPTS!")
        print(f"The secret number was {secret_number}")
        break