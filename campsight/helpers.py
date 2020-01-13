import datetime


def get_dates():
    m = int(input("Month? "))
    d = int(input("Day? "))
    y = int(input("Year? "))
    n = int(input("Window? "))
    start_date = datetime.date(y, m, d)
    end_date = start_date + datetime.timedelta(days=n)
    return start_date, end_date


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
