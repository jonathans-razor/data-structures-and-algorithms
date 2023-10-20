import random
import string
import argparse

def generate_password(length=12, include_digits=True, include_special_chars=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("--length", type=int, default=12, help="Length of the password")
    parser.add_argument("--no-digits", action="store_false", dest="include_digits", help="Exclude digits")
    parser.add_argument("--no-special-chars", action="store_false", dest="include_special_chars", help="Exclude special characters")

    args = parser.parse_args()

    password = generate_password(args.length, args.include_digits, args.include_special_chars)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
