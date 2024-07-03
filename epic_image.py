import os
import datetime
from dotenv import load_dotenv
from dowload_image_space import download_images_from_urls
from dowload_image_space import fetch_data


def get_nasa_epic(api_key):
    epic_photos = []
    for inform in fetch_data(
        "https://api.nasa.gov/EPIC/api/natural/images", {"api_key": api_key}
    ):
        image = inform["image"]
        date = datetime.datetime.strptime(inform["date"], "%Y-%m-%d %H:%M:%S").strftime(
            "%Y/%m/%d"
        )
        epic_photos.append(
            f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png"
        )

    return epic_photos


if __name__ == "__main__":
    load_dotenv()

    api_key = os.environ["NASA_API_KEY"]
    epic_image = get_nasa_EPIC(api_key)
    download_images_from_urls(urls=epic_image, file_name_prefix="EPIC", api_key=api_key)
