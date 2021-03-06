import sqlite3
from sqlite3 import Connection, Cursor
from typing import Type


class SqliteORM:
    def __init__(self, db_name):
        self.db_name: str = db_name
        self.connection: Type[Connection] = None

    def connect(self) -> Type[Connection]:
        self.connection = sqlite3.connect(self.db_name)

    def close(self) -> None:
        self.connection.close()

    def rollback(self) -> None:
        self.connection.rollback()

    def try_to_commit_and_close(self):
        try:
            self.connection.commit()
        except:
            self.connection.rollback()
            self.connection.close()
            raise
        finally:
            self.connection.close()

    def create_table(self, table: str) -> None:
        cursor = self.connection.cursor()
        cursor.execute(table)

    def insert_developer(self, values: dict) -> int:
        cursor = self.connection.cursor()

        developer = values.get("developer")
        address = values.get("developer_address")
        email = values.get("developer_email")
        google_id = values.get("developer_id")
        url = values.get("developer_url")

        cursor.execute(
            "INSERT INTO developers VALUES (NULL, ?, ?, ?, ?, ?)",
            (
                developer,
                address,
                email,
                google_id,
                url,
            ),
        )
        return cursor.lastrowid

    def insert_app(self, values: dict) -> int:
        cursor = self.connection.cursor()

        app_id = values.get("app_id")
        contains_ads = values.get("contains_ads")
        current_version = values.get("current_version")
        description = values.get("description")
        description_html = values.get("description_html")
        editors_choice = values.get("editors_choice")
        free = values.get("free")
        iap = values.get("iap")
        iap_range = values.get("iap_range")
        icon = values.get("icon")
        installs = values.get("installs")
        price = values.get("price")
        recent_changes = values.get("recent_changes")
        required_android_version = values.get("required_android_version")
        reviews = values.get("reviews")
        score = values.get("score")
        size = values.get("size")
        title = values.get("title")
        updated = values.get("updated")
        url = values.get("url")
        video = values.get("video")
        developer_id = values.get("developer_id")

        cursor.execute(
            "INSERT INTO apps VALUES (NULL,  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                app_id,
                contains_ads,
                current_version,
                description,
                description_html,
                editors_choice,
                free,
                iap,
                iap_range,
                icon,
                installs,
                price,
                recent_changes,
                required_android_version,
                reviews,
                score,
                size,
                title,
                updated,
                url,
                video,
                developer_id,
            ),
        )
        return cursor.lastrowid

    def insert_category(self, values: dict) -> int:
        cursor = self.connection.cursor()

        category = values.get("category")
        app_id = values.get("app_id")

        cursor.execute(
            "INSERT INTO categories VALUES (NULL, ?, ?)",
            (
                category,
                app_id,
            ),
        )
        return cursor.lastrowid

    def insert_content_rating(self, values: dict) -> int:
        cursor = self.connection.cursor()

        content_rating = values.get("content_rating")
        app_id = values.get("app_id")

        cursor.execute(
            "INSERT INTO content_ratings VALUES (NULL, ?, ?)",
            (
                content_rating,
                app_id,
            ),
        )
        return cursor.lastrowid

    def insert_screenshot(self, values: dict) -> int:
        cursor = self.connection.cursor()

        screenshot = values.get("screenshot")
        filename = values.get("filename")
        app_id = values.get("app_id")

        cursor.execute(
            "INSERT INTO screenshots VALUES (NULL, ?, ?, ?)",
            (
                screenshot,
                filename,
                app_id,
            ),
        )
        return cursor.lastrowid

    def insert_interactive_element(self, values: dict) -> int:
        cursor = self.connection.cursor()

        interactive_element = values.get("interactive_element")
        app_id = values.get("app_id")

        cursor.execute(
            "INSERT INTO interactive_elements VALUES (NULL, ?, ?)",
            (
                interactive_element,
                app_id,
            ),
        )
        return cursor.lastrowid

    def insert_histogram(self, values: dict) -> int:
        cursor = self.connection.cursor()

        one_star = values.get(1)
        two_stars = values.get(2)
        three_stars = values.get(3)
        four_stars = values.get(4)
        five_stars = values.get(5)
        app_id = values.get("app_id")

        cursor.execute(
            "INSERT INTO histograms VALUES (NULL, ?, ?, ?, ?, ?, ?)",
            (
                one_star,
                two_stars,
                three_stars,
                four_stars,
                five_stars,
                app_id,
            ),
        )
        return cursor.lastrowid

    def query_app(self, app_id: str) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
            SELECT
                apps.id AS appid,
                apps.app_id,
                apps.contains_ads,
                apps.current_version,
                apps.description,
                apps.description_html,
                apps.editors_choice,
                apps.free,
                apps.iap,
                apps.iap_range,
                apps.icon,
                apps.installs,
                apps.price,
                apps.recent_changes,
                apps.required_android_version,
                apps.reviews,
                apps.score,
                apps.size,
                apps.title,
                apps.updated,
                apps.url,
                apps.video,

                developers.id AS developer_id,
                developers.developer,
                developers.address,
                developers.email,
                developers.google_id,
                developers.url AS dev_url

            FROM apps 
            INNER JOIN developers ON developers.id = apps.developer_id
            WHERE apps.app_id = '{app_id}'
            """
        )
        return cursor.fetchone()

    def query_categories(self, app_id: str) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
            SELECT category FROM categories WHERE app_id = {app_id} """
        )
        return cursor.fetchall()

    def query_screenshots(self, app_id: str) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT screenshot FROM screenshots WHERE app_id = {app_id}")
        return cursor.fetchall()

    def query_interactive_elements(self, app_id: str) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
            SELECT interactive_element FROM interactive_elements WHERE app_id = {app_id}
            """
        )
        return cursor.fetchall()

    def query_content_ratings(self, app_id: str) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
            SELECT content_rating FROM content_ratings WHERE app_id = {app_id}
            """
        )
        return cursor.fetchall()

    def query_histogram(self, app_id: str) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
            SELECT 
                one_star,
                two_stars,
                three_stars,
                four_stars,
                five_stars
            FROM histograms 
            WHERE app_id = {app_id}
            """
        )
        return cursor.fetchone()

    def check_app_existance(self, app_id: str) -> bool:
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT rowid, * FROM apps WHERE app_id =  '{app_id}'")
        return True if cursor.fetchone() else False


if __name__ == "__main__":
    sqlite = SqliteORM("apps.db")
    sqlite.connect()
    data = sqlite.query_app("com.paradyme.solarsmash")
    print(data)
    print(len(data))
