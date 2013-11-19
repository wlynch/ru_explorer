var express = require('express');
var nextbus = require('nextbusjs').client();
var app = express();

app.use(express.static('public'));
function getStops(lat, lon, callback) {
	//TODO: Cache the agency so that we don't have to keep getting this MASSIVE file
	nextbus.cacheAgency('rutgers', function (err) {
		if (err) {
			throw err;
		} else {
			callback(nextbus.closestStops(lat, lon));
		}
	});
}

app.get('/hello.txt', function(req, res){
	res.send('Hello world!' + req.query.x);
});

app.get('/api/nextbus/stops', function(req, res){
	getStops(req.query.lat, req.query.lon, function(result){ 
		res.send(result) 
	});
});

app.get('test', function(req, res){
	res.send(req.query.test);
});

app.get('/api/nextbus/times', function(req, res){
	console.log(req.query.stop);
	nextbus.getAgencyCache('rutgers', function(err) {
		nextbus.stopPredict(
			req.query.stop, 
			null, 
			function(err, data) { 
				console.log(data);
				res.send(data);
			}, 
			'minutes'
		);
	});
});

app.listen(3000);
console.log('Listening on 3000');
