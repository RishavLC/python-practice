import requests

API_KEY = "157af49e9b65e171d2ec09d646ab674c"   # your real key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"  # Celsius
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if response.status_code == 200:
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    print(f"🌤 Weather in {city}: {weather}")
    print(f"🌡 Temperature: {temp}°C (feels like {feels_like}°C)")
else:
    print(f"❌ Error fetching weather: {data.get('message', 'Unknown error')}")
