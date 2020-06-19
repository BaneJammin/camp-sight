import datetime as dt
import json

from freezegun import freeze_time
import pytest
from requests_html import HTML, HTMLSession

import campsight


@freeze_time("2020-06-01 11:00:00")
def test_build_dates_before3pm():
    assert campsight.build_dates() == [
        dt.datetime(2020, 6, 2, 11, 0),
        dt.datetime(2020, 6, 3, 11, 0),
        dt.datetime(2020, 6, 4, 11, 0),
        dt.datetime(2020, 6, 5, 11, 0),
        dt.datetime(2020, 6, 6, 11, 0),
        dt.datetime(2020, 6, 7, 11, 0),
        dt.datetime(2020, 6, 8, 11, 0),
    ]


@freeze_time("2020-06-01 16:00:00")
def test_build_dates_after3pm():
    assert campsight.build_dates() == [
        dt.datetime(2020, 6, 3, 16, 0),
        dt.datetime(2020, 6, 4, 16, 0),
        dt.datetime(2020, 6, 5, 16, 0),
        dt.datetime(2020, 6, 6, 16, 0),
        dt.datetime(2020, 6, 7, 16, 0),
        dt.datetime(2020, 6, 8, 16, 0),
        dt.datetime(2020, 6, 9, 16, 0),
    ]


def test_fetch_campsite_response(monkeypatch):
    class MockCampResponse:
        def __init__(self, query_date):
            self.status_code = 200
            self.url = f"https://web1.vermontsystems.com/wbwsc/ohlakemetrowt.wsc/search.html?begindate={query_date}&Module=RN&display=Listing"

    def mock_get(*args, **kwargs):
        return MockCampResponse(kwargs["params"]["begindate"])

    monkeypatch.setattr(HTMLSession, "get", mock_get)
    res = campsight.fetch_campsite_response(dt.date(2020, 7, 1))
    assert (
        res.url
        == "https://web1.vermontsystems.com/wbwsc/ohlakemetrowt.wsc/search.html?begindate=07/01/2020&Module=RN&display=Listing"
    )


@pytest.fixture
def camp_response():
    with open("test_camp_response.html") as file:
        return HTML(html=file.read())


def test_parse_campsite_response(camp_response):
    assert campsight.parse_campsite_response(camp_response) == [
        "Tent Camping Hell Hollow",
        "Tent Camping River Road Park",
    ]


# @pytest.fixture
# def weather_response():
#     with open("test_weather_response.json") as file:
#         return json.load(file)
