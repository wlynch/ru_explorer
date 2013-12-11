import feedparser, geohash, json


#Load event feed
ru_events_url = "http://ruevents.rutgers.edu/events/getEventsRss.xml?numberOfDays=1"
feed = feedparser.parse(ru_events_url)
events = feed["items"]

# Load buildings
building_file = open("data/places.txt")
raw_buildings = json.load(building_file)
buildings = {}

# Convert buildings to events feed friendly format
for building in raw_buildings["all"]:
	buildings[building.split("_")[0]] = raw_buildings["all"][building]

# Finds nearest buildings for the given coordinates.
# Note: Due to the precision of the coordinates given by places, you should keep the
# precision value around 6-7
def find_nearest_buildings(lat, lon, precis=6):
	retval = []
	target_hash = geohash.encode(lat, lon, precision=precis)
	print target_hash
	for building in buildings.itervalues():
		if "location" in building:
			print building["location"]["latitude"]
			building_hash = geohash.encode(float(building["location"]["latitude"]), float(building["location"]["longitude"]), precision=precis)
			if target_hash == building_hash:
				retval.append(building)
	return retval

def is_nearby(building_id, lat, lon, precis=6):
	target_hash = geohash.encode(lat, lon, precision=precis)
	if building_id not in buildings:
		return False
	building = buildings[building_id]
	if "location" in building:
		building_hash = geohash.encode(float(building["location"]["latitude"]), float(building["location"]["longitude"]), precision=precis)
		if target_hash == building_hash:
			return True;
	return False

def get_nearby(lat, lon):
	retval = []
	for event in events:
		if is_nearby(event["event_buildingno"], lat, lon, 5):
			retval.append(event)
	print retval
	return retval
