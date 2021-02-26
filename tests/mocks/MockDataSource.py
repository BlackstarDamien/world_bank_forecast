class MockDataSource:
    def __init__(self):
        self.data = {
            'TEST.TIME.SERIES': {
                'AFG': {
                    'header': 'test_data',
                    'x_values': [2020, 2019, 2018],
                    'y_values': [1123, 2345, 556]
                },
                'CHN': {
                    'header': 'test_data',
                    'x_values': [2020, 2019, 2018],
                    'y_values': [122525, 464646, 35353]
                }
            }
        }

    def fetch_data(self, country, time_series):
        return self.data[time_series][country]
