#!/bin/python3

import argparse
import code
import pathlib
import time
import codecs

start_time = time.perf_counter()


# -- cli arguments --
def parse_args():
    p = argparse.ArgumentParser(
        prog="PyChef",
        description="CLI tool that encodes and decodes various ciphers (based on CyberChef)",
        epilog="Written by Daniel Herrera",
    )
    p.add_argument(
        "input",
        help="Filename or String containing the plaintext or cipher text you want to decode or encode.",
    )
    p.add_argument(
        "-d", "--decode", action="store_true", help="Decode: Decode the cipher text."
    )
    p.add_argument(
        "-e", "--encode", action="store_true", help="Encode: Encode the plain text."
    )
    p.add_argument(
        "-b", "--binary", action="store_true", help="Binary: Encode or Decode binary."
    )
    p.add_argument(
        "-b16", "--hex", action="store_true", help="Hex: Encode or decode hex."
    )
    p.add_argument(
        "-b64", "--base64", action="store_true", help="Base64: Encode or decode base64."
    )
    p.add_argument(
        "-r13", "--rot13", action="store_true", help="Rot13: Encode or decode Rot13."
    )

    return p.parse_args()


# -- if a file is used opens the file and returns as bytes --
def file_open(the_file):
    with pathlib.Path(the_file).open("rb") as fh:
        return fh.read()


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


def main():
    args = parse_args()

    try:
        if pathlib.Path.is_file(args.input):
            text = file_open(args.input).strip()
        else:
            text = args.input.encode()

        if args.encode:
            if args.binary:
                output = binary_encode(text)
            elif args.hex:
                output = hex_encode(text)
            elif args.base64:
                output = base64_encode(text)
            elif args.rot13:
                output = rot13_encode(text)
        elif args.decode:
            if args.binary:
                output = binary_decode(text)
            elif args.hex:
                output = hex_decode(text)
            elif args.base64:
                output = base64_decode(text)
            elif args.rot13:
                output = rot13_decode(text)
        else:
            print("NOPE")

        print("==========================================")
        print(f"\nOutput: {output}")

    except Exception as e:
        print(f"{str(e)} occured")

    else:
        end_time = time.perf_counter()
        print("")
        print("==========================================")
        print(f"Runtime: {end_time - start_time} seconds.")


if __name__ == "__main__":
    main()
