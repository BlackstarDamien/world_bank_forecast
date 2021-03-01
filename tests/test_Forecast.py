import pytest
import pandas as pd

from utils import Forecast, DataSourceDF

test_data = [{'date': '2020', 'value': 249791940700},
             {'date': '2019', 'value': 221358563000},
             {'date': '2018', 'value': 182162721300},
             {'date': '2017', 'value': 1222756495400}]
test_df = DataSourceDF(test_data).prepare_dataset()


@pytest.fixture()
def forecast():
    forecast = Forecast()
    yield forecast


def test_should_generate_forecast_from_test_df(forecast):
    result = forecast.generate_forecast(test_df)
    date_series = result['date']
    max_value = date_series.max()
    min_value = date_series.min()

    assert min_value == '2021'
    assert max_value == '2025'
    assert result.shape[0] == 5
