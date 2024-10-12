import os
import urllib.parse
from colorama import Fore, Style

# Define ANSI escape codes for colors
RESET = "\033[0m"
GREEN = "\033[32m"
MAGENTA = "\033[35m"

# Color variables
kng = "\033[33m"
mrh = GREEN
hju = "\033[36m"
bru = "\033[34m"
reset = RESET

# Clear the terminal (cross-platform)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Colorful author info banner
def author_info():
    print(kng + "------------------------------------------")
    print(mrh + "Tools   : " + bru + "Goats Heck")
    print(bru + "Telegram: " + hju + "@cryptodiox")
    print(mrh + "Author  : " + hju + "gay")
    print(bru + "Version  : " + hju + "6.9")
    print(kng + "------------------------------------------" + reset)

# Stylish banner
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
    author_info()

# Function to extract and save query parameters in URL-encoded format
def extract_and_save_data(url):
    # Parse the URL to extract the query string
    parsed_url = urllib.parse.urlparse(url)
    
    # Get the fragment part from the URL (after the '#')
    fragment = parsed_url.fragment

    # Parse the fragment part into a dictionary
    fragment_params = urllib.parse.parse_qs(fragment)

    # Extract the 'tgWebAppData' parameter in its raw form
    tg_web_app_data = fragment_params.get('tgWebAppData', [None])[0]

    if tg_web_app_data:
        # Directly save the URL-encoded data to the file
        file_path = 'data.txt'
        with open(file_path, 'w') as file:
            file.write(tg_web_app_data)

        print(f"{GREEN}Data saved to {file_path}{RESET}")
        
        # Optionally, run the test.py script afterward
        os.system('python test.py')
    else:
        print(f"{MAGENTA}No tgWebAppData found in the URL.{RESET}")

# Main logic
clear_screen()
_banner()

# Input the URL
url = input(f"{MAGENTA}Enter Your Query Link: {RESET}")

# Extract and save data in URL-encoded format
extract_and_save_data(url)
