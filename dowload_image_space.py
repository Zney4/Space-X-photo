import os
import requests


def check_file_path():
    os.makedirs("images", exist_ok=True)


def get_request(url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def download_images_from_urls(urls, file_name_prefix, api_key=None):
    for index, url in enumerate(urls, start=1):
        params = {"api_key": api_key}
        response = requests.get(url, params=params)
        response.raise_for_status()
        photo = response.content
        ext = get_file_extension(url)

        with open(f"images/{file_name_prefix}{index}{ext}", "wb") as file:
            file.write(photo)
    print(f"{file_name_prefix} photo download")


def get_file_extension(photo):
    _, ext = os.path.splitext(photo)
    return ext
