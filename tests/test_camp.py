import datetime
import os

import pytest
import responses

from campsight.camp import *
from campsight.config import base_url


@pytest.mark.parametrize(
    "start_date, end_date, output",
    [
        (
            datetime.date(2020, 1, 1),
            datetime.date(2020, 1, 2),
            {
                "month": 1,
                "day": 1,
                "year": 2020,
                "emonth": 1,
                "eday": 2,
                "eyear": 2020,
                "find_pk": 1,
            },
        ),
        (
            datetime.date(2020, 1, 31),
            datetime.date(2020, 2, 1),
            {
                "month": 1,
                "day": 31,
                "year": 2020,
                "emonth": 2,
                "eday": 1,
                "eyear": 2020,
                "find_pk": 1,
            },
        ),
    ],
)
def test_build_params_from_dates(start_date, end_date, output):
    assert build_params(start_date, end_date) == output


# TODO: Learn to mock `requests` calls inside imported functions


# @responses.activate
# @pytest.mark.parametrize(
#     "params",
#     [
#         {
#             "month": 1,
#             "day": 31,
#             "year": 2020,
#             "emonth": 2,
#             "eday": 1,
#             "eyear": 2020,
#             "find_pk": 1,
#         }
#     ],
# )
# def test_request_with_params(params):
#     responses.add(responses.GET, 'http://test.com', status=200)
#     res = requests.get('http://test.com', params=params)
#     assert responses.calls[0].response.status_code == 200
