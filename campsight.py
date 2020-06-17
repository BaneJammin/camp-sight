from requests_html import HTML, HTMLSession
import datetime as dt


def build_dates() -> list:
    now = dt.datetime.now()
    # Next-day reservations must be made before 3pm
    start = dt.date(now.year, now.month, now.day + 1 if now.hour >= 15 else 0)
    return [start + dt.timedelta(days=i) for i in range(7)]


def parse(html) -> list:
    available = []
    table = html.find("tbody", first=True)
    rows = table.find("tr")
    for r in rows:
        if r.find("a.success", first=True):
            available.append(r.find("td[data-title=Description]", first=True).text)
    return available


def main():
    url = "https://web1.vermontsystems.com/wbwsc/ohlakemetrowt.wsc/search.html"
    params = {"begindate": None, "Module": "RN", "display": "Listing"}
    session = HTMLSession()
    available = {}
    dates = build_dates()
    for d in dates:
        params["begindate"] = d.strftime("%m/%d/%Y")
        res = session.get(url, params=params)
        if res.status_code == 200:
            available[d] = parse(res.html)
    return available
