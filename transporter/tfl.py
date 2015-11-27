import urllib2
import json
import cgi

def getPlacesNearLocation(lat,lon,rad):
	response = urllib2.urlopen('https://api.tfl.gov.uk/Place?lat='+lat+'&lon='+lon+'&radius='+rad+'&app_id=cd00a446&app_key=bb862cf9b6f46d80f1c4e2818446b681&includeChildren=True')
	html=response.read()
	parsed=json.loads(html)
	return parsed
