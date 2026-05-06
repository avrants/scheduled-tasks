import os
import requests
from twilio.rest import Client
import pprint

API_END = "https://api.openweathermap.org"
API_END_DATA = "/data/2.5/forecast"
API_KEY = os.environ.get("TWILIO_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
from_phone = "+13362976958"
to_phone = "+359898930153"

client = Client(account_sid, auth_token)

params = {
    "lat": 45.812031,
    "lon": 9.085620,
    "units": "metric",
    "cnt": 8,
    "appid": API_KEY,
}

response = requests.get(API_END + API_END_DATA, params=params)
response.raise_for_status()

weather_data = response.json()

for forecast in weather_data["list"]:
    if forecast["weather"][0]["id"] < 700:
        #print(f"It is raining or it is going to rain at {forecast["dt_txt"]}.")
        message = client.messages.create(
            body=f"It is raining or it is going to rain at {forecast["dt_txt"]}.",
            from_=from_phone,
            to=to_phone,
        )
        print(message.body)
        break

###################################################################





