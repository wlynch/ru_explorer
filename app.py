import events, flask, json, requests
from flask import Flask, request
from secrets import wunder_key

app = Flask(__name__)
nextbusURL="http://runextbus.herokuapp.com"
weatherURL="http://api.wunderground.com/api/" + wunder_key + "/conditions/q/{0},{1}.json"

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/bus")
def bus():
#	lat = 40.5220011
#	lon = -74.46236700000001
	lat = request.args.get("lat")
	lon = request.args.get("lon")
	stops = requests.get(nextbusURL + "/nearby/" + str(lat) + "/" + str(lon)).json()
	print stops
	retval = {}
	for stop in stops:
		print stop
		print type(stop)
		tmp = requests.get(nextbusURL + "/stop/" + stop).json()
		print json.dumps(tmp)
		retval[stop] = tmp
	print "done!"
	return flask.jsonify(retval)

@app.route("/events")
def get_events():
	return flask.jsonify(events = events.events)

@app.route("/events/nearby")
def get_nearby_events():
	#Zimmerli
	#lat = 40.4991876
	#lon = -74.4473217

	# Hill Center
	lat = 40.5220011
	lon = -74.46236700000001

	#lat = request.args.get("lat")
	#lon = request.args.get("lon")
	retval = []
	for event in events.events:
		if events.is_nearby(event["event_buildingno"], lat, lon):
			print event["title"]
			retval.append(event)
	return flask.jsonify(events = retval)

@app.route("/weather")
def get_weather():
	# Hill Center
	lat = 40.5220011
	lon = -74.46236700000001

	return flask.jsonify(requests.get(weatherURL.format(lat,lon)).json())

if __name__ == "__main__":
	app.run(debug=True)
