import os
import requests
import datetime
from dotenv import load_dotenv


def get_photo(id):
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{id}")
    response.raise_for_status()
    return response.json()["links"]["flickr"]["original"]


def fetch_spacex_last_launch(space_photo_links, filename_space):
    index = 0
    for photo in space_photo_links:
        index += 1
        response = requests.get(photo)
        response.raise_for_status()

        with open(f"image/{index}{filename_space}", "wb") as file:
            file.write(response.content)


def receving_nasa_APOD(api_key):
    params = {"api_key": api_key}
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    response.raise_for_status()

    return response.json()["url"]


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
        response.raise_for_status()

        image_list_EPIC.append(response_1.content)
    return image_list_EPIC


def EPIC_download(epic_image):
    index = 0
    for photo in epic_image:
        index += 1
        with open(f"image/{index} EPIC image.jpg", "wb") as file:
            file.write(photo)


def download_image_APOUD_nasa(day_image, file_format):
    response = requests.get(day_image)
    response.raise_for_status()

    with open(f"image/ Astronomy Picture of the Day{file_format}", "wb") as file:
        file.write(response.content)


def breaks_file(day_image):
    image_format = os.path.splitext(day_image)

    return image_format[1]


if __name__ == "__main__":
    load_dotenv()

    os.makedirs("image", mode=0o777, exist_ok=True)

    id = "5eb87d47ffd86e000604b38a"

    space_photo_links = get_photo(id)
    filename_space = "spacex.jpg"
    fetch_spacex_last_launch(space_photo_links, filename_space)

    api_key = os.environ["NASA_API_KEY"]
    day_image = receving_nasa_APOD(api_key)
    epic_image = nasa_EPIC(api_key)
    file_format = breaks_file(day_image)
    download_image_APOUD_nasa(day_image, file_format)
    EPIC_download(epic_image)
