import requests
import os

IMAGE_URL = "https://play-lh.googleusercontent.com/_UoMr09v_yzBfhvO3hSR-mj6-qjEKfxsQ1YpCZGCkDysffnCNLKbxa4qOgIs84Vj2g=w720-h310-rw"


class ScreenshotDownloader:
    def __init__(self, path="./media/images/") -> None:
        self.path = path

        self.create_folder(self.path)

    def create_folder(self, folder_name: str) -> None:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

    def download(self, url: str):
        response = requests.get(url)
        with open(f"{self.path}sample_image.webp", "wb") as file:
            file.write(response.content)


if __name__ == "__main__":
    screenshot = ScreenshotDownloader()
    screenshot.download(IMAGE_URL)
