import pytest

from campsight.camp import *
from campsight.config import base_url


def test_build_params_from_dates(test_dates):
    assert (
        build_params(test_dates["start_date"], test_dates["end_date"])
        == test_dates["window_dict"]
    )


# TODO: Mock request for fetch_availability()
def test_requests():
    pass


def test_parse_response_for_open_sites(test_html):
    assert parse_response(test_html) == [
        "Girdled Road Reservation",
        "River Road Park - Area",
    ]

