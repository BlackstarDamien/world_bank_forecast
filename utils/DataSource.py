class DataSource:
    def __init__(self, data_source):
        self._data_source = data_source

    def fetch_data(self, country, time_series) -> dict:
        data_source_result = self._data_source.fetch_data(country, time_series)
        return data_source_result
