#!/bin/python3

import argparse
import code
import pathlib
import time
import codecs

start_time = time.perf_counter()


def binary_encode(input):
    s = input.decode()
    b = "".join(format(ord(char), "08b") for char in s)
    return b


def binary_decode(input):
    s = "".join(chr(int(input[i : i + 8], 2)) for i in range(0, len(input), 8))
    return s


def hex_encode(input):
    h = codecs.encode(input, "hex")
    return h.decode()


def hex_decode(input):
    s = codecs.decode(input, "hex")
    return s.decode()


def base64_encode(input):
    b64 = codecs.encode(input, "base64")
    return b64.decode().strip()


def base64_decode(input):
    s = codecs.decode(input, "base64")
    return s.decode()


def rot13_encode(input):
    s = input.decode()
    r13 = codecs.encode(s, "rot13")
    return r13


def rot13_decode(input):
    r13 = input.decode()
    s = codecs.decode(r13, "rot13")
    return s


def decimal_encode(input):
    s = input.decode()
    dec = []
    for letter in s:
        dec.append(str(ord(letter)))
    return " ".join(dec)


def decimal_decode(input):
    s = input.decode()
    decimal = s.split()
    letters = []
    for num in decimal:
        letters.append(chr(int(num)))
    return "".join(letters)


ENCODERS = {
    "binary": {
        "encode": binary_encode,
        "decode": binary_decode,
    },
    "hex": {
        "encode": hex_encode,
        "decode": hex_decode,
    },
    "base64": {
        "encode": base64_encode,
        "decode": base64_decode,
    },
    "rot13": {
        "encode": rot13_encode,
        "decode": rot13_decode,
    },
    "decimal": {
        "encode": decimal_encode,
        "decode": decimal_decode,
    },
}


# -- if a file is used opens the file and returns as bytes --
def file_open(the_file):
    with pathlib.Path(the_file).open("rb") as fh:
        return fh.read()


# -- cli arguments --
def parse_args():
    p = argparse.ArgumentParser(
        prog="PyChef",
        description="CLI tool that encodes and decodes various ciphers (based on CyberChef)",
        epilog="Written by Daniel Herrera",
    )
    p.add_argument(
        "mode",
        choices=["encode", "decode"],
        help="Choose the mode you want to use (encode/decode).",
    )
    p.add_argument(
        "scheme",
        choices=ENCODERS.keys(),
        help="Choose the cipher you want to encode/decode with.",
    )
    p.add_argument(
        "input",
        help="Filename or String containing plaintext/cipher text to decode or encode.",
    )

    return p.parse_args()


def main():
    args = parse_args()

    try:
        if pathlib.Path.is_file(args.input):
            text = file_open(args.input).strip()
        else:
            text = args.input.encode()

        func = ENCODERS[args.scheme][args.mode]
        output = func(text)

        print("==========================================")
        print(f"\nOutput:\n-------\n{output}")

    except Exception as e:
        print(f"{str(e)} occured")

    else:
        end_time = time.perf_counter()
        print("")
        print("==========================================")
        print(f"Runtime: {end_time - start_time} seconds.")


if __name__ == "__main__":
    main()
