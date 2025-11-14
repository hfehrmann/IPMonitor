from typing import Optional

from urllib.parse import urlencode

import urllib.request
import json
import os

CWD = os.getcwd()
DATA_PATH = os.path.join(CWD, "data")
FILE_PATH = os.path.join(CWD, "data", "ip.txt")

def setup_data_dir():
    os.makedirs(DATA_PATH, exist_ok=True)

def get_ip() -> Optional[str]:
    response = urllib.request.urlopen("http://ip-api.com/json/")
    data = json.load(response)
    return data.get("query")

def get_stored_ip() -> Optional[str]:
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            return f.readline().strip()
    else:
        return None

def store_ip(ip):
    with open(FILE_PATH, "w") as f:
        f.write(f"{ip}\n")

def send_notif(new_ip: str):
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    group_id = os.environ["TELEGRAM_GROUP_CHAT_ID"]
    message = f"Here is your new IP: {new_ip}"
    params = {
        "chat_id": group_id,
        "text": message,
    }
    url = f"https://api.telegram.org/bot{token}/sendMessage?{urlencode(params)}"
    urllib.request.urlopen(url)


# Main
setup_data_dir()

ip = get_ip()
stored_ip = get_stored_ip()

if ip is None:
    # ntfy about problem add redis for failure logic checking.
    print("error hitting API")
    exit(1)

if stored_ip is None or ip != stored_ip:
    print("distinct")
    # ntfy
    store_ip(ip)
    send_notif(ip)
elif ip == stored_ip:
    print("same")


