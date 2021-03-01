import argparse
import traceback
from utils import (ChartGenerator,
                   DataSource,
                   DataSourceDF,
                   Forecast,
                   WorldBankApi)


def forecast_handler(country, time_series_code):
    try:
        world_bank_api = WorldBankApi()
        data_src = DataSource(world_bank_api)
        header, result = data_src.fetch_data(country, time_series_code)
        forecast = Forecast()

        df = DataSourceDF(result).prepare_dataset()
        forecast_df = forecast.generate_forecast(df)

        chart_generator = ChartGenerator(df, forecast_df)
        chart_generator.generate_chart(
            header, f"{country}_{time_series_code}.png")
    except Exception as e:
        print(f"Error occured! Traceback:\n")
        tb = traceback.format_exc()
        print(tb)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--country', type=str, required=True,
                        help='Country name in ISO ALPHA 3 code format')
    parser.add_argument('--time_series', type=str, required=True,
                        help='World Bank API time series code')

    args = parser.parse_args()
    country = args.country
    time_series = args.time_series
    forecast_handler(country, time_series)


if __name__ == '__main__':
    main()
