import pandas as pd
import pmdarima as pm
from pmdarima.model_selection import train_test_split


class Forecast:
    def generate_forecast(self, dataset_df):
        forecast = self._generate_prediction_data(dataset_df)
        return forecast

    def _generate_prediction_data(self, dataset_df):
        train = self._generate_training_dataset(dataset_df)
        forecast = self._generate_forecast_arima(train)
        date_column = self._prepare_forecast_date_column(dataset_df)

        forecast_df = pd.DataFrame(
            zip(date_column, forecast), columns=['date', 'value'])
        return forecast_df

    def _generate_training_dataset(self, dataset_df):
        dataset_numpy = dataset_df['value'].fillna(0.0).to_numpy()
        train_size = dataset_df.shape[0] - 1
        train, _ = train_test_split(dataset_numpy, train_size=train_size)
        return train

    def _prepare_forecast_date_column(self, dataset_df):
        start_date = int(dataset_df['date'].tolist()[-1]) + 1
        end_date = int(dataset_df['date'].tolist()[-1]) + 6
        return [str(item) for item in range(start_date, end_date)]

    def _generate_forecast_arima(self, train_dataset):
        model = pm.auto_arima(train_dataset)
        return model.predict(n_periods=5)
