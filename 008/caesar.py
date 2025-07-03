import argparse
import string
import sys

ALPHABET = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + " "

def chr2idx(char: str) -> int:
    assert char in ALPHABET, f"Character '{char}' not in alphabet"
    return ALPHABET.index(char)

def idx2chr(i: int) -> str:
    assert 0 <= i < len(ALPHABET), f"Index {i} out of alphabet range"
    return ALPHABET[i]

def shift(i: int, n: int) -> int:
    return (i + n) % len(ALPHABET)

def encode(text: str, n: int) -> str:
    idxs = map(chr2idx, text)
    shifts = map(lambda i: shift(i, n), idxs)
    encoded = map(idx2chr, shifts)
    return "".join(encoded)

def decode(text: str, n: int) -> str:
    return encode(text, -n)

def main():
    parser = argparse.ArgumentParser(description='Caesar cipher encoder/decoder')
    parser.add_argument(
        'action', choices=['encode', 'decode'], help='Action to perform: encode or decode'
    )
    parser.add_argument('text', help='Text to encode or decode')
    parser.add_argument(
        'shift', type=int, help='Shift amount (positive integer)'
    )

    args = parser.parse_args()

    if args.shift < 0:
        print("Shift must be a positive integer")
        sys.exit(1)

    if args.action == "encode":
        print(encode(args.text, args.shift))
    elif args.action == "decode":
        print(decode(args.text, args.shift))
    else:
        print("Invalid action")

    sys.exit(0)

if __name__ == "__main__":
    main()
