import datetime
from dateutil.parser import isoparse

#TODO write loggers for errors


def convert_datetime(raw_datetime: str):
    try:
        return isoparse(raw_datetime)
    except TypeError:
        return None


def convert_data(raw_date: str):
    try:
        return datetime.datetime.strptime(raw_date, "%Y-%m-%d")
    except TypeError:
        return None
