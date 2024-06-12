import os
import requests
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


if __name__ == "__main__":
    load_dotenv()

    api_key = os.environ["NASA_API_KEY"]
    apod_images = get_apod_photo_links(api_key)
    download_images_from_urls(urls=apod_images, file_name_prefix="APOD")
