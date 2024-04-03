import telegram
import os
import time
import random
from dotenv import load_dotenv


def photo_puclic(chat_id, time):
    while True:
        bot.send_document(
            chat_id=chat_id, document=open(f"image/{random.choice(directory)}", "rb")
        )

        time.sleep(timer_public)


if __name__ == "__main__":
    load_dotenv()
    bot = telegram.Bot(token=os.environ["BOT_TOKEN"])
    chat_id = os.environ["CHAT_ID"]
    directory = os.listdir("image/")
    print(directory)
    timer_public = 5
    random_photo = random.shuffle(directory)
    print(random_photo)
    print(directory)
    photo_puclic(chat_id, time)
