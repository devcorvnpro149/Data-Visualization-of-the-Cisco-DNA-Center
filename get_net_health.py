import time
import requests
from requests.exceptions import ConnectionError, HTTPError
from requests.packages import urllib3
from termcolor import colored, cprint
from urllib3.exceptions import InsecureRequestWarning

# Disable SSL warnings. Not needed in production environments with valid certificates
# (REMOVE if you are not sure of its purpose)
urllib3.disable_warnings(category=InsecureRequestWarning)


def get_network_health(token, ENV):

    headers = {
        "X-Auth-Token": token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    epoch_time = int(time.time()) * 1000  # in milliseconds
    NETWORK_HEALTH_URL = f"dna/intent/api/v1/network-health?timestamp={epoch_time}"

    try:
        cprint(text="\nGetting network health...", color="magenta")
        response = requests.get(
            url=f"{ENV['BASE_URL']}/{NETWORK_HEALTH_URL}",
            headers=headers,
            data=None,
            
        )
        
        response.raise_for_status()
    except (ConnectionError, HTTPError) as e:
        raise SystemExit(colored(text=e, color="red"))
    except KeyboardInterrupt:
        raise SystemExit(
            colored(text="Process interrupted by the user", color="yellow")
        )
    else:
        cprint(text="The request was successful.\n", color="green")
        
        return response.json()["healthDistirubution"]
    
