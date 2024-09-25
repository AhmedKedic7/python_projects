import time
from datetime import datetime as dt
import os

#Enter a site to block
sites_to_block=[
    "www.facebook.com",
    "facebook.com",
    "www.youtube.com",
    "youtube.com",
]

Linux_host="/etc/hosts"
Windows_host = r"C:\Windows\System32\drivers\etc\hosts"

default_host=Linux_host

redirect ="127.0.0.1"

if os.name=='posix':
    default_host=Linux_host
elif os.name=='nt':
    default_host=Windows_host;
else:
    print("Unkown OS!")
    exit()

def block_websites(start_hour,end_hour):
    while True:
        try:
            if(
                    dt(dt.now().year, dt.now().month, dt.now().day, start_hour)
                    < dt.now()
                    < dt(dt.now().year, dt.now().month, dt.now().day, end_hour)
            ):
                print("Blocking.. ")
                with open(default_host, "r+") as hostfile:

                    hosts = hostfile.read()
                    for site in sites_to_block:
                        if site not in hosts:
                            hostfile.write(redirect + " " + site + "\n")
            else:
                with open(default_host, "r+") as hostfile:
                    hosts = hostfile.readlines()
                    hostfile.seek(0)
                    for host in hosts:
                        if not any(site in host for site in sites_to_block):
                            hostfile.write(host)
                    hostfile.truncate()
                print("Time is up!")
            time.sleep(3)
        except PermissionError as e:
            print(f"Caught a permission error: Try Running as Admin {e}")
            # handle the error here or exit the program gracefully
            break

if __name__ == "__main__":
    block_websites(0, 0)