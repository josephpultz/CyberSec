import requests
from bs4 import BeautifulSoup

###Build query
URL = "https://weather.com/weather/today/l/68befb0f8cd688f32aa9d6f4c3c7b19156ea924d4dad305270fb53c5f5b4a819"
htmlPage = requests.get(URL)
beautifulSoup = BeautifulSoup(htmlPage.content, "html.parser")

### parse results
results = beautifulSoup.find(id="WxuCurrentConditions-main-eb4b02cb-917b-45ec-97ec-d4eb947f6b6a")
currentLocation = results.find("h1", class_=("CurrentConditions--location--1YWj_"))
timeOfDay = results.find("span", class_="CurrentConditions--timestamp--1ybTk")



print("Current location", currentLocation.text)
print("Current temp", timeOfDay.text)

