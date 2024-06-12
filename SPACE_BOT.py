import telegram
import os
import time
import random
from dotenv import load_dotenv


def public_photo(chat_id, timer_public, image_in_path):
    while True:
        with open(f"image/{random.choice(image_in_path)}", "rb") as f:
            bot.send_photo(chat_id=chat_id, photo=f)
        time.sleep(timer_public)


if __name__ == "__main__":
    load_dotenv()
    bot = telegram.Bot(token=os.environ["TELEGRAM_BOT_TOKEN"])
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    image_in_path = os.listdir("image/")
    timer_public = 14400
    random.shuffle(image_in_path)
    public_photo(chat_id, timer_public, image_in_path)
