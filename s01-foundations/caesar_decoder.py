#!/usr/bin/env python3
import argparse
import string

def caesar_decode(text: str, shift: int) -> str:
    """Decode text by shifting letters backwards; preserve case and punctuation."""
    result = []
    for char in text:
        if char in string.ascii_lowercase:
            index = (ord(char) - ord("a") - shift) % 26
            result.append(chr(ord("a") + index))
        elif char in string.ascii_uppercase:
            index = (ord(char) - ord("A") - shift) % 26
            result.append(chr(ord("A") + index))
        else:
            result.append(char)

    return "".join(result)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Try all 25 non-zero Caesar cipher shifts."
    )
    parser.add_argument(
        "text",
        help='The shifted text, for example: "Khoor, Zruog!"'
    )
    args = parser.parse_args()

    print(f"Ciphertext: {args.text}")
    print("Possible decoded outputs:")

    for shift in range(1, 26):
        print(f"Shift {shift:2}: {caesar_decode(args.text, shift)}")


if __name__ == "__main__":
    main()
