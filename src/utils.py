import os
import json
import asyncio
from datetime import datetime
from colorama import *

# Initialize color variables for stylish text
mrh = Fore.LIGHTRED_EX
pth = Fore.LIGHTWHITE_EX
hju = Fore.LIGHTGREEN_EX
kng = Fore.LIGHTYELLOW_EX
bru = Fore.LIGHTBLUE_EX
reset = Style.RESET_ALL
htm = Fore.LIGHTBLACK_EX

last_log_message = None

# Author information
def author_info():
    print(kng + "------------------------------------------")
    print(mrh + "Tools   : " + bru + "Goats Heck")
    print(bru + "Telegram: " + hju + "@cryptodiox")
    print(mrh + "Author  : " + hju + "gay")
    print(bru + "Version : " + hju + "6.9")
    print(kng + "------------------------------------------" + reset)

# Banner with stylish text
def _banner():
    banner = r"""
   _____  ____       _______ _____ 
  / ____|/ __ \   /\|__   __/ ____|
 | |  __| |  | | /  \  | | | (___  
 | | |_ | |  | |/ /\ \ | |  \___ \ 
 | |__| | |__| / ____ \| |  ____) |
  \_____|\____/_/    \_\_| |_____/    
    """
    print(Fore.GREEN + Style.BRIGHT + banner + reset)
    
    # Print the author information with colors
    author_info()
    
 
    log_line()

def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Read configuration file
def read_config():
    config_path = os.path.join(os.path.dirname(__file__), '../config.json')
    with open(config_path, 'r') as file:
        try:
            config_content = file.read()
            return json.loads(config_content)
        except json.JSONDecodeError as e:
            return {}

# Log function with stylish timestamps
def log(message, **kwargs):
    global last_log_message
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    flush = kwargs.pop('flush', False)
    end = kwargs.pop('end', '\n')
    if message != last_log_message:
        print(f"{htm}[{current_time}] {message}", flush=flush, end=end)
        last_log_message = message

# Function to print stylish lines
def log_line():
    print(pth + "~" * 60)

# Function to clear the console and display the banner
def awak():
    _clear()
    _banner()
    log_line()

# Countdown timer with a colorful display
async def countdown_timer(seconds):
    while seconds:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        h = str(h).zfill(2)
        m = str(m).zfill(2)
        s = str(s).zfill(2)
        print(f"{pth}Please wait until {h}:{m}:{s} ", flush=True, end="\r")
        seconds -= 1
        await asyncio.sleep(1)
    print(f"{pth}Please wait until {h}:{m}:{s} ", flush=True, end="\r")

# Format number with commas for readability
def _number(number):
    return "{:,.0f}".format(number)

# Example usage:
# awak()
# asyncio.run(countdown_timer(10))
