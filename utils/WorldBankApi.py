import requests


class WorldBankApi:
    def __init__(self):
        self._URL = "https://api.worldbank.org/v2/"

    def fetch_data(self, country, time_series):
        resultset = self._fetch_api_data(country, time_series)
        return self._generate_final_dataset(resultset)

    def _fetch_api_data(self, country, time_series, current_page=1):
        endpoint = self._generate_endpoint(country, time_series, current_page)
        response = requests.get(endpoint)
        response_json = response.json()
        resultset = response_json[1]

        pages = response_json[0]['pages']
        if current_page < pages:
            return resultset + self._fetch_api_data(country, time_series, current_page+1)
        return resultset

    def _generate_final_dataset(self, resultset):
        header = resultset[0]['indicator']['value']
        return header, [{'date': item['date'], 'value': item['value']} for item in resultset]

    def _generate_endpoint(self, country, time_series, page=1):
        country = f"country/{country}/"
        indicator = f"indicator/{time_series}"
        output_format = "?format=json"
        page = f"&page={page}"
        return self._URL + country + indicator + output_format + page
