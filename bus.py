import requests

nextbusURL="http://runextbus.herokuapp.com"

def get_nearby(lat, lon):
	stops = requests.get(nextbusURL + "/nearby/" + str(lat) + "/" + str(lon)).json()
	retval = {}
	for stop in stops:
		tmp = requests.get(nextbusURL + "/stop/" + stop).json()
		retval[stop] = tmp
	return retval
