# Importing requests since requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!

# Importing requests since requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!

import requests
import os
from datetime import datetime

# Here we are using API so we are using API of  "https://openweathermap.org/" this is done by creating an API id. 
user_api = '2bc700c73ce46f27eba117e4fc746fbf'

#location is to be entered so input.
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s"%(location, user_api)
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
#temp_city for temperature of city, weather_desc for small description of weather, hmdt for humidity, wind_spd for wind speed
#date_time for last time its updated so recent details by that time and date

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
 
#Now for result print command

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')