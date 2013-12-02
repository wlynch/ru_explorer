import feedparser, json

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
