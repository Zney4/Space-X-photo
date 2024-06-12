import os
import requests
import datetime
from dotenv import load_dotenv
from dowload_image_space import download_images_from_urls


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


if __name__ == "__main__":
    load_dotenv()

    api_key = os.environ["NASA_API_KEY"]
    epic_image = get_nasa_EPIC(api_key)
    download_images_from_urls(urls=epic_image, file_name_prefix="EPIC", api_key=api_key)
