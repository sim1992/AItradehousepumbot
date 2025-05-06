import os
import time
import telebot
from dotenv import load_dotenv
from utils import fetch_tokens, filter_tokens, track_token_growth

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
FREE_CHANNEL = os.getenv("FREE_CHANNEL_ID")
PREMIUM_CHANNEL = os.getenv("PREMIUM_CHANNEL_ID")

bot = telebot.TeleBot(BOT_TOKEN)

premium_users = set()  # Replace with real logic to manage premium users

def send_alert(token, message, premium=False):
    channel = PREMIUM_CHANNEL if premium else FREE_CHANNEL
    bot.send_message(channel, f"{token['name']} ({token['symbol']})\n{message}\nMarket Cap: ${token['market_cap']:,}\nVolume: ${token['volume']:,}\nLink: {token['url']}")

known_tokens = {}

while True:
    try:
        tokens = fetch_tokens()
        new_tokens, trending_tokens = filter_tokens(tokens, known_tokens)

        for token in new_tokens:
            known_tokens[token["address"]] = token
            send_alert(token, "New Chinese meme token detected!")

        for token in trending_tokens:
            send_alert(token, "Trending Chinese token showing strong momentum!", premium=True)

        growth_alerts = track_token_growth(known_tokens)
        for token, growth in growth_alerts:
            send_alert(token, f"Token has grown {growth}x since detection!", premium=True)

    except Exception as e:
        print("Error:", e)

    time.sleep(300)  # Wait 5 minutes before next check.  add bot.py
