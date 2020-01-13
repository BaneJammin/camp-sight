import datetime


def get_dates():
    m = int(input("Month? "))
    d = int(input("Day? "))
    y = int(input("Year? "))
    n = int(input("Window? "))
    start_date = datetime.date(y, m, d)
    end_date = start_date + datetime.timedelta(days=n)
    return start_date, end_date


# def cross_reference():
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
