import datetime

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


def find_available_sites(params):
    res = requests.get(base_url, params=params)
    soup = bs4.BeautifulSoup(res.text, features="html.parser")

    # available_sites = []
    # for i in soup.find_all("table"):
    #     rows = i.find_all("tr")
    #     name = rows[0].td.text[: rows[0].td.text.find(":")]
    #     status = rows[2].find_all("td")[1].text
    #     if status == " Reserve now":
    #         available_sites.append(name)
    # return available_sites
