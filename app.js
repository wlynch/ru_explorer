var express = require('express');
var nextbus = require('nextbusjs').client();
var app = express();
app.use(express.static('public'));

function getStops(lat, lon, callback) {
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

app.get('/nextbus', function(req, res){
	getStops(req.query.lat, req.query.lon, function(result){ 
		res.send(result) 
	});
});

app.listen(3000);
console.log('Listening on 3000');
