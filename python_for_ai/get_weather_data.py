import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

# calculate dates
today = datetime.now()
week_ago = today - timedelta(days = 7)

# Format dates for API  (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# function to get weather data to the specific city
def get_weather(latitude, longitude):
    # get the weather for past week
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

    response =  requests.get(url)
    data = response.json()
    return data
# -------------------------------------------------------------------------------------
def daily_data_report(city, d):
    
    daily_data = d['daily']

    # create a dataframe 
    df = pd.DataFrame({
        'date': daily_data['time'],
        'max_temp': daily_data['temperature_2m_max'],
        'min_temp': daily_data['temperature_2m_min']
    })

    
    # convert date strings to datetime
    df['date'] = pd.to_datetime(df['date'])

    #------------------------------------------------------------------------
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
    plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title(f'{city} Weather - Past 7 Days')
    plt.grid(True)
    plt.legend()

    # Rotate x-axis labels for readability
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot
    # Create a data folder if it doesn't exist
    if not os.path.exists("weather_data"):
        os.makedirs("weather_data")
    plt.savefig(f'weather_data/{city}_weather_chart.png')
    plt.show()

    #---------------------------------------------------------------------
    # save to CSV
    df.to_csv(f'weather_data/{city}_weather.csv', index = False)
    print(f"Data saved to weather_data/{city}_weather.csv")

    return "Done"

# calling the functions
# Extract the daily data

city = input("Enter your city name: ")
latitude = float(input("Enter the latitude: "))
longitude = float(input("Enter the longitude: "))

get_weather_data = get_weather(latitude = latitude,longitude = longitude)
daily_data_report(city = city, d = get_weather_data)