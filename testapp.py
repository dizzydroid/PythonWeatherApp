import requests

city = "London"
api_key = "4a2205bea450247632b8fa33bae74868"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)

print(f"Status code: {response.status_code}")
print(response.json())