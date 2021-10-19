DEVELOPERS_TABLE = """CREATE TABLE IF NOT EXISTS developers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        developer TEXT,
        address TEXT,
        email TEXT,
        google_id TEXT,
        url TEXT
    )
"""

APPS_TABLE = """CREATE TABLE IF NOT EXISTS apps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        app_id TEXT,
        contains_ads TEXT,
        current_version TEXT,
        description TEXT,
        description_html TEXT,
        editors_choice INTEGER,
        free INTEGER,
        iap TEXT,
        iap_range TEXT,
        icon TEXT,
        installs TEXT,
        price TEXT,
        recent_changes TEXT,
        required_android_version TEXT,
        reviews INTEGER,
        score REAL,
        size TEXT,
        title TEXT,
        updated TEXT,
        url TEXT,
        video TEXT,
        developer_id INTEGER,
        FOREIGN KEY (developer_id) REFERENCES developers (id)
    )
"""

CATEGORIES_TABLE = """CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        app_id INTEGER,
        FOREIGN KEY (app_id) REFERENCES apps (id)
    )
"""

CONTENT_RATINGS_TABLE = """CREATE TABLE IF NOT EXISTS content_ratings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content_rating TEXT,
        app_id INTEGER,
        FOREIGN KEY (app_id) REFERENCES apps (id)
    )
"""

SCREENSHOTS_TABLE = """CREATE TABLE IF NOT EXISTS screenshots (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        screenshot TEXT,
        filename TEXT,
        app_id INTEGER,
        FOREIGN KEY (app_id) REFERENCES apps (id)
    )
"""

INTERACTIVE_ELEMENTS_TABLE = """CREATE TABLE IF NOT EXISTS interactive_elements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        interactive_element TEXT,
        app_id INTEGER,
        FOREIGN KEY (app_id) REFERENCES apps (id)
    )
"""

HISTOGRAMS_TABLE = """CREATE TABLE IF NOT EXISTS histograms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        one_star TEXT,
        two_stars TEXT,
        three_stars TEXT,
        four_stars TEXT,
        five_stars TEXT,
        app_id INTEGER,
        FOREIGN KEY (app_id) REFERENCES apps (id)
    )
"""
