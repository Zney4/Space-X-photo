import os
import datetime
from dotenv import load_dotenv
from dowload_image_space import download_images_from_urls
from dowload_image_space import get_request


def get_nasa_epic(api_key):
    epic_photos = []
    params = {"api_key": api_key}
    for link in get_request("https://api.nasa.gov/EPIC/api/natural/images", params):
        image = link["image"]
        date = datetime.datetime.strptime(link["date"], "%Y-%m-%d %H:%M:%S").strftime(
            "%Y/%m/%d"
        )
        epic_photos.append(
            f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png"
        )

    return epic_photos


if __name__ == "__main__":
    load_dotenv()

    api_key = os.environ["NASA_API_KEY"]
    epic_image = get_nasa_epic(api_key)
    download_images_from_urls(urls=epic_image, file_name_prefix="EPIC", api_key=api_key)
