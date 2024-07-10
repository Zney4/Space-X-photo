from dowload_image_space import download_images_from_urls
from dowload_image_space import get_request


if __name__ == "__main__":
    id = "5eb87d47ffd86e000604b38a"
    spacex_photos = get_request(f"https://api.spacexdata.com/v5/launches/{id}", None)["links"]["flickr"]["original"]
    download_images_from_urls(urls=spacex_photos, file_name_prefix="space")
