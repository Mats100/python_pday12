import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "70c7472a9e28c3b12fd22daf35856df1"

weather_paramas ={
    "lat":-33.924870,
    "lon":18.424055,
    "appid":api_key,
     "exclude":"current,minutely,daily"
}


response = requests.get(OWM_Endpoint, params=weather_paramas)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")