import requests
from twilio.rest import Client
from KEYS import OPEN_WEATHER_API_ENDPOINT, OPEN_WEATHER_API_KEY, account_sid, auth_token, from_number, to_number

# Toronto
city = "Toronto"
MY_LAT = 43.653225
MY_LONG = -79.383186

# Seattle
# city = "Seattle"
# MY_LAT = 47.606209
# MY_LONG = -122.332069


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": OPEN_WEATHER_API_KEY,
}

response = requests.get(url=OPEN_WEATHER_API_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour in weather_data["hourly"][:12]:
    if hour["weather"][0]["id"] < 700:
        will_rain = True


client = Client(account_sid, auth_token)


if will_rain:
    print("Rain detected")
    message = client.messages \
                    .create(
                         body=f"Woops, it looks like it's going to rain in {city} today!"
                              f" You should take an umbrella ! ☔️",
                         from_=from_number,
                         to=to_number
                     )
    print(message.status)
