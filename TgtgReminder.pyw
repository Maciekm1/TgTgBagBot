from tgtg import TgtgClient
import requests
import time
import schedule
from datetime import datetime

# Telegram
TOKEN = "YOUR_TOKEN"
chat_id = "YOUR_CHAT_ID"

# TgTg
credentials = {
    'access_token': 'YOUR_ACCESS_TOKEN',
    'refresh_token': 'YOUR_REFRESH_TOKEN',
    'user_id': 'YOUR_USER_ID'}

def func():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    
    client = TgtgClient(access_token=credentials["access_token"], refresh_token=credentials["refresh_token"],
                        user_id=credentials["user_id"])

    # Returns a list of your favourite Bags
    items = client.get_items()

    if items[0]["items_available"] > 0:
        message = f"[{current_time}] {items[0]['company_name']} Magic bag available, {items[0]['items_available']} left"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json())  # this sends the message

# Repeat the check every 5 minutes
schedule.every(5).minutes.do(func)

# Stops the program from exitting
while True:
    schedule.run_pending()
    time.sleep(1)
