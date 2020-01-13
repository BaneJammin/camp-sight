import bs4
import requests

from campsight.config import base_url


def build_params(start_date, end_date):
    return {
        "month": start_date.month,
        "day": start_date.day,
        "year": start_date.year,
        "emonth": end_date.month,
        "eday": end_date.day,
        "eyear": end_date.year,
        "find_pk": 1,
    }


def fetch_availability(params):
    # TODO: see test_camp.py
    res = requests.get(base_url, params=params)
    return res


def parse_response(response, features="html.parser"):
    if isinstance(response, requests.Response):
        soup = bs4.BeautifulSoup(response.text, features=features)
    elif isinstance(response, str):
        soup = bs4.BeautifulSoup(response, features=features)
    available_sites = []
    for i in soup.find_all("table"):
        rows = i.find_all("tr")
        name = rows[0].td.text[: rows[0].td.text.find(":")]
        status = rows[2].find_all("td")[1].text
        if status == " Reserve now":
            available_sites.append(name)
    return available_sites

