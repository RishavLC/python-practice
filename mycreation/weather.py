import requests

# Your API key
API_KEY = "157af49e9b65e171d2ec09d646ab674c"  # replace with your working key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f"❌ Error: {data.get('message', 'Unknown error')}")
            return None

        # Extract info
        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        # Nicely formatted output
        print("\n🌍 Weather App")
        print("="*30)
        print(f"📍 City: {city.title()}")
        print(f"🌤️ Condition: {weather}")
        print(f"🌡️ Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬️ Wind Speed: {wind} m/s")
        print("="*30)

    except Exception as e:
        print(f"⚠️ Something went wrong: {e}")


# Main Program
if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
