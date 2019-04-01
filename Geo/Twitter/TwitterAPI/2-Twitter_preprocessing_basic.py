'''
Description: processing the twitter data for spatiotemporal visualization 
Input: JSON file of twitters (i.e. the twitter you have downloaded)
Output: Geojson file for spatiotemporal visualization
Author: Diao
'''
import json
from shapely.geometry import Point
import geopandas as gpd


# read JSON file of the collected twitters
with open('Collected_tweets.json', 'r', encoding='utf-8') as f:
	lines = f.readlines()


# define a function extract certain fields
def Extract_certain_fields(tweet):
    user_name = tweet['user']['name']
    time = tweet['created_at']
    utc_ms = tweet['timestamp_ms']
    coords = tweet['coordinates']['coordinates']
    geo_point = Point(coords[0], coords[1])
    text = tweet['text']
    print(user_name)
    return user_name, time, utc_ms, geo_point, text

# -----------ADD YOUR CODES HERE----------------------

# extracting cetrain fields of twitters
# -----------ADD YOUR CODES HERE----------------------
user_names = []
times = []
utc_mss = []
geo_points = []
texts = []
coords = [] #added this

for i in range(0, len(lines), 2):
    line = lines[i]
    tweet = json.loads(line)
    if tweet['coordinates'] != None:
        user_name, time, utc_ms, geo_point, text = Extract_certain_fields(tweet)
        user_names.append(user_name)
        times.append(time)
        utc_mss.append(utc_ms)
        geo_points.append(geo_point)
        texts.append(text)
        coords.append(coords) #added this


# construct a geodataframe to store twitter data
# -----------ADD YOUR CODES HERE----------------------
twitter_df = gpd.GeoDataFrame(geometry = geo_points)
twitter_df['id'] = range(len(coords))
twitter_df['username'] = user_names
twitter_df['time'] = times
twitter_df['utcms'] = utc_mss
twitter_df['text'] = texts

# write the geojson file
# Change the file name to your own
filename = 'Collected_twitters.geojson'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(twitter_df.to_json())



