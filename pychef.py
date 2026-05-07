import argparse
import pathlib


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

    return p.parse_args()


def file_open(the_file):
    with pathlib.Path(the_file).open("rb") as fh:
        return fh.read()


def main():
    args = parse_args()

    try:
        if pathlib.Path.is_file(args.input):
            text = file_open(args.input).strip()
        else:
            text = args.input

        print(text)

    except Exception as e:
        print(f"{str(e)} occured")

    else:
        print("Success without error.")


if __name__ == "__main__":
    main()
