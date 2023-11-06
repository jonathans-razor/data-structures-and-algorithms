import random

def generate_telephone_number():
    area_code = random.randint(100, 999)
    exchange_code = random.randint(100, 999)
    subscriber_number = random.randint(1000, 9999)
    return f"({area_code}) {exchange_code}-{subscriber_number}"

def main():
    target_number = generate_telephone_number()
    print("Welcome to the Telephone Number Guessing Game!")
    print("Try to guess the randomly generated telephone number.")
    print(f"Hint: It looks like this: {target_number}")

    jennys_number = "(900) 867-5309"
    attempts = 0
    while True:
        guess = input("Enter your guess (in the format XXX-XXX-XXXX): ")
        attempts += 1

        if guess == jennys_number:
            print(f"Congratulations! You guessed the number {jennys_number} in {attempts} attempts.")
            break
        elif guess.lower() == "i give up":
            print(f"The correct number was {jennys_number}. Better luck next time!")
            break
        else:
            print("Incorrect guess. Try again!")

if __name__ == "__main__":
    main()
