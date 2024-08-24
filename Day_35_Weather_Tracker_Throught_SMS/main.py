import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import requests

# Define the correct endpoint for forecast data
OWN_FORECAST_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "c81d3e0d86429d785d281b68970e3f11"
account_sid = 'AC514f69bff304df3f7675a88ce7427e50'
auth_token = '4b704a0c2aa28b6434cac22a1fc80a6c'

weather_params = {
    "lat": 19.418343,
    "lon": 72.795593,
    "appid": api_key,
    "units": "metric",  # Optional: to get temperature in Celsius
    "cnt": 4  # Get the next 4 forecast data points (e.g., 4 intervals of 3 hours)
}

response = requests.get(OWN_FORECAST_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

# Loop over the forecast data to check if it will rain
for forecast_data in weather_data["list"]:
    # print(forecast_data)
    condition_code = forecast_data['weather'][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break  # Stop checking further if rain is found

if will_rain:
    print("Bring an umbrella")
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages.create(
        body="It is going to rain Today!",
        from_="+17078279132",
        to="+919325369502",
    )
    
else:
    print("No rain expected")
