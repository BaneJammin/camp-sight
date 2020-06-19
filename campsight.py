import datetime as dt
import os

from requests_html import HTML, HTMLSession


def build_dates() -> list:
    num_days = 7
    now = dt.datetime.now()
    adjust = 1 if now.hour >= 15 else 0  # Next-day reservations must be made before 3pm
    start = now + dt.timedelta(days=adjust)
    return [start + dt.timedelta(days=i + 1) for i in range(num_days)]


def fetch_campsite_response(query_date):
    session = HTMLSession()
    url = "https://web1.vermontsystems.com/wbwsc/ohlakemetrowt.wsc/search.html"
    params = {"begindate": query_date.strftime("%m/%d/%Y"), "Module": "RN", "display": "Listing"}
    res = session.get(url, params=params)
    return res


def parse_campsite_response(html) -> list:
    available = []
    table = html.find("tbody", first=True)
    rows = table.find("tr")
    for r in rows:
        if r.find("a.success", first=True):
            available.append(r.find("td[data-title=Description]", first=True).text)
    return available


# def get_weather_json():
#     session = HTMLSession()
#     key = os.environ.get("WEATHERBIT_TOKEN")
#     if not key:
#         raise ValueError("Environment variable 'WEATHERBIT_TOKEN' not found")
#     url = "https://api.weatherbit.io/v2.0/forecast/daily"
#     params = {"key": key, "postal_code": "44077"}
#     res = session.get(url, params=params)
#     return res.json()
