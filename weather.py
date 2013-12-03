import requests
from secrets import wunder_key

weatherURL="http://api.wunderground.com/api/" + wunder_key + "/conditions/q/{0},{1}.json"

def get_weather(lat, lon):
	return requests.get(weatherURL.format(lat,lon)).json()
