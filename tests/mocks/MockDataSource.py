class MockDataSource:
    def __init__(self):
        self.data = {
            'TEST.TIME.SERIES': {
                'CHN': {
                    'header': 'test_data',
                    'data': [{'date': '1967', 'value': 75300003800},
                             {'date': '1966', 'value': 62999998500},
                             {'date': '1961', 'value': 24700000300},
                             {'date': '1960', 'value': 24200001500}]
                },
                'AFG': {
                    'header': 'test_data',
                    'data': [{'date': '2004', 'value': 249791940700},
                             {'date': '2003', 'value': 221358563000},
                             {'date': '2002', 'value': 182162721300},
                             {'date': '2001', 'value': 1222756495400},
                             {'date': '1997', 'value': 1222916881118.13},
                             {'date': '1996', 'value': 221358563000}]
                }
            }
        }

    def fetch_data(self, country, time_series):
        data = self.data[time_series][country]['data']
        header = self.data[time_series][country]['header']
        return header, data
