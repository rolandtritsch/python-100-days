"""A passord generator (PWG)"""

import string
import random
import sys

import typing

_characters = string.ascii_letters + string.digits + string.punctuation


def generate_password(length: int) -> str:
    return "".join(random.choice(_characters) for _ in range(length))


def process_args(args: typing.List[str]) -> int:
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


def main() -> None:
    length = process_args(sys.argv)
    password = generate_password(length)
    print(f"Generated password: {password}")

    sys.exit(0)


if __name__ == "__main__":
    main()
