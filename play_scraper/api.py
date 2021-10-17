# -*- coding: utf-8 -*-

"""
All the methods exposed by the library
"""

from typing import AnyStr, Union
from play_scraper.scraper import PlayScraper


def details(app_id: AnyStr, hl: AnyStr = "en", gl: AnyStr = "us"):
    """Sends a GET request to the app's info page, parses the app's details, and
    returns them as a dict.

    :param app_id: the app to retrieve details from, e.g. 'com.nintendo.zaaa'
    :param gl: Alpha-2 country code for switching geolocation
    :param hl: Play Store Locale
    :return: a dictionary of app details
    """
    s = PlayScraper(hl, gl)
    return s.details(app_id)


def collection(collection, category=None, hl="en", gl="us", **kwargs):
    """Sends a POST request to the collection url, gets each app's details, and
    returns them in a list.

    List of acceptable collections and categories can be found in settings.

    :param collection: the collection ID as a string.
    :param category: the category ID as a string.
    :param gl: Alpha-2 country code for switching geolocation
    :param hl: Play Store Locale
    :param results: the number of app results to retrieve
    :param page: the page number, calculates collection start index. is limited
        to page * results <= 500
    :param age: an age range to filter by (only for FAMILY categories)
    :param detailed: if True, sends request per app for full detail

    :return: a list of app dictionaries
    """
    s = PlayScraper(hl, gl)
    return s.collection(collection, category, **kwargs)


def developer(
    developer_id: Union[AnyStr, int], hl: AnyStr = "en", gl: AnyStr = "us", **kwargs
):
    """Sends a POST request to the developer's page, extracts their apps' basic
    info, and returns them in a list.

    :param developer_id: developer name to retrieve apps from, e.g. 'Disney'
    :param gl: Alpha-2 country code for switching geolocation
    :param hl: Play Store Locale
    :param results: the number of app results to retrieve
    :param page: the page number to retrieve
    :param detailed: if True, sends request per app for full detail
    :return: a list of app dictionaries
    """
    s = PlayScraper(hl, gl)
    return s.developer(developer_id, **kwargs)


def suggestions(query: AnyStr, hl: AnyStr = "en", gl: AnyStr = "us"):
    """Sends a GET request to the Play Store's suggestion API and returns up to
    five autocompleted suggested query strings in a list.

    :param query: the query string to get autocomplete suggestions
    :param gl: Alpha-2 country code for switching geolocation
    :param hl: Play Store Locale
    :return: a list of suggestion strings
    """
    s = PlayScraper(hl, gl)
    return s.suggestions(query)


def search(
    query: AnyStr,
    page: int = None,
    detailed: bool = False,
    hl: AnyStr = "en",
    gl: AnyStr = "us",
):
    """Sends a POST request and retrieves a list of applications matching
    the query term(s).

    :param query: search query term(s) to retrieve matching apps
    :param page: the page number to retrieve; max is 12
    :param detailed: if True, sends request per app for its full detail
    :param gl: Alpha-2 country code for switching geolocation
    :param hl: Play Store Locale
    :return: a list of apps matching search terms
    """
    s = PlayScraper(hl, gl)
    return s.search(query, page, detailed)


def similar(
    app_id: AnyStr, detailed: bool = False, hl: AnyStr = "en", gl: AnyStr = "us"
):
    """Sends a GET request, follows the redirect, and retrieves a list of
    applications similar to the specified app.

    :param app_id: the app to retrieve details from, e.g. 'com.nintendo.zaaa'
    :param detailed: if True, sends request per app for its full detail
    :param gl: Alpha-2 country code for switching geolocation
    :param hl: Play Store Locale
    :return: a list of similar apps
    """
    s = PlayScraper(hl, gl)
    return s.similar(app_id, detailed=detailed)


def categories(hl: AnyStr = "en", gl: AnyStr = "us", ignore_promotions: bool = True):
    """Sends a GET request to the front page (app store base url), parses and
    returns a list of all available categories.

    Note: May contain some promotions, e.g. "Popular Characters"
    """
    s = PlayScraper(hl, gl)
    return s.categories(ignore_promotions)
