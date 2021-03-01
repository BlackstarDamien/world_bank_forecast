import pandas as pd


class DataSourceDF:
    def __init__(self, data):
        self._data = data

    def prepare_dataset(self):
        dataset_df = pd.DataFrame(self._data)
        dataset_df = dataset_df.sort_values('date', ascending=True)
        return dataset_df
