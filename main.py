import requests
from twilio.rest import Client

API = "a8dce1b38597e9ef7d3d6bf9eb34dff6"
account_sid = "ACcc998e94c8f31dc1b233b1fa18df719d"
auth_token = "6e56a3c6a21fb80eb7d0c100a4e386ae"
# 17.502778
# 74.116666
para = {
    "lat":-12.963519 ,
    "lon": -68.321296,
    "appid": API,
    "exclude":"current,minutely,daily"


}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall?",params=para)
response.raise_for_status()
data = response.json()
slice_data = data["hourly"][:12]

is_rain = False

for hr in slice_data:
    condition = hr["weather"][0]["id"]
    if int(condition) < 700:
        is_rain = True

if is_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring ☔.",
        from_="+15075225826",
        to="+919987570219"
    )

    print(message.status)