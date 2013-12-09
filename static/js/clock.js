function show() {
	var d = new Date();
	document.getElementById("date").innerHTML = d.toDateString();
	document.getElementById("time").innerHTML = d.toLocaleTimeString();
	setTimeout("show()",1000);
}
show();
