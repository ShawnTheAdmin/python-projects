import random
import pyperclip
import time


def random_character():
    return chr(random.randint(33, 125))


def password_length():
    length = input("Specify password length: ")
    length = int(length)
    return length


def countdown(num):
    for i in range(num, 0, -1):
        print(f"Clearing clipboard in {i} seconds.")
        time.sleep(1)


def generate_password():

    password = []
    for i in range(0, password_length()):
        password.append(random_character())
    pyperclip.copy("".join(password))
    countdown(20)
    pyperclip.copy("")


generate_password()
