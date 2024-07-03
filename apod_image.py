import os
from dotenv import load_dotenv
from dowload_image_space import fetch_data
from dowload_image_space import download_images_from_urls


def get_apod_photo_links(api_key):
    apod_count = 6
    apod_photos = [
        img["url"]
        for img in fetch_data(
            "https://api.nasa.gov/planetary/apod",
            {"api_key": api_key, "count": apod_count},
        )
    ]

    return apod_photos


if __name__ == "__main__":
    load_dotenv()

    api_key = os.environ["NASA_API_KEY"]
    apod_images = get_apod_photo_links(api_key)
    download_images_from_urls(urls=apod_images, file_name_prefix="APOD")
