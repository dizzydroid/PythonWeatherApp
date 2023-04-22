import requests

city = "London"
api_key = "YOUR_API"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)

print(f"Status code: {response.status_code}")
print(response.json())