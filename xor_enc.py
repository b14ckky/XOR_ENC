import os
import sys
import argparse
import random
from time import sleep

from colorama import Fore
from termcolor import colored

os.system("cls")

rainbow = ['red', 'green', 'green', 'blue', 'magenta', 'cyan']
r0 = random.randint(0, 5)
r1 = random.randint(0, 5)
r2 = random.randint(0, 5)
r3 = random.randint(0, 5)
r4 = random.randint(0, 5)

print(colored("\t┌────────────────────────┐", rainbow[r0]))
print(colored("\t│  ═╗ ╦╔═╗╦═╗  ╔═╗╔╗╔╔═╗ │", rainbow[r1]))
print(colored("\t│  ╔╩╦╝║ ║╠╦╝  ║╣ ║║║║   │", rainbow[r2]))
print(colored("\t│  ╩ ╚═╚═╝╩╚═  ╚═╝╝╚╝╚═╝ │", rainbow[r3]))
print(colored("\t└────────0xb14cky────────┘\n", rainbow[r4]))

key = 90  # Everything is Depends on this Key.


def encrypt(enc_text):
    result = b""
    for each_char in enc_text:
        tmp = ord(each_char) ^ key
        result += chr(tmp).encode()
        pass
    return result


def decrypt(dec_text):
    result = b""
    for each_char in dec_text:
        tmp = each_char ^ key
        result += chr(tmp).encode()
    pass
    return result


parser = argparse.ArgumentParser(
    description="Simple Encryption and Decryption Text ",
    formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=47)
)
parser.add_argument("-e", "--encrypt", help="Encrypt Plain Text", type=str)
parser.add_argument("-ef", "--encrypt_file", help="Encrypt File", type=str)
parser.add_argument("-d", "--decrypt", help="Decrypt Encrypted Text", type=str)
parser.add_argument("-o", "--output", help="Save The Output In a File", type=str)
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

elif args.encrypt:
    print(Fore.GREEN, "[+] Text Encrypting....", Fore.RESET)
    sleep(1)
    tmp = (encrypt(args.encrypt))
    print(Fore.GREEN, "[+] Text Encrypted Successfully....", Fore.RESET)
    print(Fore.GREEN, "[+] Encrypted Text Written on enc file....", Fore.RESET)
    with open("enc", "wb") as binary_file:
        binary_file.write(tmp)
    pass


elif args.decrypt:
    with open(args.decrypt, "rb") as binary_file:
        data = binary_file.read()
        print(Fore.GREEN, "[+] Text Decrypting....", Fore.RESET)
        sleep(1)
        print(Fore.GREEN, "[+] Decrypted Text -> ", Fore.RESET, Fore.RED, decrypt(data).decode(), Fore.RESET)
    pass

if args.encrypt_file:
    with open(args.encrypt_file, "r") as anc_file:
        data = anc_file.read()
        print(Fore.GREEN, "\n[+] File Encrypting....", Fore.RESET)
        sleep(1)
        tmp = (encrypt(data))
        print(Fore.GREEN, "[+] File Encrypted Successfully....", Fore.RESET)
        print(Fore.GREEN, "[+] Encrypted Text Written on enc file....", Fore.RESET)
        with open("enc", "wb") as binary_file:
            binary_file.write(tmp)
        pass
    pass

if args.output:
    print(Fore.GREEN, f"[+] Decrypted Data Written On {args.output} File Successfully !!", Fore.RESET)
    file = open(args.output, "w")
    data = decrypt(data).decode()
    file.write(data)
    file.close()
    pass
