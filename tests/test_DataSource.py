import pytest

from utils import DataSource
from .mocks import MockDataSource


@pytest.fixture()
def data_src():
    api_client = MockDataSource()
    data_src = DataSource(api_client)
    yield data_src


def test_should_fetch_data_for_given_time_series(data_src):
    example_time_series = "TEST.TIME.SERIES"
    example_country = "AFG"

    _, result = data_src.fetch_data(example_country, example_time_series)
    expected = [{'date': '2004', 'value': 249791940700},
                {'date': '2003', 'value': 221358563000},
                {'date': '2002', 'value': 182162721300},
                {'date': '2001', 'value': 1222756495400},
                {'date': '1997', 'value': 1222916881118.13},
                {'date': '1996', 'value': 221358563000}]
    assert result == expected


def test_should_fetch_data_for_given_country(data_src):
    example_time_series = "TEST.TIME.SERIES"
    example_country = "CHN"

    _, result = data_src.fetch_data(example_country, example_time_series)
    expected = [{'date': '1967', 'value': 75300003800},
                {'date': '1966', 'value': 62999998500},
                {'date': '1961', 'value': 24700000300},
                {'date': '1960', 'value': 24200001500}]

    assert result == expected


def test_should_fetch_proper_header(data_src):
    example_time_series = "TEST.TIME.SERIES"
    example_country = "CHN"

    header, _ = data_src.fetch_data(example_country, example_time_series)
    expected = 'test_data'

    assert header == expected
