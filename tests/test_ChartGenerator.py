import os
import pytest
import pandas as pd

from utils import ChartGenerator

test_actual_df = pd.DataFrame([{'date': '2019', 'value': 25252525}, {
                              'date': '2020', 'value': 335353}])
test_forecast_df = pd.DataFrame([{'date': '2021', 'value': 2525335532525}, {
    'date': '2022', 'value': 335353535353}])


@pytest.fixture()
def chart_generator():
    chart_generator = ChartGenerator(test_actual_df, test_forecast_df)
    yield chart_generator
    if os.path.isfile('test_data.png'):
        os.remove('test_data.png')


def test_should_generate_png_file(chart_generator):
    chart_generator.generate_chart('test_data', 'test_data.png')
    assert os.path.isfile('test_data.png')
