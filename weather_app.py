import requests


def get_weather_data(city):

    # Make an HTTP request to the OpenWeatherMap API.
    def get_weather_data(city): response = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid=4a2205bea450247632b8fa33bae74868&units=metric".format(city))
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid=4a2205bea450247632b8fa33bae74868&units=metric".format(city))

    # Check the response status code.
    if response.status_code == 200:

        # The request was successful.
        data = response.json()

        # Return the weather data.
        return data

    else:

        # The request failed.
        raise Exception("Request failed with status code {}".format(response.status_code))



def display_weather_data(data):

    # Print the current temperature.
    print("Current temperature: {} degrees Celsius".format(data["main"]["temp"]))

    # Print the humidity.
    print("Humidity: {}%".format(data["main"]["humidity"]))

    # Print the wind speed.
    print("Wind speed: {} meters per second".format(data["wind"]["speed"]))



def main():

    # Get the city from the user.
    city = input("Enter a city name: ")

    # Get the weather data for the city.
    data = get_weather_data(city)

    # Display the weather data.
    display_weather_data(data)


if __name__ == "__main__":
    main()

