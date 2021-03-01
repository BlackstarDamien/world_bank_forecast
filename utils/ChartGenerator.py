import pandas as pd
import matplotlib.pyplot as plt


class ChartGenerator:
    def __init__(self, actual_df, forecast_df):
        self._actual_df = actual_df
        self._forecast_df = forecast_df

    def generate_chart(self, title, file_name):
        df_size = self._actual_df.shape[0] - 1
        final_df = pd.concat(
            [self._actual_df, self._forecast_df], axis=0).reset_index(drop=True)
        ax = final_df.iloc[:df_size, :].plot(
            x='date', y='value', color="crimson", legend=False)
        final_df.iloc[df_size:, :].plot(color="C0", ax=ax, legend=False)

        plt.title(title)
        plt.savefig(file_name)
