from pprint import pprint

from play_scraper import details

app_id = "com.android.chrome"

app_data = details(app_id, hl="pt-BR", gl="br")

pprint(app_data)
