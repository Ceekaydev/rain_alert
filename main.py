import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

parameters = {
    "lat": 6.524379,
    "lon": 3.379206,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
print(f"Status code: {response.status_code}")
# print(response.json())
weather_data = response.json()

will_rain = False
for weather_hour in weather_data["list"]:
    condition_code = weather_hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    account_sid = os.getenv("ACCOUNT_SID")
    auth_token = os.getenv("AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="whatsapp:+14155238886",  # Twilio sandbox number
        to=f"whatsapp:{os.getenv("WHASTAPP_NO")}",   # your verified WhatsApp number
        body="Bring an Umbrella ☔"
    )

    print(message.sid)
    print(message.status)


