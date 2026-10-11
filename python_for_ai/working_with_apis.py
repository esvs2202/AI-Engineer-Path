import requests

def get_weather(latitude,longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response = requests.get(url)
    data = response.json()
    return data['current']['temperature_2m']

# get temperatures for different cities
paris_temp = get_weather(48.85,2.35)
london_temp = get_weather(51.50,-0.12)
tokyo_temp = get_weather(35.68,139.69)

print(f"Paris: {paris_temp} degrees Celsius")
print(f"London: {london_temp} degrees celsius")
print(f"Tokyo: {tokyo_temp} degrees celsius")