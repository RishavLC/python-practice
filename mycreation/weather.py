import requests

API_KEY = "your_openweathermap_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter city: ")
url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] != "404":
    weather = data["main"]
    temp = weather["temp"]
    humidity = weather["humidity"]
    desc = data["weather"][0]["description"]
    print(f"🌡 Temp: {temp}°C\n💧 Humidity: {humidity}%\n🌥 Weather: {desc}")
else:
    print("❌ City not found.")
