import pytest
from campsight.campsight import date_to_dict, dict_to_date, prompt, yield_params
import datetime
from io import StringIO


@pytest.fixture
def dateform():
    return datetime.datetime.today()


@pytest.fixture
def dictform():
    return {"month": 1, "day": 1, "year": 2020}


def test_datetime_to_dict_conversion(dateform):
    target = date_to_dict(dateform)
    assert target == {
        "month": dateform.month,
        "day": dateform.day,
        "year": dateform.year,
    }


def test_dict_to_datetime_conversion(dictform):
    target = dict_to_date(dictform)
    assert target == datetime.date(dictform["year"], dictform["month"], dictform["day"])


def test_prompt_for_date(monkeypatch):
    test_inputs = StringIO("1\n1\n2020\n1\n")
    monkeypatch.setattr("sys.stdin", test_inputs)
    assert prompt() == {"month": 1, "day": 1, "year": 2020, "window": 1}
