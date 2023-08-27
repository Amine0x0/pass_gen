from pyfiglet import Figlet
import random
import string
import time

# Colors
yellow_color = '\033[33m'
reset_color = '\033[0m'

# Banner
custom_fig = Figlet(font='shadow')
ascii_text = custom_fig.renderText('Amine0x0')

print('\033[32m' + ascii_text + '\033[0m')

# funcs
try:
    user_input = int(input(yellow_color + "Enter your desired length: " + reset_color))
except ValueError:
    print("Error: Please enter a valid integer.")
    exit()

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def loading():
    print("Loading")
    time.sleep(1)
    print("generating ...")
    time.sleep(1)
    print("generating ...")
    time.sleep(1)
    print("generating ...")
    time.sleep(1)

# Generate
password = generate_random_password(user_input)

#loading()
print(yellow_color ,"Generated Password:" + reset_color, password)

