
import requests
from requests.auth import HTTPBasicAuth as BasicAuth
from requests.exceptions import ConnectionError, HTTPError
from requests.packages import urllib3
from termcolor import colored, cprint
from urllib3.exceptions import InsecureRequestWarning

# Disable SSL warnings. Not needed in production environments with valid certificates
# (REMOVE if you are not sure of its purpose)
urllib3.disable_warnings(category=InsecureRequestWarning)


def get_token(ENV): 

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    try:
        cprint(text="Generating auth token...", color="magenta")
        response = requests.post(
            url=f"{ENV['BASE_URL']}/dna/system/api/v1/auth/token",
            auth=BasicAuth(username=ENV["USERNAME"], password=ENV["PASSWORD"]),
            headers=headers,
            data=None
        )

        response.raise_for_status()
    except (ConnectionError, HTTPError) as e:
        raise SystemExit(colored(text=e, color="red"))
    except KeyboardInterrupt:
        raise SystemExit(
            colored(text="Process interrupted by the user", color="yellow")
        )
    else:
        cprint(text="Successful Token Generation.\n", color="green")
        return response.json()["Token"]
