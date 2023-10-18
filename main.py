import requests
import os
from twilio.rest import Client
import datetime

OWN_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
MY_LAT = 41.0864
MY_LONG = 23.5484
api_key = os.environ.get("OWN_API_KEY")

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
when_rain = ""
for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True
        dt_object = datetime.datetime.fromtimestamp(hour_data["dt"])
        when_rain += (dt_object.strftime("%H")) + ", "
when_rain = when_rain[:-2]

send_message = input("Do you want to send a message? Y or N?")
if send_message == "Y" or "y":
    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"It's going to rain today at {when_rain}. Remember to bring an umbrella",
            from_='+19133747068',
            to=os.environ.get("MY_NUMBER")
        )
        print(message.status)
else:
    print(f"It's going to rain today at {when_rain}!")
