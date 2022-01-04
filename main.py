
# Import Modules
import platform
import time
from datetime import timedelta

from colorama import init

# Export modules
from export_device_list import export_device_list
from export_net_health import export_network_health

# Get modules
from get_token import get_token
from get_device_list import get_device_list
from get_net_health import get_network_health


# use Colorama to make Termcolor work on Windows too
init(autoreset=True)


# Enviroment Variables 
ENV = {
    "DOMAIN":"sandboxdnac2.cisco.com",
    "PORT":"443",
    "BASE_URL":"https://sandboxdnac2.cisco.com",
    "USERNAME":"devnetuser",
    "PASSWORD":"Cisco123!"
}


def main():
    # Start time
    start_time = time.perf_counter()

    print(f'\n\nRunning for {ENV["DOMAIN"]}\n')
    # Obtain the Cisco DNA Center Auth Token
    token = get_token(ENV=ENV)

    # Obtain devices on Cisco DNA Center
    device_list = get_device_list(token=token, ENV=ENV)
    #print(device_list)

    # Export devices to Excel sheet
    export_device_list(device_list=device_list, ENV=ENV)

    # Obtain network health
    network_health = get_network_health(token=token, ENV=ENV)
    #print(network_health)

    # Export matplotlib bar chart of network health
    export_network_health(network_health=network_health, ENV=ENV)

    # Print Elasped time
    end_time = time.perf_counter()
    delta = str(timedelta(seconds=end_time - start_time)).split(".")[0]
    print(f"\nFinishd in {delta}")


if __name__ == "__main__":
    main()
