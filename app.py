import events, flask, json, requests
from flask import Flask, request
app = Flask(__name__)

nextbusURL="http://runextbus.herokuapp.com"

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
#	lat = 40.5220011
#	lon = -74.46236700000001
	print type(events.events)
	return flask.jsonify(events = events.events)

if __name__ == "__main__":
	app.run(debug=True)
