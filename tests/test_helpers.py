from io import StringIO

import pytest

from campsight.helpers import *


def test_get_dates_from_input(monkeypatch, test_dates):
    target = StringIO(test_dates["start_str"])
    monkeypatch.setattr("sys.stdin", target)
    assert get_dates() == (test_dates["start_date"], test_dates["end_date"])
