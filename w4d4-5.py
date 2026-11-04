"""

: Final Python Project - Weather CLI App
● Take city name as input
● Fetch current weather from OpenWeatherMap API
● Display temperature, humidity, description
● Handle API errors gracefully
"""


import requests

API_KEY = " put api key here "  
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city.strip(),
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 404:
            print(" City not found. Please check spelling.")
            return
        elif response.status_code != 200:
            print(" Unable to fetch weather. Please try again later.")
            return

        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        print("\n Weather Report")
        print("────────────────────────")
        print(f"City        : {city.title()}")
        print(f"Temperature : {temperature} °C")
        print(f"Humidity    : {humidity} %")
        print(f"Condition   : {condition.title()}")
        

    except requests.exceptions.ConnectionError:
        print(" No internet connection.")
    except requests.exceptions.Timeout:
        print(" Server is not responding.")
    except Exception as error:
        print(" Unexpected error:", error)


def main():
    print("\n====== Weather CLI App ======")

    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ")

        if city.lower().strip() == "exit":
            print("Thanks for using Weather App!")
            break

        if not city.strip():
            print(" City name cannot be empty.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()
