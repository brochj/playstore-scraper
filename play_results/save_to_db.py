from play_results.sqlite3_orm import SqliteORM
from play_results.models import (
    APPS_TABLE,
    CATEGORIES_TABLE,
    CONTENT_RATINGS_TABLE,
    DEVELOPERS_TABLE,
    HISTOGRAMS_TABLE,
    INTERACTIVE_ELEMENTS_TABLE,
    SCREENSHOTS_TABLE,
)


class SaveToDB:
    def __init__(self, filename: str = "apps.db") -> None:
        self.app_data = None
        self.filename = filename
        self.app_id = None

        self.sqlite = SqliteORM(self.filename)
        self._create_tables()

    def _create_tables(self) -> None:
        self.sqlite.connect()
        self.sqlite.create_table(APPS_TABLE)
        self.sqlite.create_table(CATEGORIES_TABLE)
        self.sqlite.create_table(CONTENT_RATINGS_TABLE)
        self.sqlite.create_table(DEVELOPERS_TABLE)
        self.sqlite.create_table(HISTOGRAMS_TABLE)
        self.sqlite.create_table(INTERACTIVE_ELEMENTS_TABLE)
        self.sqlite.create_table(SCREENSHOTS_TABLE)
        self.sqlite.try_to_commit_and_close()

    def save_to_db(self, app_data: dict) -> None:
        self.app_data = app_data
        self.sqlite.connect()

        if self.sqlite.checkAppExistance(self.app_data["app_id"]):
            raise ValueError("This app is already in the database")

        self._save_developer()
        self._save_app()
        self._save_categories()
        self._save_content_ratings()
        self._save_histogram()
        self._save_interactive_elements()
        self._save_screenshots()

        self.sqlite.try_to_commit_and_close()

    def _save_developer(self) -> None:
        developer_id = self.sqlite.insert_developer(self.app_data)
        self.app_data.update({"developer_id": developer_id})

    def _save_app(self) -> None:
        self.app_id = self.sqlite.insert_app(self.app_data)

    def _save_categories(self) -> None:
        for category in self.app_data.get("category"):
            data = {"category": category, "app_id": self.app_id}
            self.sqlite.insert_category(data)

    def _save_content_ratings(self) -> None:
        for content_rating in self.app_data.get("content_rating"):
            data = {"content_rating": content_rating, "app_id": self.app_id}
            self.sqlite.insert_content_rating(data)

    def _save_histogram(self) -> None:
        self.app_data["histogram"].update({"app_id": self.app_id})
        self.sqlite.insert_histogram(self.app_data["histogram"])

    def _save_interactive_elements(self) -> None:
        for interactive_element in self.app_data.get("interactive_elements"):
            data = {"interactive_element": interactive_element, "app_id": self.app_id}
            self.sqlite.insert_interactive_element(data)

    def _save_screenshots(self) -> None:
        for screenshot in self.app_data.get("screenshots"):
            data = {"screenshot": screenshot, "app_id": self.app_id}
            self.sqlite.insert_screenshot(data)
