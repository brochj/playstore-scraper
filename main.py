from pprint import pprint

from play_scraper import details
from play_results.save_to_db import SaveToDB

app_identifier = "com.android.chrome"

app_data = details(app_identifier, hl="pt-BR", gl="br")

database = SaveToDB()
database.save_to_db(app_data)
