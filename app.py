import bus, events as ru_events, flask, sports, weather
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/bus")
def get_nearby_bus():
	lat = 40.5220011
	lon = -74.46236700000001
	#lat = request.args.get("lat")
	#lon = request.args.get("lon")
	return flask.jsonify(bus.get_nearby(lat, lon))

@app.route("/events")
def get_events():
	return flask.jsonify(events = events.events)

@app.route("/events/nearby")
def get_nearby_events():
	#Zimmerli
	lat = 40.4991876
	lon = -74.4473217

	# Hill Center
	#lat = 40.5220011
	#lon = -74.46236700000001

	#lat = request.args.get("lat")
	#lon = request.args.get("lon")
	return flask.jsonify(events = ru_events.get_nearby(lat, lon))

@app.route("/weather")
def get_weather():
	# Hill Center
	lat = 40.5220011
	lon = -74.46236700000001

	#lat = request.args.get("lat")
	#lon = request.args.get("lon")

	return flask.jsonify(weather.get_weather(lat, lon))

@app.route("/sports")
def get_sports():
	return flask.jsonify(scores = sports.get_scores())

if __name__ == "__main__":
	app.run(debug=True)
