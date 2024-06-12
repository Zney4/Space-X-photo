import os
import requests
import datetime
from dotenv import load_dotenv
from dowload_image_space import download_images_from_urls


def get_apod_photo_links(api_key):
    params = {"api_key": api_key, "count": 11}
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    response.raise_for_status()

    nasa_images = response.json()
    image_list = []
    for img in nasa_images:
        link = img["url"]
        image_list.append(link)

    return image_list


def get_nasa_EPIC(api_key):
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

        url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png"
        response.raise_for_status()

        image_list_EPIC.append(url)
    return image_list_EPIC


def get_photo(id):
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{id}")
    response.raise_for_status()
    return response.json()["links"]["flickr"]["original"]



if __name__ == "__main__":
    load_dotenv()

    api_key = os.environ["NASA_API_KEY"]
    apod_images = get_apod_photo_links(api_key)
    download_images_from_urls(urls=apod_images, file_name_prefix="APOD")

    epic_image = get_nasa_EPIC(api_key)
    download_images_from_urls(urls=epic_image, file_name_prefix="EPIC", api_key=api_key)

    id = "5eb87d47ffd86e000604b38a"
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    space_photo_links = get_photo(id)
    download_images_from_urls(urls=space_photo_links, file_name_prefix="space")

