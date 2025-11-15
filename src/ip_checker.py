from typing import Optional

from urllib.parse import urlencode

import urllib.request
import json
import os
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

CWD = os.getcwd()
FILE_PATH = os.path.join("/data", "ip.txt")

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
ip = get_ip()
stored_ip = get_stored_ip()

if ip is None:
    # ntfy about problem add redis for failure logic checking.
    logging.error("error hitting API")
    exit(1)

if stored_ip is None or ip != stored_ip:
    logging.info("distinct")
    # ntfy
    store_ip(ip)
    send_notif(ip)
elif ip == stored_ip:
    logging.info("same")


