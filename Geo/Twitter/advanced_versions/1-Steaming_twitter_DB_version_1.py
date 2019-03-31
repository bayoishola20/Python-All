'''
Below is a simple example of collecting twitters by using tweepy package;
The collected data in this versoion will be stored into a database
# Note: for this version, you should have a installed MonoDB in your computer in advance
Author: Diao
'''
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
from pymongo import MongoClient
import json
import random

# define a class of listener
# save the data to the database to your favored file name
class Stdoutlistener_db_version(StreamListener):
    def on_data(self, data):
        client = MongoClient('localhost', 27017)
        db = client['your_DB_name']
        collection = db['your_talbe_name']
        tweet = json.loads(data)
        tweetaddedid = collection.insert_one(tweet).inserted_id
        print(tweetaddedid)
    def on_error(self, status):
        print(statuses)

def main():
    # auth information, please substitute your own keys and token
    auth = OAuthHandler('8Y******', 'iK******')
    auth.set_access_token('80*****', 'jU*****')
    api = tweepy.API(auth)
    # create a instance of StdOutListener
    stdoutlistener = Stdoutlistener_file_version()
    # use the listener and auth information, we can get our own stream
    stream = Stream(auth=api.auth, listener=stdoutlistener, timeout=30.0)
    while True:
        try:
            # define the bouding box for your geo-search 
            Munich_boundingbox  = [11.3855, 47.9129, 11.8520, 48.2995]
            NYC_boudingbox = [-75,40,-73,42]
            Berlin_boudingbox = [13.0535, 52.3303, 13.7262, 52.6675]
            Multi_cities = [-74.2589, 40.4774, -73.7004, 40.9176,-118.9448, 32.8007, -117.6462, 34.8233,11.3855, 47.9129, 11.8520, 48.2995]
            # change the parameter parameters of "locations" to your own boudingbox below
            stream.filter(locations = NYC_boudingbox, languages = ['en,de'])
            # stream.filter(track=['cartograohy']) # search twitter based on keywords
            # stream.filter(track=['cartograohy'], locations = NYC_boudingbox, async=False, languages=['en,de,zh']) # searching twitters based on keywords and Geo-boudary
            break
        except Exception as e:
             # Abnormal exit: Reconnect
             print('the Exception happend, need to slepp for 60 senconds')
             nsecs=random.randint(60,63)
             time.sleep(nsecs)