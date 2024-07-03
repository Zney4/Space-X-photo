import os
from dotenv import load_dotenv
from dowload_image_space import download_images_from_urls
from dowload_image_space import fetch_data


def get_photo(id):
    spacex_photos = []
    if id:
        spacex_photos = fetch_data(
            f"https://api.spacexdata.com/v5/launches/{id}", None
        )["links"]["flickr"]["original"]

    return spacex_photos


if __name__ == "__main__":
    load_dotenv()

    id = "5eb87d47ffd86e000604b38a"
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    space_photo_links = get_photo(id)

    api_key = os.environ["NASA_API_KEY"]
    download_images_from_urls(urls=space_photo_links, file_name_prefix="space")
