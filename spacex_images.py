import os
import requests
from dotenv import load_dotenv


def check_file():
    if not os.path.exists("image"):
        os.makedirs("image")


def donload_image(filename, url):
    response = requests.get(url)
    response.raise_for_status()

    with open(f"image/{filename}", "wb") as file:
        file.write(response.content)


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


if __name__ == "__main__":
    load_dotenv()
    check_file()
    id = "5eb87d47ffd86e000604b38a"
    filename = "1.jpeg"
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    donload_image(filename, url)

    space_photo_links = get_photo(id)
    filename_space = "spacex.jpg"
    fetch_spacex_last_launch(space_photo_links, filename_space)

    api_key = os.environ["NASA_API_KEY"]
