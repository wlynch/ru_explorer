import re, requests
from bs4 import BeautifulSoup

sports_url = "http://scarletknights.com/rss/mobile/feed-scores.asp"

def get_scores():
	scores = []
	raw_scores = BeautifulSoup(requests.get(sports_url).text)
	for row in raw_scores.root.findAll("row"):
		scores.append({ "sport": str(row.sport.string), "opponent": str(row.opponent.string), 
										"score": str(row.score.string), "datetime": str(row.datetime.string),	
										"location": str(row.location.string), "url": str(row.boxhtml.string) })
	return scores
