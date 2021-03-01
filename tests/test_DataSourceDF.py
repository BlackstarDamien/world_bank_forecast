import pytest

from utils import DataSourceDF

test_data = [{'date': '2004', 'value': 249791940700},
             {'date': '2003', 'value': 221358563000},
             {'date': '2002', 'value': 182162721300},
             {'date': '2001', 'value': 1222756495400},
             {'date': '1997', 'value': 1222916881118.13},
             {'date': '1996', 'value': 221358563000}]


@pytest.fixture()
def data_src_df():
    data_src_df = DataSourceDF(test_data)
    yield data_src_df


def test_should_generate_proper_dataframe_with_test_data(data_src_df):
    result = data_src_df.prepare_dataset()
    assert len(test_data) == result.shape[0]
    assert len(test_data[0].keys()) == result.shape[1]
