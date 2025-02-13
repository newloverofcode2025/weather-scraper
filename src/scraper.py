import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_weather_data():
    url = "https://weather.com/weather/today/l/USCA0987:1:US"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    weather_data = []
    for item in soup.select('.CurrentConditions--currentConditions--3TQnv'):
        condition = item.find('span', class_='CurrentConditions--phraseValue--2xXSr').text
        temp = item.find('span', class_='CurrentConditions--tempValue--3KcTQ').text
        weather_data.append({
            'Condition': condition,
            'Temperature': temp
        })

    df = pd.DataFrame(weather_data)
    df.to_csv('../data/weather_data.csv', index=False)
    print("Weather data saved to weather_data.csv")

if __name__ == "__main__":
    scrape_weather_data()