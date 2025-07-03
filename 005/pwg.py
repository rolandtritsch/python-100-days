""" A passord generator (PWG)."""

import string
import random
import sys

_characters = string.ascii_letters + string.digits + string.punctuation

def generate_password(length):
    return ''.join(random.choice(_characters) for _ in range(length))

def process_args(args):
    if len(args) != 2:
        print("Usage: python pwg.py <length>")
        sys.exit(1)

    try:
        length = int(sys.argv[1])
        if length <= 0:
            print("Password length must be a positive integer!")
            sys.exit(1)
    except ValueError:
        print("Please provide a valid integer!")
        sys.exit(1)

    return length

def main():
    length = process_args(sys.argv)
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
