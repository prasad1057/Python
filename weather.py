import requests


def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main_data = data["main"]
        temperature = main_data["temp"]
        feels_like = main_data["feels_like"]
        humidity = main_data["humidity"]
        weather_data = data["weather"]
        weather_description = weather_data[0]["description"]
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather description: {weather_description}")
    else:
        print("City not found")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace "YOUR_API_KEY" with your OpenWeatherMap API key
    city = input("Enter city name: ")
    get_weather(api_key, city)
