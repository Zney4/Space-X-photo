import telegram
import os
import time
import random
from dotenv import load_dotenv


def photo_puclic(chat_id, time):
    while True:
        bot.send_document(
            chat_id=chat_id, document=open(f"image/{random.choice(path_image)}", "rb")
        )

        time.sleep(timer_public)


if __name__ == "__main__":
    load_dotenv()
    bot = telegram.Bot(token=os.environ["TELEGRAM_BOT_TOKEN"])
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    path_image = os.listdir("image/")
    timer_public = 14400
    random_photo = random.shuffle(path_image)
    photo_puclic(chat_id, time)
