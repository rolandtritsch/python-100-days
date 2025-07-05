"""Caesar cipher encoder/decoder"""

import argparse
import logging
import os
import string
import sys
import typing

import structlog

structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.dev.ConsoleRenderer(),
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)
logging.basicConfig(level=os.environ.get("LOG_LEVEL", "info").upper())
logger = structlog.get_logger(__name__)

ALPHABET = (
    string.ascii_lowercase
    + string.ascii_uppercase
    + string.digits
    + string.punctuation
    + " "
)


def chr2idx(char: str) -> int:
    """Return the index of a character in the alphabet"""
    assert char in ALPHABET, f"Character '{char}' not in alphabet"
    return ALPHABET.index(char)


def idx2chr(i: int) -> str:
    """Return the character at the given index in the alphabet"""
    assert 0 <= i < len(ALPHABET), f"Index {i} out of alphabet range"
    return ALPHABET[i]


def shift(i: int, n: int) -> int:
    """Return the index of a character shifted by n positions in the alphabet"""
    return (i + n) % len(ALPHABET)


def encode(text: str, n: int) -> str:
    """Return the encoded text using Caesar cipher"""
    logger.info(f"Encoding text '{text}' with shift {n}")

    idxs = list(map(chr2idx, text))
    logger.debug(f"Character indices: {idxs}")

    shifts = list(map(lambda i: shift(i, n), idxs))
    logger.debug(f"Shifted indices: {shifts}")

    encoded = list(map(idx2chr, shifts))
    logger.debug(f"Encoded characters: {encoded}")

    return "".join(encoded)


def decode(text: str, n: int) -> str:
    """Return the decoded text using Caesar cipher"""
    return encode(text, -n)


def process_commandline() -> tuple[
    typing.Callable[[str, int], str], argparse.Namespace
]:
    """Return the action to take and the args to use"""

    parser = argparse.ArgumentParser(description="Caesar cipher encoder/decoder")
    parser.add_argument(
        "action",
        choices=["encode", "decode"],
        help="Action to perform: encode or decode",
    )
    parser.add_argument("text", help="Text to encode or decode")
    parser.add_argument("shift", type=int, help="Shift amount (positive integer)")

    args = parser.parse_args()

    if args.shift < 0:
        print("Shift must be a positive integer")
        sys.exit(1)

    action = None
    if args.action == "encode":
        action = encode
    elif args.action == "decode":
        action = decode
    else:
        print("Invalid action")
        sys.exit(1)

    return (action, args)


def main() -> None:
    (action, args) = process_commandline()

    text = action(args.text, args.shift)
    print(text)

    sys.exit(0)


if __name__ == "__main__":
    main()
