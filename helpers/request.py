import os
import sys
import requests

from . import console

def makeRequest() -> requests.Response:

    # GETTING URL
    url = os.getenv('BASE_URL')

    # USERNAME, PASSWORD
    username = os.getenv('E_USERNAME')
    password = os.getenv('E_PASSWORD')

    console.console_log("Sending request...", end="\r")

    # FOR ESCHOOL
    payload = {
        'USER_LOGIN': username,
        'USER_PASSWORD': password,
        'TYPE': 'AUTH',
        'AUTH_FORM': 'Y'
    }

    response = requests.request("POST", url, data=payload)

    if response.status_code != 200:
        print(f"Something went wrong! Status {response.status_code}")
        sys.exit(0)

    console.console_log("Logged in as: ", end="")
    console.console_log(username, len(password)*"*", color=console.Fore.GREEN)
    
    return response