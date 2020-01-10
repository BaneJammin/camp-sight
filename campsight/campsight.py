import bs4
import json
import requests
import datetime


def date_to_dict(dateform, prefix=""):
    return {
        f"{prefix}month": dateform.month,
        f"{prefix}day": dateform.day,
        f"{prefix}year": dateform.year,
    }


def dict_to_date(dictform):
    return datetime.date(dictform["year"], dictform["month"], dictform["day"])


def yield_params() -> dict:
    prompt = {"month": None, "day": None, "year": None, "window": None}
    for p in prompt:
        prompt[p] = int(input(f"{p.capitalize()}? "))
    for i in range(prompt["window"]):
        start_date = dict_to_date(prompt) + datetime.timedelta(days=i)
        end_date = start_date + datetime.timedelta(days=1)
        yield {
            **date_to_dict(start_date),
            **date_to_dict(end_date, prefix="e"),
            "find_pk": 1,
        }


def yield_websoup() -> tuple:
    for params in yield_params():
        res = requests.get(base_url, params=params)
        soup = bs4.BeautifulSoup(res.text, features="html.parser")
        yield params["month"], params["day"], params["year"], soup


def parse_soup() -> dict:
    result = {}
    for m, d, y, soup in yield_websoup():
        available_sites = []
        for i in soup.find_all("table"):
            rows = i.find_all("tr")
            name = rows[0].td.text[: rows[0].td.text.find(":")]
            status = rows[2].find_all("td")[1].text
            if status == " Reserve now":
                available_sites.append(name)
        result[f"{y}-{m}-{d}"] = available_sites
    for date in result:
        if not result[date]:
            result[date] = ["None available"]
    return result


def pull_forecast() -> dict:
    params = {"postal_code": postal_code, "country": "US", "units": "I", "key": api_key}
    res = requests.get(api_url, params=params)
    weather = json.loads(res.text)
    weather = {day["datetime"]: day for day in weather["data"]}
    return weather


def compare_dates():
    parks = parse_soup()
    weather = pull_forecast()
    for date in parks:
        if date in weather:
            print(
                f"\n{date}\n",
                f"Low: {weather[date]['app_min_temp']}\n",
                f"Chance of precip: {weather[date]['pop']}%\n",
                parks[date],
            )
