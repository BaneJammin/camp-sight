import datetime
from io import StringIO

import pytest

from campsight.helpers import *

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

