import requests
import csv
import pandas as pd

class WeatherDataFetcher:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_data(self, city_name):
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.api_key}"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to fetch data for {city_name}. Status code: {response.status_code}")
            return None

    def store_data_to_csv(self, data, csv_file_name):
        if data:
            df = pd.DataFrame(data)
            df.to_csv(csv_file_name, index=False)
            print(f"Weather data stored in {csv_file_name}")

if __name__ == "__main__":
    api_key = "bab35a7d8848a283f4bafbbb86fb13ca"
    cities = ["London", "Paris", "New York", "Tokyo"]
    csv_file_name = "s3://airflowbucketgr/data/weather_data.csv"

    fetcher = WeatherDataFetcher(api_key)
    weather_data = []

    for city in cities:
        data = fetcher.fetch_data(city)
        if data:
            weather_data.append({
                "City": city,
                "Temperature (C)": data["main"]["temp"] - 273.15,
                "Weather": data["weather"][0]["main"],
                "Description": data["weather"][0]["description"]
            })

    fetcher.store_data_to_csv(weather_data, csv_file_name)
