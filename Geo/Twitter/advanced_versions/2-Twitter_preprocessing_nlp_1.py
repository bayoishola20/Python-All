'''
Description: processing the twitter data for spatiotemporal visualization 
Input: JSON file of twitters (i.e. the twitter you have downloaded)
Output: Geojson file for spatiotemporal visualization
Author: Diao
'''
import json
from shapely.geometry import Point
import re
from dateutil import tz
from datetime import datetime

# read JSON file of the collected twitters
with open('Collected_tweets.json', 'r', encoding='utf-8') as f:
	lines = f.readlines()

# extracting cetrain fields twitters
user_names = []
times = []
utc_mss = []
geo_points = []
texts = []
for i in range(0, len(lines), 2):
	line = lines[i]
	tweet = json.loads(line)
	if tweet['coordinates'] != None:
		user_name, time, utc_ms, point, text = Extract_certain_fields(tweet)
		user_names.append(user_name)
		times.append(time)
		utc_mss.append(utc_ms)
		geo_points.append(point)
		texts.append(text)

# construct a geodataframe to store twitter data
twitter_df = gpd.GeoDataFrame(geometry = geo_points)
twitter_df['id'] = range(len(coords))
twitter_df['username'] = user_names
# update the times to specify
# change to your own timezone, e.g. 'Germany/Munich'; America/New_York, ect.
times = utctimestamp_naive(utc_timestamps = utc_mss, timezone = 'Germany/Munich')
twitter_df['time'] = times
twitter_df['utcms'] = utc_mss
twitter_df['text'] = texts

# write to the geojson file
# Change the file name to your own
filename = 'C:/Users/dlint/Desktop/teaching_data_collection/twitter_API/' + 'twitter' + '.geojson'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(twitter_df.to_json())

def Extract_certain_fields(tweet):
	user_name = tweet['user']['name']
	time = tweet['created_at']
	utc_ms = tweet['timestamp_ms']
	coord = tweet['coordinates']['coordinates']
	geo_point = Point(coord[0], coord[1])

	# add a textual processing progress
	ori_text = tweet['text']
	text = clean_text(ori_text)
	return user_name, time, utc_ms, geo_point, text

def clean_text(text):
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(pic\.twitter\.com/[^\s]+))', '', text)
    text = re.sub('@[^\s]+','', text)
    text = re.sub('#([^\s]+)', '', text)
    text = re.sub('[:;>?<=*+()/,\-#!$%\{˜|\}\[^_\\@\]1234567890’‘]',' ', text)
    text = re.sub('[\d]', '', text)
    text = text.replace(".", '')
    text = text.replace("'", ' ')
    text = text.replace("\"", ' ')
    # normalize some utf8 encoding
    text = text.replace("…", ' ')
    text = text.replace("\x9d", ' ').replace("\x8c", ' ')
    text = text.replace("\xa0", ' ')
    text = text.replace("\x9d\x92", ' ').replace("\x9a\xaa\xf0\x9f\x94\xb5", ' ').replace("\xf0\x9f\x91\x8d\x87\xba\xf0\x9f\x87\xb8", ' ').replace("\x9f", ' ').replace("\x91\x8d", ' ')
    text = text.replace("\xf0\x9f\x87\xba\xf0\x9f\x87\xb8", ' ').replace("\xf0", ' ').replace('\xf0x9f', '').replace("\x9f\x91\x8d", ' ').replace("\x87\xba\x87\xb8", ' ')
    text = text.replace("\xe2\x80\x94", ' ').replace("\x9d\xa4", ' ').replace("\x96\x91", ' ').replace("\xe1\x91\xac\xc9\x8c\xce\x90\xc8\xbb\xef\xbb\x89\xd4\xbc\xef\xbb\x89\xc5\xa0\xc5\xa0\xc2\xb8", ' ')
    text = text.replace("\xe2\x80\x99s", " ").replace("\xe2\x80\x98", ' ').replace("\xe2\x80\x99", ' ').replace("\xe2\x80\x9c", " ").replace("\xe2\x80\x9d", " ")
    text = text.replace("\xe2\x82\xac", " ").replace("\xc2\xa3", " ").replace("\xc2\xa0", " ").replace("\xc2\xab", " ").replace("\xf0\x9f\x94\xb4", " ").replace("\xf0\x9f\x87\xba\xf0\x9f\x87\xb8\xf0\x9f", "")
    return text


# utc_timestamps: millisecond as the unit
def utctimestamp_naive(utc_timestamps, timezone):
    local_times = []
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz(timezone)
    for utcstamp in utc_timestamps:
        utc = datetime.utcfromtimestamp(int(utcstamp[:-3]))
        utc = utc.replace(tzinfo=from_zone)
        local_time = utc.astimezone(to_zone)
        str_local_time = datetime.strftime(local_time, "%Y-%m-%d %H:%M:%S")
        local_times.append(str_local_time)
    return local_times