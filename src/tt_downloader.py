import os
import requests
import bs4
from files_handler import get_videos_folder_path


def download_twitter_video(url: str, file_name: str):
    api_url = f"https://twitsave.com/info?url={url}"
    response = requests.get(api_url)
    data = bs4.BeautifulSoup(response.text, "html.parser")
    download_button = data.find_all("div", class_="origin-top-right")[0]
    quality_buttons = download_button.find_all("a")
    highest_quality_url = quality_buttons[0].get("href")

    response = requests.get(highest_quality_url, stream=True)

    download_path = os.path.join(get_videos_folder_path(), f'{file_name}.mp4')

    with open(download_path, "wb") as file:
        for data in response.iter_content(chunk_size=1024):
            file.write(data)

    print("Video downloaded successfully!")
