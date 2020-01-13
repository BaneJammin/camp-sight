import bs4
import requests

from .config import base_url
from .helpers import get_dates, build_params


def fetch_availability(params):
    res = requests.get(base_url, params=params)
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    return datetime.date(params["year"], params["month"], params["day"]), soup


# def parse_soup() -> dict:
#     result = {}
#     for m, d, y, soup in yield_websoup():
#         available_sites = []
#         for i in soup.find_all("table"):
#             rows = i.find_all("tr")
#             name = rows[0].td.text[: rows[0].td.text.find(":")]
#             status = rows[2].find_all("td")[1].text
#             if status == " Reserve now":
#                 available_sites.append(name)
#         result[f"{y}-{m}-{d}"] = available_sites
#     for date in result:
#         if not result[date]:
#             result[date] = ["None available"]
#     return result


# def pull_forecast() -> dict:
#     params = {"postal_code": postal_code, "country": "US", "units": "I", "key": api_key}
#     res = requests.get(api_url, params=params)
#     weather = json.loads(res.text)
#     weather = {day["datetime"]: day for day in weather["data"]}
#     return weather


# def compare_dates():
#     parks = parse_soup()
#     weather = pull_forecast()
#     for date in parks:
#         if date in weather:
#             print(
#                 f"\n{date}\n",
#                 f"Low: {weather[date]['app_min_temp']}\n",
#                 f"Chance of precip: {weather[date]['pop']}%\n",
#                 parks[date],
#             )
