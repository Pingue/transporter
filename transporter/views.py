from transporter import app
from tfl import *
from flask import render_template
from flask import request

@app.route('/')
def view_GetLocation():
	return render_template('getLocation.html',)

@app.route('/location')
def view_PlacesNearLocation():
	lat=51.5465906
	lon=-0.4761759
	rad=200
	if(request.args.get('lat')):
		lat=request.args.get('lat')
	if(request.args.get('lon')):
		lon=request.args.get('lon')
	if(request.args.get('radius')):
		rad=request.args.get('radius')
	
	return render_template('placesNearLocation.html',places=getPlacesNearLocation(lat,lon,rad),lat=lat,lon=lon,rad=rad)
