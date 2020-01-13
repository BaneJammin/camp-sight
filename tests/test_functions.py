import datetime
from io import StringIO
import requests

import pytest

from campsight.campsight import *
from campsight.config import *

# TODO: Develop test cases
@pytest.mark.parametrize(
    "inputs, outputs",
    [
        ("1\n1\n2020\n1\n", (datetime.date(2020, 1, 1), datetime.date(2020, 1, 2))),
        ("1\n31\n2020\n1\n", (datetime.date(2020, 1, 31), datetime.date(2020, 2, 1))),
    ],
)
def test_get_dates_from_input(monkeypatch, inputs, outputs):
    target = StringIO(inputs)
    monkeypatch.setattr("sys.stdin", target)
    assert get_dates() == outputs


def test_build_params_from_dates():
    pass


# TODO: Learn how to mock `requests.get()` calls with `params`
@pytest.mark.parametrize(
    "start_date, end_date, output",
    [
        (
            datetime.date(2020, 1, 1),
            datetime.date(2020, 1, 2),
            {
                "month": 1,
                "day": 2,
                "year": 2020,
                "emonth": 1,
                "eday": 2,
                "eyear": 2020,
                "find_pk": 1,
            },
        ),
        (
            datetime.date(2020, 1, 5),
            datetime.date(2020, 1, 6),
            {
                "month": 1,
                "day": 2,
                "year": 2020,
                "emonth": 1,
                "eday": 2,
                "eyear": 2020,
                "find_pk": 1,
            },
        ),
    ],
)
def test_build_params_from_dates(start_date, end_date, output):
    assert build_params(start_date, end_date) == output
