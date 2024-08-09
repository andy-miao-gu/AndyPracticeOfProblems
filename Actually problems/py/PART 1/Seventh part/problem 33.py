import requests


# Replace 'YOUR_API_KEY' with your own OpenWeatherMap API key
api_key = '6074bead44c211e327e85e9f5f51f741'
city = "tokyo"
# Make a request to the OpenWeatherMap API
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)

if response.status_code != 200:
    print({"error": "Unable to fetch temperature"})

data = response.json()

temperature = data
print(temperature)
