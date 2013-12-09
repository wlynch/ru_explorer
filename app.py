import bus, events, flask, sports, weather
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
	return render_template("index.html")

@app.route("/explore")
def explore():
	#Zimmerli
	#lat = 40.4991876
	#lon = -74.4473217
	lat = request.args.get("lat")
	lon = request.args.get("lon")
	return render_template("explore.html",
		bus = bus.get_nearby(lat, lon),
		events = events.get_nearby(lat, lon),
		sports = sports.get_scores(),
		weather = weather.get_weather(lat, lon))

@app.route("/all")
def get_all():
	# Zimmerli
	#lat = 40.4991876
	#lon = -74.4473217
	lat = request.args.get("lat")
	lon = request.args.get("lon")
	return flask.jsonify({"bus": bus.get_nearby(lat, lon), "events": events.get_nearby(lat, lon),
												"sports": sports.get_scores(), "weather": weather.get_weather(lat, lon)})

@app.route("/bus")
def get_nearby_bus():
	lat = request.args.get("lat")
	lon = request.args.get("lon")
	return flask.jsonify(bus.get_nearby(lat, lon))

@app.route("/events")
def get_events():
	return flask.jsonify(events = events.events)

@app.route("/events/nearby")
def get_nearby_events():
	# Zimmerli
	#lat = 40.4991876
	#lon = -74.4473217

	# Hill Center
	#lat = 40.5220011
	#lon = -74.46236700000001

	lat = request.args.get("lat")
	lon = request.args.get("lon")
	return flask.jsonify(events = events.get_nearby(lat, lon))

@app.route("/weather")
def get_weather():
	# Hill Center
	#lat = 40.5220011
	#lon = -74.46236700000001

	lat = request.args.get("lat")
	lon = request.args.get("lon")

	return flask.jsonify(weather.get_weather(lat, lon))

@app.route("/sports")
def get_sports():
	return flask.jsonify(sports = sports.get_scores())

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="80", debug=True)
