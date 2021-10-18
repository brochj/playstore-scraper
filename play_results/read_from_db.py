from sqlite3_orm import SqliteORM


class ReadFromDB:
    def __init__(self, filename: str = "apps.db") -> None:
        self.filename = filename
        self.sqlite = SqliteORM(self.filename)

    def query_app(self, app_id: str) -> dict:
        self.sqlite.connect()
        data = self.sqlite.query_app(app_id)

        if data:
            data = self.format_app_data(data)

        categories = self.sqlite.query_categories(data["appid"])
        categories = self.format_list(categories)

        screenshots = self.sqlite.query_screenshots(data["appid"])
        screenshots = self.format_list(screenshots)

        i_elements = self.sqlite.query_interactive_elements(data["appid"])
        i_elements = self.format_list(i_elements)

        content_ratings = self.sqlite.query_content_ratings(data["appid"])
        content_ratings = self.format_list(content_ratings)

        histogram = self.sqlite.query_histogram(data["appid"])
        histogram = self.format_histogram(histogram)

        data.update(
            category=categories,
            screenshots=screenshots,
            interactive_elements=i_elements,
            content_rating=content_ratings,
            histogram=histogram,
        )

        self.sqlite.close()

        return data

    def format_app_data(self, data: tuple) -> dict:
        return {
            "appid": data[0],
            "app_id": data[1],
            "contains_ads": data[2],
            "current_version": data[3],
            "description": data[4],
            "description_html": data[5],
            "editors_choice": data[6],
            "free": data[7],
            "iap": data[8],
            "iap_range": data[9],
            "icon": data[10],
            "installs": data[11],
            "price": data[12],
            "recent_changes": data[13],
            "required_android_version": data[14],
            "reviews": data[15],
            "score": data[16],
            "size": data[17],
            "title": data[18],
            "updated": data[19],
            "url": data[20],
            "video": data[21],
            "developer_id": data[22],
            "developer": data[23],
            "developer_address": data[24],
            "developer_email": data[25],
            "developer_google_id": data[26],
            "developer_url": data[27],
        }

    def format_list(self, items: list[tuple]) -> list[str]:
        return [elem[0] for elem in items]

    def format_histogram(self, histogram: tuple) -> dict:
        return {
            "one_star": histogram[0],
            "two_stars": histogram[1],
            "three_stars": histogram[2],
            "four_stars": histogram[3],
            "five_stars": histogram[4],
        }


if __name__ == "__main__":
    from pprint import pprint

    database = ReadFromDB("apps.db")
    data = database.query_app("com.paradyme.solarsmash")
    pprint(data)
