from dowload_image_space import download_images_from_urls
from dowload_image_space import get_request


def get_photos(id):
    spacex_photos = get_request(f"https://api.spacexdata.com/v5/launches/{id}", None)["links"]["flickr"]["original"]

    return spacex_photos


if __name__ == "__main__":
    id = "5eb87d47ffd86e000604b38a"
    space_photo_links = get_photos(id)
    download_images_from_urls(urls=space_photo_links, file_name_prefix="space")
