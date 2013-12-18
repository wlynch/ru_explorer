import requests

nextbusURL="http://runextbus.herokuapp.com"

# Removes routes that are currently not in service 
def prune_routes(routes):
	remove_route = []
	for route in routes:
		empty = True
		remove = []
		for stop in routes[route]:
			if stop["predictions"] is not None:
				empty = False
				stop["predictions"] = stop["predictions"][:3]
			else:
				remove.append(stop)
		for stop in remove:
				routes[route].remove(stop)
		if empty is True:
				remove_route.append(route)
	for route in remove_route:
		routes.pop(route)
	return routes 

def get_nearby(lat, lon):
	stops = requests.get(nextbusURL + "/nearby/" + str(lat) + "/" + str(lon)).json()
	retval = {}
	for stop in stops:
		tmp = requests.get(nextbusURL + "/stop/" + stop).json()
		retval[stop] = tmp
	return prune_routes(retval)
