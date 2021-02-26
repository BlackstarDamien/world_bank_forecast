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

    result = data_src.fetch_data(example_country, example_time_series)
    expected = {
        'header': 'test_data',
        'x_values': [2020, 2019, 2018],
        'y_values': [1123, 2345, 556]
    }
    assert result == expected


def test_should_fetch_data_for_given_country(data_src):
    example_time_series = "TEST.TIME.SERIES"
    example_country = "CHN"

    result = data_src.fetch_data(example_country, example_time_series)
    expected = {
        'header': 'test_data',
        'x_values': [2020, 2019, 2018],
        'y_values': [122525, 464646, 35353]
    }
    assert result == expected
