import unittest

from play_results.sqlite3_orm import SqliteORM

DATABASE = "test_apps.db"
APP_ID = "com.pixelbite.rr3"


class Sqlite3ORMTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sqlite = SqliteORM(DATABASE)
        self.sqlite.connect()

    def tearDown(self) -> None:
        self.sqlite.close()

    def test_query_screenshots(self):
        screenshots = self.sqlite.query_screenshots(4)
        self.assertTrue(screenshots)
        self.assertIsInstance(screenshots, list)

    def test_insert_developer(self):
        dev_id = self.sqlite.insert_developer(
            {
                "developer": "fake_data",
                "developer_address": "fake_data",
                "developer_email": "fake_data",
                "developer_id": "fake_data",
                "developer_url": "fake_data",
            }
        )
        self.assertTrue(dev_id)
        self.sqlite.try_to_commit_and_close()

    def test_check_app_existance(self):
        app_exists = self.sqlite.check_app_existance(APP_ID)
        self.assertTrue(app_exists)

    def test_check_app_existance_passing_wrong_id(self):
        app_exists = self.sqlite.check_app_existance("This id does not exist")
        self.assertFalse(app_exists)


if __name__ == "__main__":
    sqlite = SqliteORM(DATABASE)
    print(sqlite.db_name)
