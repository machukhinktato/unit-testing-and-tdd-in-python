from unittest.mock import MagicMock
import datetime

def addDays(thedate, days):
    return thedate.timedelta(days=days)

def test_addDaysImplementation(monkeypatch):
    # mock_delta = MagicMock(
    # return_value=datetime.timedelta(days=1)
    # monkeypatch(datetime.timedelta, mock_delta)
    # addDays(datetime.datetime(2020, 1, 1),1)
    # mock_delta.assert_called_once_with(days=1)
    result = addDays(datetime.datetime(2020, 1, 1),1)
    print(result.timdelta)
    assert result == datetime.datetime(2020, 1, 2)
