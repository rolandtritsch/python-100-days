"""
A morse code converter.

Usage:
    python morsecode.py <text>

Example:
    python morsecode.py "Hello, World!"
"""

import argparse
import sys

morsecode = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert text to Morse code")
    parser.add_argument("text", help="Text to convert")
    args = parser.parse_args()
    return args

def convert(text: str) -> str:
    morse = " ".join(map(lambda c: morsecode.get(c, ""), text.lower()))
    return morse

def main():
    args = parse_args()
    morse = convert(args.text)
    print(morse)

    sys.exit(0)

if __name__ == "__main__":
    main()
