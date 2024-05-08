import os
import requests
from dotenv import load_dotenv


def nasa_APOD(api_key):
    params = {"api_key": api_key}
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    response.raise_for_status()

    return response.json()["url"]


def donload_image_APOUD_nasa(day_image, file_f):
    response = requests.get(day_image)
    response.raise_for_status()

    with open(f"image/ Astronomy Picture of the Day{file_f}", "wb") as file:
        file.write(response.content)


def format_file(day_image):
    image_f = os.path.splitext(day_image)

    return image_f[1]


if __name__ == "__main__":
    load_dotenv()
    os.makedirs("image", mode=0o777, exist_ok=True)

    api_key = os.environ["API_KEY"]
    day_image = nasa_APOD(api_key)
    file_f = format_file(day_image)
    donload_image_APOUD_nasa(day_image, file_f)
