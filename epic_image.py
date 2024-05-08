import os
import requests
import datetime
from dotenv import load_dotenv


def nasa_EPIC(api_key):
    params = {"api_key": api_key}
    response = requests.get(
        f"https://api.nasa.gov/EPIC/api/natural/images", params=params
    )
    response.raise_for_status()

    image_list_EPIC = []
    for inform in response.json():
        image = inform["image"]
        date = inform["date"]
        date.split("/", maxsplit=1)

        date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        date = date.strftime("%Y/%m/%d")

        params_1 = {"api_key": api_key}
        response_1 = requests.get(
            f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png",
            params=params_1,
        )
        #                           https://api.nasa.gov/EPIC/archive/natural/03/12/2024/png/epic_1b_20240312003633?api_key=YNmiFmsTDFcAUcpYLZZsQar45WnXER1VnQ9hKFE0
        response.raise_for_status()

        image_list_EPIC.append(response_1.content)
    return image_list_EPIC


def EPIC_download(epic_image):
    index = 0
    for photo in epic_image:
        index += 1
        #        response = requests.get(photo)
        #        response.raise_for_status()

        with open(f"image/{index} EPIC image.jpg", "wb") as file:
            file.write(photo)


if __name__ == "__main__":
    load_dotenv()
    os.makedirs("image", mode=0o777, exist_ok=True)

    api_key = os.environ["NASA_API_KEY"]
    epic_image = nasa_EPIC(api_key)
    EPIC_download(epic_image)
