import os
import requests
from dotenv import load_dotenv


def nasa_APOD(api_key):
    params = {"api_key": api_key}
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    response.raise_for_status()

    return response.json()["url"]


def download_image_APOUD_nasa(day_image, image_format):
    response = requests.get(day_image)
    response.raise_for_status()

    with open(f"image/ Astronomy Picture of the Day{image_format}", "wb") as file:
        file.write(response.content)


def breaks_file(day_image):
    image_format = os.path.splitext(day_image)

    return image_format[1]


if __name__ == "__main__":
    load_dotenv()
    os.makedirs("image", mode=0o777, exist_ok=True)

    api_key = os.environ["NASA_API_KEY"]
    day_image = nasa_APOD(api_key)
    image_format = breaks_file(day_image)
    download_image_APOUD_nasa(day_image, image_format)
