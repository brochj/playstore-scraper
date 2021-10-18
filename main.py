import random
import sys
import time

from w3lib.url import url_query_parameter

from play_results.save_to_db import SaveToDB
from play_scraper import details


def random_delay(start=1, end=3):
    secs = random.randint(start, end)
    time.sleep(secs)


def get_id_from_url(url: str) -> str:
    return url_query_parameter(url, "id")


def scrape(url: str) -> dict:
    app_id = get_id_from_url(url)
    app_data = details(app_id, hl="pt-BR", gl="br")
    return app_data


def save_data(app_data: dict) -> None:
    database = SaveToDB()
    database.save_to_db(app_data)


def scrape_url(url: str) -> dict:
    try:
        app_data = scrape(url)
        save_data(app_data)
        save_url_to_txt(url, "urls")
    except ValueError as e:
        print(e)


def read_url_list(filename: str) -> list:
    with open(f"{filename}.txt", "r") as file:
        return [line.rstrip() for line in file]


def save_url_to_txt(value, filename: str) -> None:
    with open(filename + ".txt", "a", encoding="utf-8") as file:
        file.write(str(value) + "\n")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].startswith("https"):
        url = sys.argv[1]
        scrape_url(url)

    elif len(sys.argv) > 1 and sys.argv[1] == "-l":
        urls = read_url_list("urls")

        for url in urls:
            random_delay()
            try:
                print(f"scraping: {get_id_from_url(url)}")
                app_data = scrape(url)
                save_data(app_data)
            except ValueError as e:
                print(e)
                continue

    elif len(sys.argv) > 1 and sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("python main.py <app-url> : command for scrape an url")
        print("python main.py -l        : command for scrape urls.txt file")
