# 🚀 PyChef

PyChef was made to easily convert basic ciphers in the terminal without having to leave the terminal to a web browser. I use CyberChef so much during CTFs that I wanted to replicate some of the more simple things in this tool. PyChef is lacking right now with only five available ciphers. However, I plan on continuing to add more.

## 📦 Installation

Clone the repo and it's ready to go:

```bash
git clone https://github.com/danielH625/PyChef.git
cd PyChef
```

## 🛠 Usage

Run the app; put encode or decode; cipher type, string in " " or the file name containing the (cipher/plain)text

Argument format:

python3 pychef.py [encode/decode] [cipher] [string/file]

```bash
python3 pychef.py encode rot13 "Hello World"
```

```bash
python3 pychef.py decode hex "68656c6c6f20776f726c64"
```

Or you can run it with ./ and with a file

```bash
./pychef.py decode hex cipher.txt
```

You can use either pthon3 or ./. You can use a file or a string.

The placement of encode/decode cipher and string/file are specific.

## ✨ Features

- No extra modules
- Simple arguments
- Fast
- Decode in the terminal

## 🧰 Tech Stack

- Python 3.14.4
- Argparse
- PathLib
- Time
- Codecs

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

## 🙌 Credits

Inspired by [CyberChef](https://cyberchef.org/)
